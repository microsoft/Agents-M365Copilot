// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Extensions
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net.Http;
    using Microsoft.Agents.M365Copilot.Core.Requests;

    /// <summary>
    /// Contains extension methods for <see cref="HttpRequestMessage"/>
    /// </summary>
    public static class HttpRequestMessageExtensions
    {
        /// <summary>
        /// Get's feature request header value from the incoming <see cref="HttpRequestMessage"/>
        /// </summary>
        /// <param name="httpRequestMessage">The <see cref="HttpRequestMessage"/> object</param>
        /// <returns></returns>
        internal static FeatureFlag GetFeatureFlags(this HttpRequestMessage httpRequestMessage)
        {
            httpRequestMessage.Headers.TryGetValues(CoreConstants.Headers.FeatureFlag, out IEnumerable<string> flags);

            if (!Enum.TryParse(flags?.FirstOrDefault(), out FeatureFlag featureFlag))
            {
                featureFlag = FeatureFlag.None;
            }

            return featureFlag;
        }

        /// <summary>
        /// Gets a <see cref="RequestContext"/> from <see cref="HttpRequestMessage"/>
        /// </summary>
        /// <param name="httpRequestMessage">The <see cref="HttpRequestMessage"/> representation of the request.</param>
        /// <returns></returns>
        public static RequestContext GetRequestContext(this HttpRequestMessage httpRequestMessage)
        {
            RequestContext requestContext = new RequestContext();
#pragma warning disable CS0618
            if (httpRequestMessage.Properties.TryGetValue(nameof(RequestContext), out var requestContextObject))
#pragma warning restore CS0618
            {
                requestContext = (RequestContext)requestContextObject;
            }
            return requestContext;
        }
    }
}
