from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .ddm_app_automatic_app_updates import DdmAppAutomaticAppUpdates
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class MacOsDdmVppAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign a macOS Declarative Device Management (DDM) VPP mobile app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOsDdmVppAppAssignmentSettings"
    # Specifies whether the device automatically updates the app. Possible values are: 'alwaysOn', 'alwaysOff', 'storeSettings'. By default, this value is set to 'storeSettings'.
    automatic_app_updates: Optional[DdmAppAutomaticAppUpdates] = None
    # The unique identifier of the DDM app configuration to associate with the app.
    ddm_app_config_id: Optional[UUID] = None
    # If true, the device installs an iOS or iPadOS app that runs on a Mac with Apple Silicon. This is only used when the app is a VPP app. Default is false.
    is_ios_app: Optional[bool] = None
    # When TRUE, indicates that the app should be assigned using device licensing. When FALSE, indicates that the app should be assigned using user licensing. By default, this property is set to FALSE.
    use_device_licensing: Optional[bool] = None
    # Specifies the version of the VPP app to install. When not set, the device installs the latest version. When set, the device installs the specified version. The device never installs an older version of the app over a newer version. This property maps to the Version key in Apple's AppManagedInstallBehaviorObject declaration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOsDdmVppAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOsDdmVppAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOsDdmVppAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ddm_app_automatic_app_updates import DdmAppAutomaticAppUpdates
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .ddm_app_automatic_app_updates import DdmAppAutomaticAppUpdates
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "automaticAppUpdates": lambda n : setattr(self, 'automatic_app_updates', n.get_enum_value(DdmAppAutomaticAppUpdates)),
            "ddmAppConfigId": lambda n : setattr(self, 'ddm_app_config_id', n.get_uuid_value()),
            "isIosApp": lambda n : setattr(self, 'is_ios_app', n.get_bool_value()),
            "useDeviceLicensing": lambda n : setattr(self, 'use_device_licensing', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_enum_value("automaticAppUpdates", self.automatic_app_updates)
        writer.write_uuid_value("ddmAppConfigId", self.ddm_app_config_id)
        writer.write_bool_value("isIosApp", self.is_ios_app)
        writer.write_bool_value("useDeviceLicensing", self.use_device_licensing)
        writer.write_int_value("version", self.version)
    

