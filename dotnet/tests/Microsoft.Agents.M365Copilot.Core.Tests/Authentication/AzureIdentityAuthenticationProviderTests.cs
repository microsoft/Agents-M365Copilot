// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Authentication
{
    using Azure.Core;
    using Microsoft.Agents.M365Copilot.Core.Authentication;
    using Moq;
    using Xunit;

    public class AzureIdentityAuthenticationProviderTests
    {
        [Fact]
        public void AzureIdentityAuthenticationProvider_WithDefaultParameters_CreatesInstance()
        {
            // Arrange
            var mockCredential = new Mock<TokenCredential>();

            // Act
            var provider = new AzureIdentityAuthenticationProvider(
                credential: mockCredential.Object,
                allowedHosts: null,
                observabilityOptions: null,
                isCaeEnabled: true,
                scopes: new[] { "https://graph.microsoft.com/.default" });

            // Assert
            Assert.NotNull(provider);
        }

        [Fact]
        public void AzureIdentityAuthenticationProvider_WithAllParameters_CreatesInstance()
        {
            // Arrange
            var mockCredential = new Mock<TokenCredential>();
            var allowedHosts = new[] { "graph.microsoft.com" };
            var observabilityOptions = new Microsoft.Kiota.Authentication.Azure.ObservabilityOptions();
            var scopes = new[] { "User.Read", "Mail.Read" };

            // Act
            var provider = new AzureIdentityAuthenticationProvider(
                credential: mockCredential.Object,
                allowedHosts: allowedHosts,
                observabilityOptions: observabilityOptions,
                isCaeEnabled: true,
                scopes: scopes);

            // Assert
            Assert.NotNull(provider);
        }

        [Fact]
        public void AzureIdentityAuthenticationProvider_WithCAEDisabled_CreatesInstance()
        {
            // Arrange
            var mockCredential = new Mock<TokenCredential>();
            var scopes = new[] { "User.Read" };

            // Act
            var provider = new AzureIdentityAuthenticationProvider(
                credential: mockCredential.Object,
                allowedHosts: null,
                observabilityOptions: null,
                isCaeEnabled: false,
                scopes: scopes);

            // Assert
            Assert.NotNull(provider);
        }

        [Fact]
        public void AzureIdentityAuthenticationProvider_ObsoleteConstructor_CreatesInstance()
        {
            // Arrange
            var mockCredential = new Mock<TokenCredential>();
            var allowedHosts = new[] { "graph.microsoft.com" };
            var observabilityOptions = new Microsoft.Kiota.Authentication.Azure.ObservabilityOptions();
            var scopes = new[] { "User.Read" };

            // Act
            #pragma warning disable CS0618 // Type or member is obsolete
            var provider = new AzureIdentityAuthenticationProvider(
                mockCredential.Object,
                allowedHosts,
                observabilityOptions,
                scopes);
            #pragma warning restore CS0618 // Type or member is obsolete

            // Assert
            Assert.NotNull(provider);
        }

        [Fact]
        public void AzureIdentityAuthenticationProvider_WithNullOptionalParameters_CreatesInstance()
        {
            // Arrange
            var mockCredential = new Mock<TokenCredential>();

            // Act
            var provider = new AzureIdentityAuthenticationProvider(
                credential: mockCredential.Object,
                allowedHosts: null,
                observabilityOptions: null,
                isCaeEnabled: true,
                scopes: new[] { "User.Read" });

            // Assert
            Assert.NotNull(provider);
        }

        [Fact]
        public void AzureIdentityAuthenticationProvider_InheritsFromBaseBearerTokenAuthenticationProvider()
        {
            // Arrange
            var mockCredential = new Mock<TokenCredential>();

            // Act
            var provider = new AzureIdentityAuthenticationProvider(
                credential: mockCredential.Object,
                allowedHosts: null,
                observabilityOptions: null,
                isCaeEnabled: true,
                scopes: new[] { "https://graph.microsoft.com/.default" });

            // Assert
            Assert.IsAssignableFrom<Microsoft.Kiota.Abstractions.Authentication.BaseBearerTokenAuthenticationProvider>(provider);
        }
    }
}
