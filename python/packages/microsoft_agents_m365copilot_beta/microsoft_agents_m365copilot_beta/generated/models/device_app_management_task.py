from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_vulnerability_task import AppVulnerabilityTask
    from .device_app_management_task_category import DeviceAppManagementTaskCategory
    from .device_app_management_task_priority import DeviceAppManagementTaskPriority
    from .device_app_management_task_status import DeviceAppManagementTaskStatus
    from .entity import Entity
    from .security_configuration_task import SecurityConfigurationTask
    from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask

from .entity import Entity

@dataclass
class DeviceAppManagementTask(Entity, Parsable):
    """
    A device app management task.
    """
    # The name or email of the admin this task is assigned to.
    assigned_to: Optional[str] = None
    # Device app management task category.
    category: Optional[DeviceAppManagementTaskCategory] = None
    # The created date.
    created_date_time: Optional[datetime.datetime] = None
    # The email address of the creator.
    creator: Optional[str] = None
    # Notes from the creator.
    creator_notes: Optional[str] = None
    # The description.
    description: Optional[str] = None
    # The name.
    display_name: Optional[str] = None
    # The due date.
    due_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device app management task priority.
    priority: Optional[DeviceAppManagementTaskPriority] = None
    # Device app management task status.
    status: Optional[DeviceAppManagementTaskStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceAppManagementTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAppManagementTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appVulnerabilityTask".casefold():
            from .app_vulnerability_task import AppVulnerabilityTask

            return AppVulnerabilityTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityConfigurationTask".casefold():
            from .security_configuration_task import SecurityConfigurationTask

            return SecurityConfigurationTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmanagedDeviceDiscoveryTask".casefold():
            from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask

            return UnmanagedDeviceDiscoveryTask()
        return DeviceAppManagementTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_vulnerability_task import AppVulnerabilityTask
        from .device_app_management_task_category import DeviceAppManagementTaskCategory
        from .device_app_management_task_priority import DeviceAppManagementTaskPriority
        from .device_app_management_task_status import DeviceAppManagementTaskStatus
        from .entity import Entity
        from .security_configuration_task import SecurityConfigurationTask
        from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask

        from .app_vulnerability_task import AppVulnerabilityTask
        from .device_app_management_task_category import DeviceAppManagementTaskCategory
        from .device_app_management_task_priority import DeviceAppManagementTaskPriority
        from .device_app_management_task_status import DeviceAppManagementTaskStatus
        from .entity import Entity
        from .security_configuration_task import SecurityConfigurationTask
        from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(DeviceAppManagementTaskCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creator": lambda n : setattr(self, 'creator', n.get_str_value()),
            "creatorNotes": lambda n : setattr(self, 'creator_notes', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(DeviceAppManagementTaskPriority)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DeviceAppManagementTaskStatus)),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("creator", self.creator)
        writer.write_str_value("creatorNotes", self.creator_notes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("status", self.status)
    

