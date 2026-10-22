from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pre_approved_permissions import PreApprovedPermissions

from .pre_approved_permissions import PreApprovedPermissions

@dataclass
class EnumeratedPreApprovedPermissions(PreApprovedPermissions, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.enumeratedPreApprovedPermissions"
    # The list of id values for the specific resource-specific application permissions to match with. See the resourceSpecificApplicationPermissions property of the servicePrincipal object for the list of permissions.
    permission_ids: Optional[list[str]] = None
    # The appId of the resource application (the API). Required.
    resource_application_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnumeratedPreApprovedPermissions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnumeratedPreApprovedPermissions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnumeratedPreApprovedPermissions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pre_approved_permissions import PreApprovedPermissions

        from .pre_approved_permissions import PreApprovedPermissions

        fields: dict[str, Callable[[Any], None]] = {
            "permissionIds": lambda n : setattr(self, 'permission_ids', n.get_collection_of_primitive_values(str)),
            "resourceApplicationId": lambda n : setattr(self, 'resource_application_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("permissionIds", self.permission_ids)
        writer.write_str_value("resourceApplicationId", self.resource_application_id)
    

