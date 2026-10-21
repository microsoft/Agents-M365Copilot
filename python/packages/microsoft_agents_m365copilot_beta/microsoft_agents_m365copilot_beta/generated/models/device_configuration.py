from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_certificate_profile_base import AndroidCertificateProfileBase
    from .android_custom_configuration import AndroidCustomConfiguration
    from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
    from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
    from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
    from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
    from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
    from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
    from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
    from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
    from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
    from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
    from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
    from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
    from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
    from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
    from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
    from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
    from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
    from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
    from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
    from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
    from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
    from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
    from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
    from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
    from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
    from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
    from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
    from .android_oma_cp_configuration import AndroidOmaCpConfiguration
    from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
    from .android_scep_certificate_profile import AndroidScepCertificateProfile
    from .android_trusted_root_certificate import AndroidTrustedRootCertificate
    from .android_vpn_configuration import AndroidVpnConfiguration
    from .android_wi_fi_configuration import AndroidWiFiConfiguration
    from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
    from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
    from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
    from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
    from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
    from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
    from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
    from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
    from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
    from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
    from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
    from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
    from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
    from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
    from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
    from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
    from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
    from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
    from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
    from .apple_vpn_configuration import AppleVpnConfiguration
    from .device_configuration_assignment import DeviceConfigurationAssignment
    from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
    from .device_configuration_device_status import DeviceConfigurationDeviceStatus
    from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
    from .device_configuration_user_overview import DeviceConfigurationUserOverview
    from .device_configuration_user_status import DeviceConfigurationUserStatus
    from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
    from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
    from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
    from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
    from .edition_upgrade_configuration import EditionUpgradeConfiguration
    from .entity import Entity
    from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
    from .ios_certificate_profile import IosCertificateProfile
    from .ios_certificate_profile_base import IosCertificateProfileBase
    from .ios_custom_configuration import IosCustomConfiguration
    from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
    from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
    from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
    from .ios_education_device_configuration import IosEducationDeviceConfiguration
    from .ios_edu_device_configuration import IosEduDeviceConfiguration
    from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
    from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
    from .ios_general_device_configuration import IosGeneralDeviceConfiguration
    from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
    from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
    from .ios_scep_certificate_profile import IosScepCertificateProfile
    from .ios_trusted_root_certificate import IosTrustedRootCertificate
    from .ios_update_configuration import IosUpdateConfiguration
    from .ios_vpn_configuration import IosVpnConfiguration
    from .ios_wired_network_configuration import IosWiredNetworkConfiguration
    from .ios_wi_fi_configuration import IosWiFiConfiguration
    from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
    from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
    from .mac_o_s_custom_configuration import MacOSCustomConfiguration
    from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
    from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
    from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
    from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
    from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
    from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
    from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
    from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
    from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
    from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
    from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
    from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
    from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
    from .setting_state_device_summary import SettingStateDeviceSummary
    from .shared_p_c_configuration import SharedPCConfiguration
    from .unsupported_device_configuration import UnsupportedDeviceConfiguration
    from .vpn_configuration import VpnConfiguration
    from .windows10_certificate_profile_base import Windows10CertificateProfileBase
    from .windows10_custom_configuration import Windows10CustomConfiguration
    from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
    from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
    from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
    from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
    from .windows10_general_configuration import Windows10GeneralConfiguration
    from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
    from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
    from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
    from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
    from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
    from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
    from .windows10_vpn_configuration import Windows10VpnConfiguration
    from .windows81_certificate_profile_base import Windows81CertificateProfileBase
    from .windows81_general_configuration import Windows81GeneralConfiguration
    from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
    from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
    from .windows81_vpn_configuration import Windows81VpnConfiguration
    from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
    from .windows_certificate_profile_base import WindowsCertificateProfileBase
    from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
    from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
    from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
    from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
    from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
    from .windows_kiosk_configuration import WindowsKioskConfiguration
    from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
    from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
    from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
    from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
    from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
    from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
    from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
    from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
    from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
    from .windows_vpn_configuration import WindowsVpnConfiguration
    from .windows_wifi_configuration import WindowsWifiConfiguration
    from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
    from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
    from .windows_ztdns_configuration import WindowsZtdnsConfiguration

