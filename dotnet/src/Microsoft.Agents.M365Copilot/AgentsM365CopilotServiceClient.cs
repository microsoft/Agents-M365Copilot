// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net.Http;
    using System.Reflection;
    using Azure.Core;
    using Microsoft.Agents.M365Copilot;
    using Microsoft.Agents.M365Copilot.Core.Requests;
    using Microsoft.Kiota.Abstractions;
    using Microsoft.Kiota.Abstractions.Authentication;

    /// <summary>
    /// A default client implementation.
    /// </summary>
    public class AgentsM365CopilotServiceClient : BaseAgentsM365CopilotServiceClient, IBaseClient, IDisposable
    {
        private static readonly Version assemblyVersion = typeof(AgentsM365CopilotServiceClient).GetTypeInfo().Assembly.GetName().Version;
        private static readonly CopilotClientOptions copilotClientOptions = new()
        {
            ServiceLibraryClientVersion = $"{assemblyVersion.Major}.{assemblyVersion.Minor}.{assemblyVersion.Build}",
            ServiceTargetVersion = string.Empty,
        };

        /// <summary>
        /// Constructs a new <see cref="AgentsM365CopilotServiceClient"/>.
        /// </summary>
        /// <param name="requestAdapter">The custom <see cref="IRequestAdapter"/> to be used for making requests</param>
        /// <param name="baseUrl">The base service URL. For example, "https://graph.microsoft.com/v1.0"</param>
        public AgentsM365CopilotServiceClient(IRequestAdapter requestAdapter, string baseUrl = null) : base(InitializeRequestAdapterWithBaseUrl(requestAdapter, baseUrl))
        {
            this.RequestAdapter = requestAdapter;
        }

        /// <summary>
        /// Constructs a new <see cref="AgentsM365CopilotServiceClient"/>.
        /// </summary>
        /// <param name="tokenCredential">The <see cref="TokenCredential"/> for authenticating request messages.</param>
        /// <param name="scopes">List of scopes for the authentication context.</param>
        /// <param name="baseUrl">The base service URL. For example, "https://graph.microsoft.com/v1.0"</param>
        public AgentsM365CopilotServiceClient(
            TokenCredential tokenCredential,
            IEnumerable<string> scopes = null,
            string baseUrl = null
            ) : this(new Agents.M365Copilot.Core.Authentication.AzureIdentityAuthenticationProvider(tokenCredential, null, null, true, scopes?.ToArray() ?? []), baseUrl)
        {
        }

        /// <summary>
        /// Constructs a new <see cref="AgentsM365CopilotServiceClient"/>.
        /// </summary>
        /// <param name="httpClient">The customized <see cref="HttpClient"/> to be used for making requests</param>
        /// <param name="tokenCredential">The <see cref="TokenCredential"/> for authenticating request messages.</param>
        /// <param name="scopes">List of scopes for the authentication context.</param>
        /// <param name="baseUrl">The base service URL. For example, "https://graph.microsoft.com/v1.0"</param>
        public AgentsM365CopilotServiceClient(
            HttpClient httpClient,
            TokenCredential tokenCredential,
            IEnumerable<string> scopes = null,
            string baseUrl = null
            ) : this(httpClient, new Agents.M365Copilot.Core.Authentication.AzureIdentityAuthenticationProvider(tokenCredential, null, null, true, scopes?.ToArray() ?? []), baseUrl)
        {
        }

        /// <summary>
        /// Constructs a new <see cref="AgentsM365CopilotServiceClient"/>.
        /// </summary>
        /// <param name="authenticationProvider">The <see cref="IAuthenticationProvider"/> for authenticating request messages.</param>
        /// <param name="baseUrl">The base service URL. For example, "https://graph.microsoft.com/v1.0"</param>
        public AgentsM365CopilotServiceClient(
            IAuthenticationProvider authenticationProvider,
            string baseUrl = null
            ) : this(CopilotClientFactory.Create(copilotClientOptions, version: "v1.0"), authenticationProvider, baseUrl)
        {
        }

        /// <summary>
        /// Constructs a new <see cref="AgentsM365CopilotServiceClient"/>.
        /// </summary>
        /// <param name="httpClient">The customized <see cref="HttpClient"/> to be used for making requests</param>
        /// <param name="authenticationProvider">The <see cref="IAuthenticationProvider"/> for authenticating request messages.
        /// Defaults to <see cref="AnonymousAuthenticationProvider"/> so that authentication is handled by custom middleware in the httpClient</param>
        /// <param name="baseUrl">The base service URL. For example, "https://graph.microsoft.com/v1.0"</param>
        public AgentsM365CopilotServiceClient(
            HttpClient httpClient,
            IAuthenticationProvider authenticationProvider = null,
            string baseUrl = null) : this(new BaseRequestAdapter(authenticationProvider ?? new AnonymousAuthenticationProvider(), copilotClientOptions, httpClient: httpClient), baseUrl)
        {
        }

        /// <summary>
        /// Gets the <see cref="IRequestAdapter"/> for sending requests.
        /// </summary>
        public new IRequestAdapter RequestAdapter
        {
            get; set;
        }

        /// <summary>
        /// Cleanup anything as needed
        /// </summary>
        public void Dispose()
        {
            if (this.RequestAdapter is IDisposable disposable)
            {
                disposable.Dispose();
            }
        }

        private static IRequestAdapter InitializeRequestAdapterWithBaseUrl(IRequestAdapter requestAdapter, string baseUrl)
        {
            if (!string.IsNullOrEmpty(baseUrl))
            {
                requestAdapter.BaseUrl = baseUrl;
            }

            return requestAdapter;
        }
    }
}
