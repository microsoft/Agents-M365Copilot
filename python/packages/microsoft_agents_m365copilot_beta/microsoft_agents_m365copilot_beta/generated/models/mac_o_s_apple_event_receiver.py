from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

@dataclass
class MacOSAppleEventReceiver(AdditionalDataHolder, Parsable):
    """
    Represents a process that can receive an Apple Event notification.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Allow or block this app from receiving Apple events.
    allowed: Optional[bool] = None
    # Code requirement for the app or binary that receives the Apple Event.
    code_requirement: Optional[str] = None
    # Bundle ID of the app or file path of the process or executable that receives the Apple Event.
    identifier: Optional[str] = None
    # Process identifier types for MacOS Privacy Preferences
    identifier_type: Optional[MacOSProcessIdentifierType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSAppleEventReceiver:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSAppleEventReceiver
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSAppleEventReceiver()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

        from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

        fields: dict[str, Callable[[Any], None]] = {
            "allowed": lambda n : setattr(self, 'allowed', n.get_bool_value()),
            "codeRequirement": lambda n : setattr(self, 'code_requirement', n.get_str_value()),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "identifierType": lambda n : setattr(self, 'identifier_type', n.get_enum_value(MacOSProcessIdentifierType)),
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
        writer.write_bool_value("allowed", self.allowed)
        writer.write_str_value("codeRequirement", self.code_requirement)
        writer.write_str_value("identifier", self.identifier)
        writer.write_enum_value("identifierType", self.identifier_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

