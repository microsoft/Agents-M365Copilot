﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------


namespace Microsoft.Agents.M365Copilot.Core.Tests.Requests
{
    using System.Linq;
    using System.Net;
    using System.Net.Http;
    using System.Text;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Requests;
    using Microsoft.Agents.M365Copilot.Core.Tests.TestModels.ServiceModels;
    using Microsoft.Kiota.Abstractions;
    using Microsoft.Kiota.Serialization.Json;
    using Xunit;

    public class CopilotResponseTests : RequestTestBase
    {
        [Fact]
        public void CopilotResponse_Initialize()
        {
            // Arrange
            HttpResponseMessage responseMessage = new HttpResponseMessage(HttpStatusCode.OK);
            RequestInformation requestInformation = new RequestInformation() { UrlTemplate = "http://localhost" };

            // Act
            CopilotResponse response = new CopilotResponse(requestInformation, responseMessage);

            // Assert
            Assert.Equal(responseMessage, response.ToHttpResponseMessage());
            Assert.Equal(responseMessage.StatusCode, response.StatusCode);
            Assert.Equal(requestInformation, response.RequestInformation);

        }

        [Fact]
        public void CopilotResponse_ValidateHeaders()
        {
            // Arrange
            HttpResponseMessage responseMessage = new HttpResponseMessage(HttpStatusCode.OK);
            responseMessage.Headers.Add("Authorization", "bearer token");// add a test header
            RequestInformation requestInformation = new RequestInformation() { UrlTemplate = "http://localhost" };

            // Act
            CopilotResponse response = new CopilotResponse(requestInformation, responseMessage);

            // Assert
            Assert.Equal(responseMessage, response.ToHttpResponseMessage());
            Assert.Equal(responseMessage.Headers.Count(), response.HttpHeaders.Count());
            Assert.Equal("Authorization", responseMessage.Headers.First().Key);
            Assert.Equal("bearer token", responseMessage.Headers.First().Value.First());

        }

        [Fact]
        public async Task ValidateResponseHandlerAsync()
        {
            // Arrange
            HttpResponseMessage responseMessage = new HttpResponseMessage()
            {
                Content = new StringContent(@"{
                    ""id"": ""123"",
                    ""givenName"": ""Joe"",
                    ""surname"": ""Brown"",
                    ""@odata.type"":""test""
                }", Encoding.UTF8, CoreConstants.MimeTypeNames.Application.Json)
            };

            // create a custom responseHandler
            IResponseHandler responseHandler = new ResponseHandler<TestUser>(new JsonParseNodeFactory());
            RequestInformation requestInformation = new RequestInformation() { UrlTemplate = "http://localhost" };


            // Act
            CopilotResponse<TestUser> response = new CopilotResponse<TestUser>(requestInformation, responseMessage);
            TestUser user = await response.GetResponseObjectAsync(responseHandler);

            // Assert
            Assert.Equal("123", user.Id);
            Assert.Equal("Joe", user.GivenName);
            Assert.Equal("Brown", user.Surname);

        }
    }
}
