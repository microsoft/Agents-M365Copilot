﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

using System;
using System.Linq;
using Azure.Core;
using Microsoft.Kiota.Abstractions.Authentication;

namespace Microsoft.Agents.M365Copilot.Core.Authentication;

/// <summary>
/// An overload of the Access Token Provider that has the defaults for Microsoft Graph.
/// </summary>
public class AzureIdentityAccessTokenProvider : Kiota.Authentication.Azure.AzureIdentityAccessTokenProvider
{
    /// <inheritdoc/>
    public AzureIdentityAccessTokenProvider(TokenCredential credential, string[] allowedHosts = null, Microsoft.Kiota.Authentication.Azure.ObservabilityOptions observabilityOptions = null, bool isCaeEnabled = true, params string[] scopes)
        : base(credential, allowedHosts, observabilityOptions, isCaeEnabled, scopes)
    {
        if (!allowedHosts?.Any() ?? true)
            AllowedHostsValidator = new AllowedHostsValidator(new string[] { "graph.microsoft.com", "graph.microsoft.us", "dod-graph.microsoft.us", "graph.microsoft.de", "microsoftgraph.chinacloudapi.cn", "canary.graph.microsoft.com", "graph.microsoft-ppe.com" });
    }
}
