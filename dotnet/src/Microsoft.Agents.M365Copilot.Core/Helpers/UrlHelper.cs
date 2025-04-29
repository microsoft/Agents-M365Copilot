// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Helpers
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net;

    /// <summary>
    /// Helper class for working with URLs.
    /// </summary>
    public static class UrlHelper
    {
        /// <summary>
        /// Parse query options from the URL.
        /// </summary>
        /// <param name="resultUri"></param>
        /// <returns></returns>
        public static IDictionary<string, string> GetQueryOptions(Uri resultUri)
        {
            IEnumerable<string> queryParams = Enumerable.Empty<string>();
            var queryValues = new Dictionary<string, string>();

            if (!string.IsNullOrEmpty(resultUri.Fragment) && resultUri.Fragment.Length > 1)
            {
                queryParams = resultUri.Fragment.TrimStart('#').Split('&');
            }
            else if (!string.IsNullOrEmpty(resultUri.Query) && resultUri.Query.Length > 1)
            {
                queryParams = resultUri.Query.TrimStart('?').Split('&');
            }

            foreach (var param in queryParams)
            {
                if (!string.IsNullOrEmpty(param))
                {
                    string[] kvp = param.Split('=');
                    queryValues.Add(kvp[0], WebUtility.UrlDecode(kvp[1]));
                }
            }

            return queryValues;
        }
    }
}
