from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
    from .device_management_resource_access_profile_intent import DeviceManagementResourceAccessProfileIntent
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementResourceAccessProfileAssignment(Entity, Parsable):
    """
    Entity that describes tenant level settings for derived credentials
    """
    # The administrator intent for the assignment of the profile.
    intent: Optional[DeviceManagementResourceAccessProfileIntent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the source of the assignment.
    source_id: Optional[str] = None
    # Base type for assignment targets.
    target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementResourceAccessProfileAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementResourceAccessProfileAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementResourceAccessProfileAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .device_management_resource_access_profile_intent import DeviceManagementResourceAccessProfileIntent
        from .entity import Entity

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .device_management_resource_access_profile_intent import DeviceManagementResourceAccessProfileIntent
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(DeviceManagementResourceAccessProfileIntent)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_enum_value("intent", self.intent)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_object_value("target", self.target)
    

