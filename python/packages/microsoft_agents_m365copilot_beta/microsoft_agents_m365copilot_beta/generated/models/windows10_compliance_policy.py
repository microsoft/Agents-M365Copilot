from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_compliance_policy_script import DeviceCompliancePolicyScript
    from .device_threat_protection_level import DeviceThreatProtectionLevel
    from .operating_system_version_range import OperatingSystemVersionRange
    from .required_password_type import RequiredPasswordType
    from .wsl_distribution_configuration import WslDistributionConfiguration

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class Windows10CompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This class contains compliance settings for Windows 10.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10CompliancePolicy"
    # Require active firewall on Windows devices.
    active_firewall_required: Optional[bool] = None
    # Require any AntiSpyware solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
    anti_spyware_required: Optional[bool] = None
    # Require any Antivirus solution registered with Windows Decurity Center to be on and monitoring (e.g. Symantec, Windows Defender).
    antivirus_required: Optional[bool] = None
    # Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
    bit_locker_enabled: Optional[bool] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation.
    code_integrity_enabled: Optional[bool] = None
    # Require to consider SCCM Compliance state into consideration for Intune Compliance State.
    configuration_manager_compliance_required: Optional[bool] = None
    # Require Windows Defender Antimalware on Windows devices.
    defender_enabled: Optional[bool] = None
    # Require Windows Defender Antimalware minimum version on Windows devices.
    defender_version: Optional[str] = None
    # The deviceCompliancePolicyScript property
    device_compliance_policy_script: Optional[DeviceCompliancePolicyScript] = None
    # Require that devices have enabled device threat protection.
    device_threat_protection_enabled: Optional[bool] = None
    # Device threat protection levels for the Device Threat Protection API.
    device_threat_protection_required_security_level: Optional[DeviceThreatProtectionLevel] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
    early_launch_anti_malware_driver_enabled: Optional[bool] = None
    # When TRUE, indicates that Firmware protection is required to be reported as healthy by Microsoft Azure Attestion. When FALSE, indicates that Firmware protection is not required to be reported as healthy. Devices that support either Dynamic Root of Trust for Measurement (DRTM) or Firmware Attack Surface Reduction (FASR) will report compliant for this setting. Default value is FALSE.
    firmware_protection_enabled: Optional[bool] = None
    # When TRUE, indicates that Kernel Direct Memory Access (DMA) protection is required to be reported as healthy by Microsoft Azure Attestion. When FALSE, indicates that Kernel DMA Protection is not required to be reported as healthy. Default value is FALSE.
    kernel_dma_protection_enabled: Optional[bool] = None
    # When TRUE, indicates that Memory Integrity as known as Hypervisor-protected Code Integrity (HVCI) or Hypervisor Enforced Code Integrity protection is required to be reported as healthy by Microsoft Azure Attestion. When FALSE, indicates that Memory Integrity Protection is not required to be reported as healthy. Default value is FALSE.
    memory_integrity_enabled: Optional[bool] = None
    # Maximum Windows Phone version.
    mobile_os_maximum_version: Optional[str] = None
    # Minimum Windows Phone version.
    mobile_os_minimum_version: Optional[str] = None
    # Maximum Windows 10 version.
    os_maximum_version: Optional[str] = None
    # Minimum Windows 10 version.
    os_minimum_version: Optional[str] = None
    # Indicates whether or not to block simple password.
    password_block_simple: Optional[bool] = None
    # The password expiration in days.
    password_expiration_days: Optional[int] = None
    # The number of character sets required in the password.
    password_minimum_character_set_count: Optional[int] = None
    # The minimum password length.
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # The number of previous passwords to prevent re-use of.
    password_previous_password_block_count: Optional[int] = None
    # Require a password to unlock Windows device.
    password_required: Optional[bool] = None
    # Require a password to unlock an idle device.
    password_required_to_unlock_from_idle: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation.
    require_healthy_device_report: Optional[bool] = None
    # Require Windows Defender Antimalware Real-Time Protection on Windows devices.
    rtp_enabled: Optional[bool] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
    secure_boot_enabled: Optional[bool] = None
    # Require Windows Defender Antimalware Signature to be up to date on Windows devices.
    signature_out_of_date: Optional[bool] = None
    # Require encryption on windows devices.
    storage_require_encryption: Optional[bool] = None
    # Require Trusted Platform Module(TPM) to be present.
    tpm_required: Optional[bool] = None
    # The valid operating system build ranges on Windows devices. This collection can contain a maximum of 10000 elements.
    valid_operating_system_build_ranges: Optional[list[OperatingSystemVersionRange]] = None
    # When TRUE, indicates that Virtualization-based Security is required to be reported as healthy by Microsoft Azure Attestion. When FALSE, indicates that Virtualization-based Security is not required to be reported as healthy. Default value is FALSE.
    virtualization_based_security_enabled: Optional[bool] = None
    # The wslDistributions property
    wsl_distributions: Optional[list[WslDistributionConfiguration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10CompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10CompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10CompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_script import DeviceCompliancePolicyScript
        from .device_threat_protection_level import DeviceThreatProtectionLevel
        from .operating_system_version_range import OperatingSystemVersionRange
        from .required_password_type import RequiredPasswordType
        from .wsl_distribution_configuration import WslDistributionConfiguration

        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_script import DeviceCompliancePolicyScript
        from .device_threat_protection_level import DeviceThreatProtectionLevel
        from .operating_system_version_range import OperatingSystemVersionRange
        from .required_password_type import RequiredPasswordType
        from .wsl_distribution_configuration import WslDistributionConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "activeFirewallRequired": lambda n : setattr(self, 'active_firewall_required', n.get_bool_value()),
            "antiSpywareRequired": lambda n : setattr(self, 'anti_spyware_required', n.get_bool_value()),
            "antivirusRequired": lambda n : setattr(self, 'antivirus_required', n.get_bool_value()),
            "bitLockerEnabled": lambda n : setattr(self, 'bit_locker_enabled', n.get_bool_value()),
            "codeIntegrityEnabled": lambda n : setattr(self, 'code_integrity_enabled', n.get_bool_value()),
            "configurationManagerComplianceRequired": lambda n : setattr(self, 'configuration_manager_compliance_required', n.get_bool_value()),
            "defenderEnabled": lambda n : setattr(self, 'defender_enabled', n.get_bool_value()),
            "defenderVersion": lambda n : setattr(self, 'defender_version', n.get_str_value()),
            "deviceCompliancePolicyScript": lambda n : setattr(self, 'device_compliance_policy_script', n.get_object_value(DeviceCompliancePolicyScript)),
            "deviceThreatProtectionEnabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "deviceThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(DeviceThreatProtectionLevel)),
            "earlyLaunchAntiMalwareDriverEnabled": lambda n : setattr(self, 'early_launch_anti_malware_driver_enabled', n.get_bool_value()),
            "firmwareProtectionEnabled": lambda n : setattr(self, 'firmware_protection_enabled', n.get_bool_value()),
            "kernelDmaProtectionEnabled": lambda n : setattr(self, 'kernel_dma_protection_enabled', n.get_bool_value()),
            "memoryIntegrityEnabled": lambda n : setattr(self, 'memory_integrity_enabled', n.get_bool_value()),
            "mobileOsMaximumVersion": lambda n : setattr(self, 'mobile_os_maximum_version', n.get_str_value()),
            "mobileOsMinimumVersion": lambda n : setattr(self, 'mobile_os_minimum_version', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredToUnlockFromIdle": lambda n : setattr(self, 'password_required_to_unlock_from_idle', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "requireHealthyDeviceReport": lambda n : setattr(self, 'require_healthy_device_report', n.get_bool_value()),
            "rtpEnabled": lambda n : setattr(self, 'rtp_enabled', n.get_bool_value()),
            "secureBootEnabled": lambda n : setattr(self, 'secure_boot_enabled', n.get_bool_value()),
            "signatureOutOfDate": lambda n : setattr(self, 'signature_out_of_date', n.get_bool_value()),
            "storageRequireEncryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
            "tpmRequired": lambda n : setattr(self, 'tpm_required', n.get_bool_value()),
            "validOperatingSystemBuildRanges": lambda n : setattr(self, 'valid_operating_system_build_ranges', n.get_collection_of_object_values(OperatingSystemVersionRange)),
            "virtualizationBasedSecurityEnabled": lambda n : setattr(self, 'virtualization_based_security_enabled', n.get_bool_value()),
            "wslDistributions": lambda n : setattr(self, 'wsl_distributions', n.get_collection_of_object_values(WslDistributionConfiguration)),
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
        writer.write_bool_value("activeFirewallRequired", self.active_firewall_required)
        writer.write_bool_value("antiSpywareRequired", self.anti_spyware_required)
        writer.write_bool_value("antivirusRequired", self.antivirus_required)
        writer.write_bool_value("bitLockerEnabled", self.bit_locker_enabled)
        writer.write_bool_value("codeIntegrityEnabled", self.code_integrity_enabled)
        writer.write_bool_value("configurationManagerComplianceRequired", self.configuration_manager_compliance_required)
        writer.write_bool_value("defenderEnabled", self.defender_enabled)
        writer.write_str_value("defenderVersion", self.defender_version)
        writer.write_object_value("deviceCompliancePolicyScript", self.device_compliance_policy_script)
        writer.write_bool_value("deviceThreatProtectionEnabled", self.device_threat_protection_enabled)
        writer.write_enum_value("deviceThreatProtectionRequiredSecurityLevel", self.device_threat_protection_required_security_level)
        writer.write_bool_value("earlyLaunchAntiMalwareDriverEnabled", self.early_launch_anti_malware_driver_enabled)
        writer.write_bool_value("firmwareProtectionEnabled", self.firmware_protection_enabled)
        writer.write_bool_value("kernelDmaProtectionEnabled", self.kernel_dma_protection_enabled)
        writer.write_bool_value("memoryIntegrityEnabled", self.memory_integrity_enabled)
        writer.write_str_value("mobileOsMaximumVersion", self.mobile_os_maximum_version)
        writer.write_str_value("mobileOsMinimumVersion", self.mobile_os_minimum_version)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_bool_value("passwordRequiredToUnlockFromIdle", self.password_required_to_unlock_from_idle)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("requireHealthyDeviceReport", self.require_healthy_device_report)
        writer.write_bool_value("rtpEnabled", self.rtp_enabled)
        writer.write_bool_value("secureBootEnabled", self.secure_boot_enabled)
        writer.write_bool_value("signatureOutOfDate", self.signature_out_of_date)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
        writer.write_bool_value("tpmRequired", self.tpm_required)
        writer.write_collection_of_object_values("validOperatingSystemBuildRanges", self.valid_operating_system_build_ranges)
        writer.write_bool_value("virtualizationBasedSecurityEnabled", self.virtualization_based_security_enabled)
        writer.write_collection_of_object_values("wslDistributions", self.wsl_distributions)
    

