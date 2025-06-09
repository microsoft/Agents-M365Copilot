# Microsoft 365 Copilot APIs .NET Client Library

Integrate the Microsoft 365 Copilot APIs into your .NET project!

The Microsoft 365 Copilot APIs. NET Client Library targets .NetStandard 2.0.

> **Note:**
>
>Because the Microsoft 365 Copilot APIs in the beta endpoint are subject to breaking changes, don't use this preview release of the client libraries in production apps.

## Installation via NuGet

The Microsoft 365 Copilot APIs .NET client libraries are available in the following NuGet packages:

- [Microsoft.Agents.M365Copilot.Beta](https://github.com/microsoft/Agents-M365Copilot/tree/main/dotnet/src/Microsoft.Agents.M365Copilot.Beta): Contains the models and request builders for accessing the beta endpoint. Microsoft.Agents.M365Copilot.Beta has a dependency on Microsoft.Agents.M365Copilot.Core.
- [Microsoft.Agents.M365Copilot.Core](https://github.com/microsoft/Agents-M365Copilot/tree/main/dotnet/src/Microsoft.Agents.M365Copilot.Core): The core library for making calls to the Copilot APIs.

To install the client libraries via NuGet:

* Search for `Microsoft.Agents.M365Copilot.Beta` in the NuGet Library, or
* Type `Install-Package Microsoft.Agents.M365Copilot.Beta` into the Package Manager Console.

## Create a Copilot APIs client and make an API call

The following code example shows how to create an instance of a Microsoft 365 Copilot APIs client with an authentication provider in the supported languages. The authentication provider handles acquiring access tokens for the application. Many different authentication providers are available for each language and platform. The different authentication providers support different client scenarios. For details about which provider and options are appropriate for your scenario, see [Choose an Authentication Provider](https://learn.microsoft.com/graph/sdks/choose-authentication-providers). 

The example also shows how to make a call to the Microsoft 365 Copilot Retrieval API. To call this API, you first need to create a request object and then run the POST method on the request.

The client ID is the app registration ID that is generated when you [register your app in the Azure portal](https://learn.microsoft.com/graph/auth-register-app-v2).

**NOTE:**
    
> Your tenant must have a Microsoft 365 Copilot license.

```csharp

using Azure.Identity;
using Microsoft.Agents.M365Copilot.Beta;
using Microsoft.Agents.M365Copilot.Beta.Models;
using Microsoft.Agents.M365Copilot.Beta.Copilot.Retrieval;

var scopes = new[] {"Files.Read.All", "Sites.Read.All"}; 
 
// Multi-tenant apps can use "common", 
// single-tenant apps must use the tenant ID from the Azure portal 
var tenantId = "YOUR_TENANT_ID"; 
 
// Value from app registration 
var clientId = "YOUR_CLIENT_ID"; 
 
// using Azure.Identity; 
var deviceCodeCredentialOptions = new DeviceCodeCredentialOptions 
{ 
   ClientId = clientId, 
   TenantId = tenantId, 
   // Callback function that receives the user prompt 
   // Prompt contains the generated device code that user must 
   // enter during the auth process in the browser 
   DeviceCodeCallback = (deviceCodeInfo, cancellationToken) => 
   { 
       Console.WriteLine(deviceCodeInfo.Message); 
       return Task.CompletedTask; 
   }, 
}; 
 
// https://learn.microsoft.com/dotnet/api/azure.identity.devicecodecredential 
var deviceCodeCredential = new DeviceCodeCredential(deviceCodeCredentialOptions); 

//Create the client with explicit base URL 
var baseURL = “https://graph.microsoft.com/beta”; 
AgentsM365CopilotBetaServiceClient client = new AgentsM365CopilotBetaServiceClient (deviceCodeCredential, scopes, baseURL); 

try
{
  var requestBody = new RetrievalPostRequestBody
  {
      DataSource = RetrievalDataSource.SharePoint,
      QueryString = "What is the latest in my organization?",
      MaximumNumberOfResults = 10
  };
  
  var result = await client.Copilot.Retrieval.PostAsync(requestBody);
  Console.WriteLine($"Retrieval post: {result}");

  if (result != null)
  {
    Console.WriteLine("Retrieval response received successfully");
    Console.WriteLine("\nResults:");
    Console.WriteLine(result.RetrievalHits.Count.ToString());
    if (result.RetrievalHits != null)
    {
       foreach (var hit in result.RetrievalHits)
       {
         Console.WriteLine("\n---");
         Console.WriteLine($"Web URL: {hit.WebUrl}");
         Console.WriteLine($"Resource Type: {hit.ResourceType}");
         if (hit.Extracts != null && hit.Extracts.Any())
         {
            Console.WriteLine("\nExtracts:");
            foreach (var extract in hit.Extracts)
            {
              Console.WriteLine($"  {extract.Text}");
            }
          }
          if (hit.SensitivityLabel != null)
          {
            Console.WriteLine("\nSensitivity Label:");
            Console.WriteLine($"  Display Name: {hit.SensitivityLabel.DisplayName}");
            Console.WriteLine($"  Tooltip: {hit.SensitivityLabel.Tooltip}");
            Console.WriteLine($"  Priority: {hit.SensitivityLabel.Priority}");
            Console.WriteLine($"  Color: {hit.SensitivityLabel.Color}");
            if (hit.SensitivityLabel.IsEncrypted.HasValue)
            {
              Console.WriteLine($"  Is Encrypted: {hit.SensitivityLabel.IsEncrypted.Value}");
            }
          }
        }
      }
      else
      {
        Console.WriteLine("No retrieval hits found in the response");
      }
  }
}
catch (Exception ex)
{
    Console.WriteLine($"Error making retrieval request: {ex.Message}");
    Console.Error.WriteLine(ex);
}
 
```

## Issues

To view or log issues, see [issues](https://github.com/microsoft/Agents-M365Copilot/issues).

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.


