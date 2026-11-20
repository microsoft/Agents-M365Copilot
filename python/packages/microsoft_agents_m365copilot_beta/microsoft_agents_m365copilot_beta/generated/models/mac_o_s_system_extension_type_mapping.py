from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_system_extension_type import MacOSSystemExtensionType

@dataclass
class MacOSSystemExtensionTypeMapping(AdditionalDataHolder, Parsable):
    """
    Represents a mapping between team identifiers for macOS system extensions and system extension types.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Flag enum representing the allowed macOS system extension types.
    allowed_types: Optional[MacOSSystemExtensionType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Gets or sets the team identifier used to sign the system extension.
    team_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSSystemExtensionTypeMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSystemExtensionTypeMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSSystemExtensionTypeMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_system_extension_type import MacOSSystemExtensionType

        from .mac_o_s_system_extension_type import MacOSSystemExtensionType

        fields: dict[str, Callable[[Any], None]] = {
            "allowedTypes": lambda n : setattr(self, 'allowed_types', n.get_collection_of_enum_values(MacOSSystemExtensionType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "teamIdentifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
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
        writer.write_enum_value("allowedTypes", self.allowed_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("teamIdentifier", self.team_identifier)
        writer.write_additional_data_value(self.additional_data)
    

