// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Requests
{
    using Microsoft.Agents.M365Copilot.Core.Tests.Mocks;
    using Xunit;
    public class BaseClientTests
    {
        private MockAuthenticationProvider authenticationProvider;
        private MockTokenCredential tokenCredential;

        public BaseClientTests()
        {
            this.authenticationProvider = new MockAuthenticationProvider();
            this.tokenCredential = new MockTokenCredential();
        }

        [Fact]
        public void BaseClient_InitializeBaseUrlWithoutTrailingSlash()
        {
            var expectedBaseUrl = "https://localhost";

            var baseClient = new BaseClient(expectedBaseUrl, this.authenticationProvider.Object);

            Assert.Equal(expectedBaseUrl, baseClient.RequestAdapter.BaseUrl);
        }

        [Fact]
        public void BaseClient_InitializeBaseUrlTrailingSlash()
        {
            var expectedBaseUrl = "https://localhost";

            var baseClient = new BaseClient("https://localhost/", this.authenticationProvider.Object);

            Assert.Equal(expectedBaseUrl, baseClient.RequestAdapter.BaseUrl);
        }
    }
}
