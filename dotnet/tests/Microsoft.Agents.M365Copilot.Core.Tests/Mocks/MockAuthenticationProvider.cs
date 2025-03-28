﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Mocks
{
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    using Microsoft.Kiota.Abstractions;
    using Microsoft.Kiota.Abstractions.Authentication;
    using Moq;

    public class MockAuthenticationProvider : Mock<IAuthenticationProvider>
    {
        public MockAuthenticationProvider(string accessToken = null)
            : base(MockBehavior.Strict)
        {
            this.Setup(
                provider => provider.AuthenticateRequestAsync(It.IsAny<RequestInformation>(), It.IsAny<Dictionary<string, object>>(), It.IsAny<CancellationToken>()))
                .Callback<RequestInformation, Dictionary<string, object>, CancellationToken>((r, d, c) => r.Headers.Add(CoreConstants.Headers.Bearer, accessToken ?? "Default-Token"))
                .Returns(Task.FromResult(0));
        }
    }
}
