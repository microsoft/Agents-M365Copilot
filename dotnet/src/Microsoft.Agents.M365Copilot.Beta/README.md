# Microsoft 365 Copilot APIs .NET Beta Client Library

Integrate the Microsoft 365 Copilot APIs into your .NET project!

The Microsoft 365 Copilot APIs. NET Beta Client Library targets .NetStandard 2.0.

> **Note:**
>
>Because the Microsoft 365 Copilot APIs in the beta endpoint are subject to breaking changes, don't use a preview release of the client library in production apps.

## Installation via NuGet

To install the client library via NuGet:

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
## Documentation and resources

- [Microsoft 365 Copilot APIs](https://aka.ms/M365CopilotAPIs)
 
## Issues

To view or log issues, see [issues](https://github.com/microsoft/agents-m365copilot/issues).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Other resources

- NuGet Package: [https://www.nuget.org/packages/Microsoft.Agents.M365Copilot.Beta](https://www.nuget.org/packages/Microsoft.Agents.M365Copilot.Beta)

## Building library locally

If you are looking to build the library locally for the purposes of contributing code or running tests, you will need to:

- Have the .NET Core SDK (> 1.0) installed
- Run `dotnet restore` from the command line in your package directory
- Run `nuget restore` and `msbuild` from CLI or run Build from Visual Studio to restore Nuget packages and build the project

> Run `dotnet build -p:IncludeMauiTargets=true` if you wish to build the MAUI targets for the projects as well.

## License

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the MIT [license](https://github.com/microsoft/Agents-M365Copilot/blob/main/LICENSE).