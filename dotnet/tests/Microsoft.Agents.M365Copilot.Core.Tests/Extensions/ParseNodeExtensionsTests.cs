// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Extensions
{
    using Microsoft.Agents.M365Copilot.Core.Extensions;
    using Microsoft.Kiota.Abstractions.Serialization;
    using Moq;
    using Xunit;

    public class ParseNodeExtensionsTests
    {
        [Fact]
        public void GetErrorMessage_WithBothCodeAndMessage_ReturnsConcatenated()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockCodeNode = new Mock<IParseNode>();
            var mockMessageNode = new Mock<IParseNode>();

            mockCodeNode.Setup(n => n.GetStringValue()).Returns("ErrorCode123");
            mockMessageNode.Setup(n => n.GetStringValue()).Returns("Error message description");
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns(mockCodeNode.Object);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns(mockMessageNode.Object);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Equal("ErrorCode123 : Error message description", result);
        }

        [Fact]
        public void GetErrorMessage_WithOnlyCode_ReturnsCode()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockCodeNode = new Mock<IParseNode>();
            var mockMessageNode = new Mock<IParseNode>();

            mockCodeNode.Setup(n => n.GetStringValue()).Returns("ErrorCode456");
            mockMessageNode.Setup(n => n.GetStringValue()).Returns((string)null);
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns(mockCodeNode.Object);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns(mockMessageNode.Object);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Equal("ErrorCode456", result);
        }

        [Fact]
        public void GetErrorMessage_WithOnlyMessage_ReturnsMessage()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockCodeNode = new Mock<IParseNode>();
            var mockMessageNode = new Mock<IParseNode>();

            mockCodeNode.Setup(n => n.GetStringValue()).Returns((string)null);
            mockMessageNode.Setup(n => n.GetStringValue()).Returns("Error message only");
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns(mockCodeNode.Object);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns(mockMessageNode.Object);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Equal("Error message only", result);
        }

        [Fact]
        public void GetErrorMessage_WithNeitherCodeNorMessage_ReturnsNull()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockCodeNode = new Mock<IParseNode>();
            var mockMessageNode = new Mock<IParseNode>();

            mockCodeNode.Setup(n => n.GetStringValue()).Returns((string)null);
            mockMessageNode.Setup(n => n.GetStringValue()).Returns((string)null);
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns(mockCodeNode.Object);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns(mockMessageNode.Object);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Null(result);
        }

        [Fact]
        public void GetErrorMessage_WithEmptyStrings_ReturnsNull()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockCodeNode = new Mock<IParseNode>();
            var mockMessageNode = new Mock<IParseNode>();

            mockCodeNode.Setup(n => n.GetStringValue()).Returns(string.Empty);
            mockMessageNode.Setup(n => n.GetStringValue()).Returns(string.Empty);
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns(mockCodeNode.Object);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns(mockMessageNode.Object);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Null(result);
        }

        [Fact]
        public void GetErrorMessage_WithNoErrorNode_ReturnsNull()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns((IParseNode)null);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Null(result);
        }

        [Fact]
        public void GetErrorMessage_WithNoCodeNode_UsesOnlyMessage()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockMessageNode = new Mock<IParseNode>();

            mockMessageNode.Setup(n => n.GetStringValue()).Returns("Message without code");
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns((IParseNode)null);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns(mockMessageNode.Object);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Equal("Message without code", result);
        }

        [Fact]
        public void GetErrorMessage_WithNoMessageNode_UsesOnlyCode()
        {
            // Arrange
            var mockRootNode = new Mock<IParseNode>();
            var mockErrorNode = new Mock<IParseNode>();
            var mockCodeNode = new Mock<IParseNode>();

            mockCodeNode.Setup(n => n.GetStringValue()).Returns("CodeWithoutMessage");
            mockErrorNode.Setup(n => n.GetChildNode("code")).Returns(mockCodeNode.Object);
            mockErrorNode.Setup(n => n.GetChildNode("message")).Returns((IParseNode)null);
            mockRootNode.Setup(n => n.GetChildNode("error")).Returns(mockErrorNode.Object);

            // Act
            var result = ParseNodeExtensions.GetErrorMessage(mockRootNode.Object);

            // Assert
            Assert.Equal("CodeWithoutMessage", result);
        }
    }
}
