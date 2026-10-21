from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .driver_update_profile_approval_type import DriverUpdateProfileApprovalType
    from .entity import Entity
    from .windows_driver_update_inventory import WindowsDriverUpdateInventory
    from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
    from .windows_driver_update_profile_inventory_sync_status import WindowsDriverUpdateProfileInventorySyncStatus

from .entity import Entity

@dataclass
class WindowsDriverUpdateProfile(Entity, Parsable):
    """
    Windows Driver Update Profile
    """
    # An enum type to represent approval type of a driver update profile.
    approval_type: Optional[DriverUpdateProfileApprovalType] = None
    # The list of group assignments of the profile.
    assignments: Optional[list[WindowsDriverUpdateProfileAssignment]] = None
    # The date time that the profile was created.
    created_date_time: Optional[datetime.datetime] = None
    # Deployment deferral settings in days, only applicable when ApprovalType is set to automatic approval.
    deployment_deferral_in_days: Optional[int] = None
    # The description of the profile which is specified by the user.
    description: Optional[str] = None
    # Number of devices reporting for this profile
    device_reporting: Optional[int] = None
    # The display name for the profile.
    display_name: Optional[str] = None
    # Driver inventories for this profile.
    driver_inventories: Optional[list[WindowsDriverUpdateInventory]] = None
    # Driver inventory sync status for this profile.
    inventory_sync_status: Optional[WindowsDriverUpdateProfileInventorySyncStatus] = None
    # The date time that the profile was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Number of new driver updates available for this profile.
    new_updates: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Driver Update entity.
    role_scope_tag_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDriverUpdateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDriverUpdateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDriverUpdateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .driver_update_profile_approval_type import DriverUpdateProfileApprovalType
        from .entity import Entity
        from .windows_driver_update_inventory import WindowsDriverUpdateInventory
        from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
        from .windows_driver_update_profile_inventory_sync_status import WindowsDriverUpdateProfileInventorySyncStatus

        from .driver_update_profile_approval_type import DriverUpdateProfileApprovalType
        from .entity import Entity
        from .windows_driver_update_inventory import WindowsDriverUpdateInventory
        from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
        from .windows_driver_update_profile_inventory_sync_status import WindowsDriverUpdateProfileInventorySyncStatus

        fields: dict[str, Callable[[Any], None]] = {
            "approvalType": lambda n : setattr(self, 'approval_type', n.get_enum_value(DriverUpdateProfileApprovalType)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WindowsDriverUpdateProfileAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deploymentDeferralInDays": lambda n : setattr(self, 'deployment_deferral_in_days', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceReporting": lambda n : setattr(self, 'device_reporting', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "driverInventories": lambda n : setattr(self, 'driver_inventories', n.get_collection_of_object_values(WindowsDriverUpdateInventory)),
            "inventorySyncStatus": lambda n : setattr(self, 'inventory_sync_status', n.get_object_value(WindowsDriverUpdateProfileInventorySyncStatus)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "newUpdates": lambda n : setattr(self, 'new_updates', n.get_int_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("approvalType", self.approval_type)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("deploymentDeferralInDays", self.deployment_deferral_in_days)
        writer.write_str_value("description", self.description)
        writer.write_int_value("deviceReporting", self.device_reporting)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("driverInventories", self.driver_inventories)
        writer.write_object_value("inventorySyncStatus", self.inventory_sync_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("newUpdates", self.new_updates)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

