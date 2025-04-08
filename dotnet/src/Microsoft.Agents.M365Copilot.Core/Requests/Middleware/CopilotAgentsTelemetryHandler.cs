// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Requests.Middleware
{
    using System;
    using System.Net.Http;
    using System.Reflection;
    using System.Runtime.InteropServices;
    using System.Threading;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Extensions;

    /// <summary>
    /// A <see cref="DelegatingHandler"/> implementation that telemetry for copilot.
    /// </summary>
    /// <remarks>
    /// The <see cref="ClientOptions"/> constructor.
    /// </remarks>
    /// <param name="clientOptions"></param>
    public class CopilotAgentsTelemetryHandler(ClientOptions clientOptions = null) : DelegatingHandler
    {
        /// The version for current assembly.
        private static Version assemblyVersion = typeof(CopilotAgentsTelemetryHandler).GetTypeInfo().Assembly.GetName().Version;

        /// The value for the SDK version header.
        private static readonly string SdkVersionHeaderValue = string.Format(
                    CoreConstants.Headers.SdkVersionHeaderValueFormatString,
                    assemblyVersion.Major,
                    assemblyVersion.Minor,
                    assemblyVersion.Build);

        private readonly ClientOptions clientOptions = clientOptions ?? new ClientOptions();

        /// <summary>
        /// Sends a HTTP request.
        /// </summary>
        /// <param name="httpRequest">The <see cref="HttpRequestMessage"/> to be sent.</param>
        /// <param name="cancellationToken">The <see cref="CancellationToken"/> for the request.</param>
        /// <returns></returns>
        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage httpRequest, CancellationToken cancellationToken)
        {
            if (httpRequest == null)
                throw new ArgumentNullException(nameof(httpRequest));

            // Build the service library string from the options
            var serviceLibraryString = string.Empty;
            if (!string.IsNullOrEmpty(clientOptions?.ServiceLibraryClientVersion))
            {
                serviceLibraryString = clientOptions?.ProductPrefix ?? "microsoft-agents-m365copilot-dotnet";
                if (!string.IsNullOrEmpty(clientOptions?.ServiceTargetVersion))
                    serviceLibraryString += $"-{clientOptions?.ServiceTargetVersion}";
                serviceLibraryString += $"/{clientOptions?.ServiceLibraryClientVersion},";
            }

            // Default to the version string we have, otherwise use the ope provided
            var coreLibraryString = SdkVersionHeaderValue;
            if (!string.IsNullOrEmpty(clientOptions?.CoreClientVersion) && !string.IsNullOrEmpty(clientOptions?.ProductPrefix))
            {
                coreLibraryString = $"{clientOptions?.ProductPrefix}-core/{clientOptions?.CoreClientVersion}";
            }

            // Get the features section of the telemetry header
            var features = string.Empty;
            if (Environment.OSVersion != null)
                features += " hostOS=" + Environment.OSVersion + ";" + " hostArch=" + RuntimeInformation.OSArchitecture + ";"; ;
            features += " runtimeEnvironment=" + RuntimeInformation.FrameworkDescription + ";";

            var telemetryString = $"{serviceLibraryString} {coreLibraryString} (featureUsage={Enum.Format(typeof(FeatureFlag), httpRequest.GetFeatureFlags(), "x")};{features})";
            if (!httpRequest.Headers.Contains(CoreConstants.Headers.SdkVersionHeaderName))
                httpRequest.Headers.Add(CoreConstants.Headers.SdkVersionHeaderName, telemetryString);
            if (!httpRequest.Headers.Contains(CoreConstants.Headers.ClientRequestId))
                httpRequest.Headers.Add(CoreConstants.Headers.ClientRequestId, Guid.NewGuid().ToString());

            return base.SendAsync(httpRequest, cancellationToken);
        }

    }
}
