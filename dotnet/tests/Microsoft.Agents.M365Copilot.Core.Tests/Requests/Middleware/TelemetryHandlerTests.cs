// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Requests.Middleware
{
    using System;
    using System.Linq;
    using System.Net.Http;
    using System.Runtime.InteropServices;
    using System.Threading;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Requests;
    using Microsoft.Agents.M365Copilot.Core.Requests.Middleware;
    using Microsoft.Kiota.Abstractions;
    using Microsoft.Kiota.Abstractions.Authentication;
    using Microsoft.Kiota.Http.HttpClientLibrary;
    using Xunit;

    public class CopilotAgentsTelemetryHandlerTests
    {
        private readonly HttpClientRequestAdapter requestAdapter;
        public CopilotAgentsTelemetryHandlerTests()
        {
            requestAdapter = new HttpClientRequestAdapter(new AnonymousAuthenticationProvider());
        }

        [Fact]
        public async Task CopilotAgentsTelemetryHandlerShouldSetTelemetryHeaderWithDefaultsAsync()
        {
            var configuredTelemetryHandler = new CopilotAgentsTelemetryHandler
            {
                InnerHandler = new FakeSuccessHandler()
            };
            var testInvoker = new HttpMessageInvoker(configuredTelemetryHandler);

            // Arrange
            var requestInfo = new RequestInformation
            {
                HttpMethod = Method.GET,
                URI = new Uri("http://localhost")
            };

            // Act and get a request message
            var requestMessage = await requestAdapter.ConvertToNativeRequestAsync<HttpRequestMessage>(requestInfo);
            Assert.Empty(requestMessage.Headers);

            // Act
            var response = await testInvoker.SendAsync(requestMessage, new CancellationToken());

            // Assert
            Assert.True(response.RequestMessage.Headers.Contains(CoreConstants.Headers.SdkVersionHeaderName));
            Assert.True(response.RequestMessage.Headers.Contains(CoreConstants.Headers.ClientRequestId));
            var telemetryHeaderString = response.RequestMessage.Headers.GetValues(CoreConstants.Headers.SdkVersionHeaderName).First();
            Assert.Contains("graph-dotnet-core/", telemetryHeaderString);
            Assert.Contains("(featureUsage=", telemetryHeaderString);
            Assert.Contains($" hostOS={Environment.OSVersion};", telemetryHeaderString);
            Assert.Contains($" hostArch={RuntimeInformation.OSArchitecture};", telemetryHeaderString);
            Assert.Contains($" runtimeEnvironment={RuntimeInformation.FrameworkDescription};", telemetryHeaderString);
        }

        [Fact]
        public async Task CopilotAgentsTelemetryHandlerShouldSetTelemetryHeaderWithCustomConfigurationAsync()
        {
            var clientOptions = new ClientOptions
            {
                CoreClientVersion = "2.0.0",
                ServiceLibraryClientVersion = "3.0.0",
                ServiceTargetVersion = "beta",
                ProductPrefix = "graph-cli"
            };

            var configuredTelemetryHandler = new CopilotAgentsTelemetryHandler(clientOptions)
            {
                InnerHandler = new FakeSuccessHandler()
            };
            var testInvoker = new HttpMessageInvoker(configuredTelemetryHandler);

            // Arrange
            var requestInfo = new RequestInformation
            {
                HttpMethod = Method.GET,
                URI = new Uri("http://localhost")
            };

            // Act and get a request message
            var requestMessage = await requestAdapter.ConvertToNativeRequestAsync<HttpRequestMessage>(requestInfo);
            Assert.Empty(requestMessage.Headers);

            // Act
            var response = await testInvoker.SendAsync(requestMessage, new CancellationToken());

            // Assert
            Assert.True(response.RequestMessage.Headers.Contains(CoreConstants.Headers.SdkVersionHeaderName));
            Assert.True(response.RequestMessage.Headers.Contains(CoreConstants.Headers.ClientRequestId));
            var telemetryHeaderString = response.RequestMessage.Headers.GetValues(CoreConstants.Headers.SdkVersionHeaderName).First();
            Assert.Contains("graph-cli-core/2.0.0", telemetryHeaderString);
            Assert.Contains("graph-cli-beta/3.0.0", telemetryHeaderString);
            Assert.Contains("(featureUsage=", telemetryHeaderString);
            Assert.Contains($" hostOS={Environment.OSVersion};", telemetryHeaderString);
            Assert.Contains($" hostArch={RuntimeInformation.OSArchitecture};", telemetryHeaderString);
            Assert.Contains($" runtimeEnvironment={RuntimeInformation.FrameworkDescription};", telemetryHeaderString);
        }
    }

    internal class FakeSuccessHandler : DelegatingHandler
    {
        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var response = new HttpResponseMessage
            {
                StatusCode = System.Net.HttpStatusCode.OK,
                RequestMessage = request
            };
            return Task.FromResult(response);
        }
    }
}
