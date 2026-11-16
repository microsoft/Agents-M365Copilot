from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app import MobileApp
    from .mobile_app_install_status import MobileAppInstallStatus

from .entity import Entity

@dataclass
class UserAppInstallStatus(Entity, Parsable):
    """
    Contains properties for the installation status for a user. This will be deprecated starting May, 2023 (Intune Release 2305).
    """
    # The navigation link to the mobile app.
    app: Optional[MobileApp] = None
    # The install state of the app on devices.
    device_statuses: Optional[list[MobileAppInstallStatus]] = None
    # Failed Device Count.
    failed_device_count: Optional[int] = None
    # Installed Device Count.
    installed_device_count: Optional[int] = None
    # Not installed device count.
    not_installed_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User name.
    user_name: Optional[str] = None
    # User Principal Name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserAppInstallStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserAppInstallStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserAppInstallStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app import MobileApp
        from .mobile_app_install_status import MobileAppInstallStatus

        from .entity import Entity
        from .mobile_app import MobileApp
        from .mobile_app_install_status import MobileAppInstallStatus

        fields: dict[str, Callable[[Any], None]] = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(MobileApp)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(MobileAppInstallStatus)),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "installedDeviceCount": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "notInstalledDeviceCount": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_object_value("app", self.app)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("installedDeviceCount", self.installed_device_count)
        writer.write_int_value("notInstalledDeviceCount", self.not_installed_device_count)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

