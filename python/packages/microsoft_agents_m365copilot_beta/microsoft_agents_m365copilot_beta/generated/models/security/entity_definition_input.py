from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_definition_input_role import EntityDefinitionInputRole
    from .manual_alert_entity_type import ManualAlertEntityType

@dataclass
class EntityDefinitionInput(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The type of identifier used for the entity. The supported identifiers depend on the entityType. See supported entity identifiers. Key.
    entity_identifier: Optional[str] = None
    # The entityType property
    entity_type: Optional[ManualAlertEntityType] = None
    # The actual identifier value for the entity (for example, john@contoso.com for a user, or 192.168.1.1 for an IP address). Maximum 1000 characters.
    identifier_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role property
    role: Optional[EntityDefinitionInputRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntityDefinitionInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntityDefinitionInput
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntityDefinitionInput()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity_definition_input_role import EntityDefinitionInputRole
        from .manual_alert_entity_type import ManualAlertEntityType

        from .entity_definition_input_role import EntityDefinitionInputRole
        from .manual_alert_entity_type import ManualAlertEntityType

        fields: dict[str, Callable[[Any], None]] = {
            "entityIdentifier": lambda n : setattr(self, 'entity_identifier', n.get_str_value()),
            "entityType": lambda n : setattr(self, 'entity_type', n.get_enum_value(ManualAlertEntityType)),
            "identifierValue": lambda n : setattr(self, 'identifier_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(EntityDefinitionInputRole)),
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
        writer.write_str_value("entityIdentifier", self.entity_identifier)
        writer.write_enum_value("entityType", self.entity_type)
        writer.write_str_value("identifierValue", self.identifier_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

