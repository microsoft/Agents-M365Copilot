from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_quality_update_approval_setting import WindowsQualityUpdateApprovalSetting
    from .windows_quality_update_policy_assignment import WindowsQualityUpdatePolicyAssignment

from .entity import Entity

@dataclass
class WindowsQualityUpdatePolicy(Entity, Parsable):
    """
    Windows Quality Update Policy
    """
    # The list of approval settings for this policy. The maximun number of approval settings supported for one policy is 6. The expected number of approval settings for one policy from UX is 4.
    approval_settings: Optional[list[WindowsQualityUpdateApprovalSetting]] = None
    # List of the groups this profile is assgined to.
    assignments: Optional[list[WindowsQualityUpdatePolicyAssignment]] = None
    # Timestamp of when the profile was created. The value cannot be modified and is automatically populated when the profile is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. Read-only
    created_date_time: Optional[datetime.datetime] = None
    # The description of the policy which is specified by the user. Max allowed length is 1500 chars.
    description: Optional[str] = None
    # The display name for the policy. Max allowed length is 200 chars.
    display_name: Optional[str] = None
    # Indicates if hotpatch is enabled for the tenants. When 'true', tenant can apply quality updates without rebooting their devices. When 'false', tenant devices will receive cold patch associated with Windows quality updates.
    hotpatch_enabled: Optional[bool] = None
    # Timestamp of when the profile was modified. The value cannot be modified and is automatically populated when the profile is modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. Read-only
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of the scope tag ids for this profile.
    role_scope_tag_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdatePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdatePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdatePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_quality_update_approval_setting import WindowsQualityUpdateApprovalSetting
        from .windows_quality_update_policy_assignment import WindowsQualityUpdatePolicyAssignment

        from .entity import Entity
        from .windows_quality_update_approval_setting import WindowsQualityUpdateApprovalSetting
        from .windows_quality_update_policy_assignment import WindowsQualityUpdatePolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "approvalSettings": lambda n : setattr(self, 'approval_settings', n.get_collection_of_object_values(WindowsQualityUpdateApprovalSetting)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WindowsQualityUpdatePolicyAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hotpatchEnabled": lambda n : setattr(self, 'hotpatch_enabled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("approvalSettings", self.approval_settings)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hotpatchEnabled", self.hotpatch_enabled)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

