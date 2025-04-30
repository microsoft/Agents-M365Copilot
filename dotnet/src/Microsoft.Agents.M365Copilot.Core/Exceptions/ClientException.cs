// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Exceptions
{
    using System;
    using Microsoft.Kiota.Abstractions;

    /// <summary>
    /// Microsoft Copilot client exception.
    /// </summary>
    /// <remarks>
    /// Creates a new client exception.
    /// </remarks>
    /// <param name="message">The exception message.</param>
    /// <param name="innerException">The possible innerException.</param>
    public class ClientException(string message, Exception innerException = null) : ApiException(message, innerException)
    {
    }
}
