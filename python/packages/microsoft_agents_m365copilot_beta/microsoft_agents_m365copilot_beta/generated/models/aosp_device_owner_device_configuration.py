from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class AospDeviceOwnerDeviceConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the AndroidDeviceOwnerAOSPDeviceConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.aospDeviceOwnerDeviceConfiguration"
    # Indicates whether or not the user is allowed to enable unknown sources setting. When set to true, user is not allowed to enable unknown sources settings.
    apps_block_install_from_unknown_sources: Optional[bool] = None
    # Indicates whether or not to block a user from configuring bluetooth.
    bluetooth_block_configuration: Optional[bool] = None
    # Indicates whether or not to disable the use of bluetooth. When set to true, bluetooth cannot be enabled on the device.
    bluetooth_blocked: Optional[bool] = None
    # Indicates whether or not to disable the use of the camera.
    camera_blocked: Optional[bool] = None
    # Indicates whether or not the factory reset option in settings is disabled.
    factory_reset_blocked: Optional[bool] = None
    # Indicates the minimum length of the password required on the device. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
    password_required_type: Optional[AndroidDeviceOwnerRequiredPasswordType] = None
    # Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Indicates whether or not to disable the capability to take screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from enabling debugging features on the device.
    security_allow_debugging_features: Optional[bool] = None
    # Indicates whether or not to block external media.
    storage_block_external_media: Optional[bool] = None
    # Indicates whether or not to block USB file transfer.
    storage_block_usb_file_transfer: Optional[bool] = None
    # Indicates whether or not to block the user from editing the wifi connection settings.
    wifi_block_edit_configurations: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AospDeviceOwnerDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AospDeviceOwnerDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AospDeviceOwnerDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .device_configuration import DeviceConfiguration

        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "appsBlockInstallFromUnknownSources": lambda n : setattr(self, 'apps_block_install_from_unknown_sources', n.get_bool_value()),
            "bluetoothBlockConfiguration": lambda n : setattr(self, 'bluetooth_block_configuration', n.get_bool_value()),
            "bluetoothBlocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "factoryResetBlocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "securityAllowDebuggingFeatures": lambda n : setattr(self, 'security_allow_debugging_features', n.get_bool_value()),
            "storageBlockExternalMedia": lambda n : setattr(self, 'storage_block_external_media', n.get_bool_value()),
            "storageBlockUsbFileTransfer": lambda n : setattr(self, 'storage_block_usb_file_transfer', n.get_bool_value()),
            "wifiBlockEditConfigurations": lambda n : setattr(self, 'wifi_block_edit_configurations', n.get_bool_value()),
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
        writer.write_bool_value("appsBlockInstallFromUnknownSources", self.apps_block_install_from_unknown_sources)
        writer.write_bool_value("bluetoothBlockConfiguration", self.bluetooth_block_configuration)
        writer.write_bool_value("bluetoothBlocked", self.bluetooth_blocked)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("factoryResetBlocked", self.factory_reset_blocked)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("securityAllowDebuggingFeatures", self.security_allow_debugging_features)
        writer.write_bool_value("storageBlockExternalMedia", self.storage_block_external_media)
        writer.write_bool_value("storageBlockUsbFileTransfer", self.storage_block_usb_file_transfer)
        writer.write_bool_value("wifiBlockEditConfigurations", self.wifi_block_edit_configurations)
    

