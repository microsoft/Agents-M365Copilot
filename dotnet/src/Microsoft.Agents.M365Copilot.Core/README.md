# Microsoft Agents M365 Copilot Core .NET Core Client Library

The Microsoft Agents M365 Copilot .NET Core Client Library contains core classes and interfaces used by [Microsoft Agents M365 Copilot Library](https://github.com/microsoft/agents-m365copilot/dotnet) to send native HTTP requests to [Microsoft Agents M365 Copilot API](https://graph.microsoft.com). The latest core client library targets .NetStandard 2.0.

## Getting started

### 1. Register your application

Register your application to use Microsoft Agents M365 Copilot API by following the steps at [Register your application with the Microsoft identity platform](https://docs.microsoft.com/en-us/graph/auth-register-app-v2).

### 2. Authenticate for the Microsoft Agents M365 Copilot service

The Microsoft Agents M365 Copilot .NET Client Library supports the use of TokenCredential classes in the [Azure.Identity](https://www.nuget.org/packages/Azure.Identity) library.

You can read more about available Credential classes [here](https://docs.microsoft.com/en-us/dotnet/api/overview/azure/identity-readme#key-concepts) and examples on how to quickly setup TokenCredential instances can be found [here](https://github.com/microsoftgraph/msgraph-sdk-dotnet/blob/main/docs/tokencredentials.md).

The recommended library for authenticating against Microsoft Identity (Azure AD) is [MSAL](https://github.com/AzureAD/microsoft-authentication-library-for-dotnet).

For an example of authenticating a UWP app using the V2 Authentication Endpoint, see the [Microsoft Graph UWP Connect Library](https://github.com/OfficeDev/Microsoft-Graph-UWP-Connect-Library).

### 3. Example application

Use the [application](../Microsoft.Agents.M365Copilot.App) project to see how to set up the client and use it to make calls to the Copilot endpoints

## Issues

To view or log issues, see [issues](https://github.com/microsoft/agents-m365copilot/issues).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Other resources

- NuGet Package: [https://www.nuget.org/packages/Microsoft.Agents.M365Copilot.Core](https://www.nuget.org/packages/Microsoft.Agents.M365Copilot.Core)

## Building library locally

If you are looking to build the library locally for the purposes of contributing code or running tests, you will need to:

- Have the .NET Core SDK (> 1.0) installed
- Run `dotnet restore` from the command line in your package directory
- Run `nuget restore` and `msbuild` from CLI or run Build from Visual Studio to restore Nuget packages and build the project

> Run `dotnet build -p:IncludeMauiTargets=true` if you wish to build the MAUI targets for the projects as well.

## License

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the MIT [license](LICENSE.txt). See [Third Party Notices](https://github.com/microsoft/agents-m365copilot/blob/main/THIRD%20PARTY%20NOTICES) for information on the packages referenced via NuGet.
