// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Requests
{
    using Microsoft.Agents.M365Copilot.Core.Requests;
    using System.Threading;
    using Xunit;

    public class RequestContextTests
    {
        [Fact]
        public void RequestContext_ClientRequestId_CanSetAndGet()
        {
            // Arrange
            var context = new RequestContext();
            var expectedClientRequestId = "test-request-id-123";

            // Act
            context.ClientRequestId = expectedClientRequestId;

            // Assert
            Assert.Equal(expectedClientRequestId, context.ClientRequestId);
        }

        [Fact]
        public void RequestContext_CancellationToken_CanSetAndGet()
        {
            // Arrange
            var context = new RequestContext();
            var cancellationTokenSource = new CancellationTokenSource();
            var expectedToken = cancellationTokenSource.Token;

            // Act
            context.CancellationToken = expectedToken;

            // Assert
            Assert.Equal(expectedToken, context.CancellationToken);
        }

        [Fact]
        public void RequestContext_FeatureUsage_CanSetAndGet()
        {
            // Arrange
            var context = new RequestContext();
            var expectedFeatureFlag = FeatureFlag.RetryHandler | FeatureFlag.RedirectHandler;

            // Act
            context.FeatureUsage = expectedFeatureFlag;

            // Assert
            Assert.Equal(expectedFeatureFlag, context.FeatureUsage);
        }

        [Fact]
        public void RequestContext_DefaultValues_AreCorrect()
        {
            // Arrange & Act
            var context = new RequestContext();

            // Assert
            Assert.Null(context.ClientRequestId);
            Assert.Equal(default(CancellationToken), context.CancellationToken);
            Assert.Equal(default(FeatureFlag), context.FeatureUsage);
        }
    }
}
