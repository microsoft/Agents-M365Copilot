from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_guard_local_system_authority_credential_guard_state import DeviceGuardLocalSystemAuthorityCredentialGuardState
    from .device_guard_virtualization_based_security_hardware_requirement_state import DeviceGuardVirtualizationBasedSecurityHardwareRequirementState
    from .device_guard_virtualization_based_security_state import DeviceGuardVirtualizationBasedSecurityState
    from .device_licensing_status import DeviceLicensingStatus
    from .shared_apple_device_user import SharedAppleDeviceUser

@dataclass
class HardwareInformation(AdditionalDataHolder, Parsable):
    """
    Hardware information of a given device.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of charge cycles the device’s current battery has gone through. Valid values 0 to 2147483647
    battery_charge_cycles: Optional[int] = None
    # The device’s current battery’s health percentage. Valid values 0 to 100
    battery_health_percentage: Optional[int] = None
    # The battery level, between 0.0 and 100, or null if the battery level cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 5.0 and later, and is available only when Device Information access right is obtained. Valid values 0 to 100
    battery_level_percentage: Optional[float] = None
    # The serial number of the device’s current battery
    battery_serial_number: Optional[str] = None
    # Cellular technology of the device
    cellular_technology: Optional[str] = None
    # Returns the fully qualified domain name of the device (if any). If the device is not domain-joined, it returns an empty string.
    device_full_qualified_domain_name: Optional[str] = None
    # The deviceGuardLocalSystemAuthorityCredentialGuardState property
    device_guard_local_system_authority_credential_guard_state: Optional[DeviceGuardLocalSystemAuthorityCredentialGuardState] = None
    # The deviceGuardVirtualizationBasedSecurityHardwareRequirementState property
    device_guard_virtualization_based_security_hardware_requirement_state: Optional[DeviceGuardVirtualizationBasedSecurityHardwareRequirementState] = None
    # The deviceGuardVirtualizationBasedSecurityState property
    device_guard_virtualization_based_security_state: Optional[DeviceGuardVirtualizationBasedSecurityState] = None
    # A standard error code indicating the last error, or 0 indicating no error (default). The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing. Valid values 0 to 2147483647
    device_licensing_last_error_code: Optional[int] = None
    # Error text message as a descripition for deviceLicensingLastErrorCode. The update frequency of this property is daily. Note this property is currently supported only for Windows based Device based subscription licensing.
    device_licensing_last_error_description: Optional[str] = None
    # Indicates the device licensing status after Windows device based subscription has been enabled.
    device_licensing_status: Optional[DeviceLicensingStatus] = None
    # eSIM identifier
    esim_identifier: Optional[str] = None
    # Free storage space of the device.
    free_storage_space: Optional[int] = None
    # IMEI
    imei: Optional[str] = None
    # IPAddressV4
    ip_address_v4: Optional[str] = None
    # Encryption status of the device
    is_encrypted: Optional[bool] = None
    # Shared iPad
    is_shared_device: Optional[bool] = None
    # Supervised mode of the device
    is_supervised: Optional[bool] = None
    # Manufacturer of the device
    manufacturer: Optional[str] = None
    # MEID
    meid: Optional[str] = None
    # Model of the device
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # String that specifies the OS edition.
    operating_system_edition: Optional[str] = None
    # Operating system language of the device
    operating_system_language: Optional[str] = None
    # Int that specifies the Windows Operating System ProductType. More details here https://go.microsoft.com/fwlink/?linkid=2126950. Valid values 0 to 2147483647
    operating_system_product_type: Optional[int] = None
    # Operating System Build Number on Android device
    os_build_number: Optional[str] = None
    # Phone number of the device
    phone_number: Optional[str] = None
    # The product name, e.g. iPad8,12 etc. The update frequency of this property is weekly. Note this property is currently supported only on iOS/MacOS devices, and is available only when Device Information access right is obtained.
    product_name: Optional[str] = None
    # The number of users currently on this device, or null (default) if the value of this property cannot be determined. The update frequency of this property is per-checkin. Note this property is currently supported only on devices running iOS 13.4 and later, and is available only when Device Information access right is obtained. Valid values 0 to 2147483647
    resident_users_count: Optional[int] = None
    # Serial number.
    serial_number: Optional[str] = None
    # All users on the shared Apple device
    shared_device_cached_users: Optional[list[SharedAppleDeviceUser]] = None
    # SubnetAddress
    subnet_address: Optional[str] = None
    # Subscriber carrier of the device
    subscriber_carrier: Optional[str] = None
    # BIOS version as reported by SMBIOS
    system_management_b_i_o_s_version: Optional[str] = None
    # Total storage space of the device.
    total_storage_space: Optional[int] = None
    # The identifying information that uniquely names the TPM manufacturer
    tpm_manufacturer: Optional[str] = None
    # String that specifies the specification version.
    tpm_specification_version: Optional[str] = None
    # The version of the TPM, as specified by the manufacturer
    tpm_version: Optional[str] = None
    # WiFi MAC address of the device
    wifi_mac: Optional[str] = None
    # A list of wired IPv4 addresses. The update frequency (the maximum delay for the change of property value to be synchronized from the device to the cloud storage) of this property is daily. Note this property is currently supported only on devices running on Windows.
    wired_i_pv4_addresses: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwareInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwareInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_guard_local_system_authority_credential_guard_state import DeviceGuardLocalSystemAuthorityCredentialGuardState
        from .device_guard_virtualization_based_security_hardware_requirement_state import DeviceGuardVirtualizationBasedSecurityHardwareRequirementState
        from .device_guard_virtualization_based_security_state import DeviceGuardVirtualizationBasedSecurityState
        from .device_licensing_status import DeviceLicensingStatus
        from .shared_apple_device_user import SharedAppleDeviceUser

        from .device_guard_local_system_authority_credential_guard_state import DeviceGuardLocalSystemAuthorityCredentialGuardState
        from .device_guard_virtualization_based_security_hardware_requirement_state import DeviceGuardVirtualizationBasedSecurityHardwareRequirementState
        from .device_guard_virtualization_based_security_state import DeviceGuardVirtualizationBasedSecurityState
        from .device_licensing_status import DeviceLicensingStatus
        from .shared_apple_device_user import SharedAppleDeviceUser

        fields: dict[str, Callable[[Any], None]] = {
            "batteryChargeCycles": lambda n : setattr(self, 'battery_charge_cycles', n.get_int_value()),
            "batteryHealthPercentage": lambda n : setattr(self, 'battery_health_percentage', n.get_int_value()),
            "batteryLevelPercentage": lambda n : setattr(self, 'battery_level_percentage', n.get_float_value()),
            "batterySerialNumber": lambda n : setattr(self, 'battery_serial_number', n.get_str_value()),
            "cellularTechnology": lambda n : setattr(self, 'cellular_technology', n.get_str_value()),
            "deviceFullQualifiedDomainName": lambda n : setattr(self, 'device_full_qualified_domain_name', n.get_str_value()),
            "deviceGuardLocalSystemAuthorityCredentialGuardState": lambda n : setattr(self, 'device_guard_local_system_authority_credential_guard_state', n.get_enum_value(DeviceGuardLocalSystemAuthorityCredentialGuardState)),
            "deviceGuardVirtualizationBasedSecurityHardwareRequirementState": lambda n : setattr(self, 'device_guard_virtualization_based_security_hardware_requirement_state', n.get_enum_value(DeviceGuardVirtualizationBasedSecurityHardwareRequirementState)),
            "deviceGuardVirtualizationBasedSecurityState": lambda n : setattr(self, 'device_guard_virtualization_based_security_state', n.get_enum_value(DeviceGuardVirtualizationBasedSecurityState)),
            "deviceLicensingLastErrorCode": lambda n : setattr(self, 'device_licensing_last_error_code', n.get_int_value()),
            "deviceLicensingLastErrorDescription": lambda n : setattr(self, 'device_licensing_last_error_description', n.get_str_value()),
            "deviceLicensingStatus": lambda n : setattr(self, 'device_licensing_status', n.get_enum_value(DeviceLicensingStatus)),
            "esimIdentifier": lambda n : setattr(self, 'esim_identifier', n.get_str_value()),
            "freeStorageSpace": lambda n : setattr(self, 'free_storage_space', n.get_int_value()),
            "imei": lambda n : setattr(self, 'imei', n.get_str_value()),
            "ipAddressV4": lambda n : setattr(self, 'ip_address_v4', n.get_str_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "isSharedDevice": lambda n : setattr(self, 'is_shared_device', n.get_bool_value()),
            "isSupervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "meid": lambda n : setattr(self, 'meid', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystemEdition": lambda n : setattr(self, 'operating_system_edition', n.get_str_value()),
            "operatingSystemLanguage": lambda n : setattr(self, 'operating_system_language', n.get_str_value()),
            "operatingSystemProductType": lambda n : setattr(self, 'operating_system_product_type', n.get_int_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "residentUsersCount": lambda n : setattr(self, 'resident_users_count', n.get_int_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "sharedDeviceCachedUsers": lambda n : setattr(self, 'shared_device_cached_users', n.get_collection_of_object_values(SharedAppleDeviceUser)),
            "subnetAddress": lambda n : setattr(self, 'subnet_address', n.get_str_value()),
            "subscriberCarrier": lambda n : setattr(self, 'subscriber_carrier', n.get_str_value()),
            "systemManagementBIOSVersion": lambda n : setattr(self, 'system_management_b_i_o_s_version', n.get_str_value()),
            "totalStorageSpace": lambda n : setattr(self, 'total_storage_space', n.get_int_value()),
            "tpmManufacturer": lambda n : setattr(self, 'tpm_manufacturer', n.get_str_value()),
            "tpmSpecificationVersion": lambda n : setattr(self, 'tpm_specification_version', n.get_str_value()),
            "tpmVersion": lambda n : setattr(self, 'tpm_version', n.get_str_value()),
            "wifiMac": lambda n : setattr(self, 'wifi_mac', n.get_str_value()),
            "wiredIPv4Addresses": lambda n : setattr(self, 'wired_i_pv4_addresses', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("batteryChargeCycles", self.battery_charge_cycles)
        writer.write_int_value("batteryHealthPercentage", self.battery_health_percentage)
        writer.write_float_value("batteryLevelPercentage", self.battery_level_percentage)
        writer.write_str_value("batterySerialNumber", self.battery_serial_number)
        writer.write_str_value("cellularTechnology", self.cellular_technology)
        writer.write_str_value("deviceFullQualifiedDomainName", self.device_full_qualified_domain_name)
        writer.write_enum_value("deviceGuardLocalSystemAuthorityCredentialGuardState", self.device_guard_local_system_authority_credential_guard_state)
        writer.write_enum_value("deviceGuardVirtualizationBasedSecurityHardwareRequirementState", self.device_guard_virtualization_based_security_hardware_requirement_state)
        writer.write_enum_value("deviceGuardVirtualizationBasedSecurityState", self.device_guard_virtualization_based_security_state)
        writer.write_int_value("deviceLicensingLastErrorCode", self.device_licensing_last_error_code)
        writer.write_str_value("deviceLicensingLastErrorDescription", self.device_licensing_last_error_description)
        writer.write_enum_value("deviceLicensingStatus", self.device_licensing_status)
        writer.write_str_value("esimIdentifier", self.esim_identifier)
        writer.write_int_value("freeStorageSpace", self.free_storage_space)
        writer.write_str_value("imei", self.imei)
        writer.write_str_value("ipAddressV4", self.ip_address_v4)
        writer.write_bool_value("isEncrypted", self.is_encrypted)
        writer.write_bool_value("isSharedDevice", self.is_shared_device)
        writer.write_bool_value("isSupervised", self.is_supervised)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("meid", self.meid)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystemEdition", self.operating_system_edition)
        writer.write_str_value("operatingSystemLanguage", self.operating_system_language)
        writer.write_int_value("operatingSystemProductType", self.operating_system_product_type)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("productName", self.product_name)
        writer.write_int_value("residentUsersCount", self.resident_users_count)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_collection_of_object_values("sharedDeviceCachedUsers", self.shared_device_cached_users)
        writer.write_str_value("subnetAddress", self.subnet_address)
        writer.write_str_value("subscriberCarrier", self.subscriber_carrier)
        writer.write_str_value("systemManagementBIOSVersion", self.system_management_b_i_o_s_version)
        writer.write_int_value("totalStorageSpace", self.total_storage_space)
        writer.write_str_value("tpmManufacturer", self.tpm_manufacturer)
        writer.write_str_value("tpmSpecificationVersion", self.tpm_specification_version)
        writer.write_str_value("tpmVersion", self.tpm_version)
        writer.write_str_value("wifiMac", self.wifi_mac)
        writer.write_collection_of_primitive_values("wiredIPv4Addresses", self.wired_i_pv4_addresses)
        writer.write_additional_data_value(self.additional_data)
    

