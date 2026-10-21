from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .enablement import Enablement
    from .mac_o_s_file_vault_recovery_key_types import MacOSFileVaultRecoveryKeyTypes
    from .mac_o_s_firewall_application import MacOSFirewallApplication
    from .mac_o_s_gatekeeper_app_sources import MacOSGatekeeperAppSources

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSEndpointProtectionConfiguration(DeviceConfiguration, Parsable):
    """
    MacOS endpoint protection configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSEndpointProtectionConfiguration"
    # Possible values of a property
    advanced_threat_protection_automatic_sample_submission: Optional[Enablement] = None
    # Possible values of a property
    advanced_threat_protection_cloud_delivered: Optional[Enablement] = None
    # Possible values of a property
    advanced_threat_protection_diagnostic_data_collection: Optional[Enablement] = None
    # A list of file extensions to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
    advanced_threat_protection_excluded_extensions: Optional[list[str]] = None
    # A list of paths to files to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
    advanced_threat_protection_excluded_files: Optional[list[str]] = None
    # A list of paths to folders to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
    advanced_threat_protection_excluded_folders: Optional[list[str]] = None
    # A list of process names to exclude from antivirus scanning for Microsoft Defender Advanced Threat Protection on macOS.
    advanced_threat_protection_excluded_processes: Optional[list[str]] = None
    # Possible values of a property
    advanced_threat_protection_real_time: Optional[Enablement] = None
    # Optional. If set to true, the user can defer the enabling of FileVault until they sign out.
    file_vault_allow_deferral_until_sign_out: Optional[bool] = None
    # Optional. When using the Defer option, if set to true, the user is not prompted to enable FileVault at sign-out.
    file_vault_disable_prompt_at_sign_out: Optional[bool] = None
    # Whether FileVault should be enabled or not.
    file_vault_enabled: Optional[bool] = None
    # Optional. A hidden personal recovery key does not appear on the user's screen during FileVault encryption, reducing the risk of it ending up in the wrong hands.
    file_vault_hide_personal_recovery_key: Optional[bool] = None
    # Required if selected recovery key type(s) include InstitutionalRecoveryKey. The DER Encoded certificate file used to set an institutional recovery key.
    file_vault_institutional_recovery_key_certificate: Optional[bytes] = None
    # File name of the institutional recovery key certificate to display in UI. (.der).
    file_vault_institutional_recovery_key_certificate_file_name: Optional[str] = None
    # Optional. When using the Defer option, this is the maximum number of times the user can ignore prompts to enable FileVault before FileVault will be required for the user to sign in. If set to -1, it will always prompt to enable FileVault until FileVault is enabled, though it will allow the user to bypass enabling FileVault. Setting this to 0 will disable the feature.
    file_vault_number_of_times_user_can_ignore: Optional[int] = None
    # Required if selected recovery key type(s) include PersonalRecoveryKey. A short message displayed to the user that explains how they can retrieve their personal recovery key.
    file_vault_personal_recovery_key_help_message: Optional[str] = None
    # Optional. If selected recovery key type(s) include PersonalRecoveryKey, the frequency to rotate that key, in months.
    file_vault_personal_recovery_key_rotation_in_months: Optional[int] = None
    # Recovery key types for macOS FileVault
    file_vault_selected_recovery_key_types: Optional[MacOSFileVaultRecoveryKeyTypes] = None
    # List of applications with firewall settings. Firewall settings for applications not on this list are determined by the user. This collection can contain a maximum of 500 elements.
    firewall_applications: Optional[list[MacOSFirewallApplication]] = None
    # Corresponds to the 'Block all incoming connections' option.
    firewall_block_all_incoming: Optional[bool] = None
    # Corresponds to 'Enable stealth mode.'
    firewall_enable_stealth_mode: Optional[bool] = None
    # Whether the firewall should be enabled or not.
    firewall_enabled: Optional[bool] = None
    # App source options for macOS Gatekeeper.
    gatekeeper_allowed_app_source: Optional[MacOSGatekeeperAppSources] = None
    # If set to true, the user override for Gatekeeper will be disabled.
    gatekeeper_block_override: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSEndpointProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSEndpointProtectionConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSEndpointProtectionConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .mac_o_s_file_vault_recovery_key_types import MacOSFileVaultRecoveryKeyTypes
        from .mac_o_s_firewall_application import MacOSFirewallApplication
        from .mac_o_s_gatekeeper_app_sources import MacOSGatekeeperAppSources

        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .mac_o_s_file_vault_recovery_key_types import MacOSFileVaultRecoveryKeyTypes
        from .mac_o_s_firewall_application import MacOSFirewallApplication
        from .mac_o_s_gatekeeper_app_sources import MacOSGatekeeperAppSources

        fields: dict[str, Callable[[Any], None]] = {
            "advancedThreatProtectionAutomaticSampleSubmission": lambda n : setattr(self, 'advanced_threat_protection_automatic_sample_submission', n.get_enum_value(Enablement)),
            "advancedThreatProtectionCloudDelivered": lambda n : setattr(self, 'advanced_threat_protection_cloud_delivered', n.get_enum_value(Enablement)),
            "advancedThreatProtectionDiagnosticDataCollection": lambda n : setattr(self, 'advanced_threat_protection_diagnostic_data_collection', n.get_enum_value(Enablement)),
            "advancedThreatProtectionExcludedExtensions": lambda n : setattr(self, 'advanced_threat_protection_excluded_extensions', n.get_collection_of_primitive_values(str)),
            "advancedThreatProtectionExcludedFiles": lambda n : setattr(self, 'advanced_threat_protection_excluded_files', n.get_collection_of_primitive_values(str)),
            "advancedThreatProtectionExcludedFolders": lambda n : setattr(self, 'advanced_threat_protection_excluded_folders', n.get_collection_of_primitive_values(str)),
            "advancedThreatProtectionExcludedProcesses": lambda n : setattr(self, 'advanced_threat_protection_excluded_processes', n.get_collection_of_primitive_values(str)),
            "advancedThreatProtectionRealTime": lambda n : setattr(self, 'advanced_threat_protection_real_time', n.get_enum_value(Enablement)),
            "fileVaultAllowDeferralUntilSignOut": lambda n : setattr(self, 'file_vault_allow_deferral_until_sign_out', n.get_bool_value()),
            "fileVaultDisablePromptAtSignOut": lambda n : setattr(self, 'file_vault_disable_prompt_at_sign_out', n.get_bool_value()),
            "fileVaultEnabled": lambda n : setattr(self, 'file_vault_enabled', n.get_bool_value()),
            "fileVaultHidePersonalRecoveryKey": lambda n : setattr(self, 'file_vault_hide_personal_recovery_key', n.get_bool_value()),
            "fileVaultInstitutionalRecoveryKeyCertificate": lambda n : setattr(self, 'file_vault_institutional_recovery_key_certificate', n.get_bytes_value()),
            "fileVaultInstitutionalRecoveryKeyCertificateFileName": lambda n : setattr(self, 'file_vault_institutional_recovery_key_certificate_file_name', n.get_str_value()),
            "fileVaultNumberOfTimesUserCanIgnore": lambda n : setattr(self, 'file_vault_number_of_times_user_can_ignore', n.get_int_value()),
            "fileVaultPersonalRecoveryKeyHelpMessage": lambda n : setattr(self, 'file_vault_personal_recovery_key_help_message', n.get_str_value()),
            "fileVaultPersonalRecoveryKeyRotationInMonths": lambda n : setattr(self, 'file_vault_personal_recovery_key_rotation_in_months', n.get_int_value()),
            "fileVaultSelectedRecoveryKeyTypes": lambda n : setattr(self, 'file_vault_selected_recovery_key_types', n.get_collection_of_enum_values(MacOSFileVaultRecoveryKeyTypes)),
            "firewallApplications": lambda n : setattr(self, 'firewall_applications', n.get_collection_of_object_values(MacOSFirewallApplication)),
            "firewallBlockAllIncoming": lambda n : setattr(self, 'firewall_block_all_incoming', n.get_bool_value()),
            "firewallEnableStealthMode": lambda n : setattr(self, 'firewall_enable_stealth_mode', n.get_bool_value()),
            "firewallEnabled": lambda n : setattr(self, 'firewall_enabled', n.get_bool_value()),
            "gatekeeperAllowedAppSource": lambda n : setattr(self, 'gatekeeper_allowed_app_source', n.get_enum_value(MacOSGatekeeperAppSources)),
            "gatekeeperBlockOverride": lambda n : setattr(self, 'gatekeeper_block_override', n.get_bool_value()),
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
        writer.write_enum_value("advancedThreatProtectionAutomaticSampleSubmission", self.advanced_threat_protection_automatic_sample_submission)
        writer.write_enum_value("advancedThreatProtectionCloudDelivered", self.advanced_threat_protection_cloud_delivered)
        writer.write_enum_value("advancedThreatProtectionDiagnosticDataCollection", self.advanced_threat_protection_diagnostic_data_collection)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedExtensions", self.advanced_threat_protection_excluded_extensions)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedFiles", self.advanced_threat_protection_excluded_files)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedFolders", self.advanced_threat_protection_excluded_folders)
        writer.write_collection_of_primitive_values("advancedThreatProtectionExcludedProcesses", self.advanced_threat_protection_excluded_processes)
        writer.write_enum_value("advancedThreatProtectionRealTime", self.advanced_threat_protection_real_time)
        writer.write_bool_value("fileVaultAllowDeferralUntilSignOut", self.file_vault_allow_deferral_until_sign_out)
        writer.write_bool_value("fileVaultDisablePromptAtSignOut", self.file_vault_disable_prompt_at_sign_out)
        writer.write_bool_value("fileVaultEnabled", self.file_vault_enabled)
        writer.write_bool_value("fileVaultHidePersonalRecoveryKey", self.file_vault_hide_personal_recovery_key)
        writer.write_bytes_value("fileVaultInstitutionalRecoveryKeyCertificate", self.file_vault_institutional_recovery_key_certificate)
        writer.write_str_value("fileVaultInstitutionalRecoveryKeyCertificateFileName", self.file_vault_institutional_recovery_key_certificate_file_name)
        writer.write_int_value("fileVaultNumberOfTimesUserCanIgnore", self.file_vault_number_of_times_user_can_ignore)
        writer.write_str_value("fileVaultPersonalRecoveryKeyHelpMessage", self.file_vault_personal_recovery_key_help_message)
        writer.write_int_value("fileVaultPersonalRecoveryKeyRotationInMonths", self.file_vault_personal_recovery_key_rotation_in_months)
        writer.write_enum_value("fileVaultSelectedRecoveryKeyTypes", self.file_vault_selected_recovery_key_types)
        writer.write_collection_of_object_values("firewallApplications", self.firewall_applications)
        writer.write_bool_value("firewallBlockAllIncoming", self.firewall_block_all_incoming)
        writer.write_bool_value("firewallEnableStealthMode", self.firewall_enable_stealth_mode)
        writer.write_bool_value("firewallEnabled", self.firewall_enabled)
        writer.write_enum_value("gatekeeperAllowedAppSource", self.gatekeeper_allowed_app_source)
        writer.write_bool_value("gatekeeperBlockOverride", self.gatekeeper_block_override)
    

