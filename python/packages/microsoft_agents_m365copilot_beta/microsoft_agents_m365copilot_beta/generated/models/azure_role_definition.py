from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_role_definition_type import AzureRoleDefinitionType
    from .entity import Entity

from .entity import Entity

@dataclass
class AzureRoleDefinition(Entity, Parsable):
    # Scopes at which the Azure role can be assigned. For more information about common patterns, see Understand Azure role definitions: AssignableScopes. Supports $filter (eq).
    assignable_scopes: Optional[list[str]] = None
    # The azureRoleDefinitionType property
    azure_role_definition_type: Optional[AzureRoleDefinitionType] = None
    # Name of the Azure role. Supports $filter (eq, contains).
    display_name: Optional[str] = None
    # Identifier of an Azure role defined by Microsoft Azure. Alternate key. Supports $filter (eq).
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureRoleDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureRoleDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .azure_role_definition_type import AzureRoleDefinitionType
        from .entity import Entity

        from .azure_role_definition_type import AzureRoleDefinitionType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignableScopes": lambda n : setattr(self, 'assignable_scopes', n.get_collection_of_primitive_values(str)),
            "azureRoleDefinitionType": lambda n : setattr(self, 'azure_role_definition_type', n.get_enum_value(AzureRoleDefinitionType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("assignableScopes", self.assignable_scopes)
        writer.write_enum_value("azureRoleDefinitionType", self.azure_role_definition_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
    

