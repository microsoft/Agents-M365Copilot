// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Exceptions
{
    using Microsoft.Agents.M365Copilot.Core.Exceptions;
    using System;
    using Xunit;

    public class ClientExceptionTests
    {
        [Fact]
        public void ClientException_WithMessage_CreatesException()
        {
            // Arrange
            var expectedMessage = "Test error message";

            // Act
            var exception = new ClientException(expectedMessage);

            // Assert
            Assert.NotNull(exception);
            Assert.Equal(expectedMessage, exception.Message);
            Assert.Null(exception.InnerException);
        }

        [Fact]
        public void ClientException_WithMessageAndInnerException_CreatesException()
        {
            // Arrange
            var expectedMessage = "Test error message";
            var innerException = new InvalidOperationException("Inner exception message");

            // Act
            var exception = new ClientException(expectedMessage, innerException);

            // Assert
            Assert.NotNull(exception);
            Assert.Equal(expectedMessage, exception.Message);
            Assert.NotNull(exception.InnerException);
            Assert.Equal(innerException, exception.InnerException);
            Assert.Equal("Inner exception message", exception.InnerException.Message);
        }

        [Fact]
        public void ClientException_CanBeThrown()
        {
            // Arrange
            var expectedMessage = "Test exception to throw";
            ClientException caughtException = null;

            // Act
            try
            {
                throw new ClientException(expectedMessage);
            }
            catch (ClientException ex)
            {
                caughtException = ex;
            }

            // Assert
            Assert.NotNull(caughtException);
            Assert.Equal(expectedMessage, caughtException.Message);
        }

        [Fact]
        public void ClientException_CanBeCaught()
        {
            // Arrange
            var expectedMessage = "Caught exception";
            ClientException caughtException = null;

            // Act
            try
            {
                throw new ClientException(expectedMessage);
            }
            catch (ClientException ex)
            {
                caughtException = ex;
            }

            // Assert
            Assert.NotNull(caughtException);
            Assert.Equal(expectedMessage, caughtException.Message);
        }

        [Fact]
        public void ClientException_InheritsFromApiException()
        {
            // Arrange
            var exception = new ClientException("Test");

            // Act & Assert
            Assert.IsAssignableFrom<Microsoft.Kiota.Abstractions.ApiException>(exception);
        }

        [Fact]
        public void ClientException_WithNullInnerException_IsValid()
        {
            // Arrange & Act
            var exception = new ClientException("Test message", null);

            // Assert
            Assert.NotNull(exception);
            Assert.Null(exception.InnerException);
        }
    }
}
