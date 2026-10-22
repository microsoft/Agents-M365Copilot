from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class MobileAppInstallSummary(Entity, Parsable):
    """
    Contains properties for the installation summary of a mobile app. This will be deprecated starting May, 2023 (Intune Release 2305).
    """
    # Number of Devices that have failed to install this app.
    failed_device_count: Optional[int] = None
    # Number of Users that have 1 or more device that failed to install this app.
    failed_user_count: Optional[int] = None
    # Number of Devices that have successfully installed this app.
    installed_device_count: Optional[int] = None
    # Number of Users whose devices have all succeeded to install this app.
    installed_user_count: Optional[int] = None
    # Number of Devices that are not applicable for this app.
    not_applicable_device_count: Optional[int] = None
    # Number of Users whose devices were all not applicable for this app.
    not_applicable_user_count: Optional[int] = None
    # Number of Devices that does not have this app installed.
    not_installed_device_count: Optional[int] = None
    # Number of Users that have 1 or more devices that did not install this app.
    not_installed_user_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of Devices that have been notified to install this app.
    pending_install_device_count: Optional[int] = None
    # Number of Users that have 1 or more device that have been notified to install this app and have 0 devices with failures.
    pending_install_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppInstallSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppInstallSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppInstallSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "failedUserCount": lambda n : setattr(self, 'failed_user_count', n.get_int_value()),
            "installedDeviceCount": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "installedUserCount": lambda n : setattr(self, 'installed_user_count', n.get_int_value()),
            "notApplicableDeviceCount": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "notApplicableUserCount": lambda n : setattr(self, 'not_applicable_user_count', n.get_int_value()),
            "notInstalledDeviceCount": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
            "notInstalledUserCount": lambda n : setattr(self, 'not_installed_user_count', n.get_int_value()),
            "pendingInstallDeviceCount": lambda n : setattr(self, 'pending_install_device_count', n.get_int_value()),
            "pendingInstallUserCount": lambda n : setattr(self, 'pending_install_user_count', n.get_int_value()),
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
    