from .entity import Entity

@dataclass
class DeviceConfiguration(Entity, Parsable):
    """
    Device Configuration.
    """
    # The list of assignments for the device configuration profile.
    assignments: Optional[list[DeviceConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # The device mode applicability rule for this Policy.
    device_management_applicability_rule_device_mode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = None
    # The OS edition applicability for this Policy.
    device_management_applicability_rule_os_edition: Optional[DeviceManagementApplicabilityRuleOsEdition] = None
    # The OS version applicability rule for this Policy.
    device_management_applicability_rule_os_version: Optional[DeviceManagementApplicabilityRuleOsVersion] = None
    # Device Configuration Setting State Device Summary
    device_setting_state_summaries: Optional[list[SettingStateDeviceSummary]] = None
    # Device Configuration devices status overview
    device_status_overview: Optional[DeviceConfigurationDeviceOverview] = None
    # Device configuration installation status by device.
    device_statuses: Optional[list[DeviceConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # The list of group assignments for the device configuration profile.
    group_assignments: Optional[list[DeviceConfigurationGroupAssignment]] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[list[str]] = None
    # Indicates whether or not the underlying Device Configuration supports the assignment of scope tags. Assigning to the ScopeTags property is not allowed when this value is false and entities will not be visible to scoped users. This occurs for Legacy policies created in Silverlight and can be resolved by deleting and recreating the policy in the Azure Portal. This property is read-only.
    supports_scope_tags: Optional[bool] = None
    # Device Configuration users status overview
    user_status_overview: Optional[DeviceConfigurationUserOverview] = None
    # Device configuration installation status by user.
    user_statuses: Optional[list[DeviceConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCertificateProfileBase".casefold():
            from .android_certificate_profile_base import AndroidCertificateProfileBase

            return AndroidCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from .android_custom_configuration import AndroidCustomConfiguration

            return AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerCertificateProfileBase".casefold():
            from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase

            return AndroidDeviceOwnerCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration".casefold():
            from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration

            return AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration

            return AndroidDeviceOwnerEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration".casefold():
            from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration

            return AndroidDeviceOwnerGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerImportedPFXCertificateProfile".casefold():
            from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile

            return AndroidDeviceOwnerImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerPkcsCertificateProfile".casefold():
            from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile

            return AndroidDeviceOwnerPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerScepCertificateProfile".casefold():
            from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile

            return AndroidDeviceOwnerScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerTrustedRootCertificate".casefold():
            from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate

            return AndroidDeviceOwnerTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerVpnConfiguration".casefold():
            from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration

            return AndroidDeviceOwnerVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerWiFiConfiguration".casefold():
            from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration

            return AndroidDeviceOwnerWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidEasEmailProfileConfiguration".casefold():
            from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration

            return AndroidEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidEnterpriseWiFiConfiguration".casefold():
            from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration

            return AndroidEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCertificateProfileBase".casefold():
            from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase

            return AndroidForWorkCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkCustomConfiguration".casefold():
            from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration

            return AndroidForWorkCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEasEmailProfileBase".casefold():
            from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

            return AndroidForWorkEasEmailProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkEnterpriseWiFiConfiguration".casefold():
            from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration

            return AndroidForWorkEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGeneralDeviceConfiguration".casefold():
            from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration

            return AndroidForWorkGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkGmailEasConfiguration".casefold():
            from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration

            return AndroidForWorkGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkImportedPFXCertificateProfile".casefold():
            from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile

            return AndroidForWorkImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkNineWorkEasConfiguration".casefold():
            from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration

            return AndroidForWorkNineWorkEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkPkcsCertificateProfile".casefold():
            from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile

            return AndroidForWorkPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkScepCertificateProfile".casefold():
            from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile

            return AndroidForWorkScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkTrustedRootCertificate".casefold():
            from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate

            return AndroidForWorkTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkVpnConfiguration".casefold():
            from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration

            return AndroidForWorkVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkWiFiConfiguration".casefold():
            from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration

            return AndroidForWorkWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from .android_general_device_configuration import AndroidGeneralDeviceConfiguration

            return AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidImportedPFXCertificateProfile".casefold():
            from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile

            return AndroidImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidOmaCpConfiguration".casefold():
            from .android_oma_cp_configuration import AndroidOmaCpConfiguration

            return AndroidOmaCpConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidPkcsCertificateProfile".casefold():
            from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile

            return AndroidPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidScepCertificateProfile".casefold():
            from .android_scep_certificate_profile import AndroidScepCertificateProfile

            return AndroidScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidTrustedRootCertificate".casefold():
            from .android_trusted_root_certificate import AndroidTrustedRootCertificate

            return AndroidTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidVpnConfiguration".casefold():
            from .android_vpn_configuration import AndroidVpnConfiguration

            return AndroidVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWiFiConfiguration".casefold():
            from .android_wi_fi_configuration import AndroidWiFiConfiguration

            return AndroidWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCertificateProfileBase".casefold():
            from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase

            return AndroidWorkProfileCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration

            return AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEasEmailProfileBase".casefold():
            from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase

            return AndroidWorkProfileEasEmailProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration".casefold():
            from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration

            return AndroidWorkProfileEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration

            return AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGmailEasConfiguration".casefold():
            from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration

            return AndroidWorkProfileGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration".casefold():
            from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration

            return AndroidWorkProfileNineWorkEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfilePkcsCertificateProfile".casefold():
            from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile

            return AndroidWorkProfilePkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileScepCertificateProfile".casefold():
            from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile

            return AndroidWorkProfileScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileTrustedRootCertificate".casefold():
            from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate

            return AndroidWorkProfileTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileVpnConfiguration".casefold():
            from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration

            return AndroidWorkProfileVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileWiFiConfiguration".casefold():
            from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration

            return AndroidWorkProfileWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerCertificateProfileBase".casefold():
            from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase

            return AospDeviceOwnerCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerDeviceConfiguration".casefold():
            from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration

            return AospDeviceOwnerDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration

            return AospDeviceOwnerEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile".casefold():
            from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile

            return AospDeviceOwnerPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerScepCertificateProfile".casefold():
            from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile

            return AospDeviceOwnerScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerTrustedRootCertificate".casefold():
            from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate

            return AospDeviceOwnerTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aospDeviceOwnerWiFiConfiguration".casefold():
            from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration

            return AospDeviceOwnerWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

            return AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleExpeditedCheckinConfigurationBase".casefold():
            from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase

            return AppleExpeditedCheckinConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleVpnConfiguration".casefold():
            from .apple_vpn_configuration import AppleVpnConfiguration

            return AppleVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.easEmailProfileConfigurationBase".casefold():
            from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase

            return EasEmailProfileConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from .edition_upgrade_configuration import EditionUpgradeConfiguration

            return EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from .ios_certificate_profile import IosCertificateProfile

            return IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfileBase".casefold():
            from .ios_certificate_profile_base import IosCertificateProfileBase

            return IosCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from .ios_custom_configuration import IosCustomConfiguration

            return IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration".casefold():
            from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration

            return IosDerivedCredentialAuthenticationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from .ios_device_features_configuration import IosDeviceFeaturesConfiguration

            return IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEasEmailProfileConfiguration".casefold():
            from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration

            return IosEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEducationDeviceConfiguration".casefold():
            from .ios_education_device_configuration import IosEducationDeviceConfiguration

            return IosEducationDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEduDeviceConfiguration".casefold():
            from .ios_edu_device_configuration import IosEduDeviceConfiguration

            return IosEduDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEnterpriseWiFiConfiguration".casefold():
            from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration

            return IosEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosExpeditedCheckinConfiguration".casefold():
            from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration

            return IosExpeditedCheckinConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from .ios_general_device_configuration import IosGeneralDeviceConfiguration

            return IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosikEv2VpnConfiguration".casefold():
            from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration

            return IosikEv2VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosImportedPFXCertificateProfile".casefold():
            from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile

            return IosImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosPkcsCertificateProfile".casefold():
            from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile

            return IosPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosScepCertificateProfile".casefold():
            from .ios_scep_certificate_profile import IosScepCertificateProfile

            return IosScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosTrustedRootCertificate".casefold():
            from .ios_trusted_root_certificate import IosTrustedRootCertificate

            return IosTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from .ios_update_configuration import IosUpdateConfiguration

            return IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVpnConfiguration".casefold():
            from .ios_vpn_configuration import IosVpnConfiguration

            return IosVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosWiFiConfiguration".casefold():
            from .ios_wi_fi_configuration import IosWiFiConfiguration

            return IosWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosWiredNetworkConfiguration".casefold():
            from .ios_wired_network_configuration import IosWiredNetworkConfiguration

            return IosWiredNetworkConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCertificateProfileBase".casefold():
            from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase

            return MacOSCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomAppConfiguration".casefold():
            from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration

            return MacOSCustomAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from .mac_o_s_custom_configuration import MacOSCustomConfiguration

            return MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

            return MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEndpointProtectionConfiguration".casefold():
            from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration

            return MacOSEndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEnterpriseWiFiConfiguration".casefold():
            from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration

            return MacOSEnterpriseWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSExtensionsConfiguration".casefold():
            from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration

            return MacOSExtensionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration

            return MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSImportedPFXCertificateProfile".casefold():
            from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile

            return MacOSImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkcsCertificateProfile".casefold():
            from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile

            return MacOSPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSScepCertificateProfile".casefold():
            from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

            return MacOSScepCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSoftwareUpdateConfiguration".casefold():
            from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration

            return MacOSSoftwareUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSTrustedRootCertificate".casefold():
            from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate

            return MacOSTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSVpnConfiguration".casefold():
            from .mac_o_s_vpn_configuration import MacOSVpnConfiguration

            return MacOSVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWiFiConfiguration".casefold():
            from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration

            return MacOSWiFiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWiredNetworkConfiguration".casefold():
            from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration

            return MacOSWiredNetworkConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from .shared_p_c_configuration import SharedPCConfiguration

            return SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unsupportedDeviceConfiguration".casefold():
            from .unsupported_device_configuration import UnsupportedDeviceConfiguration

            return UnsupportedDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vpnConfiguration".casefold():
            from .vpn_configuration import VpnConfiguration

            return VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CertificateProfileBase".casefold():
            from .windows10_certificate_profile_base import Windows10CertificateProfileBase

            return Windows10CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from .windows10_custom_configuration import Windows10CustomConfiguration

            return Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface".casefold():
            from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface

            return Windows10DeviceFirmwareConfigurationInterface()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EasEmailProfileConfiguration".casefold():
            from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration

            return Windows10EasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration

            return Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration

            return Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from .windows10_general_configuration import Windows10GeneralConfiguration

            return Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10ImportedPFXCertificateProfile".casefold():
            from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile

            return Windows10ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10NetworkBoundaryConfiguration".casefold():
            from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration

            return Windows10NetworkBoundaryConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PFXImportCertificateProfile".casefold():
            from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile

            return Windows10PFXImportCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PkcsCertificateProfile".casefold():
            from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile

            return Windows10PkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration

            return Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration

            return Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10VpnConfiguration".casefold():
            from .windows10_vpn_configuration import Windows10VpnConfiguration

            return Windows10VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CertificateProfileBase".casefold():
            from .windows81_certificate_profile_base import Windows81CertificateProfileBase

            return Windows81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from .windows81_general_configuration import Windows81GeneralConfiguration

            return Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81SCEPCertificateProfile".casefold():
            from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile

            return Windows81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81TrustedRootCertificate".casefold():
            from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate

            return Windows81TrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81VpnConfiguration".casefold():
            from .windows81_vpn_configuration import Windows81VpnConfiguration

            return Windows81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81WifiImportConfiguration".casefold():
            from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration

            return Windows81WifiImportConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsCertificateProfileBase".casefold():
            from .windows_certificate_profile_base import WindowsCertificateProfileBase

            return WindowsCertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration

            return WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDeliveryOptimizationConfiguration".casefold():
            from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration

            return WindowsDeliveryOptimizationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDomainJoinConfiguration".casefold():
            from .windows_domain_join_configuration import WindowsDomainJoinConfiguration

            return WindowsDomainJoinConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHealthMonitoringConfiguration".casefold():
            from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration

            return WindowsHealthMonitoringConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsIdentityProtectionConfiguration".casefold():
            from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration

            return WindowsIdentityProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskConfiguration".casefold():
            from .windows_kiosk_configuration import WindowsKioskConfiguration

            return WindowsKioskConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CertificateProfileBase".casefold():
            from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

            return WindowsPhone81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration

            return WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration

            return WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile".casefold():
            from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

            return WindowsPhone81ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81SCEPCertificateProfile".casefold():
            from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

            return WindowsPhone81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81TrustedRootCertificate".casefold():
            from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate

            return WindowsPhone81TrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81VpnConfiguration".casefold():
            from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration

            return WindowsPhone81VpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration".casefold():
            from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

            return WindowsPhoneEASEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

            return WindowsUpdateForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsVpnConfiguration".casefold():
            from .windows_vpn_configuration import WindowsVpnConfiguration

            return WindowsVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiConfiguration".casefold():
            from .windows_wifi_configuration import WindowsWifiConfiguration

            return WindowsWifiConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration".casefold():
            from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration

            return WindowsWifiEnterpriseEAPConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWiredNetworkConfiguration".casefold():
            from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration

            return WindowsWiredNetworkConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsZtdnsConfiguration".casefold():
            from .windows_ztdns_configuration import WindowsZtdnsConfiguration

            return WindowsZtdnsConfiguration()
        return DeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
        from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
        from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
        from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
        from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
        from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
        from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
        from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
        from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
        from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
        from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
        from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
        from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
        from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
        from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
        from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
        from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
        from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
        from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
        from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
        from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
        from .android_oma_cp_configuration import AndroidOmaCpConfiguration
        from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
        from .android_scep_certificate_profile import AndroidScepCertificateProfile
        from .android_trusted_root_certificate import AndroidTrustedRootCertificate
        from .android_vpn_configuration import AndroidVpnConfiguration
        from .android_wi_fi_configuration import AndroidWiFiConfiguration
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
        from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
        from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
        from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
        from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
        from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
        from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
        from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
        from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
        from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
        from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
        from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
        from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
        from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
        from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
        from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
        from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
        from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .entity import Entity
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
        from .ios_education_device_configuration import IosEducationDeviceConfiguration
        from .ios_edu_device_configuration import IosEduDeviceConfiguration
        from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
        from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
        from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
        from .ios_scep_certificate_profile import IosScepCertificateProfile
        from .ios_trusted_root_certificate import IosTrustedRootCertificate
        from .ios_update_configuration import IosUpdateConfiguration
        from .ios_vpn_configuration import IosVpnConfiguration
        from .ios_wired_network_configuration import IosWiredNetworkConfiguration
        from .ios_wi_fi_configuration import IosWiFiConfiguration
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
        from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
        from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
        from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
        from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
        from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_p_c_configuration import SharedPCConfiguration
        from .unsupported_device_configuration import UnsupportedDeviceConfiguration
        from .vpn_configuration import VpnConfiguration
        from .windows10_certificate_profile_base import Windows10CertificateProfileBase
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
        from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
        from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows10_vpn_configuration import Windows10VpnConfiguration
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
        from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
        from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
        from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
        from .windows_kiosk_configuration import WindowsKioskConfiguration
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
        from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
        from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
        from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
        from .windows_vpn_configuration import WindowsVpnConfiguration
        from .windows_wifi_configuration import WindowsWifiConfiguration
        from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
        from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
        from .windows_ztdns_configuration import WindowsZtdnsConfiguration

        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
        from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
        from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
        from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
        from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
        from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
        from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
        from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
        from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
        from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
        from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
        from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
        from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
        from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
        from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
        from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
        from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
        from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
        from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
        from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
        from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
        from .android_oma_cp_configuration import AndroidOmaCpConfiguration
        from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
        from .android_scep_certificate_profile import AndroidScepCertificateProfile
        from .android_trusted_root_certificate import AndroidTrustedRootCertificate
        from .android_vpn_configuration import AndroidVpnConfiguration
        from .android_wi_fi_configuration import AndroidWiFiConfiguration
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
        from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
        from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
        from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
        from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
        from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
        from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
        from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
        from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
        from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
        from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
        from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
        from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
        from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
        from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
        from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
        from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
        from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .entity import Entity
        from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
        from .ios_education_device_configuration import IosEducationDeviceConfiguration
        from .ios_edu_device_configuration import IosEduDeviceConfiguration
        from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
        from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
        from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
        from .ios_scep_certificate_profile import IosScepCertificateProfile
        from .ios_trusted_root_certificate import IosTrustedRootCertificate
        from .ios_update_configuration import IosUpdateConfiguration
        from .ios_vpn_configuration import IosVpnConfiguration
        from .ios_wired_network_configuration import IosWiredNetworkConfiguration
        from .ios_wi_fi_configuration import IosWiFiConfiguration
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
        from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
        from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
        from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
        from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
        from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_p_c_configuration import SharedPCConfiguration
        from .unsupported_device_configuration import UnsupportedDeviceConfiguration
        from .vpn_configuration import VpnConfiguration
        from .windows10_certificate_profile_base import Windows10CertificateProfileBase
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
        from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
        from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows10_vpn_configuration import Windows10VpnConfiguration
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows81_vpn_configuration import Windows81VpnConfiguration
        from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
        from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
        from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
        from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
        from .windows_kiosk_configuration import WindowsKioskConfiguration
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
        from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
        from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
        from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
        from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
        from .windows_vpn_configuration import WindowsVpnConfiguration
        from .windows_wifi_configuration import WindowsWifiConfiguration
        from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
        from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
        from .windows_ztdns_configuration import WindowsZtdnsConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceManagementApplicabilityRuleDeviceMode": lambda n : setattr(self, 'device_management_applicability_rule_device_mode', n.get_object_value(DeviceManagementApplicabilityRuleDeviceMode)),
            "deviceManagementApplicabilityRuleOsEdition": lambda n : setattr(self, 'device_management_applicability_rule_os_edition', n.get_object_value(DeviceManagementApplicabilityRuleOsEdition)),
            "deviceManagementApplicabilityRuleOsVersion": lambda n : setattr(self, 'device_management_applicability_rule_os_version', n.get_object_value(DeviceManagementApplicabilityRuleOsVersion)),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(SettingStateDeviceSummary)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(DeviceConfigurationDeviceOverview)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(DeviceConfigurationDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupAssignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(DeviceConfigurationGroupAssignment)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supportsScopeTags": lambda n : setattr(self, 'supports_scope_tags', n.get_bool_value()),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(DeviceConfigurationUserOverview)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(DeviceConfigurationUserStatus)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("deviceManagementApplicabilityRuleDeviceMode", self.device_management_applicability_rule_device_mode)
        writer.write_object_value("deviceManagementApplicabilityRuleOsEdition", self.device_management_applicability_rule_os_edition)
        writer.write_object_value("deviceManagementApplicabilityRuleOsVersion", self.device_management_applicability_rule_os_version)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

