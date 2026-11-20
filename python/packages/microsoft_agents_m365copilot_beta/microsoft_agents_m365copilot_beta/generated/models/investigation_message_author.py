from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .investigation_message_role import InvestigationMessageRole

@dataclass
class InvestigationMessageAuthor(AdditionalDataHolder, Parsable):
    """
    Embedded message-author role and identifier, not an independently addressable resource.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Recorded author identifier. For a user it identifies a Microsoft Entra user; for an agent it identifies a service catalog/runtime agent, not an Entra directory object. Maps to backend id; a structural value, not an OData entity key. The source can return an empty value when no author id is recorded.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Transcript message role or recorded author kind. These are independent fields; a tool or system message can have an agent author.
    role: Optional[InvestigationMessageRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationMessageAuthor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationMessageAuthor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationMessageAuthor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .investigation_message_role import InvestigationMessageRole

        from .investigation_message_role import InvestigationMessageRole

        fields: dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(InvestigationMessageRole)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

