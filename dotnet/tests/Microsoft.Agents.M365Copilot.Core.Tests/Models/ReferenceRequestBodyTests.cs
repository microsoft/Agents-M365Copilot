// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Models
{
    using Microsoft.Agents.M365Copilot.Core.Models;
    using System.Text.Json;
    using Xunit;

    public class ReferenceRequestBodyTests
    {
        [Fact]
        public void ReferenceRequestBody_ODataId_CanSetAndGet()
        {
            // Arrange
            var referenceBody = new ReferenceRequestBody();
            var expectedODataId = "https://graph.microsoft.com/v1.0/users/12345";

            // Act
            referenceBody.ODataId = expectedODataId;

            // Assert
            Assert.Equal(expectedODataId, referenceBody.ODataId);
        }

        [Fact]
        public void ReferenceRequestBody_DefaultValue_IsNull()
        {
            // Arrange & Act
            var referenceBody = new ReferenceRequestBody();

            // Assert
            Assert.Null(referenceBody.ODataId);
        }

        [Fact]
        public void ReferenceRequestBody_SerializesCorrectly()
        {
            // Arrange
            var referenceBody = new ReferenceRequestBody
            {
                ODataId = "https://graph.microsoft.com/v1.0/users/12345"
            };

            // Act
            var json = JsonSerializer.Serialize(referenceBody);

            // Assert
            Assert.Contains("\"@odata.id\"", json);
            Assert.Contains("https://graph.microsoft.com/v1.0/users/12345", json);
        }

        [Fact]
        public void ReferenceRequestBody_DeserializesCorrectly()
        {
            // Arrange
            var json = """{"@odata.id":"https://graph.microsoft.com/v1.0/users/67890"}""";

            // Act
            var referenceBody = JsonSerializer.Deserialize<ReferenceRequestBody>(json);

            // Assert
            Assert.NotNull(referenceBody);
            Assert.Equal("https://graph.microsoft.com/v1.0/users/67890", referenceBody.ODataId);
        }
    }
}
