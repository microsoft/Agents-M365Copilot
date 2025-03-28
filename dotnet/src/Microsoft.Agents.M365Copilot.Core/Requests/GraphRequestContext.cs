﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Requests
{
    using System.Threading;

    /// <summary>
    /// The graph request context class
    /// </summary>
    public class GraphRequestContext
    {
        /// <summary>
        /// A ClientRequestId property
        /// </summary>
        public string ClientRequestId
        {
            get; set;
        }

        /// <summary>
        /// A CancellationToken property
        /// </summary>
        public CancellationToken CancellationToken
        {
            get; set;
        }

        /// <summary>
        /// A FeatureUsage property
        /// </summary>
        public FeatureFlag FeatureUsage
        {
            get; set;
        }
    }
}
