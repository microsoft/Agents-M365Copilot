# Microsoft Agents M365 Copilot Core SDK for Typescript

Get started with the Microsoft Agents M365 Copilot SDK for Typescript by integrating the [Microsoft Agents M365 Copilot API](https://docs.microsoft.com/graph/overview) into your Typescript application!

> **Note:** this package contains the core feature of the TypeScript SDK. To get the full experience checkout [the v1 SDK](https://github.com/microsoftgraph/msgraph-sdk-typescript) and [the beta SDK](https://github.com/microsoftgraph/msgraph-beta-sdk-typescript).
>
> **Note:** the Microsoft Agents M365 Copilot Typescript SDK is currently in Pre-Release.

## 1. Installation

```shell
# this will install the core package
npm install @microsoft/msgraph-sdk-core
```

## 2. Getting started

> Note: we are working to add the getting started information for Typescript to our public documentation, in the meantime the following sample should help you getting started.

### 2.1 Register your application

Register your application by following the steps at [Register your app with the Microsoft Identity Platform](https://docs.microsoft.com/graph/auth-register-app-v2).

### 2.2 Create an AuthenticationProvider object

An instance of the **FetchClient** class handles making requests to the service. To create a new instance of this class, you need to provide an instance of **AuthenticationProvider**, which can authenticate requests to Microsoft Agents M365 Copilot.

<!-- TODO restore that and remove the snippets below once the SDK hits GA and the public documentation has been updated -->
<!-- For an example of how to get an authentication provider, see [choose a Microsoft Agents M365 Copilot authentication provider](https://docs.microsoft.com/graph/sdks/choose-authentication-providers?tabs=typescript). -->

#### 2.2.1 Authorization Code Provider

```TypeScript
// @azure/identity
const credential = new AuthorizationCodeCredential(
  'YOUR_TENANT_ID',
  'YOUR_CLIENT_ID',
  'YOUR_CLIENT_SECRET',
  'AUTHORIZATION_CODE',
  'REDIRECT_URL',
);

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["User.Read"]);
```

#### 2.2.2 Client Credentials Provider

##### With a certificate

```TypeScript
// @azure/identity
const credential = new ClientCertificateCredential(
  'YOUR_TENANT_ID',
  'YOUR_CLIENT_ID',
  'YOUR_CERTIFICATE_PATH',
);

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["https://graph.microsoft.com/.default"]);
```

##### With a secret

```TypeScript
// @azure/identity
const credential = new ClientSecretCredential(
  'YOUR_TENANT_ID',
  'YOUR_CLIENT_ID',
  'YOUR_CLIENT_SECRET',
);

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["https://graph.microsoft.com/.default"]);
```

#### 2.2.3 On-behalf-of provider

```TypeScript
// @azure/identity
const credential = new OnBehalfOfCredential({
  tenantId: 'YOUR_TENANT_ID',
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET',
  userAssertionToken: 'JWT_TOKEN_TO_EXCHANGE',
});

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["https://graph.microsoft.com/.default"]);
```

#### 2.2.4 Device code provider

```TypeScript
// @azure/identity
const credential = new DeviceCodeCredential({
  tenantId: 'YOUR_TENANT_ID',
  clientId: 'YOUR_CLIENT_ID',
  userPromptCallback: (info) => {
    console.log(info.message);
  },
});

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["User.Read"]);
```

#### 2.2.5 Interactive provider

```TypeScript
// @azure/identity
const credential = new InteractiveBrowserCredential({
  tenantId: 'YOUR_TENANT_ID',
  clientId: 'YOUR_CLIENT_ID',
  redirectUri: 'http://localhost',
});

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["User.Read"]);
```

#### 2.2.6 Username/password provider

```TypeScript
// @azure/identity
const credential = new UsernamePasswordCredential(
  'YOUR_TENANT_ID',
  'YOUR_CLIENT_ID',
  'YOUR_USER_NAME',
  'YOUR_PASSWORD',
);

// @microsoft/kiota-authentication-azure
const authProvider = new AzureIdentityAuthenticationProvider(credential, ["User.Read"]);
```

## 3. Make requests against the service

TODO: document how the fetch client augmented with middleware handlers can be used to make arbitrary requests.

## 4. Documentation

For more detailed documentation, see:

- [Known issues](https://github.com/microsoft/Agents-M365Copilot/issues)
- [Contributions](https://github.com/microsoft/Agents-M365Copilot?tab=readme-ov-file#contributing)

## 5. Issues

For known issues, see [issues](https://github.com/microsoft/Agents-M365Copilot/issues).

## 6. Contributions

The Microsoft Agents M365 Copilot SDK is open for contribution. To contribute to this project, see [Contributing](https://github.com/microsoft/Agents-M365Copilot?tab=readme-ov-file#contributing).

## 7. License

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the [MIT license](LICENSE).

## 8. Third-party notices

[Third-party notices](THIRD%20PARTY%20NOTICES)
