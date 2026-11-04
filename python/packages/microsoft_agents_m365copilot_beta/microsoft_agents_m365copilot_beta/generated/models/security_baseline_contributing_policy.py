from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_baseline_policy_source_type import SecurityBaselinePolicySourceType

@dataclass
class SecurityBaselineContributingPolicy(AdditionalDataHolder, Parsable):
    """
    The security baseline compliance state of a setting for a device
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name of the policy
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier of the policy
    source_id: Optional[str] = None
    # Authoring source of a policy
    source_type: Optional[SecurityBaselinePolicySourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineContributingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineContributingPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineContributingPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .security_baseline_policy_source_type import SecurityBaselinePolicySourceType

        from .security_baseline_policy_source_type import SecurityBaselinePolicySourceType

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(SecurityBaselinePolicySourceType)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_additional_data_value(self.additional_data)
    

