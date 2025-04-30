// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Requests
{
    /// <summary>
    /// The options for setting up a given  client
    /// </summary>
    public class CopilotClientOptions
    {
        /// <summary>
        /// The target version of the api endpoint we are targeting (v1 or beta)
        /// </summary>
        public string ServiceTargetVersion
        {
            get; set;
        }

        /// <summary>
        /// The version of the service library in use. Should be in the format `x.x.x` (Semantic version)
        /// </summary>
        public string ServiceLibraryClientVersion
        {
            get; set;
        }

        /// <summary>
        /// The version of the core library in use. Should be in the format `x.x.x` (Semantic version).
        /// </summary>
        public string CoreClientVersion
        {
            get; set;
        }

        /// <summary>
        /// The product prefix to use in setting the telemetry headers.
        /// Will default to `-dotnet` if not set.
        /// </summary>
        public string ProductPrefix
        {
            get; set;
        }
    }
}
