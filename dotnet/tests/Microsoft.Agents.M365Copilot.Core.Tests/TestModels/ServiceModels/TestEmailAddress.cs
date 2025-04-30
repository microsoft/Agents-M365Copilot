﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.TestModels.ServiceModels
{
    using System;
    using System.Collections.Generic;
    using Microsoft.Kiota.Abstractions.Serialization;

    /// <summary>
    /// The type TestEmailAddress.
    /// </summary>
    public partial class TestEmailAddress : IParsable, IAdditionalDataHolder
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TestEmailAddress"/> class.
        /// </summary>
        public TestEmailAddress()
        {
            this.ODataType = "microsoft.graph.emailAddress";
        }

        /// <summary>
        /// Gets or sets name.
        /// The display name of the person or entity.
        /// </summary>
        public string Name
        {
            get; set;
        }

        /// <summary>
        /// Gets or sets address.
        /// The email address of the person or entity.
        /// </summary>
        public string Address
        {
            get; set;
        }

        /// <summary>
        /// Gets or sets additional data.
        /// </summary>
        public IDictionary<string, object> AdditionalData { get; set; } = new Dictionary<string, object>();

        /// <summary>
        /// Gets or sets @odata.type.
        /// </summary>
        public string ODataType
        {
            get; set;
        }

        /// <summary>
        /// Gets the field deserializers for the <see cref="TestEmailAddress"/> instance
        /// </summary>
        /// <returns></returns>
        public IDictionary<string, Action<IParseNode>> GetFieldDeserializers()
        {
            return new Dictionary<string, Action<IParseNode>>
            {
                {"@odata.type", (n) => { ODataType = n.GetStringValue(); } },
                {"address", (n) => { Address = n.GetStringValue(); } },
                {"name", (n) => { Name = n.GetStringValue(); } },
            };
        }

        /// <summary>
        /// Serialize the <see cref="TestEmailAddress"/> instance
        /// </summary>
        /// <param name="writer">The <see cref="ISerializationWriter"/> to serialize the instance</param>
        /// <exception cref="ArgumentNullException">Thrown when the writer is null</exception>
        public void Serialize(ISerializationWriter writer)
        {
            _ = writer ?? throw new ArgumentNullException(nameof(writer));
            writer.WriteStringValue("name", Name);
            writer.WriteStringValue("address", Address);
            writer.WriteStringValue("@odata.type", ODataType);
            writer.WriteAdditionalData(AdditionalData);
        }

        /// <summary>
        /// Creates a new instance of the appropriate class based on discriminator value
        /// <param name="parseNode">The parse node to use to read the discriminator value and create the object</param>
        /// </summary>
        public static TestEmailAddress CreateFromDiscriminatorValue(IParseNode parseNode)
        {
            _ = parseNode ?? throw new ArgumentNullException(nameof(parseNode));
            return new TestEmailAddress();
        }
    }
}
