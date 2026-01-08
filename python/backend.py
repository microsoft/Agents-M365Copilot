"""
Backend API (Middle Tier) - Implements OBO Flow
This API receives a user token from the frontend and uses OBO to call Copilot API
"""
import os
import asyncio
from datetime import datetime
from flask import Flask, request, jsonify
import msal
from dotenv import load_dotenv
from kiota_abstractions.api_error import APIError

from microsoft_agents_m365copilot_beta import AgentsM365CopilotBetaServiceClient
from microsoft_agents_m365copilot_beta.generated.copilot.retrieval.retrieval_post_request_body import (
    RetrievalPostRequestBody,
)
from microsoft_agents_m365copilot_beta.generated.models.retrieval_data_source import RetrievalDataSource

load_dotenv()

app = Flask(__name__)


TENANT_ID = os.getenv("TENANT_ID")
BACKEND_CLIENT_ID = os.getenv("BACKEND_CLIENT_ID")  # Backend API app ID
BACKEND_CLIENT_SECRET = os.getenv("BACKEND_CLIENT_SECRET")  # Backend API secret

# Scopes needed to call Copilot API
COPILOT_SCOPES = [
    'https://graph.microsoft.com/Files.Read.All',
    'https://graph.microsoft.com/Sites.Read.All',
    'https://graph.microsoft.com/User.Read'
]


class SimpleTokenProvider:
    """Simple credential provider for using OBO-acquired tokens"""
    def __init__(self, token: str):
        self._token = token
    
    def get_token(self, *scopes, **kwargs):
        """Return a token object compatible with Azure SDK"""
        from collections import namedtuple
        AccessToken = namedtuple("AccessToken", ["token", "expires_on"])
        # expires_on should be a timestamp in the future (1 hour from now)
        import time
        expires_on = int(time.time()) + 3600
        return AccessToken(token=self._token, expires_on=expires_on)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "Backend API with OBO"}), 200


@app.route('/api/copilot/retrieval', methods=['POST'])
def copilot_retrieval():
    """
    Endpoint that receives user token and uses OBO to call Copilot API
    Expects: Authorization header with Bearer token from frontend
    Body: { "query": "search query", "dataSource": "SharePoint" }
    """
    try:
        # Extract the user's access token from Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
        
        user_access_token = auth_header.replace('Bearer ', '')
        
        # Get request body
        body = request.get_json()
        query_string = body.get('query', 'What is the latest in my organization?')
        data_source = body.get('dataSource', 'SharePoint')
        
        print(f"\n{'='*60}")
        print("🔄 Starting OBO Flow")
        print(f"{'='*60}")
        print(f"\n📨 Received request from frontend")
        print(f"   Query: {query_string}")
        print(f"   Data Source: {data_source}")
        
        # Use MSAL to perform OBO flow
        print(f"\n📝 Step 1: Exchanging user token using OBO flow...")
        
        authority = f"https://login.microsoftonline.com/{TENANT_ID}"
        
        # Create MSAL confidential client for OBO
        msal_app = msal.ConfidentialClientApplication(
            client_id=BACKEND_CLIENT_ID,
            client_credential=BACKEND_CLIENT_SECRET,
            authority=authority
        )
        
        # OBO flow: Exchange the incoming user token for a new token
        result = msal_app.acquire_token_on_behalf_of(
            user_assertion=user_access_token,
            scopes=COPILOT_SCOPES
        )
        
        if "access_token" not in result:
            error_desc = result.get("error_description", "Unknown error")
            error_code = result.get("error", "unknown_error")
            print(f"❌ OBO token acquisition failed!")
            print(f"   Error: {error_code}")
            print(f"   Description: {error_desc}")
            return jsonify({
                "error": "OBO flow failed",
                "error_code": error_code,
                "error_description": error_desc
            }), 401
        
        copilot_token = result["access_token"]
        expires_on = datetime.fromtimestamp(result["expires_in"] + datetime.now().timestamp())
        
        print(f"✅ OBO token acquired successfully!")
        print(f"   Token expires at: {expires_on}")
        
        # Call Copilot API using the OBO token
        print(f"\n📝 Step 2: Calling Copilot API with OBO token...")
        copilot_result = asyncio.run(call_copilot_api(copilot_token, query_string, data_source))
        
        print(f"\n{'='*60}")
        print("✅ OBO Flow Completed Successfully!")
        print(f"{'='*60}\n")
        return jsonify(copilot_result), 200
        
    except APIError as e:
        error_msg = f"Copilot API Error: {e}"
        print(f"❌ {error_msg}")
        return jsonify({
            "error": "Copilot API Error",
            "details": str(e),
            "status_code": e.response_status_code if hasattr(e, 'response_status_code') else 500
        }), 500
        
    except Exception as e:
        error_msg = f"Backend API Error: {type(e).__name__}: {str(e)}"
        print(f"❌ {error_msg}")
        return jsonify({
            "error": "Internal Server Error",
            "details": str(e)
        }), 500


async def call_copilot_api(copilot_token, query_string, data_source):
    """
    Call the Copilot API using the OBO-acquired token
    """
    import httpx
    
    # Prepare the request
    url = "https://graph.microsoft.com/beta/copilot/retrieval"
    headers = {
        "Authorization": f"Bearer {copilot_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "dataSource": data_source,
        "queryString": query_string
    }
    
    print(f"   Making direct HTTP call to Copilot API...")
    print(f"   URL: {url}")
    
    # Make the HTTP request
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers, timeout=60.0)
        
        if response.status_code != 200:
            error_detail = response.text
            print(f"   ❌ API returned status {response.status_code}")
            print(f"   Response: {error_detail[:200]}")
            raise Exception(f"Copilot API returned {response.status_code}: {error_detail}")
        
        result_data = response.json()
    
    # Process results
    results = []
    retrieval_hits = result_data.get("retrievalHits", [])
    
    if retrieval_hits:
        print(f"✅ Received {len(retrieval_hits)} hits from Copilot API")
        for hit in retrieval_hits:
            hit_data = {
                "web_url": hit.get("webUrl"),
                "extracts": []
            }
            
            extracts = hit.get("extracts", [])
            for extract in extracts:
                hit_data["extracts"].append({
                    "text": extract.get("text")
                })
            results.append(hit_data)
    else:
        print(f"   No hits returned from Copilot API")
    
    return {
        "query": query_string,
        "data_source": data_source,
        "total_hits": len(results),
        "results": results
    }


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting Backend API with OBO Flow")
    print("="*60)
    print(f"Tenant ID: {TENANT_ID}")
    print(f"Backend Client ID: {BACKEND_CLIENT_ID}")
    print(f"Endpoint: http://localhost:5000/api/copilot/retrieval")
    print(f"Health Check: http://localhost:5000/health")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
