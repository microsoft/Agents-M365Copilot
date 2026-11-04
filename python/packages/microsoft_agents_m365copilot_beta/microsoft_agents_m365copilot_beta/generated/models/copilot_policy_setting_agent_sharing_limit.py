from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CopilotPolicySettingAgentSharingLimit(AdditionalDataHolder, Parsable):
    """
    The supported range and default value for an agent sharing limit.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Default value.
    default: Optional[str] = None
    # Maximum supported value.
    max_value: Optional[str] = None
    # Minimum supported value.
    min_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPolicySettingAgentSharingLimit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPolicySettingAgentSharingLimit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPolicySettingAgentSharingLimit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "default": lambda n : setattr(self, 'default', n.get_str_value()),
            "maxValue": lambda n : setattr(self, 'max_value', n.get_str_value()),
            "minValue": lambda n : setattr(self, 'min_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("default", self.default)
        writer.write_str_value("maxValue", self.max_value)
        writer.write_str_value("minValue", self.min_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

