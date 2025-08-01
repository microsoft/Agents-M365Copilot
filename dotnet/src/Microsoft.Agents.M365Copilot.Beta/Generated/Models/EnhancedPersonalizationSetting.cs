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
    public partial class EnhancedPersonalizationSetting : global::Microsoft.Agents.M365Copilot.Beta.Models.Entity, IParsable
    #pragma warning restore CS1591
    {
        /// <summary>The ID of a Microsoft Entra group to which the value is used to disable the control for populated users. The default value is null. This parameter is optional.</summary>
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public string? DisabledForGroup
        {
            get { return BackingStore?.Get<string?>("disabledForGroup"); }
            set { BackingStore?.Set("disabledForGroup", value); }
        }
#nullable restore
#else
        public string DisabledForGroup
        {
            get { return BackingStore?.Get<string>("disabledForGroup"); }
            set { BackingStore?.Set("disabledForGroup", value); }
        }
#endif
        /// <summary>If true, enables the enhanced personalization control and therefore related features as defined in control enhanced personalization privacy</summary>
        public bool? IsEnabledInOrganization
        {
            get { return BackingStore?.Get<bool?>("isEnabledInOrganization"); }
            set { BackingStore?.Set("isEnabledInOrganization", value); }
        }
        /// <summary>
        /// Creates a new instance of the appropriate class based on discriminator value
        /// </summary>
        /// <returns>A <see cref="global::Microsoft.Agents.M365Copilot.Beta.Models.EnhancedPersonalizationSetting"/></returns>
        /// <param name="parseNode">The parse node to use to read the discriminator value and create the object</param>
        public static new global::Microsoft.Agents.M365Copilot.Beta.Models.EnhancedPersonalizationSetting CreateFromDiscriminatorValue(IParseNode parseNode)
        {
            _ = parseNode ?? throw new ArgumentNullException(nameof(parseNode));
            return new global::Microsoft.Agents.M365Copilot.Beta.Models.EnhancedPersonalizationSetting();
        }
        /// <summary>
        /// The deserialization information for the current model
        /// </summary>
        /// <returns>A IDictionary&lt;string, Action&lt;IParseNode&gt;&gt;</returns>
        public override IDictionary<string, Action<IParseNode>> GetFieldDeserializers()
        {
            return new Dictionary<string, Action<IParseNode>>(base.GetFieldDeserializers())
            {
                { "disabledForGroup", n => { DisabledForGroup = n.GetStringValue(); } },
                { "isEnabledInOrganization", n => { IsEnabledInOrganization = n.GetBoolValue(); } },
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
            writer.WriteStringValue("disabledForGroup", DisabledForGroup);
            writer.WriteBoolValue("isEnabledInOrganization", IsEnabledInOrganization);
        }
    }
}
#pragma warning restore CS0618
