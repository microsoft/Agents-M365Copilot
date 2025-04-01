// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Mocks
{
    using System;
    using Microsoft.Agents.M365Copilot.Core.Models;
    using Moq;
    public class MockProgress : Mock<IProgress<AsyncOperationStatus>>
    {
        public MockProgress()
            : base(MockBehavior.Strict)
        {
            this.Setup(mockProgress => mockProgress.Report(It.IsAny<AsyncOperationStatus>()));
        }
    }
}
