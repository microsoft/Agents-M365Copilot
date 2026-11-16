from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_store_auto_update_mode import AndroidManagedStoreAutoUpdateMode
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class AndroidManagedStoreAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign an Android Managed Store mobile app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidManagedStoreAppAssignmentSettings"
    # The track IDs to enable for this app assignment.
    android_managed_store_app_track_ids: Optional[list[str]] = None
    # Prioritization for automatic updates of Android Managed Store apps set on assignment.
    auto_update_mode: Optional[AndroidManagedStoreAutoUpdateMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedStoreAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedStoreAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_store_auto_update_mode import AndroidManagedStoreAutoUpdateMode
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .android_managed_store_auto_update_mode import AndroidManagedStoreAutoUpdateMode
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "androidManagedStoreAppTrackIds": lambda n : setattr(self, 'android_managed_store_app_track_ids', n.get_collection_of_primitive_values(str)),
            "autoUpdateMode": lambda n : setattr(self, 'auto_update_mode', n.get_enum_value(AndroidManagedStoreAutoUpdateMode)),
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
        writer.write_collection_of_primitive_values("androidManagedStoreAppTrackIds", self.android_managed_store_app_track_ids)
        writer.write_enum_value("autoUpdateMode", self.auto_update_mode)
    

