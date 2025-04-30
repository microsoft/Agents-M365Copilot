﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Helpers
{
    using System;
    using Microsoft.Agents.M365Copilot.Core.Helpers;
    using Xunit;
    public class UrlHelperTests
    {
        [Fact]
        public void GetQueryOptions_EmptyFragment()
        {
            var uri = new Uri("https://localhost#");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Empty(queryValues);
        }

        [Fact]
        public void GetQueryOptions_EmptyQueryString()
        {
            var uri = new Uri("https://localhost?");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Empty(queryValues);
        }

        [Fact]
        public void GetQueryOptions_NoQueryString()
        {
            var uri = new Uri("https://localhost");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Empty(queryValues);
        }

        [Fact]
        public void GetQueryOptions_MultipleFragments()
        {
            var uri = new Uri("https://localhost#key=value&key2=value%202");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Equal(2, queryValues.Count);
            Assert.Equal("value", queryValues["key"]);
            Assert.Equal("value 2", queryValues["key2"]);
        }

        [Fact]
        public void GetQueryOptions_SingleFragment()
        {
            var uri = new Uri("https://localhost#key=value");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Single(queryValues);
            Assert.Equal("value", queryValues["key"]);
        }

        [Fact]
        public void GetQueryOptions_MultipleQueryOptions()
        {
            var uri = new Uri("https://localhost?key=value&key2=value%202");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Equal(2, queryValues.Count);
            Assert.Equal("value 2", queryValues["key2"]);
        }

        [Fact]
        public void GetQueryOptions_SingleQueryOption()
        {
            var uri = new Uri("https://localhost?key=value");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Single(queryValues);
            Assert.Equal("value", queryValues["key"]);
        }

        [Fact]
        public void GetQueryOptions_TrailingAmpersand()
        {
            var uri = new Uri("https://localhost?key=value&");

            var queryValues = UrlHelper.GetQueryOptions(uri);

            Assert.Single(queryValues);
            Assert.Equal("value", queryValues["key"]);
        }
    }
}
