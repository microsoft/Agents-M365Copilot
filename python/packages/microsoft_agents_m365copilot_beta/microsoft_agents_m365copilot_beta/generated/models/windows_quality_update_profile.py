from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .expedited_windows_quality_update_settings import ExpeditedWindowsQualityUpdateSettings
    from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment

from .entity import Entity

@dataclass
class WindowsQualityUpdateProfile(Entity, Parsable):
    """
    Windows Quality Update Profile
    """
    # The list of group assignments of the profile.
    assignments: Optional[list[WindowsQualityUpdateProfileAssignment]] = None
    # The date time that the profile was created.
    created_date_time: Optional[datetime.datetime] = None
    # Friendly display name of the quality update profile deployable content
    deployable_content_display_name: Optional[str] = None
    # The description of the profile which is specified by the user.
    description: Optional[str] = None
    # The display name for the profile.
    display_name: Optional[str] = None
    # Expedited update settings.
    expedited_update_settings: Optional[ExpeditedWindowsQualityUpdateSettings] = None
    # The date time that the profile was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Friendly release date to display for a Quality Update release
    release_date_display_name: Optional[str] = None
    # List of Scope Tags for this Quality Update entity.
    role_scope_tag_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .expedited_windows_quality_update_settings import ExpeditedWindowsQualityUpdateSettings
        from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment

        from .entity import Entity
        from .expedited_windows_quality_update_settings import ExpeditedWindowsQualityUpdateSettings
        from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WindowsQualityUpdateProfileAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployableContentDisplayName": lambda n : setattr(self, 'deployable_content_display_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expeditedUpdateSettings": lambda n : setattr(self, 'expedited_update_settings', n.get_object_value(ExpeditedWindowsQualityUpdateSettings)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "releaseDateDisplayName": lambda n : setattr(self, 'release_date_display_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deployableContentDisplayName", self.deployable_content_display_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("expeditedUpdateSettings", self.expedited_update_settings)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("releaseDateDisplayName", self.release_date_display_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

