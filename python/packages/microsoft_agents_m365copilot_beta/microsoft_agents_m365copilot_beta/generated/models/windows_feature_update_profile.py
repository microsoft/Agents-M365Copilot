from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
    from .windows_update_rollout_settings import WindowsUpdateRolloutSettings

from .entity import Entity

@dataclass
class WindowsFeatureUpdateProfile(Entity, Parsable):
    """
    Windows Feature Update Profile
    """
    # The list of group assignments of the profile.
    assignments: Optional[list[WindowsFeatureUpdateProfileAssignment]] = None
    # The date time that the profile was created.
    created_date_time: Optional[datetime.datetime] = None
    # Friendly display name of the quality update profile deployable content
    deployable_content_display_name: Optional[str] = None
    # The description of the profile which is specified by the user.
    description: Optional[str] = None
    # The display name of the profile.
    display_name: Optional[str] = None
    # The last supported date for a feature update
    end_of_support_date: Optional[datetime.datetime] = None
    # The feature update version that will be deployed to the devices targeted by this profile. The version could be any supported version for example 1709, 1803 or 1809 and so on.
    feature_update_version: Optional[str] = None
    # If true, the Windows 11 update will become optional
    install_feature_updates_optional: Optional[bool] = None
    # If true, the latest Microsoft Windows 10 update will be installed on devices ineligible for Microsoft Windows 11
    install_latest_windows10_on_windows11_ineligible_device: Optional[bool] = None
    # The date time that the profile was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Feature Update entity.
    role_scope_tag_ids: Optional[list[str]] = None
    # The windows update rollout settings, including offer start date time, offer end date time, and days between each set of offers.
    rollout_settings: Optional[WindowsUpdateRolloutSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsFeatureUpdateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsFeatureUpdateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsFeatureUpdateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
        from .windows_update_rollout_settings import WindowsUpdateRolloutSettings

        from .entity import Entity
        from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment
        from .windows_update_rollout_settings import WindowsUpdateRolloutSettings

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WindowsFeatureUpdateProfileAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployableContentDisplayName": lambda n : setattr(self, 'deployable_content_display_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endOfSupportDate": lambda n : setattr(self, 'end_of_support_date', n.get_datetime_value()),
            "featureUpdateVersion": lambda n : setattr(self, 'feature_update_version', n.get_str_value()),
            "installFeatureUpdatesOptional": lambda n : setattr(self, 'install_feature_updates_optional', n.get_bool_value()),
            "installLatestWindows10OnWindows11IneligibleDevice": lambda n : setattr(self, 'install_latest_windows10_on_windows11_ineligible_device', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "rolloutSettings": lambda n : setattr(self, 'rollout_settings', n.get_object_value(WindowsUpdateRolloutSettings)),
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
        writer.write_datetime_value("endOfSupportDate", self.end_of_support_date)
        writer.write_str_value("featureUpdateVersion", self.feature_update_version)
        writer.write_bool_value("installFeatureUpdatesOptional", self.install_feature_updates_optional)
        writer.write_bool_value("installLatestWindows10OnWindows11IneligibleDevice", self.install_latest_windows10_on_windows11_ineligible_device)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_object_value("rolloutSettings", self.rollout_settings)
    

