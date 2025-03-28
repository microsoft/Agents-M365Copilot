﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Requests
{
    using Microsoft.Agents.M365Copilot.Core.Core.Requests.Requests;
    using Microsoft.Kiota.Abstractions;

    /// <summary>
    /// A default client interface.
    /// </summary>
    public interface IBaseClient
    {
        /// <summary>
        /// Gets the <see cref="IRequestAdapter"/> for sending requests.
        /// </summary>
        IRequestAdapter RequestAdapter
        {
            get; set;
        }

        /// <summary>
        /// Gets the <see cref="BatchRequestBuilder"/> for building batch Requests
        /// </summary>
        public BatchRequestBuilder Batch
        {
            get;
        }
    }
}
