// <auto-generated/>
#pragma warning disable CS0618
using Microsoft.Kiota.Abstractions.Extensions;
using Microsoft.Kiota.Abstractions.Serialization;
using System.Collections.Generic;
using System.IO;
using System;
namespace Microsoft.Agents.M365Copilot.Beta.Models
{
    [global::System.CodeDom.Compiler.GeneratedCode("Kiota", "1.0.0")]
    #pragma warning disable CS1591
    public partial class SharePointIdentitySet : global::Microsoft.Agents.M365Copilot.Beta.Models.IdentitySet, IParsable
    #pragma warning restore CS1591
    {
        /// <summary>The group associated with this action. Optional.</summary>
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public global::Microsoft.Agents.M365Copilot.Beta.Models.Identity? Group
        {
            get { return BackingStore?.Get<global::Microsoft.Agents.M365Copilot.Beta.Models.Identity?>("group"); }
            set { BackingStore?.Set("group", value); }
        }
#nullable restore
#else
        public global::Microsoft.Agents.M365Copilot.Beta.Models.Identity Group
        {
            get { return BackingStore?.Get<global::Microsoft.Agents.M365Copilot.Beta.Models.Identity>("group"); }
            set { BackingStore?.Set("group", value); }
        }
#endif
        /// <summary>The SharePoint group associated with this action. Optional.</summary>
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity? SiteGroup
        {
            get { return BackingStore?.Get<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity?>("siteGroup"); }
            set { BackingStore?.Set("siteGroup", value); }
        }
#nullable restore
#else
        public global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity SiteGroup
        {
            get { return BackingStore?.Get<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity>("siteGroup"); }
            set { BackingStore?.Set("siteGroup", value); }
        }
#endif
        /// <summary>The SharePoint user associated with this action. Optional.</summary>
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity? SiteUser
        {
            get { return BackingStore?.Get<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity?>("siteUser"); }
            set { BackingStore?.Set("siteUser", value); }
        }
#nullable restore
#else
        public global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity SiteUser
        {
            get { return BackingStore?.Get<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity>("siteUser"); }
            set { BackingStore?.Set("siteUser", value); }
        }
#endif
        /// <summary>
        /// Instantiates a new <see cref="global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentitySet"/> and sets the default values.
        /// </summary>
        public SharePointIdentitySet() : base()
        {
            OdataType = "#microsoft.graph.sharePointIdentitySet";
        }
        /// <summary>
        /// Creates a new instance of the appropriate class based on discriminator value
        /// </summary>
        /// <returns>A <see cref="global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentitySet"/></returns>
        /// <param name="parseNode">The parse node to use to read the discriminator value and create the object</param>
        public static new global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentitySet CreateFromDiscriminatorValue(IParseNode parseNode)
        {
            _ = parseNode ?? throw new ArgumentNullException(nameof(parseNode));
            return new global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentitySet();
        }
        /// <summary>
        /// The deserialization information for the current model
        /// </summary>
        /// <returns>A IDictionary&lt;string, Action&lt;IParseNode&gt;&gt;</returns>
        public override IDictionary<string, Action<IParseNode>> GetFieldDeserializers()
        {
            return new Dictionary<string, Action<IParseNode>>(base.GetFieldDeserializers())
            {
                { "group", n => { Group = n.GetObjectValue<global::Microsoft.Agents.M365Copilot.Beta.Models.Identity>(global::Microsoft.Agents.M365Copilot.Beta.Models.Identity.CreateFromDiscriminatorValue); } },
                { "siteGroup", n => { SiteGroup = n.GetObjectValue<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity>(global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity.CreateFromDiscriminatorValue); } },
                { "siteUser", n => { SiteUser = n.GetObjectValue<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity>(global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity.CreateFromDiscriminatorValue); } },
            };
        }
        /// <summary>
        /// Serializes information the current object
        /// </summary>
        /// <param name="writer">Serialization writer to use to serialize this model</param>
        public override void Serialize(ISerializationWriter writer)
        {
            _ = writer ?? throw new ArgumentNullException(nameof(writer));
            base.Serialize(writer);
            writer.WriteObjectValue<global::Microsoft.Agents.M365Copilot.Beta.Models.Identity>("group", Group);
            writer.WriteObjectValue<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity>("siteGroup", SiteGroup);
            writer.WriteObjectValue<global::Microsoft.Agents.M365Copilot.Beta.Models.SharePointIdentity>("siteUser", SiteUser);
        }
    }
}
#pragma warning restore CS0618
