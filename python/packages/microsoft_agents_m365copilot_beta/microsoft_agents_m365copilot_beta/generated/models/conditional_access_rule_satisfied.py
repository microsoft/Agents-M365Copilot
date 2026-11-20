from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_conditions import ConditionalAccessConditions
    from .conditional_access_rule import ConditionalAccessRule

@dataclass
class ConditionalAccessRuleSatisfied(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client, ipAddressSeenByAzureAD, ipAddressSeenByResourceProvider, unknownFutureValue, servicePrincipals, servicePrincipalRisk, authenticationFlows, insiderRisk. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals, servicePrincipalRisk, authenticationFlows, insiderRisk. conditionalAccessConditions is a multi-valued enumeration and the property can contain multiple values in a comma-separated list.
    conditional_access_condition: Optional[ConditionalAccessConditions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Refers to the conditional access policy conditions that were satisfied. The possible values are: allApps, firstPartyApps, office365, appId, acr, appFilter, allUsers, guest, groupId, roleId, userId, allDevicePlatforms, devicePlatform, allLocations, insideCorpnet, allTrustedLocations, locationId, allDevices, deviceFilter, deviceState, unknownFutureValue, deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider, microsoftAdminPortals, deviceCodeFlow, accountTransfer, insiderRisk. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider, microsoftAdminPortals, deviceCodeFlow, accountTransfer, insiderRisk.
    rule_satisfied: Optional[ConditionalAccessRule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessRuleSatisfied:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessRuleSatisfied
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessRuleSatisfied()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_conditions import ConditionalAccessConditions
        from .conditional_access_rule import ConditionalAccessRule

        from .conditional_access_conditions import ConditionalAccessConditions
        from .conditional_access_rule import ConditionalAccessRule

        fields: dict[str, Callable[[Any], None]] = {
            "conditionalAccessCondition": lambda n : setattr(self, 'conditional_access_condition', n.get_collection_of_enum_values(ConditionalAccessConditions)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleSatisfied": lambda n : setattr(self, 'rule_satisfied', n.get_enum_value(ConditionalAccessRule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("conditionalAccessCondition", self.conditional_access_condition)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleSatisfied", self.rule_satisfied)
        writer.write_additional_data_value(self.additional_data)
    

