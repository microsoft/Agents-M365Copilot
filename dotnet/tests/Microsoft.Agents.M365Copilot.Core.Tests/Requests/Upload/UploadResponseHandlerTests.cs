﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Requests
{
    using System;
    using System.Linq;
    using System.Net;
    using System.Net.Http;
    using System.Text;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Exceptions;
    using Microsoft.Agents.M365Copilot.Core.Requests.Upload;
    using Microsoft.Agents.M365Copilot.Core.Tests.TestModels.ServiceModels;
    using Microsoft.Kiota.Abstractions.Serialization;
    using Microsoft.Kiota.Serialization.Json;
    using Xunit;

    public class UploadResponseHandlerTests
    {
        public UploadResponseHandlerTests()
        {
            // register the default serialization instance as the generator would.
            ParseNodeFactoryRegistry.DefaultInstance.ContentTypeAssociatedFactories.TryAdd(CoreConstants.MimeTypeNames.Application.Json, new JsonParseNodeFactory());
        }

        [Theory]
        [InlineData(HttpStatusCode.Created)]
        [InlineData(HttpStatusCode.OK)]
        public async Task GetDriveItemOnCompletedUploadAsync(HttpStatusCode statusCode)
        {
            // Arrange
            var responseHandler = new UploadResponseHandler();
            var hrm = new HttpResponseMessage
            {
                Content = new StringContent(@"{
                    ""id"": ""912310013A123"",
                    ""name"": ""largeFile.vhd"",
                    ""size"": 33
                }", Encoding.UTF8, CoreConstants.MimeTypeNames.Application.Json),
                StatusCode = statusCode//upload successful!
            };

            // Act
            var uploadResult = await responseHandler.HandleResponseAsync<TestDriveItem>(hrm);
            var driveItem = uploadResult.ItemResponse;

            //Assert
            Assert.True(uploadResult.UploadSucceeded);
            Assert.NotNull(driveItem);
            Assert.Equal("912310013A123", driveItem.Id);
            Assert.Equal("largeFile.vhd", driveItem.Name);
            Assert.Equal(33, driveItem.Size);
        }

        [Fact]
        public async Task GetFileAttachmentLocationItemOnCompletedUploadAsync()
        {
            // Arrange
            var responseHandler = new UploadResponseHandler();
            var hrm = new HttpResponseMessage()
            {
                Content = new StringContent("")
            };
            hrm.Headers.Location = new Uri("http://localhost");
            hrm.StatusCode = HttpStatusCode.Created;//upload successful!

            // Act
            var uploadResult = await responseHandler.HandleResponseAsync<TestDriveItem>(hrm);
            var fileAttachment = uploadResult.ItemResponse;

            //Assert
            Assert.True(uploadResult.UploadSucceeded);
            Assert.Null(fileAttachment);
            Assert.Equal("http://localhost", uploadResult.Location.OriginalString);
        }

        [Fact]
        public async Task GetUploadSessionOnProgressingUploadAsync()
        {
            // Arrange
            var responseHandler = new UploadResponseHandler();
            var hrm = new HttpResponseMessage
            {
                Content = new StringContent(@"{
                  ""expirationDateTime"": ""2015 - 01 - 29T09: 21:55.523Z"",
                  ""nextExpectedRanges"": [
                  ""12345-55232"",
                  ""77829-99375""
                  ]
                }", Encoding.UTF8, CoreConstants.MimeTypeNames.Application.Json),
                StatusCode = HttpStatusCode.OK//upload successful!
            };

            // Act
            var uploadResult = await responseHandler.HandleResponseAsync<TestDriveItem>(hrm);
            var uploadSession = uploadResult.UploadSession;

            //Assert
            Assert.False(uploadResult.UploadSucceeded);
            Assert.NotNull(uploadSession);
            Assert.Null(uploadSession.UploadUrl);
            Assert.Equal(DateTimeOffset.Parse("2015 - 01 - 29T09: 21:55.523Z"), uploadSession.ExpirationDateTime);
            Assert.Equal("12345-55232", uploadSession.NextExpectedRanges.First());
            Assert.Equal("77829-99375", uploadSession.NextExpectedRanges.Last());
            Assert.Equal(2, uploadSession.NextExpectedRanges.Count());
        }

        [Fact]
        public async Task ThrowsServiceExceptionOnErrorResponseAsync()
        {
            // Arrange
            var responseHandler = new UploadResponseHandler();
            var hrm = new HttpResponseMessage
            {
                Content = new StringContent(@"{
                  ""error"": {
                    ""code"": ""InvalidAuthenticationToken"",
                    ""message"": ""Access token is empty."",
                    ""innerError"": {
                                ""request-id"": ""0e4cbf06-018b-4596-8614-50d5f7eef218"",
                                ""date"": ""2019-11-21T13:57:37""
                            }
                        }
                    }", Encoding.UTF8, CoreConstants.MimeTypeNames.Application.Json),
                StatusCode = HttpStatusCode.Unauthorized//error
            };

            // Act
            var serviceException = await Assert.ThrowsAsync<ServiceException>(() => responseHandler.HandleResponseAsync<TestDriveItem>(hrm));

            //Assert
            Assert.NotNull(serviceException);
            Assert.Equal(ErrorConstants.Codes.GeneralException, serviceException.Message);
            Assert.Equal(HttpStatusCode.Unauthorized, (HttpStatusCode)serviceException.ResponseStatusCode);
        }

        [Fact]
        public async Task ThrowsSerializationErrorOnInvalidJsonAsync()
        {
            // Arrange
            var responseHandler = new UploadResponseHandler();
            //The message has a missing open brace in the json payload.
            string malformedResponse = @"
                  ""error"": {
                    ""code"": ""InvalidAuthenticationToken"",
                    ""message"": ""Access token is empty."",
                    ""innerError"": {
                                ""request-id"": ""0e4cbf06-018b-4596-8614-50d5f7eef218"",
                                ""date"": ""2019-11-21T13:57:37""
                            }
                        }
                    }";

            var hrm = new HttpResponseMessage
            {
                Content = new StringContent(malformedResponse, Encoding.UTF8, CoreConstants.MimeTypeNames.Application.Json),
                StatusCode = HttpStatusCode.Unauthorized//error
            };

            // Act
            var serviceException = await Assert.ThrowsAsync<ServiceException>(() => responseHandler.HandleResponseAsync<TestDriveItem>(hrm));

            //Assert
            Assert.NotNull(serviceException);
            Assert.Equal(ErrorConstants.Codes.GeneralException, serviceException.Message);
            Assert.Equal(malformedResponse, serviceException.RawResponseBody);
        }
    }
}
