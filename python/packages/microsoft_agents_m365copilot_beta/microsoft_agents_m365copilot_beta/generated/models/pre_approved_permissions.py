from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all_pre_approved_permissions import AllPreApprovedPermissions
    from .all_pre_approved_permissions_on_resource_app import AllPreApprovedPermissionsOnResourceApp
    from .enumerated_pre_approved_permissions import EnumeratedPreApprovedPermissions
    from .permission_kind import PermissionKind
    from .permission_type import PermissionType

@dataclass
class PreApprovedPermissions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the scope of permissions that are included in this condition set. Possible values: all for all permissions, enumerated for a given list of permissions, or allPermissionsOnResourceApp for all permissions from a given API. Required.
    permission_kind: Optional[PermissionKind] = None
    # The type of permission being granted. Possible values: application for application permissions, or delegated for delegated permissions. Required.
    permission_type: Optional[PermissionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PreApprovedPermissions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PreApprovedPermissions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allPreApprovedPermissions".casefold():
            from .all_pre_approved_permissions import AllPreApprovedPermissions

            return AllPreApprovedPermissions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allPreApprovedPermissionsOnResourceApp".casefold():
            from .all_pre_approved_permissions_on_resource_app import AllPreApprovedPermissionsOnResourceApp

            return AllPreApprovedPermissionsOnResourceApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enumeratedPreApprovedPermissions".casefold():
            from .enumerated_pre_approved_permissions import EnumeratedPreApprovedPermissions

            return EnumeratedPreApprovedPermissions()
        return PreApprovedPermissions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .all_pre_approved_permissions import AllPreApprovedPermissions
        from .all_pre_approved_permissions_on_resource_app import AllPreApprovedPermissionsOnResourceApp
        from .enumerated_pre_approved_permissions import EnumeratedPreApprovedPermissions
        from .permission_kind import PermissionKind
        from .permission_type import PermissionType

        from .all_pre_approved_permissions import AllPreApprovedPermissions
        from .all_pre_approved_permissions_on_resource_app import AllPreApprovedPermissionsOnResourceApp
        from .enumerated_pre_approved_permissions import EnumeratedPreApprovedPermissions
        from .permission_kind import PermissionKind
        from .permission_type import PermissionType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissionKind": lambda n : setattr(self, 'permission_kind', n.get_enum_value(PermissionKind)),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_enum_value(PermissionType)),
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
        writer.write_enum_value("permissionKind", self.permission_kind)
        writer.write_enum_value("permissionType", self.permission_type)
        writer.write_additional_data_value(self.additional_data)
    

