from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
    from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
    from .application_guard_enabled_options import ApplicationGuardEnabledOptions
    from .app_locker_application_control_type import AppLockerApplicationControlType
    from .bit_locker_fixed_drive_policy import BitLockerFixedDrivePolicy
    from .bit_locker_recovery_password_rotation_type import BitLockerRecoveryPasswordRotationType
    from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
    from .bit_locker_system_drive_policy import BitLockerSystemDrivePolicy
    from .defender_attack_surface_type import DefenderAttackSurfaceType
    from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
    from .defender_detected_malware_actions import DefenderDetectedMalwareActions
    from .defender_protection_type import DefenderProtectionType
    from .defender_realtime_scan_direction import DefenderRealtimeScanDirection
    from .defender_scan_type import DefenderScanType
    from .defender_security_center_i_t_contact_display_type import DefenderSecurityCenterITContactDisplayType
    from .defender_security_center_notifications_from_app_type import DefenderSecurityCenterNotificationsFromAppType
    from .defender_submit_samples_consent_type import DefenderSubmitSamplesConsentType
    from .device_configuration import DeviceConfiguration
    from .device_guard_local_system_authority_credential_guard_type import DeviceGuardLocalSystemAuthorityCredentialGuardType
    from .device_management_user_rights_setting import DeviceManagementUserRightsSetting
    from .dma_guard_device_enumeration_policy_type import DmaGuardDeviceEnumerationPolicyType
    from .enablement import Enablement
    from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
    from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
    from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
    from .folder_protection_type import FolderProtectionType
    from .lan_manager_authentication_level import LanManagerAuthenticationLevel
    from .local_security_options_administrator_elevation_prompt_behavior_type import LocalSecurityOptionsAdministratorElevationPromptBehaviorType
    from .local_security_options_format_and_eject_of_removable_media_allowed_user_type import LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType
    from .local_security_options_information_displayed_on_lock_screen_type import LocalSecurityOptionsInformationDisplayedOnLockScreenType
    from .local_security_options_information_shown_on_lock_screen_type import LocalSecurityOptionsInformationShownOnLockScreenType
    from .local_security_options_minimum_session_security import LocalSecurityOptionsMinimumSessionSecurity
    from .local_security_options_smart_card_removal_behavior_type import LocalSecurityOptionsSmartCardRemovalBehaviorType
    from .local_security_options_standard_user_elevation_prompt_behavior_type import LocalSecurityOptionsStandardUserElevationPromptBehaviorType
    from .secure_boot_with_d_m_a_type import SecureBootWithDMAType
    from .service_start_type import ServiceStartType
    from .weekly_schedule import WeeklySchedule
    from .windows_defender_tamper_protection_options import WindowsDefenderTamperProtectionOptions
    from .windows_firewall_network_profile import WindowsFirewallNetworkProfile
    from .windows_firewall_rule import WindowsFirewallRule

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10EndpointProtectionConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the Windows10EndpointProtectionConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10EndpointProtectionConfiguration"
    # Possible values of AppLocker Application Control Types
    app_locker_application_control: Optional[AppLockerApplicationControlType] = None
    # Gets or sets whether applications inside Microsoft Defender Application Guard can access the device’s camera and microphone.
    application_guard_allow_camera_microphone_redirection: Optional[bool] = None
    # Allow users to download files from Edge in the application guard container and save them on the host file system
    application_guard_allow_file_save_on_host: Optional[bool] = None
    # Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
    application_guard_allow_persistence: Optional[bool] = None
    # Allow printing to Local Printers from Container
    application_guard_allow_print_to_local_printers: Optional[bool] = None
    # Allow printing to Network Printers from Container
    application_guard_allow_print_to_network_printers: Optional[bool] = None
    # Allow printing to PDF from Container
    application_guard_allow_print_to_p_d_f: Optional[bool] = None
    # Allow printing to XPS from Container
    application_guard_allow_print_to_x_p_s: Optional[bool] = None
    # Allow application guard to use virtual GPU
    application_guard_allow_virtual_g_p_u: Optional[bool] = None
    # Possible values for applicationGuardBlockClipboardSharingType
    application_guard_block_clipboard_sharing: Optional[ApplicationGuardBlockClipboardSharingType] = None
    # Possible values for applicationGuardBlockFileTransfer
    application_guard_block_file_transfer: Optional[ApplicationGuardBlockFileTransferType] = None
    # Block enterprise sites to load non-enterprise content, such as third party plug-ins
    application_guard_block_non_enterprise_content: Optional[bool] = None
    # Allows certain device level Root Certificates to be shared with the Microsoft Defender Application Guard container.
    application_guard_certificate_thumbprints: Optional[list[str]] = None
    # Enable Windows Defender Application Guard
    application_guard_enabled: Optional[bool] = None
    # Possible values for ApplicationGuardEnabledOptions
    application_guard_enabled_options: Optional[ApplicationGuardEnabledOptions] = None
    # Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
    application_guard_force_auditing: Optional[bool] = None
    # Allows the admin to allow standard users to enable encrpytion during Azure AD Join.
    bit_locker_allow_standard_user_encryption: Optional[bool] = None
    # Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
    bit_locker_disable_warning_for_other_disk_encryption: Optional[bool] = None
    # Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
    bit_locker_enable_storage_card_encryption_on_mobile: Optional[bool] = None
    # Allows the admin to require encryption to be turned on using BitLocker.
    bit_locker_encrypt_device: Optional[bool] = None
    # BitLocker Fixed Drive Policy.
    bit_locker_fixed_drive_policy: Optional[BitLockerFixedDrivePolicy] = None
    # BitLocker recovery password rotation type
    bit_locker_recovery_password_rotation: Optional[BitLockerRecoveryPasswordRotationType] = None
    # BitLocker Removable Drive Policy.
    bit_locker_removable_drive_policy: Optional[BitLockerRemovableDrivePolicy] = None
    # BitLocker System Drive Policy.
    bit_locker_system_drive_policy: Optional[BitLockerSystemDrivePolicy] = None
    # List of folder paths to be added to the list of protected folders
    defender_additional_guarded_folders: Optional[list[str]] = None
    # Possible values of Defender PUA Protection
    defender_adobe_reader_launch_child_process: Optional[DefenderProtectionType] = None
    # Possible values of Defender PUA Protection
    defender_advanced_ransomeware_protection_type: Optional[DefenderProtectionType] = None
    # Allows or disallows Windows Defender Behavior Monitoring functionality.
    defender_allow_behavior_monitoring: Optional[bool] = None
    # To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
    defender_allow_cloud_protection: Optional[bool] = None
    # Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
    defender_allow_end_user_access: Optional[bool] = None
    # Allows or disallows Windows Defender Intrusion Prevention functionality.
    defender_allow_intrusion_prevention_system: Optional[bool] = None
    # Allows or disallows Windows Defender On Access Protection functionality.
    defender_allow_on_access_protection: Optional[bool] = None
    # Allows or disallows Windows Defender Realtime Monitoring functionality.
    defender_allow_real_time_monitoring: Optional[bool] = None
    # Allows or disallows scanning of archives.
    defender_allow_scan_archive_files: Optional[bool] = None
    # Allows or disallows Windows Defender IOAVP Protection functionality.
    defender_allow_scan_downloads: Optional[bool] = None
    # Allows or disallows a scanning of network files.
    defender_allow_scan_network_files: Optional[bool] = None
    # Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
    defender_allow_scan_removable_drives_during_full_scan: Optional[bool] = None
    # Allows or disallows Windows Defender Script Scanning functionality.
    defender_allow_scan_scripts_loaded_in_internet_explorer: Optional[bool] = None
    # List of exe files and folders to be excluded from attack surface reduction rules
    defender_attack_surface_reduction_excluded_paths: Optional[list[str]] = None
    # Allows or disallows user access to the Windows Defender UI. If disallowed, all Windows Defender notifications will also be suppressed.
    defender_block_end_user_access: Optional[bool] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_block_persistence_through_wmi_type: Optional[DefenderAttackSurfaceType] = None
    # This policy setting allows you to manage whether a check for new virus and spyware definitions will occur before running a scan.
    defender_check_for_signatures_before_running_scan: Optional[bool] = None
    # Added in Windows 10, version 1709. This policy setting determines how aggressive Windows Defender Antivirus will be in blocking and scanning suspicious files. Value type is integer. This feature requires the 'Join Microsoft MAPS' setting enabled in order to function. Possible values are: notConfigured, high, highPlus, zeroTolerance.
    defender_cloud_block_level: Optional[DefenderCloudBlockLevelType] = None
    # Added in Windows 10, version 1709. This feature allows Windows Defender Antivirus to block a suspicious file for up to 60 seconds, and scan it in the cloud to make sure it's safe. Value type is integer, range is 0 - 50. This feature depends on three other MAPS settings the must all be enabled- 'Configure the 'Block at First Sight' feature; 'Join Microsoft MAPS'; 'Send file samples when further analysis is required'. Valid values 0 to 50
    defender_cloud_extended_timeout_in_seconds: Optional[int] = None
    # Time period (in days) that quarantine items will be stored on the system. Valid values 0 to 90
    defender_days_before_deleting_quarantined_malware: Optional[int] = None
    # Allows an administrator to specify any valid threat severity levels and the corresponding default action ID to take.
    defender_detected_malware_actions: Optional[DefenderDetectedMalwareActions] = None
    # Allows or disallows Windows Defender Behavior Monitoring functionality.
    defender_disable_behavior_monitoring: Optional[bool] = None
    # This policy setting allows you to configure catch-up scans for scheduled full scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
    defender_disable_catchup_full_scan: Optional[bool] = None
    # This policy setting allows you to configure catch-up scans for scheduled quick scans. A catch-up scan is a scan that is initiated because a regularly scheduled scan was missed. Usually these scheduled scans are missed because the computer was turned off at the scheduled time.
    defender_disable_catchup_quick_scan: Optional[bool] = None
    # To best protect your PC, Windows Defender will send information to Microsoft about any problems it finds. Microsoft will analyze that information, learn more about problems affecting you and other customers, and offer improved solutions.
    defender_disable_cloud_protection: Optional[bool] = None
    # Allows or disallows Windows Defender Intrusion Prevention functionality.
    defender_disable_intrusion_prevention_system: Optional[bool] = None
    # Allows or disallows Windows Defender On Access Protection functionality.
    defender_disable_on_access_protection: Optional[bool] = None
    # Allows or disallows Windows Defender Realtime Monitoring functionality.
    defender_disable_real_time_monitoring: Optional[bool] = None
    # Allows or disallows scanning of archives.
    defender_disable_scan_archive_files: Optional[bool] = None
    # Allows or disallows Windows Defender IOAVP Protection functionality.
    defender_disable_scan_downloads: Optional[bool] = None
    # Allows or disallows a scanning of network files.
    defender_disable_scan_network_files: Optional[bool] = None
    # Allows or disallows a full scan of removable drives. During a quick scan, removable drives may still be scanned.
    defender_disable_scan_removable_drives_during_full_scan: Optional[bool] = None
    # Allows or disallows Windows Defender Script Scanning functionality.
    defender_disable_scan_scripts_loaded_in_internet_explorer: Optional[bool] = None
    # Possible values of Defender PUA Protection
    defender_email_content_execution: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_email_content_execution_type: Optional[DefenderAttackSurfaceType] = None
    # This policy setting allows you to enable or disable low CPU priority for scheduled scans.
    defender_enable_low_cpu_priority: Optional[bool] = None
    # Allows or disallows scanning of email.
    defender_enable_scan_incoming_mail: Optional[bool] = None
    # Allows or disallows a full scan of mapped network drives.
    defender_enable_scan_mapped_network_drives_during_full_scan: Optional[bool] = None
    # Xml content containing information regarding exploit protection details.
    defender_exploit_protection_xml: Optional[bytes] = None
    # Name of the file from which DefenderExploitProtectionXml was obtained.
    defender_exploit_protection_xml_file_name: Optional[str] = None
    # File extensions to exclude from scans and real time protection.
    defender_file_extensions_to_exclude: Optional[list[str]] = None
    # Files and folder to exclude from scans and real time protection.
    defender_files_and_folders_to_exclude: Optional[list[str]] = None
    # Possible values of Folder Protection
    defender_guard_my_folders_type: Optional[FolderProtectionType] = None
    # List of paths to exe that are allowed to access protected folders
    defender_guarded_folders_allowed_app_paths: Optional[list[str]] = None
    # Possible values of Defender PUA Protection
    defender_network_protection_type: Optional[DefenderProtectionType] = None
    # Possible values of Defender PUA Protection
    defender_office_apps_executable_content_creation_or_launch: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_office_apps_executable_content_creation_or_launch_type: Optional[DefenderAttackSurfaceType] = None
    # Possible values of Defender PUA Protection
    defender_office_apps_launch_child_process: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_office_apps_launch_child_process_type: Optional[DefenderAttackSurfaceType] = None
    # Possible values of Defender PUA Protection
    defender_office_apps_other_process_injection: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_office_apps_other_process_injection_type: Optional[DefenderAttackSurfaceType] = None
    # Possible values of Defender PUA Protection
    defender_office_communication_apps_launch_child_process: Optional[DefenderProtectionType] = None
    # Possible values of Defender PUA Protection
    defender_office_macro_code_allow_win32_imports: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_office_macro_code_allow_win32_imports_type: Optional[DefenderAttackSurfaceType] = None
    # Added in Windows 10, version 1607. Specifies the level of detection for potentially unwanted applications (PUAs). Windows Defender alerts you when potentially unwanted software is being downloaded or attempts to install itself on your computer. Possible values are: userDefined, enable, auditMode, warn, notConfigured.
    defender_potentially_unwanted_app_action: Optional[DefenderProtectionType] = None
    # Possible values of Defender PUA Protection
    defender_prevent_credential_stealing_type: Optional[DefenderProtectionType] = None
    # Possible values of Defender PUA Protection
    defender_process_creation: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_process_creation_type: Optional[DefenderAttackSurfaceType] = None
    # Processes to exclude from scans and real time protection.
    defender_processes_to_exclude: Optional[list[str]] = None
    # Controls which sets of files should be monitored. Possible values are: monitorAllFiles, monitorIncomingFilesOnly, monitorOutgoingFilesOnly.
    defender_scan_direction: Optional[DefenderRealtimeScanDirection] = None
    # Represents the average CPU load factor for the Windows Defender scan (in percent). The default value is 50. Valid values 0 to 100
    defender_scan_max_cpu_percentage: Optional[int] = None
    # Selects whether to perform a quick scan or full scan. Possible values are: userDefined, disabled, quick, full.
    defender_scan_type: Optional[DefenderScanType] = None
    # Selects the time of day that the Windows Defender quick scan should run. For example, a value of 0=12:00AM, a value of 60=1:00AM, a value of 120=2:00, and so on, up to a value of 1380=11:00PM. The default value is 120
    defender_scheduled_quick_scan_time: Optional[datetime.time] = None
    # Selects the day that the Windows Defender scan should run. Possible values are: userDefined, everyday, sunday, monday, tuesday, wednesday, thursday, friday, saturday, noScheduledScan.
    defender_scheduled_scan_day: Optional[WeeklySchedule] = None
    # Selects the time of day that the Windows Defender scan should run.
    defender_scheduled_scan_time: Optional[datetime.time] = None
    # Possible values of Defender PUA Protection
    defender_script_downloaded_payload_execution: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_script_downloaded_payload_execution_type: Optional[DefenderAttackSurfaceType] = None
    # Possible values of Defender PUA Protection
    defender_script_obfuscated_macro_code: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_script_obfuscated_macro_code_type: Optional[DefenderAttackSurfaceType] = None
    # Indicates whether or not to block user from overriding Exploit Protection settings.
    defender_security_center_block_exploit_protection_override: Optional[bool] = None
    # Used to disable the display of the account protection area.
    defender_security_center_disable_account_u_i: Optional[bool] = None
    # Used to disable the display of the app and browser protection area.
    defender_security_center_disable_app_browser_u_i: Optional[bool] = None
    # Used to disable the display of the Clear TPM button.
    defender_security_center_disable_clear_tpm_u_i: Optional[bool] = None
    # Used to disable the display of the family options area.
    defender_security_center_disable_family_u_i: Optional[bool] = None
    # Used to disable the display of the hardware protection area.
    defender_security_center_disable_hardware_u_i: Optional[bool] = None
    # Used to disable the display of the device performance and health area.
    defender_security_center_disable_health_u_i: Optional[bool] = None
    # Used to disable the display of the firewall and network protection area.
    defender_security_center_disable_network_u_i: Optional[bool] = None
    # Used to disable the display of the notification area control. The user needs to either sign out and sign in or reboot the computer for this setting to take effect.
    defender_security_center_disable_notification_area_u_i: Optional[bool] = None
    # Used to disable the display of the ransomware protection area.
    defender_security_center_disable_ransomware_u_i: Optional[bool] = None
    # Used to disable the display of the secure boot area under Device security.
    defender_security_center_disable_secure_boot_u_i: Optional[bool] = None
    # Used to disable the display of the security process troubleshooting under Device security.
    defender_security_center_disable_troubleshooting_u_i: Optional[bool] = None
    # Used to disable the display of the virus and threat protection area.
    defender_security_center_disable_virus_u_i: Optional[bool] = None
    # Used to disable the display of update TPM Firmware when a vulnerable firmware is detected.
    defender_security_center_disable_vulnerable_tpm_firmware_update_u_i: Optional[bool] = None
    # The email address that is displayed to users.
    defender_security_center_help_email: Optional[str] = None
    # The phone number or Skype ID that is displayed to users.
    defender_security_center_help_phone: Optional[str] = None
    # The help portal URL this is displayed to users.
    defender_security_center_help_u_r_l: Optional[str] = None
    # Possible values for defenderSecurityCenterITContactDisplay
    defender_security_center_i_t_contact_display: Optional[DefenderSecurityCenterITContactDisplayType] = None
    # Possible values for defenderSecurityCenterNotificationsFromApp
    defender_security_center_notifications_from_app: Optional[DefenderSecurityCenterNotificationsFromAppType] = None
    # The company name that is displayed to the users.
    defender_security_center_organization_display_name: Optional[str] = None
    # Specifies the interval (in hours) that will be used to check for signatures, so instead of using the ScheduleDay and ScheduleTime the check for new signatures will be set according to the interval. Valid values 0 to 24
    defender_signature_update_interval_in_hours: Optional[int] = None
    # Checks for the user consent level in Windows Defender to send data. Possible values are: sendSafeSamplesAutomatically, alwaysPrompt, neverSend, sendAllSamplesAutomatically.
    defender_submit_samples_consent_type: Optional[DefenderSubmitSamplesConsentType] = None
    # Possible values of Defender PUA Protection
    defender_untrusted_executable: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_untrusted_executable_type: Optional[DefenderAttackSurfaceType] = None
    # Possible values of Defender PUA Protection
    defender_untrusted_u_s_b_process: Optional[DefenderProtectionType] = None
    # Possible values of Defender Attack Surface Reduction Rules
    defender_untrusted_u_s_b_process_type: Optional[DefenderAttackSurfaceType] = None
    # This property will be deprecated in May 2019 and will be replaced with property DeviceGuardSecureBootWithDMA. Specifies whether Platform Security Level is enabled at next reboot.
    device_guard_enable_secure_boot_with_d_m_a: Optional[bool] = None
    # Turns On Virtualization Based Security(VBS).
    device_guard_enable_virtualization_based_security: Optional[bool] = None
    # Possible values of a property
    device_guard_launch_system_guard: Optional[Enablement] = None
    # Possible values of Credential Guard settings.
    device_guard_local_system_authority_credential_guard_settings: Optional[DeviceGuardLocalSystemAuthorityCredentialGuardType] = None
    # Possible values of Secure Boot with DMA
    device_guard_secure_boot_with_d_m_a: Optional[SecureBootWithDMAType] = None
    # Possible values of the DmaGuardDeviceEnumerationPolicy.
    dma_guard_device_enumeration_policy: Optional[DmaGuardDeviceEnumerationPolicyType] = None
    # Blocks stateful FTP connections to the device
    firewall_block_stateful_f_t_p: Optional[bool] = None
    # Possible values for firewallCertificateRevocationListCheckMethod
    firewall_certificate_revocation_list_check_method: Optional[FirewallCertificateRevocationListCheckMethodType] = None
    # Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
    firewall_i_p_sec_exemptions_allow_d_h_c_p: Optional[bool] = None
    # Configures IPSec exemptions to allow ICMP
    firewall_i_p_sec_exemptions_allow_i_c_m_p: Optional[bool] = None
    # Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
    firewall_i_p_sec_exemptions_allow_neighbor_discovery: Optional[bool] = None
    # Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
    firewall_i_p_sec_exemptions_allow_router_discovery: Optional[bool] = None
    # Configures IPSec exemptions to no exemptions
    firewall_i_p_sec_exemptions_none: Optional[bool] = None
    # Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
    firewall_idle_timeout_for_security_association_in_seconds: Optional[int] = None
    # If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
    firewall_merge_keying_module_settings: Optional[bool] = None
    # Possible values for firewallPacketQueueingMethod
    firewall_packet_queueing_method: Optional[FirewallPacketQueueingMethodType] = None
    # Possible values for firewallPreSharedKeyEncodingMethod
    firewall_pre_shared_key_encoding_method: Optional[FirewallPreSharedKeyEncodingMethodType] = None
    # Configures the firewall profile settings for domain networks
    firewall_profile_domain: Optional[WindowsFirewallNetworkProfile] = None
    # Configures the firewall profile settings for private networks
    firewall_profile_private: Optional[WindowsFirewallNetworkProfile] = None
    # Configures the firewall profile settings for public networks
    firewall_profile_public: Optional[WindowsFirewallNetworkProfile] = None
    # Configures the firewall rule settings. This collection can contain a maximum of 150 elements.
    firewall_rules: Optional[list[WindowsFirewallRule]] = None
    # Possible values for LanManagerAuthenticationLevel
    lan_manager_authentication_level: Optional[LanManagerAuthenticationLevel] = None
    # If enabled,the SMB client will allow insecure guest logons. If not configured, the SMB client will reject insecure guest logons.
    lan_manager_workstation_disable_insecure_guest_logons: Optional[bool] = None
    # Define a different account name to be associated with the security identifier (SID) for the account 'Administrator'.
    local_security_options_administrator_account_name: Optional[str] = None
    # Possible values for LocalSecurityOptionsAdministratorElevationPromptBehavior
    local_security_options_administrator_elevation_prompt_behavior: Optional[LocalSecurityOptionsAdministratorElevationPromptBehaviorType] = None
    # This security setting determines whether to allows anonymous users to perform certain activities, such as enumerating the names of domain accounts and network shares.
    local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares: Optional[bool] = None
    # Block PKU2U authentication requests to this device to use online identities.
    local_security_options_allow_p_k_u2_u_authentication_requests: Optional[bool] = None
    # Edit the default Security Descriptor Definition Language string to allow or deny users and groups to make remote calls to the SAM.
    local_security_options_allow_remote_calls_to_security_accounts_manager: Optional[str] = None
    # UI helper boolean for LocalSecurityOptionsAllowRemoteCallsToSecurityAccountsManager entity
    local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool: Optional[bool] = None
    # This security setting determines whether a computer can be shut down without having to log on to Windows.
    local_security_options_allow_system_to_be_shut_down_without_having_to_log_on: Optional[bool] = None
    # Allow UIAccess apps to prompt for elevation without using the secure desktop.
    local_security_options_allow_u_i_access_application_elevation: Optional[bool] = None
    # Allow UIAccess apps to prompt for elevation without using the secure desktop.Default is enabled
    local_security_options_allow_u_i_access_applications_for_secure_locations: Optional[bool] = None
    # Prevent a portable computer from being undocked without having to log in.
    local_security_options_allow_undock_without_having_to_logon: Optional[bool] = None
    # Prevent users from adding new Microsoft accounts to this computer.
    local_security_options_block_microsoft_accounts: Optional[bool] = None
    # Enable Local accounts that are not password protected to log on from locations other than the physical device.Default is enabled
    local_security_options_block_remote_logon_with_blank_password: Optional[bool] = None
    # Enabling this settings allows only interactively logged on user to access CD-ROM media.
    local_security_options_block_remote_optical_drive_access: Optional[bool] = None
    # Restrict installing printer drivers as part of connecting to a shared printer to admins only.
    local_security_options_block_users_installing_printer_drivers: Optional[bool] = None
    # This security setting determines whether the virtual memory pagefile is cleared when the system is shut down.
    local_security_options_clear_virtual_memory_page_file: Optional[bool] = None
    # This security setting determines whether packet signing is required by the SMB client component.
    local_security_options_client_digitally_sign_communications_always: Optional[bool] = None
    # If this security setting is enabled, the Server Message Block (SMB) redirector is allowed to send plaintext passwords to non-Microsoft SMB servers that do not support password encryption during authentication.
    local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers: Optional[bool] = None
    # App installations requiring elevated privileges will prompt for admin credentials.Default is enabled
    local_security_options_detect_application_installations_and_prompt_for_elevation: Optional[bool] = None
    # Determines whether the Local Administrator account is enabled or disabled.
    local_security_options_disable_administrator_account: Optional[bool] = None
    # This security setting determines whether the SMB client attempts to negotiate SMB packet signing.
    local_security_options_disable_client_digitally_sign_communications_if_server_agrees: Optional[bool] = None
    # Determines if the Guest account is enabled or disabled.
    local_security_options_disable_guest_account: Optional[bool] = None
    # This security setting determines whether packet signing is required by the SMB server component.
    local_security_options_disable_server_digitally_sign_communications_always: Optional[bool] = None
    # This security setting determines whether the SMB server will negotiate SMB packet signing with clients that request it.
    local_security_options_disable_server_digitally_sign_communications_if_client_agrees: Optional[bool] = None
    # This security setting determines what additional permissions will be granted for anonymous connections to the computer.
    local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts: Optional[bool] = None
    # Require CTRL+ALT+DEL to be pressed before a user can log on.
    local_security_options_do_not_require_ctrl_alt_del: Optional[bool] = None
    # This security setting determines if, at the next password change, the LAN Manager (LM) hash value for the new password is stored. It’s not stored by default.
    local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change: Optional[bool] = None
    # Possible values for LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser
    local_security_options_format_and_eject_of_removable_media_allowed_user: Optional[LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType] = None
    # Define a different account name to be associated with the security identifier (SID) for the account 'Guest'.
    local_security_options_guest_account_name: Optional[str] = None
    # Do not display the username of the last person who signed in on this device.
    local_security_options_hide_last_signed_in_user: Optional[bool] = None
    # Do not display the username of the person signing in to this device after credentials are entered and before the device’s desktop is shown.
    local_security_options_hide_username_at_sign_in: Optional[bool] = None
    # Possible values for LocalSecurityOptionsInformationDisplayedOnLockScreen
    local_security_options_information_displayed_on_lock_screen: Optional[LocalSecurityOptionsInformationDisplayedOnLockScreenType] = None
    # Possible values for LocalSecurityOptionsInformationShownOnLockScreenType
    local_security_options_information_shown_on_lock_screen: Optional[LocalSecurityOptionsInformationShownOnLockScreenType] = None
    # Set message text for users attempting to log in.
    local_security_options_log_on_message_text: Optional[str] = None
    # Set message title for users attempting to log in.
    local_security_options_log_on_message_title: Optional[str] = None
    # Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
    local_security_options_machine_inactivity_limit: Optional[int] = None
    # Define maximum minutes of inactivity on the interactive desktop’s login screen until the screen saver runs. Valid values 0 to 9999
    local_security_options_machine_inactivity_limit_in_minutes: Optional[int] = None
    # Possible values for LocalSecurityOptionsMinimumSessionSecurity
    local_security_options_minimum_session_security_for_ntlm_ssp_based_clients: Optional[LocalSecurityOptionsMinimumSessionSecurity] = None
    # Possible values for LocalSecurityOptionsMinimumSessionSecurity
    local_security_options_minimum_session_security_for_ntlm_ssp_based_servers: Optional[LocalSecurityOptionsMinimumSessionSecurity] = None
    # Enforce PKI certification path validation for a given executable file before it is permitted to run.
    local_security_options_only_elevate_signed_executables: Optional[bool] = None
    # By default, this security setting restricts anonymous access to shares and pipes to the settings for named pipes that can be accessed anonymously and Shares that can be accessed anonymously
    local_security_options_restrict_anonymous_access_to_named_pipes_and_shares: Optional[bool] = None
    # Possible values for LocalSecurityOptionsSmartCardRemovalBehaviorType
    local_security_options_smart_card_removal_behavior: Optional[LocalSecurityOptionsSmartCardRemovalBehaviorType] = None
    # Possible values for LocalSecurityOptionsStandardUserElevationPromptBehavior
    local_security_options_standard_user_elevation_prompt_behavior: Optional[LocalSecurityOptionsStandardUserElevationPromptBehaviorType] = None
    # Enable all elevation requests to go to the interactive user's desktop rather than the secure desktop. Prompt behavior policy settings for admins and standard users are used.
    local_security_options_switch_to_secure_desktop_when_prompting_for_elevation: Optional[bool] = None
    # Defines whether the built-in admin account uses Admin Approval Mode or runs all apps with full admin privileges.Default is enabled
    local_security_options_use_admin_approval_mode: Optional[bool] = None
    # Define whether Admin Approval Mode and all UAC policy settings are enabled, default is enabled
    local_security_options_use_admin_approval_mode_for_administrators: Optional[bool] = None
    # Virtualize file and registry write failures to per user locations
    local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations: Optional[bool] = None
    # Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
    smart_screen_block_override_for_files: Optional[bool] = None
    # Allows IT Admins to configure SmartScreen for Windows.
    smart_screen_enable_in_shell: Optional[bool] = None
    # This user right is used by Credential Manager during Backup/Restore. Users' saved credentials might be compromised if this privilege is given to other entities. Only states NotConfigured and Allowed are supported
    user_rights_access_credential_manager_as_trusted_caller: Optional[DeviceManagementUserRightsSetting] = None
    # This user right allows a process to impersonate any user without authentication. The process can therefore gain access to the same local resources as that user. Only states NotConfigured and Allowed are supported
    user_rights_act_as_part_of_the_operating_system: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users and groups are allowed to connect to the computer over the network. State Allowed is supported.
    user_rights_allow_access_from_network: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when backing up files and directories. Only states NotConfigured and Allowed are supported
    user_rights_backup_data: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users and groups are block from connecting to the computer over the network. State Block is supported.
    user_rights_block_access_from_network: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users and groups can change the time and date on the internal clock of the computer. Only states NotConfigured and Allowed are supported
    user_rights_change_system_time: Optional[DeviceManagementUserRightsSetting] = None
    # This security setting determines whether users can create global objects that are available to all sessions. Users who can create global objects could affect processes that run under other users' sessions, which could lead to application failure or data corruption. Only states NotConfigured and Allowed are supported
    user_rights_create_global_objects: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users and groups can call an internal API to create and change the size of a page file. Only states NotConfigured and Allowed are supported
    user_rights_create_page_file: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which accounts can be used by processes to create a directory object using the object manager. Only states NotConfigured and Allowed are supported
    user_rights_create_permanent_shared_objects: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines if the user can create a symbolic link from the computer to which they are logged on. Only states NotConfigured and Allowed are supported
    user_rights_create_symbolic_links: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users/groups can be used by processes to create a token that can then be used to get access to any local resources when the process uses an internal API to create an access token. Only states NotConfigured and Allowed are supported
    user_rights_create_token: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can attach a debugger to any process or to the kernel. Only states NotConfigured and Allowed are supported
    user_rights_debug_programs: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can set the Trusted for Delegation setting on a user or computer object. Only states NotConfigured and Allowed are supported.
    user_rights_delegation: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users cannot log on to the computer. States NotConfigured, Blocked are supported
    user_rights_deny_local_log_on: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which accounts can be used by a process to add entries to the security log. The security log is used to trace unauthorized system access.  Only states NotConfigured and Allowed are supported.
    user_rights_generate_security_audits: Optional[DeviceManagementUserRightsSetting] = None
    # Assigning this user right to a user allows programs running on behalf of that user to impersonate a client. Requiring this user right for this kind of impersonation prevents an unauthorized user from convincing a client to connect to a service that they have created and then impersonating that client, which can elevate the unauthorized user's permissions to administrative or system levels. Only states NotConfigured and Allowed are supported.
    user_rights_impersonate_client: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which accounts can use a process with Write Property access to another process to increase the execution priority assigned to the other process. Only states NotConfigured and Allowed are supported.
    user_rights_increase_scheduling_priority: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can dynamically load and unload device drivers or other code in to kernel mode. Only states NotConfigured and Allowed are supported.
    user_rights_load_unload_drivers: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can log on to the computer. States NotConfigured, Allowed are supported
    user_rights_local_log_on: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which accounts can use a process to keep data in physical memory, which prevents the system from paging the data to virtual memory on disk. Only states NotConfigured and Allowed are supported.
    user_rights_lock_memory: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can specify object access auditing options for individual resources, such as files, Active Directory objects, and registry keys. Only states NotConfigured and Allowed are supported.
    user_rights_manage_auditing_and_security_logs: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users and groups can run maintenance tasks on a volume, such as remote defragmentation. Only states NotConfigured and Allowed are supported.
    user_rights_manage_volumes: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines who can modify firmware environment values. Only states NotConfigured and Allowed are supported.
    user_rights_modify_firmware_environment: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which user accounts can modify the integrity label of objects, such as files, registry keys, or processes owned by other users. Only states NotConfigured and Allowed are supported.
    user_rights_modify_object_labels: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can use performance monitoring tools to monitor the performance of system processes. Only states NotConfigured and Allowed are supported.
    user_rights_profile_single_process: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users and groups are prohibited from logging on as a Remote Desktop Services client. Only states NotConfigured and Blocked are supported
    user_rights_remote_desktop_services_log_on: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users are allowed to shut down a computer from a remote location on the network. Misuse of this user right can result in a denial of service. Only states NotConfigured and Allowed are supported.
    user_rights_remote_shutdown: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can bypass file, directory, registry, and other persistent objects permissions when restoring backed up files and directories, and determines which users can set any valid security principal as the owner of an object. Only states NotConfigured and Allowed are supported.
    user_rights_restore_data: Optional[DeviceManagementUserRightsSetting] = None
    # This user right determines which users can take ownership of any securable object in the system, including Active Directory objects, files and folders, printers, registry keys, processes, and threads. Only states NotConfigured and Allowed are supported.
    user_rights_take_ownership: Optional[DeviceManagementUserRightsSetting] = None
    # Defender TamperProtection setting options
    windows_defender_tamper_protection: Optional[WindowsDefenderTamperProtectionOptions] = None
    # Possible values of xbox service start type
    xbox_services_accessory_management_service_startup_mode: Optional[ServiceStartType] = None
    # This setting determines whether xbox game save is enabled (1) or disabled (0).
    xbox_services_enable_xbox_game_save_task: Optional[bool] = None
    # Possible values of xbox service start type
    xbox_services_live_auth_manager_service_startup_mode: Optional[ServiceStartType] = None
    # Possible values of xbox service start type
    xbox_services_live_game_save_service_startup_mode: Optional[ServiceStartType] = None
    # Possible values of xbox service start type
    xbox_services_live_networking_service_startup_mode: Optional[ServiceStartType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10EndpointProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EndpointProtectionConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10EndpointProtectionConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
        from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
        from .application_guard_enabled_options import ApplicationGuardEnabledOptions
        from .app_locker_application_control_type import AppLockerApplicationControlType
        from .bit_locker_fixed_drive_policy import BitLockerFixedDrivePolicy
        from .bit_locker_recovery_password_rotation_type import BitLockerRecoveryPasswordRotationType
        from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
        from .bit_locker_system_drive_policy import BitLockerSystemDrivePolicy
        from .defender_attack_surface_type import DefenderAttackSurfaceType
        from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
        from .defender_detected_malware_actions import DefenderDetectedMalwareActions
        from .defender_protection_type import DefenderProtectionType
        from .defender_realtime_scan_direction import DefenderRealtimeScanDirection
        from .defender_scan_type import DefenderScanType
        from .defender_security_center_i_t_contact_display_type import DefenderSecurityCenterITContactDisplayType
        from .defender_security_center_notifications_from_app_type import DefenderSecurityCenterNotificationsFromAppType
        from .defender_submit_samples_consent_type import DefenderSubmitSamplesConsentType
        from .device_configuration import DeviceConfiguration
        from .device_guard_local_system_authority_credential_guard_type import DeviceGuardLocalSystemAuthorityCredentialGuardType
        from .device_management_user_rights_setting import DeviceManagementUserRightsSetting
        from .dma_guard_device_enumeration_policy_type import DmaGuardDeviceEnumerationPolicyType
        from .enablement import Enablement
        from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
        from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
        from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
        from .folder_protection_type import FolderProtectionType
        from .lan_manager_authentication_level import LanManagerAuthenticationLevel
        from .local_security_options_administrator_elevation_prompt_behavior_type import LocalSecurityOptionsAdministratorElevationPromptBehaviorType
        from .local_security_options_format_and_eject_of_removable_media_allowed_user_type import LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType
        from .local_security_options_information_displayed_on_lock_screen_type import LocalSecurityOptionsInformationDisplayedOnLockScreenType
        from .local_security_options_information_shown_on_lock_screen_type import LocalSecurityOptionsInformationShownOnLockScreenType
        from .local_security_options_minimum_session_security import LocalSecurityOptionsMinimumSessionSecurity
        from .local_security_options_smart_card_removal_behavior_type import LocalSecurityOptionsSmartCardRemovalBehaviorType
        from .local_security_options_standard_user_elevation_prompt_behavior_type import LocalSecurityOptionsStandardUserElevationPromptBehaviorType
        from .secure_boot_with_d_m_a_type import SecureBootWithDMAType
        from .service_start_type import ServiceStartType
        from .weekly_schedule import WeeklySchedule
        from .windows_defender_tamper_protection_options import WindowsDefenderTamperProtectionOptions
        from .windows_firewall_network_profile import WindowsFirewallNetworkProfile
        from .windows_firewall_rule import WindowsFirewallRule

        from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
        from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
        from .application_guard_enabled_options import ApplicationGuardEnabledOptions
        from .app_locker_application_control_type import AppLockerApplicationControlType
        from .bit_locker_fixed_drive_policy import BitLockerFixedDrivePolicy
        from .bit_locker_recovery_password_rotation_type import BitLockerRecoveryPasswordRotationType
        from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
        from .bit_locker_system_drive_policy import BitLockerSystemDrivePolicy
        from .defender_attack_surface_type import DefenderAttackSurfaceType
        from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
        from .defender_detected_malware_actions import DefenderDetectedMalwareActions
        from .defender_protection_type import DefenderProtectionType
        from .defender_realtime_scan_direction import DefenderRealtimeScanDirection
        from .defender_scan_type import DefenderScanType
        from .defender_security_center_i_t_contact_display_type import DefenderSecurityCenterITContactDisplayType
        from .defender_security_center_notifications_from_app_type import DefenderSecurityCenterNotificationsFromAppType
        from .defender_submit_samples_consent_type import DefenderSubmitSamplesConsentType
        from .device_configuration import DeviceConfiguration
        from .device_guard_local_system_authority_credential_guard_type import DeviceGuardLocalSystemAuthorityCredentialGuardType
        from .device_management_user_rights_setting import DeviceManagementUserRightsSetting
        from .dma_guard_device_enumeration_policy_type import DmaGuardDeviceEnumerationPolicyType
        from .enablement import Enablement
        from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
        from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
        from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
        from .folder_protection_type import FolderProtectionType
        from .lan_manager_authentication_level import LanManagerAuthenticationLevel
        from .local_security_options_administrator_elevation_prompt_behavior_type import LocalSecurityOptionsAdministratorElevationPromptBehaviorType
        from .local_security_options_format_and_eject_of_removable_media_allowed_user_type import LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType
        from .local_security_options_information_displayed_on_lock_screen_type import LocalSecurityOptionsInformationDisplayedOnLockScreenType
        from .local_security_options_information_shown_on_lock_screen_type import LocalSecurityOptionsInformationShownOnLockScreenType
        from .local_security_options_minimum_session_security import LocalSecurityOptionsMinimumSessionSecurity
        from .local_security_options_smart_card_removal_behavior_type import LocalSecurityOptionsSmartCardRemovalBehaviorType
        from .local_security_options_standard_user_elevation_prompt_behavior_type import LocalSecurityOptionsStandardUserElevationPromptBehaviorType
        from .secure_boot_with_d_m_a_type import SecureBootWithDMAType
        from .service_start_type import ServiceStartType
        from .weekly_schedule import WeeklySchedule
        from .windows_defender_tamper_protection_options import WindowsDefenderTamperProtectionOptions
        from .windows_firewall_network_profile import WindowsFirewallNetworkProfile
        from .windows_firewall_rule import WindowsFirewallRule

        fields: dict[str, Callable[[Any], None]] = {
            "appLockerApplicationControl": lambda n : setattr(self, 'app_locker_application_control', n.get_enum_value(AppLockerApplicationControlType)),
            "applicationGuardAllowCameraMicrophoneRedirection": lambda n : setattr(self, 'application_guard_allow_camera_microphone_redirection', n.get_bool_value()),
            "applicationGuardAllowFileSaveOnHost": lambda n : setattr(self, 'application_guard_allow_file_save_on_host', n.get_bool_value()),
            "applicationGuardAllowPersistence": lambda n : setattr(self, 'application_guard_allow_persistence', n.get_bool_value()),
            "applicationGuardAllowPrintToLocalPrinters": lambda n : setattr(self, 'application_guard_allow_print_to_local_printers', n.get_bool_value()),
            "applicationGuardAllowPrintToNetworkPrinters": lambda n : setattr(self, 'application_guard_allow_print_to_network_printers', n.get_bool_value()),
            "applicationGuardAllowPrintToPDF": lambda n : setattr(self, 'application_guard_allow_print_to_p_d_f', n.get_bool_value()),
            "applicationGuardAllowPrintToXPS": lambda n : setattr(self, 'application_guard_allow_print_to_x_p_s', n.get_bool_value()),
            "applicationGuardAllowVirtualGPU": lambda n : setattr(self, 'application_guard_allow_virtual_g_p_u', n.get_bool_value()),
            "applicationGuardBlockClipboardSharing": lambda n : setattr(self, 'application_guard_block_clipboard_sharing', n.get_enum_value(ApplicationGuardBlockClipboardSharingType)),
            "applicationGuardBlockFileTransfer": lambda n : setattr(self, 'application_guard_block_file_transfer', n.get_enum_value(ApplicationGuardBlockFileTransferType)),
            "applicationGuardBlockNonEnterpriseContent": lambda n : setattr(self, 'application_guard_block_non_enterprise_content', n.get_bool_value()),
            "applicationGuardCertificateThumbprints": lambda n : setattr(self, 'application_guard_certificate_thumbprints', n.get_collection_of_primitive_values(str)),
            "applicationGuardEnabled": lambda n : setattr(self, 'application_guard_enabled', n.get_bool_value()),
            "applicationGuardEnabledOptions": lambda n : setattr(self, 'application_guard_enabled_options', n.get_enum_value(ApplicationGuardEnabledOptions)),
            "applicationGuardForceAuditing": lambda n : setattr(self, 'application_guard_force_auditing', n.get_bool_value()),
            "bitLockerAllowStandardUserEncryption": lambda n : setattr(self, 'bit_locker_allow_standard_user_encryption', n.get_bool_value()),
            "bitLockerDisableWarningForOtherDiskEncryption": lambda n : setattr(self, 'bit_locker_disable_warning_for_other_disk_encryption', n.get_bool_value()),
            "bitLockerEnableStorageCardEncryptionOnMobile": lambda n : setattr(self, 'bit_locker_enable_storage_card_encryption_on_mobile', n.get_bool_value()),
            "bitLockerEncryptDevice": lambda n : setattr(self, 'bit_locker_encrypt_device', n.get_bool_value()),
            "bitLockerFixedDrivePolicy": lambda n : setattr(self, 'bit_locker_fixed_drive_policy', n.get_object_value(BitLockerFixedDrivePolicy)),
            "bitLockerRecoveryPasswordRotation": lambda n : setattr(self, 'bit_locker_recovery_password_rotation', n.get_enum_value(BitLockerRecoveryPasswordRotationType)),
            "bitLockerRemovableDrivePolicy": lambda n : setattr(self, 'bit_locker_removable_drive_policy', n.get_object_value(BitLockerRemovableDrivePolicy)),
            "bitLockerSystemDrivePolicy": lambda n : setattr(self, 'bit_locker_system_drive_policy', n.get_object_value(BitLockerSystemDrivePolicy)),
            "defenderAdditionalGuardedFolders": lambda n : setattr(self, 'defender_additional_guarded_folders', n.get_collection_of_primitive_values(str)),
            "defenderAdobeReaderLaunchChildProcess": lambda n : setattr(self, 'defender_adobe_reader_launch_child_process', n.get_enum_value(DefenderProtectionType)),
            "defenderAdvancedRansomewareProtectionType": lambda n : setattr(self, 'defender_advanced_ransomeware_protection_type', n.get_enum_value(DefenderProtectionType)),
            "defenderAllowBehaviorMonitoring": lambda n : setattr(self, 'defender_allow_behavior_monitoring', n.get_bool_value()),
            "defenderAllowCloudProtection": lambda n : setattr(self, 'defender_allow_cloud_protection', n.get_bool_value()),
            "defenderAllowEndUserAccess": lambda n : setattr(self, 'defender_allow_end_user_access', n.get_bool_value()),
            "defenderAllowIntrusionPreventionSystem": lambda n : setattr(self, 'defender_allow_intrusion_prevention_system', n.get_bool_value()),
            "defenderAllowOnAccessProtection": lambda n : setattr(self, 'defender_allow_on_access_protection', n.get_bool_value()),
            "defenderAllowRealTimeMonitoring": lambda n : setattr(self, 'defender_allow_real_time_monitoring', n.get_bool_value()),
            "defenderAllowScanArchiveFiles": lambda n : setattr(self, 'defender_allow_scan_archive_files', n.get_bool_value()),
            "defenderAllowScanDownloads": lambda n : setattr(self, 'defender_allow_scan_downloads', n.get_bool_value()),
            "defenderAllowScanNetworkFiles": lambda n : setattr(self, 'defender_allow_scan_network_files', n.get_bool_value()),
            "defenderAllowScanRemovableDrivesDuringFullScan": lambda n : setattr(self, 'defender_allow_scan_removable_drives_during_full_scan', n.get_bool_value()),
            "defenderAllowScanScriptsLoadedInInternetExplorer": lambda n : setattr(self, 'defender_allow_scan_scripts_loaded_in_internet_explorer', n.get_bool_value()),
            "defenderAttackSurfaceReductionExcludedPaths": lambda n : setattr(self, 'defender_attack_surface_reduction_excluded_paths', n.get_collection_of_primitive_values(str)),
            "defenderBlockEndUserAccess": lambda n : setattr(self, 'defender_block_end_user_access', n.get_bool_value()),
            "defenderBlockPersistenceThroughWmiType": lambda n : setattr(self, 'defender_block_persistence_through_wmi_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderCheckForSignaturesBeforeRunningScan": lambda n : setattr(self, 'defender_check_for_signatures_before_running_scan', n.get_bool_value()),
            "defenderCloudBlockLevel": lambda n : setattr(self, 'defender_cloud_block_level', n.get_enum_value(DefenderCloudBlockLevelType)),
            "defenderCloudExtendedTimeoutInSeconds": lambda n : setattr(self, 'defender_cloud_extended_timeout_in_seconds', n.get_int_value()),
            "defenderDaysBeforeDeletingQuarantinedMalware": lambda n : setattr(self, 'defender_days_before_deleting_quarantined_malware', n.get_int_value()),
            "defenderDetectedMalwareActions": lambda n : setattr(self, 'defender_detected_malware_actions', n.get_object_value(DefenderDetectedMalwareActions)),
            "defenderDisableBehaviorMonitoring": lambda n : setattr(self, 'defender_disable_behavior_monitoring', n.get_bool_value()),
            "defenderDisableCatchupFullScan": lambda n : setattr(self, 'defender_disable_catchup_full_scan', n.get_bool_value()),
            "defenderDisableCatchupQuickScan": lambda n : setattr(self, 'defender_disable_catchup_quick_scan', n.get_bool_value()),
            "defenderDisableCloudProtection": lambda n : setattr(self, 'defender_disable_cloud_protection', n.get_bool_value()),
            "defenderDisableIntrusionPreventionSystem": lambda n : setattr(self, 'defender_disable_intrusion_prevention_system', n.get_bool_value()),
            "defenderDisableOnAccessProtection": lambda n : setattr(self, 'defender_disable_on_access_protection', n.get_bool_value()),
            "defenderDisableRealTimeMonitoring": lambda n : setattr(self, 'defender_disable_real_time_monitoring', n.get_bool_value()),
            "defenderDisableScanArchiveFiles": lambda n : setattr(self, 'defender_disable_scan_archive_files', n.get_bool_value()),
            "defenderDisableScanDownloads": lambda n : setattr(self, 'defender_disable_scan_downloads', n.get_bool_value()),
            "defenderDisableScanNetworkFiles": lambda n : setattr(self, 'defender_disable_scan_network_files', n.get_bool_value()),
            "defenderDisableScanRemovableDrivesDuringFullScan": lambda n : setattr(self, 'defender_disable_scan_removable_drives_during_full_scan', n.get_bool_value()),
            "defenderDisableScanScriptsLoadedInInternetExplorer": lambda n : setattr(self, 'defender_disable_scan_scripts_loaded_in_internet_explorer', n.get_bool_value()),
            "defenderEmailContentExecution": lambda n : setattr(self, 'defender_email_content_execution', n.get_enum_value(DefenderProtectionType)),
            "defenderEmailContentExecutionType": lambda n : setattr(self, 'defender_email_content_execution_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderEnableLowCpuPriority": lambda n : setattr(self, 'defender_enable_low_cpu_priority', n.get_bool_value()),
            "defenderEnableScanIncomingMail": lambda n : setattr(self, 'defender_enable_scan_incoming_mail', n.get_bool_value()),
            "defenderEnableScanMappedNetworkDrivesDuringFullScan": lambda n : setattr(self, 'defender_enable_scan_mapped_network_drives_during_full_scan', n.get_bool_value()),
            "defenderExploitProtectionXml": lambda n : setattr(self, 'defender_exploit_protection_xml', n.get_bytes_value()),
            "defenderExploitProtectionXmlFileName": lambda n : setattr(self, 'defender_exploit_protection_xml_file_name', n.get_str_value()),
            "defenderFileExtensionsToExclude": lambda n : setattr(self, 'defender_file_extensions_to_exclude', n.get_collection_of_primitive_values(str)),
            "defenderFilesAndFoldersToExclude": lambda n : setattr(self, 'defender_files_and_folders_to_exclude', n.get_collection_of_primitive_values(str)),
            "defenderGuardMyFoldersType": lambda n : setattr(self, 'defender_guard_my_folders_type', n.get_enum_value(FolderProtectionType)),
            "defenderGuardedFoldersAllowedAppPaths": lambda n : setattr(self, 'defender_guarded_folders_allowed_app_paths', n.get_collection_of_primitive_values(str)),
            "defenderNetworkProtectionType": lambda n : setattr(self, 'defender_network_protection_type', n.get_enum_value(DefenderProtectionType)),
            "defenderOfficeAppsExecutableContentCreationOrLaunch": lambda n : setattr(self, 'defender_office_apps_executable_content_creation_or_launch', n.get_enum_value(DefenderProtectionType)),
            "defenderOfficeAppsExecutableContentCreationOrLaunchType": lambda n : setattr(self, 'defender_office_apps_executable_content_creation_or_launch_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderOfficeAppsLaunchChildProcess": lambda n : setattr(self, 'defender_office_apps_launch_child_process', n.get_enum_value(DefenderProtectionType)),
            "defenderOfficeAppsLaunchChildProcessType": lambda n : setattr(self, 'defender_office_apps_launch_child_process_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderOfficeAppsOtherProcessInjection": lambda n : setattr(self, 'defender_office_apps_other_process_injection', n.get_enum_value(DefenderProtectionType)),
            "defenderOfficeAppsOtherProcessInjectionType": lambda n : setattr(self, 'defender_office_apps_other_process_injection_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderOfficeCommunicationAppsLaunchChildProcess": lambda n : setattr(self, 'defender_office_communication_apps_launch_child_process', n.get_enum_value(DefenderProtectionType)),
            "defenderOfficeMacroCodeAllowWin32Imports": lambda n : setattr(self, 'defender_office_macro_code_allow_win32_imports', n.get_enum_value(DefenderProtectionType)),
            "defenderOfficeMacroCodeAllowWin32ImportsType": lambda n : setattr(self, 'defender_office_macro_code_allow_win32_imports_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderPotentiallyUnwantedAppAction": lambda n : setattr(self, 'defender_potentially_unwanted_app_action', n.get_enum_value(DefenderProtectionType)),
            "defenderPreventCredentialStealingType": lambda n : setattr(self, 'defender_prevent_credential_stealing_type', n.get_enum_value(DefenderProtectionType)),
            "defenderProcessCreation": lambda n : setattr(self, 'defender_process_creation', n.get_enum_value(DefenderProtectionType)),
            "defenderProcessCreationType": lambda n : setattr(self, 'defender_process_creation_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderProcessesToExclude": lambda n : setattr(self, 'defender_processes_to_exclude', n.get_collection_of_primitive_values(str)),
            "defenderScanDirection": lambda n : setattr(self, 'defender_scan_direction', n.get_enum_value(DefenderRealtimeScanDirection)),
            "defenderScanMaxCpuPercentage": lambda n : setattr(self, 'defender_scan_max_cpu_percentage', n.get_int_value()),
            "defenderScanType": lambda n : setattr(self, 'defender_scan_type', n.get_enum_value(DefenderScanType)),
            "defenderScheduledQuickScanTime": lambda n : setattr(self, 'defender_scheduled_quick_scan_time', n.get_time_value()),
            "defenderScheduledScanDay": lambda n : setattr(self, 'defender_scheduled_scan_day', n.get_enum_value(WeeklySchedule)),
            "defenderScheduledScanTime": lambda n : setattr(self, 'defender_scheduled_scan_time', n.get_time_value()),
            "defenderScriptDownloadedPayloadExecution": lambda n : setattr(self, 'defender_script_downloaded_payload_execution', n.get_enum_value(DefenderProtectionType)),
            "defenderScriptDownloadedPayloadExecutionType": lambda n : setattr(self, 'defender_script_downloaded_payload_execution_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderScriptObfuscatedMacroCode": lambda n : setattr(self, 'defender_script_obfuscated_macro_code', n.get_enum_value(DefenderProtectionType)),
            "defenderScriptObfuscatedMacroCodeType": lambda n : setattr(self, 'defender_script_obfuscated_macro_code_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderSecurityCenterBlockExploitProtectionOverride": lambda n : setattr(self, 'defender_security_center_block_exploit_protection_override', n.get_bool_value()),
            "defenderSecurityCenterDisableAccountUI": lambda n : setattr(self, 'defender_security_center_disable_account_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableAppBrowserUI": lambda n : setattr(self, 'defender_security_center_disable_app_browser_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableClearTpmUI": lambda n : setattr(self, 'defender_security_center_disable_clear_tpm_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableFamilyUI": lambda n : setattr(self, 'defender_security_center_disable_family_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableHardwareUI": lambda n : setattr(self, 'defender_security_center_disable_hardware_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableHealthUI": lambda n : setattr(self, 'defender_security_center_disable_health_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableNetworkUI": lambda n : setattr(self, 'defender_security_center_disable_network_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableNotificationAreaUI": lambda n : setattr(self, 'defender_security_center_disable_notification_area_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableRansomwareUI": lambda n : setattr(self, 'defender_security_center_disable_ransomware_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableSecureBootUI": lambda n : setattr(self, 'defender_security_center_disable_secure_boot_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableTroubleshootingUI": lambda n : setattr(self, 'defender_security_center_disable_troubleshooting_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableVirusUI": lambda n : setattr(self, 'defender_security_center_disable_virus_u_i', n.get_bool_value()),
            "defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI": lambda n : setattr(self, 'defender_security_center_disable_vulnerable_tpm_firmware_update_u_i', n.get_bool_value()),
            "defenderSecurityCenterHelpEmail": lambda n : setattr(self, 'defender_security_center_help_email', n.get_str_value()),
            "defenderSecurityCenterHelpPhone": lambda n : setattr(self, 'defender_security_center_help_phone', n.get_str_value()),
            "defenderSecurityCenterHelpURL": lambda n : setattr(self, 'defender_security_center_help_u_r_l', n.get_str_value()),
            "defenderSecurityCenterITContactDisplay": lambda n : setattr(self, 'defender_security_center_i_t_contact_display', n.get_enum_value(DefenderSecurityCenterITContactDisplayType)),
            "defenderSecurityCenterNotificationsFromApp": lambda n : setattr(self, 'defender_security_center_notifications_from_app', n.get_enum_value(DefenderSecurityCenterNotificationsFromAppType)),
            "defenderSecurityCenterOrganizationDisplayName": lambda n : setattr(self, 'defender_security_center_organization_display_name', n.get_str_value()),
            "defenderSignatureUpdateIntervalInHours": lambda n : setattr(self, 'defender_signature_update_interval_in_hours', n.get_int_value()),
            "defenderSubmitSamplesConsentType": lambda n : setattr(self, 'defender_submit_samples_consent_type', n.get_enum_value(DefenderSubmitSamplesConsentType)),
            "defenderUntrustedExecutable": lambda n : setattr(self, 'defender_untrusted_executable', n.get_enum_value(DefenderProtectionType)),
            "defenderUntrustedExecutableType": lambda n : setattr(self, 'defender_untrusted_executable_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "defenderUntrustedUSBProcess": lambda n : setattr(self, 'defender_untrusted_u_s_b_process', n.get_enum_value(DefenderProtectionType)),
            "defenderUntrustedUSBProcessType": lambda n : setattr(self, 'defender_untrusted_u_s_b_process_type', n.get_enum_value(DefenderAttackSurfaceType)),
            "deviceGuardEnableSecureBootWithDMA": lambda n : setattr(self, 'device_guard_enable_secure_boot_with_d_m_a', n.get_bool_value()),
            "deviceGuardEnableVirtualizationBasedSecurity": lambda n : setattr(self, 'device_guard_enable_virtualization_based_security', n.get_bool_value()),
            "deviceGuardLaunchSystemGuard": lambda n : setattr(self, 'device_guard_launch_system_guard', n.get_enum_value(Enablement)),
            "deviceGuardLocalSystemAuthorityCredentialGuardSettings": lambda n : setattr(self, 'device_guard_local_system_authority_credential_guard_settings', n.get_enum_value(DeviceGuardLocalSystemAuthorityCredentialGuardType)),
            "deviceGuardSecureBootWithDMA": lambda n : setattr(self, 'device_guard_secure_boot_with_d_m_a', n.get_enum_value(SecureBootWithDMAType)),
            "dmaGuardDeviceEnumerationPolicy": lambda n : setattr(self, 'dma_guard_device_enumeration_policy', n.get_enum_value(DmaGuardDeviceEnumerationPolicyType)),
            "firewallBlockStatefulFTP": lambda n : setattr(self, 'firewall_block_stateful_f_t_p', n.get_bool_value()),
            "firewallCertificateRevocationListCheckMethod": lambda n : setattr(self, 'firewall_certificate_revocation_list_check_method', n.get_enum_value(FirewallCertificateRevocationListCheckMethodType)),
            "firewallIPSecExemptionsAllowDHCP": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_d_h_c_p', n.get_bool_value()),
            "firewallIPSecExemptionsAllowICMP": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_i_c_m_p', n.get_bool_value()),
            "firewallIPSecExemptionsAllowNeighborDiscovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_neighbor_discovery', n.get_bool_value()),
            "firewallIPSecExemptionsAllowRouterDiscovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_router_discovery', n.get_bool_value()),
            "firewallIPSecExemptionsNone": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_none', n.get_bool_value()),
            "firewallIdleTimeoutForSecurityAssociationInSeconds": lambda n : setattr(self, 'firewall_idle_timeout_for_security_association_in_seconds', n.get_int_value()),
            "firewallMergeKeyingModuleSettings": lambda n : setattr(self, 'firewall_merge_keying_module_settings', n.get_bool_value()),
            "firewallPacketQueueingMethod": lambda n : setattr(self, 'firewall_packet_queueing_method', n.get_enum_value(FirewallPacketQueueingMethodType)),
            "firewallPreSharedKeyEncodingMethod": lambda n : setattr(self, 'firewall_pre_shared_key_encoding_method', n.get_enum_value(FirewallPreSharedKeyEncodingMethodType)),
            "firewallProfileDomain": lambda n : setattr(self, 'firewall_profile_domain', n.get_object_value(WindowsFirewallNetworkProfile)),
            "firewallProfilePrivate": lambda n : setattr(self, 'firewall_profile_private', n.get_object_value(WindowsFirewallNetworkProfile)),
            "firewallProfilePublic": lambda n : setattr(self, 'firewall_profile_public', n.get_object_value(WindowsFirewallNetworkProfile)),
            "firewallRules": lambda n : setattr(self, 'firewall_rules', n.get_collection_of_object_values(WindowsFirewallRule)),
            "lanManagerAuthenticationLevel": lambda n : setattr(self, 'lan_manager_authentication_level', n.get_enum_value(LanManagerAuthenticationLevel)),
            "lanManagerWorkstationDisableInsecureGuestLogons": lambda n : setattr(self, 'lan_manager_workstation_disable_insecure_guest_logons', n.get_bool_value()),
            "localSecurityOptionsAdministratorAccountName": lambda n : setattr(self, 'local_security_options_administrator_account_name', n.get_str_value()),
            "localSecurityOptionsAdministratorElevationPromptBehavior": lambda n : setattr(self, 'local_security_options_administrator_elevation_prompt_behavior', n.get_enum_value(LocalSecurityOptionsAdministratorElevationPromptBehaviorType)),
            "localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares": lambda n : setattr(self, 'local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares', n.get_bool_value()),
            "localSecurityOptionsAllowPKU2UAuthenticationRequests": lambda n : setattr(self, 'local_security_options_allow_p_k_u2_u_authentication_requests', n.get_bool_value()),
            "localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager": lambda n : setattr(self, 'local_security_options_allow_remote_calls_to_security_accounts_manager', n.get_str_value()),
            "localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool": lambda n : setattr(self, 'local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool', n.get_bool_value()),
            "localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn": lambda n : setattr(self, 'local_security_options_allow_system_to_be_shut_down_without_having_to_log_on', n.get_bool_value()),
            "localSecurityOptionsAllowUIAccessApplicationElevation": lambda n : setattr(self, 'local_security_options_allow_u_i_access_application_elevation', n.get_bool_value()),
            "localSecurityOptionsAllowUIAccessApplicationsForSecureLocations": lambda n : setattr(self, 'local_security_options_allow_u_i_access_applications_for_secure_locations', n.get_bool_value()),
            "localSecurityOptionsAllowUndockWithoutHavingToLogon": lambda n : setattr(self, 'local_security_options_allow_undock_without_having_to_logon', n.get_bool_value()),
            "localSecurityOptionsBlockMicrosoftAccounts": lambda n : setattr(self, 'local_security_options_block_microsoft_accounts', n.get_bool_value()),
            "localSecurityOptionsBlockRemoteLogonWithBlankPassword": lambda n : setattr(self, 'local_security_options_block_remote_logon_with_blank_password', n.get_bool_value()),
            "localSecurityOptionsBlockRemoteOpticalDriveAccess": lambda n : setattr(self, 'local_security_options_block_remote_optical_drive_access', n.get_bool_value()),
            "localSecurityOptionsBlockUsersInstallingPrinterDrivers": lambda n : setattr(self, 'local_security_options_block_users_installing_printer_drivers', n.get_bool_value()),
            "localSecurityOptionsClearVirtualMemoryPageFile": lambda n : setattr(self, 'local_security_options_clear_virtual_memory_page_file', n.get_bool_value()),
            "localSecurityOptionsClientDigitallySignCommunicationsAlways": lambda n : setattr(self, 'local_security_options_client_digitally_sign_communications_always', n.get_bool_value()),
            "localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers": lambda n : setattr(self, 'local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers', n.get_bool_value()),
            "localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation": lambda n : setattr(self, 'local_security_options_detect_application_installations_and_prompt_for_elevation', n.get_bool_value()),
            "localSecurityOptionsDisableAdministratorAccount": lambda n : setattr(self, 'local_security_options_disable_administrator_account', n.get_bool_value()),
            "localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees": lambda n : setattr(self, 'local_security_options_disable_client_digitally_sign_communications_if_server_agrees', n.get_bool_value()),
            "localSecurityOptionsDisableGuestAccount": lambda n : setattr(self, 'local_security_options_disable_guest_account', n.get_bool_value()),
            "localSecurityOptionsDisableServerDigitallySignCommunicationsAlways": lambda n : setattr(self, 'local_security_options_disable_server_digitally_sign_communications_always', n.get_bool_value()),
            "localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees": lambda n : setattr(self, 'local_security_options_disable_server_digitally_sign_communications_if_client_agrees', n.get_bool_value()),
            "localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts": lambda n : setattr(self, 'local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts', n.get_bool_value()),
            "localSecurityOptionsDoNotRequireCtrlAltDel": lambda n : setattr(self, 'local_security_options_do_not_require_ctrl_alt_del', n.get_bool_value()),
            "localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange": lambda n : setattr(self, 'local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change', n.get_bool_value()),
            "localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser": lambda n : setattr(self, 'local_security_options_format_and_eject_of_removable_media_allowed_user', n.get_enum_value(LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType)),
            "localSecurityOptionsGuestAccountName": lambda n : setattr(self, 'local_security_options_guest_account_name', n.get_str_value()),
            "localSecurityOptionsHideLastSignedInUser": lambda n : setattr(self, 'local_security_options_hide_last_signed_in_user', n.get_bool_value()),
            "localSecurityOptionsHideUsernameAtSignIn": lambda n : setattr(self, 'local_security_options_hide_username_at_sign_in', n.get_bool_value()),
            "localSecurityOptionsInformationDisplayedOnLockScreen": lambda n : setattr(self, 'local_security_options_information_displayed_on_lock_screen', n.get_enum_value(LocalSecurityOptionsInformationDisplayedOnLockScreenType)),
            "localSecurityOptionsInformationShownOnLockScreen": lambda n : setattr(self, 'local_security_options_information_shown_on_lock_screen', n.get_enum_value(LocalSecurityOptionsInformationShownOnLockScreenType)),
            "localSecurityOptionsLogOnMessageText": lambda n : setattr(self, 'local_security_options_log_on_message_text', n.get_str_value()),
            "localSecurityOptionsLogOnMessageTitle": lambda n : setattr(self, 'local_security_options_log_on_message_title', n.get_str_value()),
            "localSecurityOptionsMachineInactivityLimit": lambda n : setattr(self, 'local_security_options_machine_inactivity_limit', n.get_int_value()),
            "localSecurityOptionsMachineInactivityLimitInMinutes": lambda n : setattr(self, 'local_security_options_machine_inactivity_limit_in_minutes', n.get_int_value()),
            "localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients": lambda n : setattr(self, 'local_security_options_minimum_session_security_for_ntlm_ssp_based_clients', n.get_enum_value(LocalSecurityOptionsMinimumSessionSecurity)),
            "localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers": lambda n : setattr(self, 'local_security_options_minimum_session_security_for_ntlm_ssp_based_servers', n.get_enum_value(LocalSecurityOptionsMinimumSessionSecurity)),
            "localSecurityOptionsOnlyElevateSignedExecutables": lambda n : setattr(self, 'local_security_options_only_elevate_signed_executables', n.get_bool_value()),
            "localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares": lambda n : setattr(self, 'local_security_options_restrict_anonymous_access_to_named_pipes_and_shares', n.get_bool_value()),
            "localSecurityOptionsSmartCardRemovalBehavior": lambda n : setattr(self, 'local_security_options_smart_card_removal_behavior', n.get_enum_value(LocalSecurityOptionsSmartCardRemovalBehaviorType)),
            "localSecurityOptionsStandardUserElevationPromptBehavior": lambda n : setattr(self, 'local_security_options_standard_user_elevation_prompt_behavior', n.get_enum_value(LocalSecurityOptionsStandardUserElevationPromptBehaviorType)),
            "localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation": lambda n : setattr(self, 'local_security_options_switch_to_secure_desktop_when_prompting_for_elevation', n.get_bool_value()),
            "localSecurityOptionsUseAdminApprovalMode": lambda n : setattr(self, 'local_security_options_use_admin_approval_mode', n.get_bool_value()),
            "localSecurityOptionsUseAdminApprovalModeForAdministrators": lambda n : setattr(self, 'local_security_options_use_admin_approval_mode_for_administrators', n.get_bool_value()),
            "localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations": lambda n : setattr(self, 'local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations', n.get_bool_value()),
            "smartScreenBlockOverrideForFiles": lambda n : setattr(self, 'smart_screen_block_override_for_files', n.get_bool_value()),
            "smartScreenEnableInShell": lambda n : setattr(self, 'smart_screen_enable_in_shell', n.get_bool_value()),
            "userRightsAccessCredentialManagerAsTrustedCaller": lambda n : setattr(self, 'user_rights_access_credential_manager_as_trusted_caller', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsActAsPartOfTheOperatingSystem": lambda n : setattr(self, 'user_rights_act_as_part_of_the_operating_system', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsAllowAccessFromNetwork": lambda n : setattr(self, 'user_rights_allow_access_from_network', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsBackupData": lambda n : setattr(self, 'user_rights_backup_data', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsBlockAccessFromNetwork": lambda n : setattr(self, 'user_rights_block_access_from_network', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsChangeSystemTime": lambda n : setattr(self, 'user_rights_change_system_time', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsCreateGlobalObjects": lambda n : setattr(self, 'user_rights_create_global_objects', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsCreatePageFile": lambda n : setattr(self, 'user_rights_create_page_file', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsCreatePermanentSharedObjects": lambda n : setattr(self, 'user_rights_create_permanent_shared_objects', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsCreateSymbolicLinks": lambda n : setattr(self, 'user_rights_create_symbolic_links', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsCreateToken": lambda n : setattr(self, 'user_rights_create_token', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsDebugPrograms": lambda n : setattr(self, 'user_rights_debug_programs', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsDelegation": lambda n : setattr(self, 'user_rights_delegation', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsDenyLocalLogOn": lambda n : setattr(self, 'user_rights_deny_local_log_on', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsGenerateSecurityAudits": lambda n : setattr(self, 'user_rights_generate_security_audits', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsImpersonateClient": lambda n : setattr(self, 'user_rights_impersonate_client', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsIncreaseSchedulingPriority": lambda n : setattr(self, 'user_rights_increase_scheduling_priority', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsLoadUnloadDrivers": lambda n : setattr(self, 'user_rights_load_unload_drivers', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsLocalLogOn": lambda n : setattr(self, 'user_rights_local_log_on', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsLockMemory": lambda n : setattr(self, 'user_rights_lock_memory', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsManageAuditingAndSecurityLogs": lambda n : setattr(self, 'user_rights_manage_auditing_and_security_logs', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsManageVolumes": lambda n : setattr(self, 'user_rights_manage_volumes', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsModifyFirmwareEnvironment": lambda n : setattr(self, 'user_rights_modify_firmware_environment', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsModifyObjectLabels": lambda n : setattr(self, 'user_rights_modify_object_labels', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsProfileSingleProcess": lambda n : setattr(self, 'user_rights_profile_single_process', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsRemoteDesktopServicesLogOn": lambda n : setattr(self, 'user_rights_remote_desktop_services_log_on', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsRemoteShutdown": lambda n : setattr(self, 'user_rights_remote_shutdown', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsRestoreData": lambda n : setattr(self, 'user_rights_restore_data', n.get_object_value(DeviceManagementUserRightsSetting)),
            "userRightsTakeOwnership": lambda n : setattr(self, 'user_rights_take_ownership', n.get_object_value(DeviceManagementUserRightsSetting)),
            "windowsDefenderTamperProtection": lambda n : setattr(self, 'windows_defender_tamper_protection', n.get_enum_value(WindowsDefenderTamperProtectionOptions)),
            "xboxServicesAccessoryManagementServiceStartupMode": lambda n : setattr(self, 'xbox_services_accessory_management_service_startup_mode', n.get_enum_value(ServiceStartType)),
            "xboxServicesEnableXboxGameSaveTask": lambda n : setattr(self, 'xbox_services_enable_xbox_game_save_task', n.get_bool_value()),
            "xboxServicesLiveAuthManagerServiceStartupMode": lambda n : setattr(self, 'xbox_services_live_auth_manager_service_startup_mode', n.get_enum_value(ServiceStartType)),
            "xboxServicesLiveGameSaveServiceStartupMode": lambda n : setattr(self, 'xbox_services_live_game_save_service_startup_mode', n.get_enum_value(ServiceStartType)),
            "xboxServicesLiveNetworkingServiceStartupMode": lambda n : setattr(self, 'xbox_services_live_networking_service_startup_mode', n.get_enum_value(ServiceStartType)),
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
        writer.write_enum_value("appLockerApplicationControl", self.app_locker_application_control)
        writer.write_bool_value("applicationGuardAllowCameraMicrophoneRedirection", self.application_guard_allow_camera_microphone_redirection)
        writer.write_bool_value("applicationGuardAllowFileSaveOnHost", self.application_guard_allow_file_save_on_host)
        writer.write_bool_value("applicationGuardAllowPersistence", self.application_guard_allow_persistence)
        writer.write_bool_value("applicationGuardAllowPrintToLocalPrinters", self.application_guard_allow_print_to_local_printers)
        writer.write_bool_value("applicationGuardAllowPrintToNetworkPrinters", self.application_guard_allow_print_to_network_printers)
        writer.write_bool_value("applicationGuardAllowPrintToPDF", self.application_guard_allow_print_to_p_d_f)
        writer.write_bool_value("applicationGuardAllowPrintToXPS", self.application_guard_allow_print_to_x_p_s)
        writer.write_bool_value("applicationGuardAllowVirtualGPU", self.application_guard_allow_virtual_g_p_u)
        writer.write_enum_value("applicationGuardBlockClipboardSharing", self.application_guard_block_clipboard_sharing)
        writer.write_enum_value("applicationGuardBlockFileTransfer", self.application_guard_block_file_transfer)
        writer.write_bool_value("applicationGuardBlockNonEnterpriseContent", self.application_guard_block_non_enterprise_content)
        writer.write_collection_of_primitive_values("applicationGuardCertificateThumbprints", self.application_guard_certificate_thumbprints)
        writer.write_bool_value("applicationGuardEnabled", self.application_guard_enabled)
        writer.write_enum_value("applicationGuardEnabledOptions", self.application_guard_enabled_options)
        writer.write_bool_value("applicationGuardForceAuditing", self.application_guard_force_auditing)
        writer.write_bool_value("bitLockerAllowStandardUserEncryption", self.bit_locker_allow_standard_user_encryption)
        writer.write_bool_value("bitLockerDisableWarningForOtherDiskEncryption", self.bit_locker_disable_warning_for_other_disk_encryption)
        writer.write_bool_value("bitLockerEnableStorageCardEncryptionOnMobile", self.bit_locker_enable_storage_card_encryption_on_mobile)
        writer.write_bool_value("bitLockerEncryptDevice", self.bit_locker_encrypt_device)
        writer.write_object_value("bitLockerFixedDrivePolicy", self.bit_locker_fixed_drive_policy)
        writer.write_enum_value("bitLockerRecoveryPasswordRotation", self.bit_locker_recovery_password_rotation)
        writer.write_object_value("bitLockerRemovableDrivePolicy", self.bit_locker_removable_drive_policy)
        writer.write_object_value("bitLockerSystemDrivePolicy", self.bit_locker_system_drive_policy)
        writer.write_collection_of_primitive_values("defenderAdditionalGuardedFolders", self.defender_additional_guarded_folders)
        writer.write_enum_value("defenderAdobeReaderLaunchChildProcess", self.defender_adobe_reader_launch_child_process)
        writer.write_enum_value("defenderAdvancedRansomewareProtectionType", self.defender_advanced_ransomeware_protection_type)
        writer.write_bool_value("defenderAllowBehaviorMonitoring", self.defender_allow_behavior_monitoring)
        writer.write_bool_value("defenderAllowCloudProtection", self.defender_allow_cloud_protection)
        writer.write_bool_value("defenderAllowEndUserAccess", self.defender_allow_end_user_access)
        writer.write_bool_value("defenderAllowIntrusionPreventionSystem", self.defender_allow_intrusion_prevention_system)
        writer.write_bool_value("defenderAllowOnAccessProtection", self.defender_allow_on_access_protection)
        writer.write_bool_value("defenderAllowRealTimeMonitoring", self.defender_allow_real_time_monitoring)
        writer.write_bool_value("defenderAllowScanArchiveFiles", self.defender_allow_scan_archive_files)
        writer.write_bool_value("defenderAllowScanDownloads", self.defender_allow_scan_downloads)
        writer.write_bool_value("defenderAllowScanNetworkFiles", self.defender_allow_scan_network_files)
        writer.write_bool_value("defenderAllowScanRemovableDrivesDuringFullScan", self.defender_allow_scan_removable_drives_during_full_scan)
        writer.write_bool_value("defenderAllowScanScriptsLoadedInInternetExplorer", self.defender_allow_scan_scripts_loaded_in_internet_explorer)
        writer.write_collection_of_primitive_values("defenderAttackSurfaceReductionExcludedPaths", self.defender_attack_surface_reduction_excluded_paths)
        writer.write_bool_value("defenderBlockEndUserAccess", self.defender_block_end_user_access)
        writer.write_enum_value("defenderBlockPersistenceThroughWmiType", self.defender_block_persistence_through_wmi_type)
        writer.write_bool_value("defenderCheckForSignaturesBeforeRunningScan", self.defender_check_for_signatures_before_running_scan)
        writer.write_enum_value("defenderCloudBlockLevel", self.defender_cloud_block_level)
        writer.write_int_value("defenderCloudExtendedTimeoutInSeconds", self.defender_cloud_extended_timeout_in_seconds)
        writer.write_int_value("defenderDaysBeforeDeletingQuarantinedMalware", self.defender_days_before_deleting_quarantined_malware)
        writer.write_object_value("defenderDetectedMalwareActions", self.defender_detected_malware_actions)
        writer.write_bool_value("defenderDisableBehaviorMonitoring", self.defender_disable_behavior_monitoring)
        writer.write_bool_value("defenderDisableCatchupFullScan", self.defender_disable_catchup_full_scan)
        writer.write_bool_value("defenderDisableCatchupQuickScan", self.defender_disable_catchup_quick_scan)
        writer.write_bool_value("defenderDisableCloudProtection", self.defender_disable_cloud_protection)
        writer.write_bool_value("defenderDisableIntrusionPreventionSystem", self.defender_disable_intrusion_prevention_system)
        writer.write_bool_value("defenderDisableOnAccessProtection", self.defender_disable_on_access_protection)
        writer.write_bool_value("defenderDisableRealTimeMonitoring", self.defender_disable_real_time_monitoring)
        writer.write_bool_value("defenderDisableScanArchiveFiles", self.defender_disable_scan_archive_files)
        writer.write_bool_value("defenderDisableScanDownloads", self.defender_disable_scan_downloads)
        writer.write_bool_value("defenderDisableScanNetworkFiles", self.defender_disable_scan_network_files)
        writer.write_bool_value("defenderDisableScanRemovableDrivesDuringFullScan", self.defender_disable_scan_removable_drives_during_full_scan)
        writer.write_bool_value("defenderDisableScanScriptsLoadedInInternetExplorer", self.defender_disable_scan_scripts_loaded_in_internet_explorer)
        writer.write_enum_value("defenderEmailContentExecution", self.defender_email_content_execution)
        writer.write_enum_value("defenderEmailContentExecutionType", self.defender_email_content_execution_type)
        writer.write_bool_value("defenderEnableLowCpuPriority", self.defender_enable_low_cpu_priority)
        writer.write_bool_value("defenderEnableScanIncomingMail", self.defender_enable_scan_incoming_mail)
        writer.write_bool_value("defenderEnableScanMappedNetworkDrivesDuringFullScan", self.defender_enable_scan_mapped_network_drives_during_full_scan)
        writer.write_bytes_value("defenderExploitProtectionXml", self.defender_exploit_protection_xml)
        writer.write_str_value("defenderExploitProtectionXmlFileName", self.defender_exploit_protection_xml_file_name)
        writer.write_collection_of_primitive_values("defenderFileExtensionsToExclude", self.defender_file_extensions_to_exclude)
        writer.write_collection_of_primitive_values("defenderFilesAndFoldersToExclude", self.defender_files_and_folders_to_exclude)
        writer.write_enum_value("defenderGuardMyFoldersType", self.defender_guard_my_folders_type)
        writer.write_collection_of_primitive_values("defenderGuardedFoldersAllowedAppPaths", self.defender_guarded_folders_allowed_app_paths)
        writer.write_enum_value("defenderNetworkProtectionType", self.defender_network_protection_type)
        writer.write_enum_value("defenderOfficeAppsExecutableContentCreationOrLaunch", self.defender_office_apps_executable_content_creation_or_launch)
        writer.write_enum_value("defenderOfficeAppsExecutableContentCreationOrLaunchType", self.defender_office_apps_executable_content_creation_or_launch_type)
        writer.write_enum_value("defenderOfficeAppsLaunchChildProcess", self.defender_office_apps_launch_child_process)
        writer.write_enum_value("defenderOfficeAppsLaunchChildProcessType", self.defender_office_apps_launch_child_process_type)
        writer.write_enum_value("defenderOfficeAppsOtherProcessInjection", self.defender_office_apps_other_process_injection)
        writer.write_enum_value("defenderOfficeAppsOtherProcessInjectionType", self.defender_office_apps_other_process_injection_type)
        writer.write_enum_value("defenderOfficeCommunicationAppsLaunchChildProcess", self.defender_office_communication_apps_launch_child_process)
        writer.write_enum_value("defenderOfficeMacroCodeAllowWin32Imports", self.defender_office_macro_code_allow_win32_imports)
        writer.write_enum_value("defenderOfficeMacroCodeAllowWin32ImportsType", self.defender_office_macro_code_allow_win32_imports_type)
        writer.write_enum_value("defenderPotentiallyUnwantedAppAction", self.defender_potentially_unwanted_app_action)
        writer.write_enum_value("defenderPreventCredentialStealingType", self.defender_prevent_credential_stealing_type)
        writer.write_enum_value("defenderProcessCreation", self.defender_process_creation)
        writer.write_enum_value("defenderProcessCreationType", self.defender_process_creation_type)
        writer.write_collection_of_primitive_values("defenderProcessesToExclude", self.defender_processes_to_exclude)
        writer.write_enum_value("defenderScanDirection", self.defender_scan_direction)
        writer.write_int_value("defenderScanMaxCpuPercentage", self.defender_scan_max_cpu_percentage)
        writer.write_enum_value("defenderScanType", self.defender_scan_type)
        writer.write_time_value("defenderScheduledQuickScanTime", self.defender_scheduled_quick_scan_time)
        writer.write_enum_value("defenderScheduledScanDay", self.defender_scheduled_scan_day)
        writer.write_time_value("defenderScheduledScanTime", self.defender_scheduled_scan_time)
        writer.write_enum_value("defenderScriptDownloadedPayloadExecution", self.defender_script_downloaded_payload_execution)
        writer.write_enum_value("defenderScriptDownloadedPayloadExecutionType", self.defender_script_downloaded_payload_execution_type)
        writer.write_enum_value("defenderScriptObfuscatedMacroCode", self.defender_script_obfuscated_macro_code)
        writer.write_enum_value("defenderScriptObfuscatedMacroCodeType", self.defender_script_obfuscated_macro_code_type)
        writer.write_bool_value("defenderSecurityCenterBlockExploitProtectionOverride", self.defender_security_center_block_exploit_protection_override)
        writer.write_bool_value("defenderSecurityCenterDisableAccountUI", self.defender_security_center_disable_account_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableAppBrowserUI", self.defender_security_center_disable_app_browser_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableClearTpmUI", self.defender_security_center_disable_clear_tpm_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableFamilyUI", self.defender_security_center_disable_family_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableHardwareUI", self.defender_security_center_disable_hardware_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableHealthUI", self.defender_security_center_disable_health_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableNetworkUI", self.defender_security_center_disable_network_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableNotificationAreaUI", self.defender_security_center_disable_notification_area_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableRansomwareUI", self.defender_security_center_disable_ransomware_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableSecureBootUI", self.defender_security_center_disable_secure_boot_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableTroubleshootingUI", self.defender_security_center_disable_troubleshooting_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableVirusUI", self.defender_security_center_disable_virus_u_i)
        writer.write_bool_value("defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI", self.defender_security_center_disable_vulnerable_tpm_firmware_update_u_i)
        writer.write_str_value("defenderSecurityCenterHelpEmail", self.defender_security_center_help_email)
        writer.write_str_value("defenderSecurityCenterHelpPhone", self.defender_security_center_help_phone)
        writer.write_str_value("defenderSecurityCenterHelpURL", self.defender_security_center_help_u_r_l)
        writer.write_enum_value("defenderSecurityCenterITContactDisplay", self.defender_security_center_i_t_contact_display)
        writer.write_enum_value("defenderSecurityCenterNotificationsFromApp", self.defender_security_center_notifications_from_app)
        writer.write_str_value("defenderSecurityCenterOrganizationDisplayName", self.defender_security_center_organization_display_name)
        writer.write_int_value("defenderSignatureUpdateIntervalInHours", self.defender_signature_update_interval_in_hours)
        writer.write_enum_value("defenderSubmitSamplesConsentType", self.defender_submit_samples_consent_type)
        writer.write_enum_value("defenderUntrustedExecutable", self.defender_untrusted_executable)
        writer.write_enum_value("defenderUntrustedExecutableType", self.defender_untrusted_executable_type)
        writer.write_enum_value("defenderUntrustedUSBProcess", self.defender_untrusted_u_s_b_process)
        writer.write_enum_value("defenderUntrustedUSBProcessType", self.defender_untrusted_u_s_b_process_type)
        writer.write_bool_value("deviceGuardEnableSecureBootWithDMA", self.device_guard_enable_secure_boot_with_d_m_a)
        writer.write_bool_value("deviceGuardEnableVirtualizationBasedSecurity", self.device_guard_enable_virtualization_based_security)
        writer.write_enum_value("deviceGuardLaunchSystemGuard", self.device_guard_launch_system_guard)
        writer.write_enum_value("deviceGuardLocalSystemAuthorityCredentialGuardSettings", self.device_guard_local_system_authority_credential_guard_settings)
        writer.write_enum_value("deviceGuardSecureBootWithDMA", self.device_guard_secure_boot_with_d_m_a)
        writer.write_enum_value("dmaGuardDeviceEnumerationPolicy", self.dma_guard_device_enumeration_policy)
        writer.write_bool_value("firewallBlockStatefulFTP", self.firewall_block_stateful_f_t_p)
        writer.write_enum_value("firewallCertificateRevocationListCheckMethod", self.firewall_certificate_revocation_list_check_method)
        writer.write_bool_value("firewallIPSecExemptionsAllowDHCP", self.firewall_i_p_sec_exemptions_allow_d_h_c_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowICMP", self.firewall_i_p_sec_exemptions_allow_i_c_m_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowNeighborDiscovery", self.firewall_i_p_sec_exemptions_allow_neighbor_discovery)
        writer.write_bool_value("firewallIPSecExemptionsAllowRouterDiscovery", self.firewall_i_p_sec_exemptions_allow_router_discovery)
        writer.write_bool_value("firewallIPSecExemptionsNone", self.firewall_i_p_sec_exemptions_none)
        writer.write_int_value("firewallIdleTimeoutForSecurityAssociationInSeconds", self.firewall_idle_timeout_for_security_association_in_seconds)
        writer.write_bool_value("firewallMergeKeyingModuleSettings", self.firewall_merge_keying_module_settings)
        writer.write_enum_value("firewallPacketQueueingMethod", self.firewall_packet_queueing_method)
        writer.write_enum_value("firewallPreSharedKeyEncodingMethod", self.firewall_pre_shared_key_encoding_method)
        writer.write_object_value("firewallProfileDomain", self.firewall_profile_domain)
        writer.write_object_value("firewallProfilePrivate", self.firewall_profile_private)
        writer.write_object_value("firewallProfilePublic", self.firewall_profile_public)
        writer.write_collection_of_object_values("firewallRules", self.firewall_rules)
        writer.write_enum_value("lanManagerAuthenticationLevel", self.lan_manager_authentication_level)
        writer.write_bool_value("lanManagerWorkstationDisableInsecureGuestLogons", self.lan_manager_workstation_disable_insecure_guest_logons)
        writer.write_str_value("localSecurityOptionsAdministratorAccountName", self.local_security_options_administrator_account_name)
        writer.write_enum_value("localSecurityOptionsAdministratorElevationPromptBehavior", self.local_security_options_administrator_elevation_prompt_behavior)
        writer.write_bool_value("localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares", self.local_security_options_allow_anonymous_enumeration_of_s_a_m_accounts_and_shares)
        writer.write_bool_value("localSecurityOptionsAllowPKU2UAuthenticationRequests", self.local_security_options_allow_p_k_u2_u_authentication_requests)
        writer.write_str_value("localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager", self.local_security_options_allow_remote_calls_to_security_accounts_manager)
        writer.write_bool_value("localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool", self.local_security_options_allow_remote_calls_to_security_accounts_manager_helper_bool)
        writer.write_bool_value("localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn", self.local_security_options_allow_system_to_be_shut_down_without_having_to_log_on)
        writer.write_bool_value("localSecurityOptionsAllowUIAccessApplicationElevation", self.local_security_options_allow_u_i_access_application_elevation)
        writer.write_bool_value("localSecurityOptionsAllowUIAccessApplicationsForSecureLocations", self.local_security_options_allow_u_i_access_applications_for_secure_locations)
        writer.write_bool_value("localSecurityOptionsAllowUndockWithoutHavingToLogon", self.local_security_options_allow_undock_without_having_to_logon)
        writer.write_bool_value("localSecurityOptionsBlockMicrosoftAccounts", self.local_security_options_block_microsoft_accounts)
        writer.write_bool_value("localSecurityOptionsBlockRemoteLogonWithBlankPassword", self.local_security_options_block_remote_logon_with_blank_password)
        writer.write_bool_value("localSecurityOptionsBlockRemoteOpticalDriveAccess", self.local_security_options_block_remote_optical_drive_access)
        writer.write_bool_value("localSecurityOptionsBlockUsersInstallingPrinterDrivers", self.local_security_options_block_users_installing_printer_drivers)
        writer.write_bool_value("localSecurityOptionsClearVirtualMemoryPageFile", self.local_security_options_clear_virtual_memory_page_file)
        writer.write_bool_value("localSecurityOptionsClientDigitallySignCommunicationsAlways", self.local_security_options_client_digitally_sign_communications_always)
        writer.write_bool_value("localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers", self.local_security_options_client_send_unencrypted_password_to_third_party_s_m_b_servers)
        writer.write_bool_value("localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation", self.local_security_options_detect_application_installations_and_prompt_for_elevation)
        writer.write_bool_value("localSecurityOptionsDisableAdministratorAccount", self.local_security_options_disable_administrator_account)
        writer.write_bool_value("localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees", self.local_security_options_disable_client_digitally_sign_communications_if_server_agrees)
        writer.write_bool_value("localSecurityOptionsDisableGuestAccount", self.local_security_options_disable_guest_account)
        writer.write_bool_value("localSecurityOptionsDisableServerDigitallySignCommunicationsAlways", self.local_security_options_disable_server_digitally_sign_communications_always)
        writer.write_bool_value("localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees", self.local_security_options_disable_server_digitally_sign_communications_if_client_agrees)
        writer.write_bool_value("localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts", self.local_security_options_do_not_allow_anonymous_enumeration_of_s_a_m_accounts)
        writer.write_bool_value("localSecurityOptionsDoNotRequireCtrlAltDel", self.local_security_options_do_not_require_ctrl_alt_del)
        writer.write_bool_value("localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange", self.local_security_options_do_not_store_l_a_n_manager_hash_value_on_next_password_change)
        writer.write_enum_value("localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser", self.local_security_options_format_and_eject_of_removable_media_allowed_user)
        writer.write_str_value("localSecurityOptionsGuestAccountName", self.local_security_options_guest_account_name)
        writer.write_bool_value("localSecurityOptionsHideLastSignedInUser", self.local_security_options_hide_last_signed_in_user)
        writer.write_bool_value("localSecurityOptionsHideUsernameAtSignIn", self.local_security_options_hide_username_at_sign_in)
        writer.write_enum_value("localSecurityOptionsInformationDisplayedOnLockScreen", self.local_security_options_information_displayed_on_lock_screen)
        writer.write_enum_value("localSecurityOptionsInformationShownOnLockScreen", self.local_security_options_information_shown_on_lock_screen)
        writer.write_str_value("localSecurityOptionsLogOnMessageText", self.local_security_options_log_on_message_text)
        writer.write_str_value("localSecurityOptionsLogOnMessageTitle", self.local_security_options_log_on_message_title)
        writer.write_int_value("localSecurityOptionsMachineInactivityLimit", self.local_security_options_machine_inactivity_limit)
        writer.write_int_value("localSecurityOptionsMachineInactivityLimitInMinutes", self.local_security_options_machine_inactivity_limit_in_minutes)
        writer.write_enum_value("localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients", self.local_security_options_minimum_session_security_for_ntlm_ssp_based_clients)
        writer.write_enum_value("localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers", self.local_security_options_minimum_session_security_for_ntlm_ssp_based_servers)
        writer.write_bool_value("localSecurityOptionsOnlyElevateSignedExecutables", self.local_security_options_only_elevate_signed_executables)
        writer.write_bool_value("localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares", self.local_security_options_restrict_anonymous_access_to_named_pipes_and_shares)
        writer.write_enum_value("localSecurityOptionsSmartCardRemovalBehavior", self.local_security_options_smart_card_removal_behavior)
        writer.write_enum_value("localSecurityOptionsStandardUserElevationPromptBehavior", self.local_security_options_standard_user_elevation_prompt_behavior)
        writer.write_bool_value("localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation", self.local_security_options_switch_to_secure_desktop_when_prompting_for_elevation)
        writer.write_bool_value("localSecurityOptionsUseAdminApprovalMode", self.local_security_options_use_admin_approval_mode)
        writer.write_bool_value("localSecurityOptionsUseAdminApprovalModeForAdministrators", self.local_security_options_use_admin_approval_mode_for_administrators)
        writer.write_bool_value("localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations", self.local_security_options_virtualize_file_and_registry_write_failures_to_per_user_locations)
        writer.write_bool_value("smartScreenBlockOverrideForFiles", self.smart_screen_block_override_for_files)
        writer.write_bool_value("smartScreenEnableInShell", self.smart_screen_enable_in_shell)
        writer.write_object_value("userRightsAccessCredentialManagerAsTrustedCaller", self.user_rights_access_credential_manager_as_trusted_caller)
        writer.write_object_value("userRightsActAsPartOfTheOperatingSystem", self.user_rights_act_as_part_of_the_operating_system)
        writer.write_object_value("userRightsAllowAccessFromNetwork", self.user_rights_allow_access_from_network)
        writer.write_object_value("userRightsBackupData", self.user_rights_backup_data)
        writer.write_object_value("userRightsBlockAccessFromNetwork", self.user_rights_block_access_from_network)
        writer.write_object_value("userRightsChangeSystemTime", self.user_rights_change_system_time)
        writer.write_object_value("userRightsCreateGlobalObjects", self.user_rights_create_global_objects)
        writer.write_object_value("userRightsCreatePageFile", self.user_rights_create_page_file)
        writer.write_object_value("userRightsCreatePermanentSharedObjects", self.user_rights_create_permanent_shared_objects)
        writer.write_object_value("userRightsCreateSymbolicLinks", self.user_rights_create_symbolic_links)
        writer.write_object_value("userRightsCreateToken", self.user_rights_create_token)
        writer.write_object_value("userRightsDebugPrograms", self.user_rights_debug_programs)
        writer.write_object_value("userRightsDelegation", self.user_rights_delegation)
        writer.write_object_value("userRightsDenyLocalLogOn", self.user_rights_deny_local_log_on)
        writer.write_object_value("userRightsGenerateSecurityAudits", self.user_rights_generate_security_audits)
        writer.write_object_value("userRightsImpersonateClient", self.user_rights_impersonate_client)
        writer.write_object_value("userRightsIncreaseSchedulingPriority", self.user_rights_increase_scheduling_priority)
        writer.write_object_value("userRightsLoadUnloadDrivers", self.user_rights_load_unload_drivers)
        writer.write_object_value("userRightsLocalLogOn", self.user_rights_local_log_on)
        writer.write_object_value("userRightsLockMemory", self.user_rights_lock_memory)
        writer.write_object_value("userRightsManageAuditingAndSecurityLogs", self.user_rights_manage_auditing_and_security_logs)
        writer.write_object_value("userRightsManageVolumes", self.user_rights_manage_volumes)
        writer.write_object_value("userRightsModifyFirmwareEnvironment", self.user_rights_modify_firmware_environment)
        writer.write_object_value("userRightsModifyObjectLabels", self.user_rights_modify_object_labels)
        writer.write_object_value("userRightsProfileSingleProcess", self.user_rights_profile_single_process)
        writer.write_object_value("userRightsRemoteDesktopServicesLogOn", self.user_rights_remote_desktop_services_log_on)
        writer.write_object_value("userRightsRemoteShutdown", self.user_rights_remote_shutdown)
        writer.write_object_value("userRightsRestoreData", self.user_rights_restore_data)
        writer.write_object_value("userRightsTakeOwnership", self.user_rights_take_ownership)
        writer.write_enum_value("windowsDefenderTamperProtection", self.windows_defender_tamper_protection)
        writer.write_enum_value("xboxServicesAccessoryManagementServiceStartupMode", self.xbox_services_accessory_management_service_startup_mode)
        writer.write_bool_value("xboxServicesEnableXboxGameSaveTask", self.xbox_services_enable_xbox_game_save_task)
        writer.write_enum_value("xboxServicesLiveAuthManagerServiceStartupMode", self.xbox_services_live_auth_manager_service_startup_mode)
        writer.write_enum_value("xboxServicesLiveGameSaveServiceStartupMode", self.xbox_services_live_game_save_service_startup_mode)
        writer.write_enum_value("xboxServicesLiveNetworkingServiceStartupMode", self.xbox_services_live_networking_service_startup_mode)
    

