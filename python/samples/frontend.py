"""
Frontend Client - Authenticates user and calls Backend API
User signs in here, gets token for backend API, then calls backend
"""
import os
from datetime import datetime

import requests
from azure.identity import InteractiveBrowserCredential
from dotenv import load_dotenv

load_dotenv()

# Frontend app registration (your existing app)
FRONTEND_CLIENT_ID = os.getenv("FRONTEND_CLIENT_ID")  # Your existing: 048d1f20-ad35-44d4-a382-b7edbfaef97f
BACKEND_CLIENT_ID = os.getenv("BACKEND_CLIENT_ID")  # New backend API app
TENANT_ID = os.getenv("TENANT_ID")
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:5000")


def main():
    """
    Frontend client that:
    1. Authenticates user with Interactive Browser
    2. Gets token for backend API (not Graph!)
    3. Calls backend API with user token
    4. Backend uses OBO to get token for Copilot API
    """
    print("🚀 Starting OBO Flow Demo - Frontend Client")
    print(f"   Frontend Client ID: {FRONTEND_CLIENT_ID}")
    print(f"   Backend API Client ID: {BACKEND_CLIENT_ID}")
    print(f"   Backend API URL: {BACKEND_API_URL}")
    print(f"   Tenant ID: {TENANT_ID}\n")
    
    # Step 1: Authenticate user with Interactive Browser
    print("📝 Step 1: Authenticating user...")
    print(f"   Requesting token with audience: api://{BACKEND_CLIENT_ID}")
    print(f"   🌐 Browser will open automatically for authentication...")
    
    # Create Interactive Browser credential (better UX than Device Code)
    credentials = InteractiveBrowserCredential(
        client_id=FRONTEND_CLIENT_ID,
        tenant_id=TENANT_ID
    )
    
    # IMPORTANT: Request token for backend API, not Graph!
    # This is the key difference in OBO flow
    backend_scope = f"api://{BACKEND_CLIENT_ID}/.default"
    
    try:
        token = credentials.get_token(backend_scope)
        print(f"\n✅ User authenticated successfully!")
        print(f"   Token audience: Backend API (api://{BACKEND_CLIENT_ID})")
        print(f"   Token expires at: {datetime.fromtimestamp(token.expires_on)}")
        
    except Exception as e:
        print(f"\n❌ Authentication failed: {e}")
        print(f"\n⚠️  Make sure:")
        print(f"   1. Backend API app exposes 'api://{BACKEND_CLIENT_ID}' scope")
        print(f"   2. Frontend app has permission to access backend API")
        print(f"   3. Conditional Access policy allows your device (or is disabled)")
        return
    
    # Step 2: Call backend API with user token
    print(f"\n📝 Step 2: Calling Backend API...")
    print(f"   URL: {BACKEND_API_URL}/api/copilot/retrieval")
    
    headers = {
        "Authorization": f"Bearer {token.token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": "What are the methods of Watering",
        "dataSource": "SharePoint"
    }
    
    try:
        print(f"   Query: {payload['query']}")
        print(f"   Data Source: {payload['dataSource']}")
        
        response = requests.post(
            f"{BACKEND_API_URL}/api/copilot/retrieval",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            
            print(f"\n{'='*60}")
            print("✅ SUCCESS! OBO Flow Completed")
            print(f"{'='*60}")
            print(f"\n📊 Results:")
            print(f"   Total hits: {result.get('total_hits', 0)}")
            
            results = result.get('results', [])
            for idx, hit in enumerate(results[:3], 1):  # Show first 3
                print(f"\n   Result {idx}:")
                print(f"   URL: {hit.get('web_url', 'N/A')}")
                if hit.get('extracts'):
                    for extract in hit['extracts'][:1]:  # Show first extract
                        text = extract.get('text', '')
                        preview = text[:150] + "..." if len(text) > 150 else text
                        print(f"   Text: {preview}")
            
            print(f"\n{'='*60}\n")
            
        else:
            print(f"\n❌ Backend API returned error:")
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print(f"\n❌ Could not connect to backend API at {BACKEND_API_URL}")
        print(f"   Make sure backend API is running:")
        print(f"   python backend_api.py")
        
    except Exception as e:
        print(f"\n❌ Error calling backend API: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
