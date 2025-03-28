﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Models
{
    using System;
    using System.Collections.Generic;
    using Microsoft.Kiota.Abstractions.Serialization;

    /// <summary>
    /// The IUploadSession interface
    /// </summary>
    public interface IUploadSession : IParsable, IAdditionalDataHolder
    {
        /// <summary>
        /// Expiration date of the upload session
        /// </summary>
        DateTimeOffset? ExpirationDateTime
        {
            get; set;
        }

        /// <summary>
        /// The ranges yet to be uploaded to the server
        /// </summary>
        List<string> NextExpectedRanges
        {
            get; set;
        }

        /// <summary>
        /// The URL for upload
        /// </summary>
        string UploadUrl
        {
            get; set;
        }

    }
}
