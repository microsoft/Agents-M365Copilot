from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_minimum_operating_system import AndroidMinimumOperatingSystem
    from .android_targeted_platforms import AndroidTargetedPlatforms
    from .mobile_lob_app import MobileLobApp

from .mobile_lob_app import MobileLobApp

@dataclass
class AndroidLobApp(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for Android Line Of Business apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidLobApp"
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[AndroidMinimumOperatingSystem] = None
    # The package identifier.
    package_id: Optional[str] = None
    # Specifies which platform(s) can be targeted for a given Android LOB application or Managed Android LOB application.
    targeted_platforms: Optional[AndroidTargetedPlatforms] = None
    # The version code of Android Line of Business (LoB) app.
    version_code: Optional[str] = None
    # The version name of Android Line of Business (LoB) app.
    version_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidLobApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidLobApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_minimum_operating_system import AndroidMinimumOperatingSystem
        from .android_targeted_platforms import AndroidTargetedPlatforms
        from .mobile_lob_app import MobileLobApp

        from .android_minimum_operating_system import AndroidMinimumOperatingSystem
        from .android_targeted_platforms import AndroidTargetedPlatforms
        from .mobile_lob_app import MobileLobApp

        fields: dict[str, Callable[[Any], None]] = {
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(AndroidMinimumOperatingSystem)),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "targetedPlatforms": lambda n : setattr(self, 'targeted_platforms', n.get_collection_of_enum_values(AndroidTargetedPlatforms)),
            "versionCode": lambda n : setattr(self, 'version_code', n.get_str_value()),
            "versionName": lambda n : setattr(self, 'version_name', n.get_str_value()),
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
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("packageId", self.package_id)
        writer.write_enum_value("targetedPlatforms", self.targeted_platforms)
        writer.write_str_value("versionCode", self.version_code)
        writer.write_str_value("versionName", self.version_name)
    

