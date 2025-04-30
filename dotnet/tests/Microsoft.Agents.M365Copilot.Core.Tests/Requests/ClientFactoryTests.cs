// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Requests
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net;
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Threading;
    using System.Threading.Tasks;
    using Azure.Core;
    using Microsoft.Agents.M365Copilot.Core.Requests;
    using Microsoft.Agents.M365Copilot.Core.Requests.Middleware;
    using Microsoft.Agents.M365Copilot.Core.Tests.Mocks;
    using Microsoft.Kiota.Abstractions.Authentication;
    using Microsoft.Kiota.Http.HttpClientLibrary.Middleware;
    using Microsoft.Kiota.Http.HttpClientLibrary.Middleware.Options;
    using Moq;
    using Xunit;

    public class ClientFactoryTests : IDisposable
    {
        private MockRedirectHandler testHttpMessageHandler;
        private DelegatingHandler[] handlers;
        private const string expectedAccessToken = "copilot-agent-client-factory-infused-token";

        public ClientFactoryTests()
        {
            this.testHttpMessageHandler = new MockRedirectHandler();
            handlers = CopilotClientFactory.CreateDefaultHandlers().ToArray();
        }

        public void Dispose()
        {
            this.testHttpMessageHandler.Dispose();
        }

        // Note:
        // 1. Xunit's IsType doesn't consider inheritance behind the classes.
        // 2. We can't control the order of execution for the tests
        // and 'ClientFactory.DefaultHttpHandler' can easily be modified
        // by other tests since it's a static delegate.

#if IOS || MACOS
        [Fact]
        public void Should_CreatePipeline_Without_CompressionHandler()
        {
            using (RetryHandler retryHandler = (RetryHandler)CopilotClientFactory.CreatePipeline(handlers))
            using (RedirectHandler redirectHandler = (RedirectHandler)retryHandler.InnerHandler)
#if IOS
            using (NSUrlSessionHandler innerMost = (NSUrlSessionHandler)redirectHandler.InnerHandler)
#elif MACOS
            using (Foundation.NSUrlSessionHandler innerMost = (Foundation.NSUrlSessionHandler)redirectHandler.InnerHandler)
#endif
            {
                Assert.NotNull(retryHandler);
                Assert.NotNull(redirectHandler);
                Assert.NotNull(innerMost);
                Assert.IsType<RetryHandler>(retryHandler);
                Assert.IsType<RedirectHandler>(redirectHandler);
#if IOS
                Assert.IsType<NSUrlSessionHandler>(innerMost);
#elif MACOS
                Assert.IsType<Foundation.NSUrlSessionHandler>(innerMost);
#endif
            }
        }
#else
        [Fact]
        public void Should_CreatePipeline_Without_HttpMessageHandlerInput()
        {
            using UriReplacementHandler<UriReplacementHandlerOption> uriReplacementHandler = (UriReplacementHandler<UriReplacementHandlerOption>)CopilotClientFactory.CreatePipeline(handlers, new MockRedirectHandler());
            using RetryHandler retryHandler = (RetryHandler)uriReplacementHandler.InnerHandler;
            using RedirectHandler redirectHandler = (RedirectHandler)retryHandler.InnerHandler;
            using ParametersNameDecodingHandler odataQueryHandler = (ParametersNameDecodingHandler)redirectHandler.InnerHandler;
            using UserAgentHandler userAgentHandler = (UserAgentHandler)odataQueryHandler.InnerHandler;
            using HeadersInspectionHandler headersInspectionHandler = (HeadersInspectionHandler)userAgentHandler.InnerHandler;
            using BodyInspectionHandler bodyInspectionHandler = (BodyInspectionHandler)headersInspectionHandler.InnerHandler;
            using CopilotAgentsTelemetryHandler telemetryHandler = (CopilotAgentsTelemetryHandler)bodyInspectionHandler.InnerHandler;
            using MockRedirectHandler innerMost = (MockRedirectHandler)telemetryHandler.InnerHandler;

            Assert.NotNull(telemetryHandler);
            Assert.NotNull(userAgentHandler);
            Assert.NotNull(headersInspectionHandler);
            Assert.NotNull(odataQueryHandler);
            Assert.NotNull(retryHandler);
            Assert.NotNull(redirectHandler);
            Assert.NotNull(innerMost);
            Assert.IsType<CopilotAgentsTelemetryHandler>(telemetryHandler);
            Assert.IsType<ParametersNameDecodingHandler>(odataQueryHandler);
            Assert.IsType<HeadersInspectionHandler>(headersInspectionHandler);
            Assert.IsType<UserAgentHandler>(userAgentHandler);
            Assert.IsType<RetryHandler>(retryHandler);
            Assert.IsType<RedirectHandler>(redirectHandler);
            Assert.True(innerMost is HttpMessageHandler);
        }
#endif

        [Fact]
        public void CreatePipelineWithHttpMessageHandlerInput()
        {
            using UriReplacementHandler<UriReplacementHandlerOption> uriReplacementHandler = (UriReplacementHandler<UriReplacementHandlerOption>)CopilotClientFactory.CreatePipeline(handlers, new MockRedirectHandler());
            using RetryHandler retryHandler = (RetryHandler)uriReplacementHandler.InnerHandler;
            using RedirectHandler redirectHandler = (RedirectHandler)retryHandler.InnerHandler;
            using ParametersNameDecodingHandler odataQueryHandler = (ParametersNameDecodingHandler)redirectHandler.InnerHandler;
            using UserAgentHandler userAgentHandler = (UserAgentHandler)odataQueryHandler.InnerHandler;
            using HeadersInspectionHandler headersInspectionHandler = (HeadersInspectionHandler)userAgentHandler.InnerHandler;
            using BodyInspectionHandler bodyInspectionHandler = (BodyInspectionHandler)headersInspectionHandler.InnerHandler;
            using CopilotAgentsTelemetryHandler telemetryHandler = (CopilotAgentsTelemetryHandler)bodyInspectionHandler.InnerHandler;
            using MockRedirectHandler innerMost = (MockRedirectHandler)telemetryHandler.InnerHandler;

            Assert.NotNull(telemetryHandler);
            Assert.NotNull(userAgentHandler);
            Assert.NotNull(headersInspectionHandler);
            Assert.NotNull(odataQueryHandler);
            Assert.NotNull(retryHandler);
            Assert.NotNull(redirectHandler);
            Assert.NotNull(innerMost);
            Assert.IsType<CopilotAgentsTelemetryHandler>(telemetryHandler);
            Assert.IsType<ParametersNameDecodingHandler>(odataQueryHandler);
            Assert.IsType<HeadersInspectionHandler>(headersInspectionHandler);
            Assert.IsType<RetryHandler>(retryHandler);
            Assert.IsType<UserAgentHandler>(userAgentHandler);
            Assert.IsType<RedirectHandler>(redirectHandler);
            Assert.IsType<MockRedirectHandler>(innerMost);
        }

        [Fact]
        public void CreatePipelineWithoutPipeline()
        {
            using (MockRedirectHandler handler = (MockRedirectHandler)CopilotClientFactory.CreatePipeline(null, this.testHttpMessageHandler))
            {
                Assert.NotNull(handler);
                Assert.IsType<MockRedirectHandler>(handler);
            }
        }

        [Fact]
        public void CreatePipeline_Should_Throw_Exception_With_Duplicate_Handlers()
        {
            var handlers = CopilotClientFactory.CreateDefaultHandlers();
            handlers.Add(new CopilotAgentsTelemetryHandler());

            ArgumentException exception = Assert.Throws<ArgumentException>(() => CopilotClientFactory.CreatePipeline(handlers));

            Assert.Contains($"{typeof(CopilotAgentsTelemetryHandler)} has a duplicate handler.", exception.Message);
        }

        [Fact]
        public void CreateClient_CustomHttpHandlingBehaviors()
        {
            var timeout = TimeSpan.FromSeconds(200);
            var baseAddress = new Uri("https://localhost");
            var cacheHeader = new CacheControlHeaderValue();

            using (HttpClient client = CopilotClientFactory.Create())
            {
                client.Timeout = timeout;
                client.BaseAddress = baseAddress;
                Assert.NotNull(client);
                Assert.Equal(client.Timeout, timeout);
                Assert.Equal(client.BaseAddress, baseAddress);
            }
        }

        [Fact]
        public void CreateClient_SelectedCloud()
        {
            using (HttpClient httpClient = CopilotClientFactory.Create(version: "beta", nationalCloud: CopilotClientFactory.Germany_Cloud))
            {
                Assert.NotNull(httpClient);
                Uri clouldEndpoint = new Uri("https://graph.microsoft.de/beta/");
                Assert.Equal(httpClient.BaseAddress, clouldEndpoint);
                Assert.Equal(httpClient.Timeout, TimeSpan.FromSeconds(100));
            }
        }

        [Fact]
        public void CreateClient_SelectedCloudWithExceptions()
        {
            string nation = "Canada";
            try
            {
                HttpClient httpClient = CopilotClientFactory.Create(nationalCloud: nation);
            }
            catch (ArgumentException exception)
            {
                Assert.IsType<ArgumentException>(exception);
                Assert.Equal(exception.Message, String.Format("{0} is an unexpected national cloud.", nation));
            }
        }

        [Fact]
        public void CreateClient_WithHandlers()
        {
            using (HttpClient client = CopilotClientFactory.Create(handlers: CopilotClientFactory.CreateDefaultHandlers()))
            {
                Assert.NotNull(client);
            }
        }

        [Fact]
        public async Task SendRequest_RedirectAsync()
        {
            var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post, "http://example.org/foo");
            var redirectResponse = new HttpResponseMessage(HttpStatusCode.MovedPermanently);

            redirectResponse.Headers.Location = new Uri("http://example.org/bar");
            var oKResponse = new HttpResponseMessage(HttpStatusCode.OK);
            this.testHttpMessageHandler.SetHttpResponse(redirectResponse, oKResponse);

            using (HttpClient client = CopilotClientFactory.Create(finalHandler: this.testHttpMessageHandler))
            {
                var response = await client.SendAsync(httpRequestMessage, new CancellationToken());
                Assert.Equal(response, oKResponse);
                Assert.Equal(response.RequestMessage.Method, httpRequestMessage.Method);
                Assert.NotSame(response.RequestMessage, httpRequestMessage);
            }

        }

        [Fact]
        public async Task SendRequest_RetryAsync()
        {
            var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post, "http://example.org/foo");
            httpRequestMessage.Content = new StringContent("Hello World");

            var retryResponse = new HttpResponseMessage(HttpStatusCode.ServiceUnavailable);
            retryResponse.Headers.TryAddWithoutValidation("Retry-After", 30.ToString());
            var response_2 = new HttpResponseMessage(HttpStatusCode.OK);

            this.testHttpMessageHandler.SetHttpResponse(retryResponse, response_2);

            using (HttpClient client = CopilotClientFactory.Create(finalHandler: this.testHttpMessageHandler))
            {
                var response = await client.SendAsync(httpRequestMessage, new CancellationToken());
                Assert.Same(response, response_2);
                IEnumerable<string> values;
                Assert.True(response.RequestMessage.Headers.TryGetValues("Retry-Attempt", out values), "Don't set Retry-Attemp Header");
                Assert.Single(values);
                Assert.Equal(values.First(), 1.ToString());
                Assert.NotSame(response.RequestMessage, httpRequestMessage);
            }

        }

        [Fact]
        public void CreateClient_WithHandlersHasExceptions()
        {
            var pipelineHandlers = CopilotClientFactory.CreateDefaultHandlers().ToArray();
            pipelineHandlers[pipelineHandlers.Length - 1] = null;
            try
            {
                HttpClient client = CopilotClientFactory.Create(handlers: pipelineHandlers);
            }
            catch (ArgumentNullException exception)
            {
                Assert.IsType<ArgumentNullException>(exception);
                Assert.Equal("handlers", exception.ParamName);
            }
        }

        [Fact]
        public void CreateClient_WithInnerHandlerReference()
        {
            DelegatingHandler[] handlers = new DelegatingHandler[1];
            handlers[0] = new RetryHandler()
            {
                InnerHandler = this.testHttpMessageHandler
            };
            // Creation should ignore the InnerHandler on RetryHandler
            HttpClient client = CopilotClientFactory.Create(handlers: handlers);
            Assert.NotNull(client);
            Assert.IsType<SocketsHttpHandler>(handlers[0].InnerHandler);
        }

        [Fact]
        public void CreatePipelineWithFeatureFlags_Should_Set_FeatureFlag_For_Default_Handlers()
        {
            FeatureFlag expectedFlag = FeatureFlag.RetryHandler | FeatureFlag.RedirectHandler;
            string expectedFlagHeaderValue = Enum.Format(typeof(FeatureFlag), expectedFlag, "x");
            var handlers = CopilotClientFactory.CreateDefaultHandlers();
            var pipelineWithHandlers = CopilotClientFactory.CreatePipelineWithFeatureFlags(handlers);

            Assert.NotNull(pipelineWithHandlers.Pipeline);
            Assert.True(pipelineWithHandlers.FeatureFlags.HasFlag(expectedFlag));
        }

        [Fact]
        public void CreatePipelineWithFeatureFlags_Should_Set_FeatureFlag_For_Speficied_Handlers()
        {
            FeatureFlag expectedFlag = FeatureFlag.RetryHandler;
            var handlers = CopilotClientFactory.CreateDefaultHandlers();
            //Exclude the redirect handler for this test
            handlers = handlers.Where(handler => !handler.GetType().Equals(typeof(RedirectHandler))).ToList();
            var pipelineWithHandlers = CopilotClientFactory.CreatePipelineWithFeatureFlags(handlers);

            Assert.NotNull(pipelineWithHandlers.Pipeline);
            Assert.True(pipelineWithHandlers.FeatureFlags.HasFlag(expectedFlag));
        }

        [Theory]
        [InlineData(true)]
        [InlineData(false)]
        public void CreateClientWithFinalHandlerDisposesTheFinalHandler(bool shouldDisposeHandler)
        {
            // Arrange
            var finalHandler = new MockHttpHandler();

            // Act
            using (var client = CopilotClientFactory.Create(handlers: CopilotClientFactory.CreateDefaultHandlers(), finalHandler: finalHandler, disposeHandler: shouldDisposeHandler))
            {
                Assert.NotNull(client);
            }

            // Assert
            Assert.Equal(shouldDisposeHandler, finalHandler.Disposed);
        }

        [Fact]
        public async Task CreateClientWithAuthenticationProviderAuthenticatesRequestAsync()
        {
            var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post, "https://graph.microsoft.com/me");
            var responseMessage = new HttpResponseMessage(HttpStatusCode.OK);
            this.testHttpMessageHandler.SetHttpResponse(responseMessage);

            var authProvider = new Mock<BaseBearerTokenAuthenticationProvider>(new MockAccessTokenProvider("token").Object);

            using (HttpClient client = CopilotClientFactory.Create(authenticationProvider: authProvider.Object, finalHandler: this.testHttpMessageHandler))
            {
                var response = await client.SendAsync(httpRequestMessage, new CancellationToken());
                Assert.Equal("Bearer token", response.RequestMessage.Headers.Authorization.ToString());
            }
        }

        [Fact]
        public async Task CreateClientWithTokenCredentialAuthenticatesRequestAsync()
        {
            var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post, "https://graph.microsoft.com/me");
            var responseMessage = new HttpResponseMessage(HttpStatusCode.OK);
            this.testHttpMessageHandler.SetHttpResponse(responseMessage);

            var tokenCredential = new Mock<TokenCredential>();
            tokenCredential.Setup(x => x.GetTokenAsync(It.IsAny<TokenRequestContext>(), It.IsAny<CancellationToken>()))
                .ReturnsAsync(new AccessToken("mockToken", DateTimeOffset.UtcNow.AddMinutes(10)));

            using (HttpClient client = CopilotClientFactory.Create(tokenCredential: tokenCredential.Object, finalHandler: this.testHttpMessageHandler))
            {
                var response = await client.SendAsync(httpRequestMessage, new CancellationToken());
                Assert.Equal("Bearer mockToken", response.RequestMessage.Headers.Authorization.ToString());
            }
        }

        private class MockHttpHandler : HttpMessageHandler
        {
            public bool Disposed;

            protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
            {
                throw new NotImplementedException();
            }

            protected override void Dispose(bool disposing)
            {
                Disposed = true;
                base.Dispose(disposing);
            }
        }
    }
}