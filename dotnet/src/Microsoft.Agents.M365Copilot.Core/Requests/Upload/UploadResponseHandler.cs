﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Requests.Upload
{
    using System.IO;
    using System.Net;
    using System.Net.Http;
    using System.Text.Json;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Exceptions;
    using Microsoft.Agents.M365Copilot.Core.Models;
    using Microsoft.Kiota.Abstractions.Serialization;

    /// <summary>
    /// The ResponseHandler for upload requests
    /// </summary>
    internal class UploadResponseHandler
    {
        private readonly IAsyncParseNodeFactory _parseNodeFactory;

        /// <summary>
        /// Constructs a new <see cref="UploadResponseHandler"/>.
        /// </summary>
        /// <param name="parseNodeFactory"> The <see cref="IParseNodeFactory"/> to use for response handling</param>
        public UploadResponseHandler(IParseNodeFactory parseNodeFactory = null)
        {
            _parseNodeFactory = parseNodeFactory as IAsyncParseNodeFactory ?? ParseNodeFactoryRegistry.DefaultInstance;
        }

        /// <summary>
        /// Process raw HTTP response from Upload request
        /// </summary>
        /// <typeparam name="T">The type to return</typeparam>
        /// <param name="response">The HttpResponseMessage to handle.</param>
        /// <returns></returns>
        public async Task<UploadResult<T>> HandleResponseAsync<T>(HttpResponseMessage response) where T : IParsable, new()
        {
            if (response.Content == null)
            {
                throw new ServiceException(ErrorConstants.Messages.NoResponseForUpload);
            }

            // Give back the info from the server for ongoing upload as the upload is ongoing
            using Stream responseStream = await response.Content.ReadAsStreamAsync().ConfigureAwait(false);
            try
            {
                if (!response.IsSuccessStatusCode)
                {
                    string rawResponseBody = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
                    // Throw exception to know something went wrong.
                    throw new ServiceException(ErrorConstants.Codes.GeneralException, response.Headers, (int)response.StatusCode, rawResponseBody);
                }

                var uploadResult = new UploadResult<T>();

                /*
                 * Check if we have a status code 201 to know if the upload completed successfully.
                 * This will be returned when uploading a FileAttachment with a location header but empty response hence
                 * This could also be returned when uploading a DriveItem with  an ItemResponse but no location header.
                 */
                if (response.StatusCode == HttpStatusCode.Created)
                {
                    if (responseStream.Length > 0) //system.text.json wont deserialize an empty string
                    {
                        var jsonParseNode = await _parseNodeFactory.GetRootParseNodeAsync(response.Content.Headers?.ContentType?.MediaType?.ToLowerInvariant(), responseStream);
                        uploadResult.ItemResponse = jsonParseNode.GetObjectValue<T>((parsable) => new T());
                    }
                    uploadResult.Location = response.Headers.Location;
                }
                else
                {
                    /*
                     * The response could be either a 200 or a 202 response.
                     * DriveItem Upload returns the upload session in a 202 response while FileAttachment in a 200 response
                     * However, successful upload completion for a DriveItem the response could also come in a 200 response and
                     * hence we validate this by checking the NextExpectedRanges parameter which is present in an ongoing upload
                     */
                    var uploadSessionParseNode = await _parseNodeFactory.GetRootParseNodeAsync(response.Content.Headers?.ContentType?.MediaType?.ToLowerInvariant(), responseStream);
                    UploadSession uploadSession = uploadSessionParseNode.GetObjectValue<UploadSession>(UploadSession.CreateFromDiscriminatorValue);
                    if (uploadSession?.NextExpectedRanges != null)
                    {
                        uploadResult.UploadSession = uploadSession;
                    }
                    else
                    {
                        //Upload is most likely done as DriveItem info may come in a 200 response
                        responseStream.Position = 0; //reset 
                        var objectParseNode = await _parseNodeFactory.GetRootParseNodeAsync(response.Content.Headers?.ContentType?.MediaType?.ToLowerInvariant(), responseStream);
                        uploadResult.ItemResponse = objectParseNode.GetObjectValue<T>((parsable) => new T());
                    }
                }

                return uploadResult;
            }
            catch (JsonException exception)
            {
                throw new ClientException(ErrorConstants.Messages.UnableToDeserializeContent, exception);
            }
        }
    }
}
