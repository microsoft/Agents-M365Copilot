from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_store_app_track import AndroidManagedStoreAppTrack
    from .android_managed_store_web_app import AndroidManagedStoreWebApp
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class AndroidManagedStoreApp(MobileApp, Parsable):
    """
    Contains properties and inherited properties for Android Managed Store Apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidManagedStoreApp"
    # The Identity Name.
    app_identifier: Optional[str] = None
    # The Play for Work Store app URL. This property is read-only.
    app_store_url: Optional[str] = None
    # The tracks that are visible to this enterprise. This property is read-only.
    app_tracks: Optional[list[AndroidManagedStoreAppTrack]] = None
    # Indicates whether the app is only available to a given enterprise's users. This property is read-only.
    is_private: Optional[bool] = None
    # Indicates whether the app is a preinstalled system app.
    is_system_app: Optional[bool] = None
    # The package identifier. This property is read-only.
    package_id: Optional[str] = None
    # Whether this app supports OEMConfig policy. This property is read-only.
    supports_oem_config: Optional[bool] = None
    # The total number of VPP licenses. This property is read-only.
    total_license_count: Optional[int] = None
    # The number of VPP licenses in use. This property is read-only.
    used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreWebApp".casefold():
            from .android_managed_store_web_app import AndroidManagedStoreWebApp

            return AndroidManagedStoreWebApp()
        return AndroidManagedStoreApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_store_app_track import AndroidManagedStoreAppTrack
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .mobile_app import MobileApp

        from .android_managed_store_app_track import AndroidManagedStoreAppTrack
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "appIdentifier": lambda n : setattr(self, 'app_identifier', n.get_str_value()),
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "appTracks": lambda n : setattr(self, 'app_tracks', n.get_collection_of_object_values(AndroidManagedStoreAppTrack)),
            "isPrivate": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "isSystemApp": lambda n : setattr(self, 'is_system_app', n.get_bool_value()),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "supportsOemConfig": lambda n : setattr(self, 'supports_oem_config', n.get_bool_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
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
        writer.write_str_value("appIdentifier", self.app_identifier)
        writer.write_bool_value("isSystemApp", self.is_system_app)
    

