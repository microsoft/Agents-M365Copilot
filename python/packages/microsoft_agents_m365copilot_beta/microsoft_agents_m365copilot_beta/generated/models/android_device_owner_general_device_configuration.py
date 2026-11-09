from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_app_auto_update_policy_type import AndroidDeviceOwnerAppAutoUpdatePolicyType
    from .android_device_owner_battery_plugged_mode import AndroidDeviceOwnerBatteryPluggedMode
    from .android_device_owner_cross_profile_data_sharing import AndroidDeviceOwnerCrossProfileDataSharing
    from .android_device_owner_default_app_permission_policy_type import AndroidDeviceOwnerDefaultAppPermissionPolicyType
    from .android_device_owner_delegated_scope_app_setting import AndroidDeviceOwnerDelegatedScopeAppSetting
    from .android_device_owner_enrollment_profile_type import AndroidDeviceOwnerEnrollmentProfileType
    from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy
    from .android_device_owner_kiosk_customization_status_bar import AndroidDeviceOwnerKioskCustomizationStatusBar
    from .android_device_owner_kiosk_customization_system_navigation import AndroidDeviceOwnerKioskCustomizationSystemNavigation
    from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
    from .android_device_owner_kiosk_mode_app_position_item import AndroidDeviceOwnerKioskModeAppPositionItem
    from .android_device_owner_kiosk_mode_folder_icon import AndroidDeviceOwnerKioskModeFolderIcon
    from .android_device_owner_kiosk_mode_icon_size import AndroidDeviceOwnerKioskModeIconSize
    from .android_device_owner_kiosk_mode_managed_folder import AndroidDeviceOwnerKioskModeManagedFolder
    from .android_device_owner_kiosk_mode_screen_orientation import AndroidDeviceOwnerKioskModeScreenOrientation
    from .android_device_owner_location_mode import AndroidDeviceOwnerLocationMode
    from .android_device_owner_play_store_mode import AndroidDeviceOwnerPlayStoreMode
    from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
    from .android_device_owner_required_password_unlock import AndroidDeviceOwnerRequiredPasswordUnlock
    from .android_device_owner_system_update_freeze_period import AndroidDeviceOwnerSystemUpdateFreezePeriod
    from .android_device_owner_system_update_install_type import AndroidDeviceOwnerSystemUpdateInstallType
    from .android_device_owner_user_facing_message import AndroidDeviceOwnerUserFacingMessage
    from .android_device_owner_virtual_home_button_type import AndroidDeviceOwnerVirtualHomeButtonType
    from .android_keyguard_feature import AndroidKeyguardFeature
    from .app_list_item import AppListItem
    from .device_configuration import DeviceConfiguration
    from .kiosk_mode_managed_home_screen_pin_complexity import KioskModeManagedHomeScreenPinComplexity
    from .kiosk_mode_type import KioskModeType
    from .microsoft_launcher_dock_presence import MicrosoftLauncherDockPresence
    from .microsoft_launcher_search_bar_placement import MicrosoftLauncherSearchBarPlacement
    from .personal_profile_personal_play_store_mode import PersonalProfilePersonalPlayStoreMode

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidDeviceOwnerGeneralDeviceConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the androidDeviceOwnerGeneralDeviceConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration"
    # Indicates whether or not adding or removing accounts is disabled.
    accounts_block_modification: Optional[bool] = None
    # Specifies the list of managed apps with app details and its associated delegated scope(s). This collection can contain a maximum of 500 elements.
    android_device_owner_delegated_scope_app_settings: Optional[list[AndroidDeviceOwnerDelegatedScopeAppSetting]] = None
    # Indicates whether or not the user is allowed to enable to unknown sources setting.
    apps_allow_install_from_unknown_sources: Optional[bool] = None
    # Indicates the value of the app auto update policy. Possible values are: notConfigured, userChoice, never, wiFiOnly, always.
    apps_auto_update_policy: Optional[AndroidDeviceOwnerAppAutoUpdatePolicyType] = None
    # Indicates the permission policy for requests for runtime permissions if one is not defined for the app specifically. Possible values are: deviceDefault, prompt, autoGrant, autoDeny.
    apps_default_permission_policy: Optional[AndroidDeviceOwnerDefaultAppPermissionPolicyType] = None
    # Whether or not to recommend all apps skip any first-time-use hints they may have added.
    apps_recommend_skipping_first_use_hints: Optional[bool] = None
    # A list of managed apps that will have their data cleared during a global sign-out in AAD shared device mode. This collection can contain a maximum of 500 elements.
    azure_ad_shared_device_data_clear_apps: Optional[list[AppListItem]] = None
    # Indicates whether or not to block a user from configuring bluetooth.
    bluetooth_block_configuration: Optional[bool] = None
    # Indicates whether or not to block a user from sharing contacts via bluetooth.
    bluetooth_block_contact_sharing: Optional[bool] = None
    # Indicates whether or not to disable the use of the camera.
    camera_blocked: Optional[bool] = None
    # Indicates whether or not to block Wi-Fi tethering.
    cellular_block_wi_fi_tethering: Optional[bool] = None
    # Indicates whether or not to block users from any certificate credential configuration.
    certificate_credential_configuration_disabled: Optional[bool] = None
    # Indicates whether or not text copied from one profile (personal or work) can be pasted in the other.
    cross_profile_policies_allow_copy_paste: Optional[bool] = None
    # Indicates whether data from one profile (personal or work) can be shared with apps in the other profile. Possible values are: notConfigured, crossProfileDataSharingBlocked, dataSharingFromWorkToPersonalBlocked, crossProfileDataSharingAllowed, unkownFutureValue.
    cross_profile_policies_allow_data_sharing: Optional[AndroidDeviceOwnerCrossProfileDataSharing] = None
    # Indicates whether or not contacts stored in work profile are shown in personal profile contact searches/incoming calls.
    cross_profile_policies_show_work_contacts_in_personal_profile: Optional[bool] = None
    # Indicates whether or not to block a user from data roaming.
    data_roaming_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from manually changing the date or time on the device
    date_time_configuration_blocked: Optional[bool] = None
    # Represents the customized detailed help text provided to users when they attempt to modify managed settings on their device.
    detailed_help_text: Optional[AndroidDeviceOwnerUserFacingMessage] = None
    # Indicates the location setting configuration for fully managed devices (COBO) and corporate owned devices with a work profile (COPE). Possible values are: notConfigured, disabled, unknownFutureValue.
    device_location_mode: Optional[AndroidDeviceOwnerLocationMode] = None
    # Represents the customized lock screen message provided to users when they attempt to modify managed settings on their device.
    device_owner_lock_screen_message: Optional[AndroidDeviceOwnerUserFacingMessage] = None
    # Android Device Owner Enrollment Profile types.
    enrollment_profile: Optional[AndroidDeviceOwnerEnrollmentProfileType] = None
    # Indicates whether or not the factory reset option in settings is disabled.
    factory_reset_blocked: Optional[bool] = None
    # List of Google account emails that will be required to authenticate after a device is factory reset before it can be set up.
    factory_reset_device_administrator_emails: Optional[list[str]] = None
    # Proxy is set up directly with host, port and excluded hosts.
    global_proxy: Optional[AndroidDeviceOwnerGlobalProxy] = None
    # Indicates whether or not google accounts will be blocked.
    google_accounts_blocked: Optional[bool] = None
    # Exit code to allow a user to escape from Kiosk Mode when the device is in Kiosk Mode.
    is_kiosk_mode_exit_code_set: Optional[bool] = None
    # Indicates whether a user can access the device's Settings app while in Kiosk Mode.
    kiosk_customization_device_settings_blocked: Optional[bool] = None
    # Whether the power menu is shown when a user long presses the Power button of a device in Kiosk Mode.
    kiosk_customization_power_button_actions_blocked: Optional[bool] = None
    # Indicates whether system info and notifications are disabled in Kiosk Mode. Possible values are: notConfigured, notificationsAndSystemInfoEnabled, systemInfoOnly.
    kiosk_customization_status_bar: Optional[AndroidDeviceOwnerKioskCustomizationStatusBar] = None
    # Indicates whether system error dialogs for crashed or unresponsive apps are shown in Kiosk Mode.
    kiosk_customization_system_error_warnings: Optional[bool] = None
    # Indicates which navigation features are enabled in Kiosk Mode. Possible values are: notConfigured, navigationEnabled, homeButtonOnly.
    kiosk_customization_system_navigation: Optional[AndroidDeviceOwnerKioskCustomizationSystemNavigation] = None
    # Whether or not to enable app ordering in Kiosk Mode.
    kiosk_mode_app_order_enabled: Optional[bool] = None
    # The ordering of items on Kiosk Mode Managed Home Screen. This collection can contain a maximum of 500 elements.
    kiosk_mode_app_positions: Optional[list[AndroidDeviceOwnerKioskModeAppPositionItem]] = None
    # A list of managed apps that will be shown when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
    kiosk_mode_apps: Optional[list[AppListItem]] = None
    # Whether or not to alphabetize applications within a folder in Kiosk Mode.
    kiosk_mode_apps_in_folder_ordered_by_name: Optional[bool] = None
    # Whether or not to allow a user to configure Bluetooth settings in Kiosk Mode.
    kiosk_mode_bluetooth_configuration_enabled: Optional[bool] = None
    # Whether or not to allow a user to easy access to the debug menu in Kiosk Mode.
    kiosk_mode_debug_menu_easy_access_enabled: Optional[bool] = None
    # Exit code to allow a user to escape from Kiosk Mode when the device is in Kiosk Mode.
    kiosk_mode_exit_code: Optional[str] = None
    # Whether or not to allow a user to use the flashlight in Kiosk Mode.
    kiosk_mode_flashlight_configuration_enabled: Optional[bool] = None
    # Folder icon configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, darkSquare, darkCircle, lightSquare, lightCircle.
    kiosk_mode_folder_icon: Optional[AndroidDeviceOwnerKioskModeFolderIcon] = None
    # Number of rows for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
    kiosk_mode_grid_height: Optional[int] = None
    # Number of columns for Managed Home Screen grid with app ordering enabled in Kiosk Mode. Valid values 1 to 9999999
    kiosk_mode_grid_width: Optional[int] = None
    # Icon size configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, smallest, small, regular, large, largest.
    kiosk_mode_icon_size: Optional[AndroidDeviceOwnerKioskModeIconSize] = None
    # Whether or not to lock home screen to the end user in Kiosk Mode.
    kiosk_mode_lock_home_screen: Optional[bool] = None
    # A list of managed folders for a device in Kiosk Mode. This collection can contain a maximum of 500 elements.
    kiosk_mode_managed_folders: Optional[list[AndroidDeviceOwnerKioskModeManagedFolder]] = None
    # Indicates the list of managed applications and associated settings, which will be applied when android device is run on kiosk mode with Managed Home Screen. This collection can contain a maximum of 500 elements.
    kiosk_mode_managed_home_screen_app_settings: Optional[list[AndroidDeviceOwnerKioskModeApp]] = None
    # Whether or not to automatically sign-out of MHS and Shared device mode applications after inactive for Managed Home Screen.
    kiosk_mode_managed_home_screen_auto_signout: Optional[bool] = None
    # Number of seconds to give user notice before automatically signing them out for Managed Home Screen. Valid values 0 to 9999999
    kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds: Optional[int] = None
    # Number of seconds device is inactive before automatically signing user out for Managed Home Screen. Valid values 0 to 9999999
    kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds: Optional[int] = None
    # Complexity of PIN for sign-in session for Managed Home Screen. Possible values are: notConfigured, simple, complex.
    kiosk_mode_managed_home_screen_pin_complexity: Optional[KioskModeManagedHomeScreenPinComplexity] = None
    # Whether or not require user to set a PIN for sign-in session for Managed Home Screen.
    kiosk_mode_managed_home_screen_pin_required: Optional[bool] = None
    # Whether or not required user to enter session PIN if screensaver has appeared for Managed Home Screen.
    kiosk_mode_managed_home_screen_pin_required_to_resume: Optional[bool] = None
    # Custom URL background for sign-in screen for Managed Home Screen.
    kiosk_mode_managed_home_screen_sign_in_background: Optional[str] = None
    # Custom URL branding logo for sign-in screen and session pin page for Managed Home Screen.
    kiosk_mode_managed_home_screen_sign_in_branding_logo: Optional[str] = None
    # Whether or not show sign-in screen for Managed Home Screen.
    kiosk_mode_managed_home_screen_sign_in_enabled: Optional[bool] = None
    # Whether or not to display the Managed Settings entry point on the managed home screen in Kiosk Mode.
    kiosk_mode_managed_settings_entry_disabled: Optional[bool] = None
    # Whether or not to allow a user to change the media volume in Kiosk Mode.
    kiosk_mode_media_volume_configuration_enabled: Optional[bool] = None
    # Screen orientation configuration for managed home screen in Kiosk Mode. Possible values are: notConfigured, portrait, landscape, autoRotate.
    kiosk_mode_screen_orientation: Optional[AndroidDeviceOwnerKioskModeScreenOrientation] = None
    # Whether or not to enable screen saver mode or not in Kiosk Mode.
    kiosk_mode_screen_saver_configuration_enabled: Optional[bool] = None
    # Whether or not the device screen should show the screen saver if audio/video is playing in Kiosk Mode.
    kiosk_mode_screen_saver_detect_media_disabled: Optional[bool] = None
    # The number of seconds that the device will display the screen saver for in Kiosk Mode. Valid values 0 to 9999999
    kiosk_mode_screen_saver_display_time_in_seconds: Optional[int] = None
    # URL for an image that will be the device's screen saver in Kiosk Mode.
    kiosk_mode_screen_saver_image_url: Optional[str] = None
    # The number of seconds the device needs to be inactive for before the screen saver is shown in Kiosk Mode. Valid values 1 to 9999999
    kiosk_mode_screen_saver_start_delay_in_seconds: Optional[int] = None
    # Whether or not to display application notification badges in Kiosk Mode.
    kiosk_mode_show_app_notification_badge: Optional[bool] = None
    # Whether or not to allow a user to access basic device information.
    kiosk_mode_show_device_info: Optional[bool] = None
    # Whether or not to use single app kiosk mode or multi-app kiosk mode. Possible values are: notConfigured, singleAppMode, multiAppMode.
    kiosk_mode_use_managed_home_screen_app: Optional[KioskModeType] = None
    # Whether or not to display a virtual home button when the device is in Kiosk Mode.
    kiosk_mode_virtual_home_button_enabled: Optional[bool] = None
    # Indicates whether the virtual home button is a swipe up home button or a floating home button. Possible values are: notConfigured, swipeUp, floating.
    kiosk_mode_virtual_home_button_type: Optional[AndroidDeviceOwnerVirtualHomeButtonType] = None
    # URL to a publicly accessible image to use for the wallpaper when the device is in Kiosk Mode.
    kiosk_mode_wallpaper_url: Optional[str] = None
    # Whether or not to allow a user to configure Wi-Fi settings in Kiosk Mode.
    kiosk_mode_wi_fi_configuration_enabled: Optional[bool] = None
    # The restricted set of WIFI SSIDs available for the user to configure in Kiosk Mode. This collection can contain a maximum of 500 elements.
    kiosk_mode_wifi_allowed_ssids: Optional[list[str]] = None
    # Indicates whether or not LocateDevice for devices with lost mode (COBO, COPE) is enabled.
    locate_device_lost_mode_enabled: Optional[bool] = None
    # Indicates whether or not LocateDevice for userless (COSU) devices is disabled.
    locate_device_userless_disabled: Optional[bool] = None
    # Indicates whether or not to block unmuting the microphone on the device.
    microphone_force_mute: Optional[bool] = None
    # Indicates whether or not to you want configure Microsoft Launcher.
    microsoft_launcher_configuration_enabled: Optional[bool] = None
    # Indicates whether or not the user can modify the wallpaper to personalize their device.
    microsoft_launcher_custom_wallpaper_allow_user_modification: Optional[bool] = None
    # Indicates whether or not to configure the wallpaper on the targeted devices.
    microsoft_launcher_custom_wallpaper_enabled: Optional[bool] = None
    # Indicates the URL for the image file to use as the wallpaper on the targeted devices.
    microsoft_launcher_custom_wallpaper_image_url: Optional[str] = None
    # Indicates whether or not the user can modify the device dock configuration on the device.
    microsoft_launcher_dock_presence_allow_user_modification: Optional[bool] = None
    # Indicates whether or not you want to configure the device dock. Possible values are: notConfigured, show, hide, disabled.
    microsoft_launcher_dock_presence_configuration: Optional[MicrosoftLauncherDockPresence] = None
    # Indicates whether or not the user can modify the launcher feed on the device.
    microsoft_launcher_feed_allow_user_modification: Optional[bool] = None
    # Indicates whether or not you want to enable the launcher feed on the device.
    microsoft_launcher_feed_enabled: Optional[bool] = None
    # Indicates the search bar placement configuration on the device. Possible values are: notConfigured, top, bottom, hide.
    microsoft_launcher_search_bar_placement_configuration: Optional[MicrosoftLauncherSearchBarPlacement] = None
    # Indicates whether or not the device will allow connecting to a temporary network connection at boot time.
    network_escape_hatch_allowed: Optional[bool] = None
    # Indicates whether or not to block NFC outgoing beam.
    nfc_block_outgoing_beam: Optional[bool] = None
    # Indicates whether or not the keyguard is disabled.
    password_block_keyguard: Optional[bool] = None
    # List of device keyguard features to block. This collection can contain a maximum of 11 elements.
    password_block_keyguard_features: Optional[list[AndroidKeyguardFeature]] = None
    # Indicates the amount of time that a password can be set for before it expires and a new password will be required. Valid values 1 to 365
    password_expiration_days: Optional[int] = None
    # Indicates the minimum length of the password required on the device. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Indicates the minimum number of letter characters required for device password. Valid values 1 to 16
    password_minimum_letter_characters: Optional[int] = None
    # Indicates the minimum number of lower case characters required for device password. Valid values 1 to 16
    password_minimum_lower_case_characters: Optional[int] = None
    # Indicates the minimum number of non-letter characters required for device password. Valid values 1 to 16
    password_minimum_non_letter_characters: Optional[int] = None
    # Indicates the minimum number of numeric characters required for device password. Valid values 1 to 16
    password_minimum_numeric_characters: Optional[int] = None
    # Indicates the minimum number of symbol characters required for device password. Valid values 1 to 16
    password_minimum_symbol_characters: Optional[int] = None
    # Indicates the minimum number of upper case letter characters required for device password. Valid values 1 to 16
    password_minimum_upper_case_characters: Optional[int] = None
    # Minutes of inactivity before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Indicates the length of password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
    password_previous_password_count_to_block: Optional[int] = None
    # Indicates the timeout period after which a device must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
    password_require_unlock: Optional[AndroidDeviceOwnerRequiredPasswordUnlock] = None
    # Indicates the minimum password quality required on the device. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
    password_required_type: Optional[AndroidDeviceOwnerRequiredPasswordType] = None
    # Indicates the number of times a user can enter an incorrect password before the device is wiped. Valid values 4 to 11
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Indicates whether the user can install apps from unknown sources on the personal profile.
    personal_profile_apps_allow_install_from_unknown_sources: Optional[bool] = None
    # Indicates whether to disable the use of the camera on the personal profile.
    personal_profile_camera_blocked: Optional[bool] = None
    # Policy applied to applications in the personal profile. This collection can contain a maximum of 500 elements.
    personal_profile_personal_applications: Optional[list[AppListItem]] = None
    # Used together with PersonalProfilePersonalApplications to control how apps in the personal profile are allowed or blocked. Possible values are: notConfigured, blockedApps, allowedApps.
    personal_profile_play_store_mode: Optional[PersonalProfilePersonalPlayStoreMode] = None
    # Indicates whether to disable the capability to take screenshots on the personal profile.
    personal_profile_screen_capture_blocked: Optional[bool] = None
    # Indicates the Play Store mode of the device. Possible values are: notConfigured, allowList, blockList.
    play_store_mode: Optional[AndroidDeviceOwnerPlayStoreMode] = None
    # Indicates whether or not to disable the capability to take screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Represents the security common criteria mode enabled provided to users when they attempt to modify managed settings on their device.
    security_common_criteria_mode_enabled: Optional[bool] = None
    # Indicates whether or not the user is allowed to access developer settings like developer options and safe boot on the device.
    security_developer_settings_enabled: Optional[bool] = None
    # Indicates whether or not verify apps is required.
    security_require_verify_apps: Optional[bool] = None
    # Indicates whether or not location sharing is disabled for fully managed devices (COBO), and corporate owned devices with a work profile (COPE)
    share_device_location_disabled: Optional[bool] = None
    # Represents the customized short help text provided to users when they attempt to modify managed settings on their device.
    short_help_text: Optional[AndroidDeviceOwnerUserFacingMessage] = None
    # Indicates whether or the status bar is disabled, including notifications, quick settings and other screen overlays.
    status_bar_blocked: Optional[bool] = None
    # List of modes in which the device's display will stay powered-on. This collection can contain a maximum of 4 elements.
    stay_on_modes: Optional[list[AndroidDeviceOwnerBatteryPluggedMode]] = None
    # Indicates whether or not to allow USB mass storage.
    storage_allow_usb: Optional[bool] = None
    # Indicates whether or not to block external media.
    storage_block_external_media: Optional[bool] = None
    # Indicates whether or not to block USB file transfer.
    storage_block_usb_file_transfer: Optional[bool] = None
    # Indicates the annually repeating time periods during which system updates are postponed. This collection can contain a maximum of 500 elements.
    system_update_freeze_periods: Optional[list[AndroidDeviceOwnerSystemUpdateFreezePeriod]] = None
    # The type of system update configuration. Possible values are: deviceDefault, postpone, windowed, automatic.
    system_update_install_type: Optional[AndroidDeviceOwnerSystemUpdateInstallType] = None
    # Indicates the number of minutes after midnight that the system update window ends. Valid values 0 to 1440
    system_update_window_end_minutes_after_midnight: Optional[int] = None
    # Indicates the number of minutes after midnight that the system update window starts. Valid values 0 to 1440
    system_update_window_start_minutes_after_midnight: Optional[int] = None
    # Whether or not to block Android system prompt windows, like toasts, phone activities, and system alerts.
    system_windows_blocked: Optional[bool] = None
    # Indicates whether or not adding users and profiles is disabled.
    users_block_add: Optional[bool] = None
    # Indicates whether or not to disable removing other users from the device.
    users_block_remove: Optional[bool] = None
    # Indicates whether or not adjusting the master volume is disabled.
    volume_block_adjustment: Optional[bool] = None
    # If an always on VPN package name is specified, whether or not to lock network traffic when that VPN is disconnected.
    vpn_always_on_lockdown_mode: Optional[bool] = None
    # Android app package name for app that will handle an always-on VPN connection.
    vpn_always_on_package_identifier: Optional[str] = None
    # Indicates whether or not to block the user from editing the wifi connection settings.
    wifi_block_edit_configurations: Optional[bool] = None
    # Indicates whether or not to block the user from editing just the networks defined by the policy.
    wifi_block_edit_policy_defined_configurations: Optional[bool] = None
    # Indicates the number of days that a work profile password can be set before it expires and a new password will be required. Valid values 1 to 365
    work_profile_password_expiration_days: Optional[int] = None
    # Indicates the minimum length of the work profile password. Valid values 4 to 16
    work_profile_password_minimum_length: Optional[int] = None
    # Indicates the minimum number of letter characters required for the work profile password. Valid values 1 to 16
    work_profile_password_minimum_letter_characters: Optional[int] = None
    # Indicates the minimum number of lower-case characters required for the work profile password. Valid values 1 to 16
    work_profile_password_minimum_lower_case_characters: Optional[int] = None
    # Indicates the minimum number of non-letter characters required for the work profile password. Valid values 1 to 16
    work_profile_password_minimum_non_letter_characters: Optional[int] = None
    # Indicates the minimum number of numeric characters required for the work profile password. Valid values 1 to 16
    work_profile_password_minimum_numeric_characters: Optional[int] = None
    # Indicates the minimum number of symbol characters required for the work profile password. Valid values 1 to 16
    work_profile_password_minimum_symbol_characters: Optional[int] = None
    # Indicates the minimum number of upper-case letter characters required for the work profile password. Valid values 1 to 16
    work_profile_password_minimum_upper_case_characters: Optional[int] = None
    # Indicates the length of the work profile password history, where the user will not be able to enter a new password that is the same as any password in the history. Valid values 0 to 24
    work_profile_password_previous_password_count_to_block: Optional[int] = None
    # Indicates the timeout period after which a work profile must be unlocked using a form of strong authentication. Possible values are: deviceDefault, daily, unkownFutureValue.
    work_profile_password_require_unlock: Optional[AndroidDeviceOwnerRequiredPasswordUnlock] = None
    # Indicates the minimum password quality required on the work profile password. Possible values are: deviceDefault, required, numeric, numericComplex, alphabetic, alphanumeric, alphanumericWithSymbols, lowSecurityBiometric, customPassword.
    work_profile_password_required_type: Optional[AndroidDeviceOwnerRequiredPasswordType] = None
    # Indicates the number of times a user can enter an incorrect work profile password before the device is wiped. Valid values 4 to 11
    work_profile_password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_app_auto_update_policy_type import AndroidDeviceOwnerAppAutoUpdatePolicyType
        from .android_device_owner_battery_plugged_mode import AndroidDeviceOwnerBatteryPluggedMode
        from .android_device_owner_cross_profile_data_sharing import AndroidDeviceOwnerCrossProfileDataSharing
        from .android_device_owner_default_app_permission_policy_type import AndroidDeviceOwnerDefaultAppPermissionPolicyType
        from .android_device_owner_delegated_scope_app_setting import AndroidDeviceOwnerDelegatedScopeAppSetting
        from .android_device_owner_enrollment_profile_type import AndroidDeviceOwnerEnrollmentProfileType
        from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy
        from .android_device_owner_kiosk_customization_status_bar import AndroidDeviceOwnerKioskCustomizationStatusBar
        from .android_device_owner_kiosk_customization_system_navigation import AndroidDeviceOwnerKioskCustomizationSystemNavigation
        from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
        from .android_device_owner_kiosk_mode_app_position_item import AndroidDeviceOwnerKioskModeAppPositionItem
        from .android_device_owner_kiosk_mode_folder_icon import AndroidDeviceOwnerKioskModeFolderIcon
        from .android_device_owner_kiosk_mode_icon_size import AndroidDeviceOwnerKioskModeIconSize
        from .android_device_owner_kiosk_mode_managed_folder import AndroidDeviceOwnerKioskModeManagedFolder
        from .android_device_owner_kiosk_mode_screen_orientation import AndroidDeviceOwnerKioskModeScreenOrientation
        from .android_device_owner_location_mode import AndroidDeviceOwnerLocationMode
        from .android_device_owner_play_store_mode import AndroidDeviceOwnerPlayStoreMode
        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .android_device_owner_required_password_unlock import AndroidDeviceOwnerRequiredPasswordUnlock
        from .android_device_owner_system_update_freeze_period import AndroidDeviceOwnerSystemUpdateFreezePeriod
        from .android_device_owner_system_update_install_type import AndroidDeviceOwnerSystemUpdateInstallType
        from .android_device_owner_user_facing_message import AndroidDeviceOwnerUserFacingMessage
        from .android_device_owner_virtual_home_button_type import AndroidDeviceOwnerVirtualHomeButtonType
        from .android_keyguard_feature import AndroidKeyguardFeature
        from .app_list_item import AppListItem
        from .device_configuration import DeviceConfiguration
        from .kiosk_mode_managed_home_screen_pin_complexity import KioskModeManagedHomeScreenPinComplexity
        from .kiosk_mode_type import KioskModeType
        from .microsoft_launcher_dock_presence import MicrosoftLauncherDockPresence
        from .microsoft_launcher_search_bar_placement import MicrosoftLauncherSearchBarPlacement
        from .personal_profile_personal_play_store_mode import PersonalProfilePersonalPlayStoreMode

        from .android_device_owner_app_auto_update_policy_type import AndroidDeviceOwnerAppAutoUpdatePolicyType
        from .android_device_owner_battery_plugged_mode import AndroidDeviceOwnerBatteryPluggedMode
        from .android_device_owner_cross_profile_data_sharing import AndroidDeviceOwnerCrossProfileDataSharing
        from .android_device_owner_default_app_permission_policy_type import AndroidDeviceOwnerDefaultAppPermissionPolicyType
        from .android_device_owner_delegated_scope_app_setting import AndroidDeviceOwnerDelegatedScopeAppSetting
        from .android_device_owner_enrollment_profile_type import AndroidDeviceOwnerEnrollmentProfileType
        from .android_device_owner_global_proxy import AndroidDeviceOwnerGlobalProxy
        from .android_device_owner_kiosk_customization_status_bar import AndroidDeviceOwnerKioskCustomizationStatusBar
        from .android_device_owner_kiosk_customization_system_navigation import AndroidDeviceOwnerKioskCustomizationSystemNavigation
        from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
        from .android_device_owner_kiosk_mode_app_position_item import AndroidDeviceOwnerKioskModeAppPositionItem
        from .android_device_owner_kiosk_mode_folder_icon import AndroidDeviceOwnerKioskModeFolderIcon
        from .android_device_owner_kiosk_mode_icon_size import AndroidDeviceOwnerKioskModeIconSize
        from .android_device_owner_kiosk_mode_managed_folder import AndroidDeviceOwnerKioskModeManagedFolder
        from .android_device_owner_kiosk_mode_screen_orientation import AndroidDeviceOwnerKioskModeScreenOrientation
        from .android_device_owner_location_mode import AndroidDeviceOwnerLocationMode
        from .android_device_owner_play_store_mode import AndroidDeviceOwnerPlayStoreMode
        from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
        from .android_device_owner_required_password_unlock import AndroidDeviceOwnerRequiredPasswordUnlock
        from .android_device_owner_system_update_freeze_period import AndroidDeviceOwnerSystemUpdateFreezePeriod
        from .android_device_owner_system_update_install_type import AndroidDeviceOwnerSystemUpdateInstallType
        from .android_device_owner_user_facing_message import AndroidDeviceOwnerUserFacingMessage
        from .android_device_owner_virtual_home_button_type import AndroidDeviceOwnerVirtualHomeButtonType
        from .android_keyguard_feature import AndroidKeyguardFeature
        from .app_list_item import AppListItem
        from .device_configuration import DeviceConfiguration
        from .kiosk_mode_managed_home_screen_pin_complexity import KioskModeManagedHomeScreenPinComplexity
        from .kiosk_mode_type import KioskModeType
        from .microsoft_launcher_dock_presence import MicrosoftLauncherDockPresence
        from .microsoft_launcher_search_bar_placement import MicrosoftLauncherSearchBarPlacement
        from .personal_profile_personal_play_store_mode import PersonalProfilePersonalPlayStoreMode

        fields: dict[str, Callable[[Any], None]] = {
            "accountsBlockModification": lambda n : setattr(self, 'accounts_block_modification', n.get_bool_value()),
            "androidDeviceOwnerDelegatedScopeAppSettings": lambda n : setattr(self, 'android_device_owner_delegated_scope_app_settings', n.get_collection_of_object_values(AndroidDeviceOwnerDelegatedScopeAppSetting)),
            "appsAllowInstallFromUnknownSources": lambda n : setattr(self, 'apps_allow_install_from_unknown_sources', n.get_bool_value()),
            "appsAutoUpdatePolicy": lambda n : setattr(self, 'apps_auto_update_policy', n.get_enum_value(AndroidDeviceOwnerAppAutoUpdatePolicyType)),
            "appsDefaultPermissionPolicy": lambda n : setattr(self, 'apps_default_permission_policy', n.get_enum_value(AndroidDeviceOwnerDefaultAppPermissionPolicyType)),
            "appsRecommendSkippingFirstUseHints": lambda n : setattr(self, 'apps_recommend_skipping_first_use_hints', n.get_bool_value()),
            "azureAdSharedDeviceDataClearApps": lambda n : setattr(self, 'azure_ad_shared_device_data_clear_apps', n.get_collection_of_object_values(AppListItem)),
            "bluetoothBlockConfiguration": lambda n : setattr(self, 'bluetooth_block_configuration', n.get_bool_value()),
            "bluetoothBlockContactSharing": lambda n : setattr(self, 'bluetooth_block_contact_sharing', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellularBlockWiFiTethering": lambda n : setattr(self, 'cellular_block_wi_fi_tethering', n.get_bool_value()),
            "certificateCredentialConfigurationDisabled": lambda n : setattr(self, 'certificate_credential_configuration_disabled', n.get_bool_value()),
            "crossProfilePoliciesAllowCopyPaste": lambda n : setattr(self, 'cross_profile_policies_allow_copy_paste', n.get_bool_value()),
            "crossProfilePoliciesAllowDataSharing": lambda n : setattr(self, 'cross_profile_policies_allow_data_sharing', n.get_enum_value(AndroidDeviceOwnerCrossProfileDataSharing)),
            "crossProfilePoliciesShowWorkContactsInPersonalProfile": lambda n : setattr(self, 'cross_profile_policies_show_work_contacts_in_personal_profile', n.get_bool_value()),
            "dataRoamingBlocked": lambda n : setattr(self, 'data_roaming_blocked', n.get_bool_value()),
            "dateTimeConfigurationBlocked": lambda n : setattr(self, 'date_time_configuration_blocked', n.get_bool_value()),
            "detailedHelpText": lambda n : setattr(self, 'detailed_help_text', n.get_object_value(AndroidDeviceOwnerUserFacingMessage)),
            "deviceLocationMode": lambda n : setattr(self, 'device_location_mode', n.get_enum_value(AndroidDeviceOwnerLocationMode)),
            "deviceOwnerLockScreenMessage": lambda n : setattr(self, 'device_owner_lock_screen_message', n.get_object_value(AndroidDeviceOwnerUserFacingMessage)),
            "enrollmentProfile": lambda n : setattr(self, 'enrollment_profile', n.get_enum_value(AndroidDeviceOwnerEnrollmentProfileType)),
            "factoryResetBlocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "factoryResetDeviceAdministratorEmails": lambda n : setattr(self, 'factory_reset_device_administrator_emails', n.get_collection_of_primitive_values(str)),
            "globalProxy": lambda n : setattr(self, 'global_proxy', n.get_object_value(AndroidDeviceOwnerGlobalProxy)),
            "googleAccountsBlocked": lambda n : setattr(self, 'google_accounts_blocked', n.get_bool_value()),
            "isKioskModeExitCodeSet": lambda n : setattr(self, 'is_kiosk_mode_exit_code_set', n.get_bool_value()),
            "kioskCustomizationDeviceSettingsBlocked": lambda n : setattr(self, 'kiosk_customization_device_settings_blocked', n.get_bool_value()),
            "kioskCustomizationPowerButtonActionsBlocked": lambda n : setattr(self, 'kiosk_customization_power_button_actions_blocked', n.get_bool_value()),
            "kioskCustomizationStatusBar": lambda n : setattr(self, 'kiosk_customization_status_bar', n.get_enum_value(AndroidDeviceOwnerKioskCustomizationStatusBar)),
            "kioskCustomizationSystemErrorWarnings": lambda n : setattr(self, 'kiosk_customization_system_error_warnings', n.get_bool_value()),
            "kioskCustomizationSystemNavigation": lambda n : setattr(self, 'kiosk_customization_system_navigation', n.get_enum_value(AndroidDeviceOwnerKioskCustomizationSystemNavigation)),
            "kioskModeAppOrderEnabled": lambda n : setattr(self, 'kiosk_mode_app_order_enabled', n.get_bool_value()),
            "kioskModeAppPositions": lambda n : setattr(self, 'kiosk_mode_app_positions', n.get_collection_of_object_values(AndroidDeviceOwnerKioskModeAppPositionItem)),
            "kioskModeApps": lambda n : setattr(self, 'kiosk_mode_apps', n.get_collection_of_object_values(AppListItem)),
            "kioskModeAppsInFolderOrderedByName": lambda n : setattr(self, 'kiosk_mode_apps_in_folder_ordered_by_name', n.get_bool_value()),
            "kioskModeBluetoothConfigurationEnabled": lambda n : setattr(self, 'kiosk_mode_bluetooth_configuration_enabled', n.get_bool_value()),
            "kioskModeDebugMenuEasyAccessEnabled": lambda n : setattr(self, 'kiosk_mode_debug_menu_easy_access_enabled', n.get_bool_value()),
            "kioskModeExitCode": lambda n : setattr(self, 'kiosk_mode_exit_code', n.get_str_value()),
            "kioskModeFlashlightConfigurationEnabled": lambda n : setattr(self, 'kiosk_mode_flashlight_configuration_enabled', n.get_bool_value()),
            "kioskModeFolderIcon": lambda n : setattr(self, 'kiosk_mode_folder_icon', n.get_enum_value(AndroidDeviceOwnerKioskModeFolderIcon)),
            "kioskModeGridHeight": lambda n : setattr(self, 'kiosk_mode_grid_height', n.get_int_value()),
            "kioskModeGridWidth": lambda n : setattr(self, 'kiosk_mode_grid_width', n.get_int_value()),
            "kioskModeIconSize": lambda n : setattr(self, 'kiosk_mode_icon_size', n.get_enum_value(AndroidDeviceOwnerKioskModeIconSize)),
            "kioskModeLockHomeScreen": lambda n : setattr(self, 'kiosk_mode_lock_home_screen', n.get_bool_value()),
            "kioskModeManagedFolders": lambda n : setattr(self, 'kiosk_mode_managed_folders', n.get_collection_of_object_values(AndroidDeviceOwnerKioskModeManagedFolder)),
            "kioskModeManagedHomeScreenAppSettings": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_app_settings', n.get_collection_of_object_values(AndroidDeviceOwnerKioskModeApp)),
            "kioskModeManagedHomeScreenAutoSignout": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_auto_signout', n.get_bool_value()),
            "kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds', n.get_int_value()),
            "kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds', n.get_int_value()),
            "kioskModeManagedHomeScreenPinComplexity": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_pin_complexity', n.get_enum_value(KioskModeManagedHomeScreenPinComplexity)),
            "kioskModeManagedHomeScreenPinRequired": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_pin_required', n.get_bool_value()),
            "kioskModeManagedHomeScreenPinRequiredToResume": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_pin_required_to_resume', n.get_bool_value()),
            "kioskModeManagedHomeScreenSignInBackground": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_sign_in_background', n.get_str_value()),
            "kioskModeManagedHomeScreenSignInBrandingLogo": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_sign_in_branding_logo', n.get_str_value()),
            "kioskModeManagedHomeScreenSignInEnabled": lambda n : setattr(self, 'kiosk_mode_managed_home_screen_sign_in_enabled', n.get_bool_value()),
            "kioskModeManagedSettingsEntryDisabled": lambda n : setattr(self, 'kiosk_mode_managed_settings_entry_disabled', n.get_bool_value()),
            "kioskModeMediaVolumeConfigurationEnabled": lambda n : setattr(self, 'kiosk_mode_media_volume_configuration_enabled', n.get_bool_value()),
            "kioskModeScreenOrientation": lambda n : setattr(self, 'kiosk_mode_screen_orientation', n.get_enum_value(AndroidDeviceOwnerKioskModeScreenOrientation)),
            "kioskModeScreenSaverConfigurationEnabled": lambda n : setattr(self, 'kiosk_mode_screen_saver_configuration_enabled', n.get_bool_value()),
            "kioskModeScreenSaverDetectMediaDisabled": lambda n : setattr(self, 'kiosk_mode_screen_saver_detect_media_disabled', n.get_bool_value()),
            "kioskModeScreenSaverDisplayTimeInSeconds": lambda n : setattr(self, 'kiosk_mode_screen_saver_display_time_in_seconds', n.get_int_value()),
            "kioskModeScreenSaverImageUrl": lambda n : setattr(self, 'kiosk_mode_screen_saver_image_url', n.get_str_value()),
            "kioskModeScreenSaverStartDelayInSeconds": lambda n : setattr(self, 'kiosk_mode_screen_saver_start_delay_in_seconds', n.get_int_value()),
            "kioskModeShowAppNotificationBadge": lambda n : setattr(self, 'kiosk_mode_show_app_notification_badge', n.get_bool_value()),
            "kioskModeShowDeviceInfo": lambda n : setattr(self, 'kiosk_mode_show_device_info', n.get_bool_value()),
            "kioskModeUseManagedHomeScreenApp": lambda n : setattr(self, 'kiosk_mode_use_managed_home_screen_app', n.get_enum_value(KioskModeType)),
            "kioskModeVirtualHomeButtonEnabled": lambda n : setattr(self, 'kiosk_mode_virtual_home_button_enabled', n.get_bool_value()),
            "kioskModeVirtualHomeButtonType": lambda n : setattr(self, 'kiosk_mode_virtual_home_button_type', n.get_enum_value(AndroidDeviceOwnerVirtualHomeButtonType)),
            "kioskModeWallpaperUrl": lambda n : setattr(self, 'kiosk_mode_wallpaper_url', n.get_str_value()),
            "kioskModeWiFiConfigurationEnabled": lambda n : setattr(self, 'kiosk_mode_wi_fi_configuration_enabled', n.get_bool_value()),
            "kioskModeWifiAllowedSsids": lambda n : setattr(self, 'kiosk_mode_wifi_allowed_ssids', n.get_collection_of_primitive_values(str)),
            "locateDeviceLostModeEnabled": lambda n : setattr(self, 'locate_device_lost_mode_enabled', n.get_bool_value()),
            "locateDeviceUserlessDisabled": lambda n : setattr(self, 'locate_device_userless_disabled', n.get_bool_value()),
            "microphoneForceMute": lambda n : setattr(self, 'microphone_force_mute', n.get_bool_value()),
            "microsoftLauncherConfigurationEnabled": lambda n : setattr(self, 'microsoft_launcher_configuration_enabled', n.get_bool_value()),
            "microsoftLauncherCustomWallpaperAllowUserModification": lambda n : setattr(self, 'microsoft_launcher_custom_wallpaper_allow_user_modification', n.get_bool_value()),
            "microsoftLauncherCustomWallpaperEnabled": lambda n : setattr(self, 'microsoft_launcher_custom_wallpaper_enabled', n.get_bool_value()),
            "microsoftLauncherCustomWallpaperImageUrl": lambda n : setattr(self, 'microsoft_launcher_custom_wallpaper_image_url', n.get_str_value()),
            "microsoftLauncherDockPresenceAllowUserModification": lambda n : setattr(self, 'microsoft_launcher_dock_presence_allow_user_modification', n.get_bool_value()),
            "microsoftLauncherDockPresenceConfiguration": lambda n : setattr(self, 'microsoft_launcher_dock_presence_configuration', n.get_enum_value(MicrosoftLauncherDockPresence)),
            "microsoftLauncherFeedAllowUserModification": lambda n : setattr(self, 'microsoft_launcher_feed_allow_user_modification', n.get_bool_value()),
            "microsoftLauncherFeedEnabled": lambda n : setattr(self, 'microsoft_launcher_feed_enabled', n.get_bool_value()),
            "microsoftLauncherSearchBarPlacementConfiguration": lambda n : setattr(self, 'microsoft_launcher_search_bar_placement_configuration', n.get_enum_value(MicrosoftLauncherSearchBarPlacement)),
            "networkEscapeHatchAllowed": lambda n : setattr(self, 'network_escape_hatch_allowed', n.get_bool_value()),
            "nfcBlockOutgoingBeam": lambda n : setattr(self, 'nfc_block_outgoing_beam', n.get_bool_value()),
            "passwordBlockKeyguard": lambda n : setattr(self, 'password_block_keyguard', n.get_bool_value()),
            "passwordBlockKeyguardFeatures": lambda n : setattr(self, 'password_block_keyguard_features', n.get_collection_of_enum_values(AndroidKeyguardFeature)),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinimumLetterCharacters": lambda n : setattr(self, 'password_minimum_letter_characters', n.get_int_value()),
            "passwordMinimumLowerCaseCharacters": lambda n : setattr(self, 'password_minimum_lower_case_characters', n.get_int_value()),
            "passwordMinimumNonLetterCharacters": lambda n : setattr(self, 'password_minimum_non_letter_characters', n.get_int_value()),
            "passwordMinimumNumericCharacters": lambda n : setattr(self, 'password_minimum_numeric_characters', n.get_int_value()),
            "passwordMinimumSymbolCharacters": lambda n : setattr(self, 'password_minimum_symbol_characters', n.get_int_value()),
            "passwordMinimumUpperCaseCharacters": lambda n : setattr(self, 'password_minimum_upper_case_characters', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordCountToBlock": lambda n : setattr(self, 'password_previous_password_count_to_block', n.get_int_value()),
            "passwordRequireUnlock": lambda n : setattr(self, 'password_require_unlock', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordUnlock)),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "personalProfileAppsAllowInstallFromUnknownSources": lambda n : setattr(self, 'personal_profile_apps_allow_install_from_unknown_sources', n.get_bool_value()),
            "personalProfileCameraBlocked": lambda n : setattr(self, 'personal_profile_camera_blocked', n.get_bool_value()),
            "personalProfilePersonalApplications": lambda n : setattr(self, 'personal_profile_personal_applications', n.get_collection_of_object_values(AppListItem)),
            "personalProfilePlayStoreMode": lambda n : setattr(self, 'personal_profile_play_store_mode', n.get_enum_value(PersonalProfilePersonalPlayStoreMode)),
            "personalProfileScreenCaptureBlocked": lambda n : setattr(self, 'personal_profile_screen_capture_blocked', n.get_bool_value()),
            "playStoreMode": lambda n : setattr(self, 'play_store_mode', n.get_enum_value(AndroidDeviceOwnerPlayStoreMode)),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "securityCommonCriteriaModeEnabled": lambda n : setattr(self, 'security_common_criteria_mode_enabled', n.get_bool_value()),
            "securityDeveloperSettingsEnabled": lambda n : setattr(self, 'security_developer_settings_enabled', n.get_bool_value()),
            "securityRequireVerifyApps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "shareDeviceLocationDisabled": lambda n : setattr(self, 'share_device_location_disabled', n.get_bool_value()),
            "shortHelpText": lambda n : setattr(self, 'short_help_text', n.get_object_value(AndroidDeviceOwnerUserFacingMessage)),
            "statusBarBlocked": lambda n : setattr(self, 'status_bar_blocked', n.get_bool_value()),
            "stayOnModes": lambda n : setattr(self, 'stay_on_modes', n.get_collection_of_enum_values(AndroidDeviceOwnerBatteryPluggedMode)),
            "storageAllowUsb": lambda n : setattr(self, 'storage_allow_usb', n.get_bool_value()),
            "storageBlockExternalMedia": lambda n : setattr(self, 'storage_block_external_media', n.get_bool_value()),
            "storageBlockUsbFileTransfer": lambda n : setattr(self, 'storage_block_usb_file_transfer', n.get_bool_value()),
            "systemUpdateFreezePeriods": lambda n : setattr(self, 'system_update_freeze_periods', n.get_collection_of_object_values(AndroidDeviceOwnerSystemUpdateFreezePeriod)),
            "systemUpdateInstallType": lambda n : setattr(self, 'system_update_install_type', n.get_enum_value(AndroidDeviceOwnerSystemUpdateInstallType)),
            "systemUpdateWindowEndMinutesAfterMidnight": lambda n : setattr(self, 'system_update_window_end_minutes_after_midnight', n.get_int_value()),
            "systemUpdateWindowStartMinutesAfterMidnight": lambda n : setattr(self, 'system_update_window_start_minutes_after_midnight', n.get_int_value()),
            "systemWindowsBlocked": lambda n : setattr(self, 'system_windows_blocked', n.get_bool_value()),
            "usersBlockAdd": lambda n : setattr(self, 'users_block_add', n.get_bool_value()),
            "usersBlockRemove": lambda n : setattr(self, 'users_block_remove', n.get_bool_value()),
            "volumeBlockAdjustment": lambda n : setattr(self, 'volume_block_adjustment', n.get_bool_value()),
            "vpnAlwaysOnLockdownMode": lambda n : setattr(self, 'vpn_always_on_lockdown_mode', n.get_bool_value()),
            "vpnAlwaysOnPackageIdentifier": lambda n : setattr(self, 'vpn_always_on_package_identifier', n.get_str_value()),
            "wifiBlockEditConfigurations": lambda n : setattr(self, 'wifi_block_edit_configurations', n.get_bool_value()),
            "wifiBlockEditPolicyDefinedConfigurations": lambda n : setattr(self, 'wifi_block_edit_policy_defined_configurations', n.get_bool_value()),
            "workProfilePasswordExpirationDays": lambda n : setattr(self, 'work_profile_password_expiration_days', n.get_int_value()),
            "workProfilePasswordMinimumLength": lambda n : setattr(self, 'work_profile_password_minimum_length', n.get_int_value()),
            "workProfilePasswordMinimumLetterCharacters": lambda n : setattr(self, 'work_profile_password_minimum_letter_characters', n.get_int_value()),
            "workProfilePasswordMinimumLowerCaseCharacters": lambda n : setattr(self, 'work_profile_password_minimum_lower_case_characters', n.get_int_value()),
            "workProfilePasswordMinimumNonLetterCharacters": lambda n : setattr(self, 'work_profile_password_minimum_non_letter_characters', n.get_int_value()),
            "workProfilePasswordMinimumNumericCharacters": lambda n : setattr(self, 'work_profile_password_minimum_numeric_characters', n.get_int_value()),
            "workProfilePasswordMinimumSymbolCharacters": lambda n : setattr(self, 'work_profile_password_minimum_symbol_characters', n.get_int_value()),
            "workProfilePasswordMinimumUpperCaseCharacters": lambda n : setattr(self, 'work_profile_password_minimum_upper_case_characters', n.get_int_value()),
            "workProfilePasswordPreviousPasswordCountToBlock": lambda n : setattr(self, 'work_profile_password_previous_password_count_to_block', n.get_int_value()),
            "workProfilePasswordRequireUnlock": lambda n : setattr(self, 'work_profile_password_require_unlock', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordUnlock)),
            "workProfilePasswordRequiredType": lambda n : setattr(self, 'work_profile_password_required_type', n.get_enum_value(AndroidDeviceOwnerRequiredPasswordType)),
            "workProfilePasswordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'work_profile_password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
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
        writer.write_bool_value("accountsBlockModification", self.accounts_block_modification)
        writer.write_collection_of_object_values("androidDeviceOwnerDelegatedScopeAppSettings", self.android_device_owner_delegated_scope_app_settings)
        writer.write_bool_value("appsAllowInstallFromUnknownSources", self.apps_allow_install_from_unknown_sources)
        writer.write_enum_value("appsAutoUpdatePolicy", self.apps_auto_update_policy)
        writer.write_enum_value("appsDefaultPermissionPolicy", self.apps_default_permission_policy)
        writer.write_bool_value("appsRecommendSkippingFirstUseHints", self.apps_recommend_skipping_first_use_hints)
        writer.write_collection_of_object_values("azureAdSharedDeviceDataClearApps", self.azure_ad_shared_device_data_clear_apps)
        writer.write_bool_value("bluetoothBlockConfiguration", self.bluetooth_block_configuration)
        writer.write_bool_value("bluetoothBlockContactSharing", self.bluetooth_block_contact_sharing)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockWiFiTethering", self.cellular_block_wi_fi_tethering)
        writer.write_bool_value("certificateCredentialConfigurationDisabled", self.certificate_credential_configuration_disabled)
        writer.write_bool_value("crossProfilePoliciesAllowCopyPaste", self.cross_profile_policies_allow_copy_paste)
        writer.write_enum_value("crossProfilePoliciesAllowDataSharing", self.cross_profile_policies_allow_data_sharing)
        writer.write_bool_value("crossProfilePoliciesShowWorkContactsInPersonalProfile", self.cross_profile_policies_show_work_contacts_in_personal_profile)
        writer.write_bool_value("dataRoamingBlocked", self.data_roaming_blocked)
        writer.write_bool_value("dateTimeConfigurationBlocked", self.date_time_configuration_blocked)
        writer.write_object_value("detailedHelpText", self.detailed_help_text)
        writer.write_enum_value("deviceLocationMode", self.device_location_mode)
        writer.write_object_value("deviceOwnerLockScreenMessage", self.device_owner_lock_screen_message)
        writer.write_enum_value("enrollmentProfile", self.enrollment_profile)
        writer.write_bool_value("factoryResetBlocked", self.factory_reset_blocked)
        writer.write_collection_of_primitive_values("factoryResetDeviceAdministratorEmails", self.factory_reset_device_administrator_emails)
        writer.write_object_value("globalProxy", self.global_proxy)
        writer.write_bool_value("googleAccountsBlocked", self.google_accounts_blocked)
        writer.write_bool_value("isKioskModeExitCodeSet", self.is_kiosk_mode_exit_code_set)
        writer.write_bool_value("kioskCustomizationDeviceSettingsBlocked", self.kiosk_customization_device_settings_blocked)
        writer.write_bool_value("kioskCustomizationPowerButtonActionsBlocked", self.kiosk_customization_power_button_actions_blocked)
        writer.write_enum_value("kioskCustomizationStatusBar", self.kiosk_customization_status_bar)
        writer.write_bool_value("kioskCustomizationSystemErrorWarnings", self.kiosk_customization_system_error_warnings)
        writer.write_enum_value("kioskCustomizationSystemNavigation", self.kiosk_customization_system_navigation)
        writer.write_bool_value("kioskModeAppOrderEnabled", self.kiosk_mode_app_order_enabled)
        writer.write_collection_of_object_values("kioskModeAppPositions", self.kiosk_mode_app_positions)
        writer.write_collection_of_object_values("kioskModeApps", self.kiosk_mode_apps)
        writer.write_bool_value("kioskModeAppsInFolderOrderedByName", self.kiosk_mode_apps_in_folder_ordered_by_name)
        writer.write_bool_value("kioskModeBluetoothConfigurationEnabled", self.kiosk_mode_bluetooth_configuration_enabled)
        writer.write_bool_value("kioskModeDebugMenuEasyAccessEnabled", self.kiosk_mode_debug_menu_easy_access_enabled)
        writer.write_str_value("kioskModeExitCode", self.kiosk_mode_exit_code)
        writer.write_bool_value("kioskModeFlashlightConfigurationEnabled", self.kiosk_mode_flashlight_configuration_enabled)
        writer.write_enum_value("kioskModeFolderIcon", self.kiosk_mode_folder_icon)
        writer.write_int_value("kioskModeGridHeight", self.kiosk_mode_grid_height)
        writer.write_int_value("kioskModeGridWidth", self.kiosk_mode_grid_width)
        writer.write_enum_value("kioskModeIconSize", self.kiosk_mode_icon_size)
        writer.write_bool_value("kioskModeLockHomeScreen", self.kiosk_mode_lock_home_screen)
        writer.write_collection_of_object_values("kioskModeManagedFolders", self.kiosk_mode_managed_folders)
        writer.write_collection_of_object_values("kioskModeManagedHomeScreenAppSettings", self.kiosk_mode_managed_home_screen_app_settings)
        writer.write_bool_value("kioskModeManagedHomeScreenAutoSignout", self.kiosk_mode_managed_home_screen_auto_signout)
        writer.write_int_value("kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds", self.kiosk_mode_managed_home_screen_inactive_sign_out_delay_in_seconds)
        writer.write_int_value("kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds", self.kiosk_mode_managed_home_screen_inactive_sign_out_notice_in_seconds)
        writer.write_enum_value("kioskModeManagedHomeScreenPinComplexity", self.kiosk_mode_managed_home_screen_pin_complexity)
        writer.write_bool_value("kioskModeManagedHomeScreenPinRequired", self.kiosk_mode_managed_home_screen_pin_required)
        writer.write_bool_value("kioskModeManagedHomeScreenPinRequiredToResume", self.kiosk_mode_managed_home_screen_pin_required_to_resume)
        writer.write_str_value("kioskModeManagedHomeScreenSignInBackground", self.kiosk_mode_managed_home_screen_sign_in_background)
        writer.write_str_value("kioskModeManagedHomeScreenSignInBrandingLogo", self.kiosk_mode_managed_home_screen_sign_in_branding_logo)
        writer.write_bool_value("kioskModeManagedHomeScreenSignInEnabled", self.kiosk_mode_managed_home_screen_sign_in_enabled)
        writer.write_bool_value("kioskModeManagedSettingsEntryDisabled", self.kiosk_mode_managed_settings_entry_disabled)
        writer.write_bool_value("kioskModeMediaVolumeConfigurationEnabled", self.kiosk_mode_media_volume_configuration_enabled)
        writer.write_enum_value("kioskModeScreenOrientation", self.kiosk_mode_screen_orientation)
        writer.write_bool_value("kioskModeScreenSaverConfigurationEnabled", self.kiosk_mode_screen_saver_configuration_enabled)
        writer.write_bool_value("kioskModeScreenSaverDetectMediaDisabled", self.kiosk_mode_screen_saver_detect_media_disabled)
        writer.write_int_value("kioskModeScreenSaverDisplayTimeInSeconds", self.kiosk_mode_screen_saver_display_time_in_seconds)
        writer.write_str_value("kioskModeScreenSaverImageUrl", self.kiosk_mode_screen_saver_image_url)
        writer.write_int_value("kioskModeScreenSaverStartDelayInSeconds", self.kiosk_mode_screen_saver_start_delay_in_seconds)
        writer.write_bool_value("kioskModeShowAppNotificationBadge", self.kiosk_mode_show_app_notification_badge)
        writer.write_bool_value("kioskModeShowDeviceInfo", self.kiosk_mode_show_device_info)
        writer.write_enum_value("kioskModeUseManagedHomeScreenApp", self.kiosk_mode_use_managed_home_screen_app)
        writer.write_bool_value("kioskModeVirtualHomeButtonEnabled", self.kiosk_mode_virtual_home_button_enabled)
        writer.write_enum_value("kioskModeVirtualHomeButtonType", self.kiosk_mode_virtual_home_button_type)
        writer.write_str_value("kioskModeWallpaperUrl", self.kiosk_mode_wallpaper_url)
        writer.write_bool_value("kioskModeWiFiConfigurationEnabled", self.kiosk_mode_wi_fi_configuration_enabled)
        writer.write_collection_of_primitive_values("kioskModeWifiAllowedSsids", self.kiosk_mode_wifi_allowed_ssids)
        writer.write_bool_value("locateDeviceLostModeEnabled", self.locate_device_lost_mode_enabled)
        writer.write_bool_value("locateDeviceUserlessDisabled", self.locate_device_userless_disabled)
        writer.write_bool_value("microphoneForceMute", self.microphone_force_mute)
        writer.write_bool_value("microsoftLauncherConfigurationEnabled", self.microsoft_launcher_configuration_enabled)
        writer.write_bool_value("microsoftLauncherCustomWallpaperAllowUserModification", self.microsoft_launcher_custom_wallpaper_allow_user_modification)
        writer.write_bool_value("microsoftLauncherCustomWallpaperEnabled", self.microsoft_launcher_custom_wallpaper_enabled)
        writer.write_str_value("microsoftLauncherCustomWallpaperImageUrl", self.microsoft_launcher_custom_wallpaper_image_url)
        writer.write_bool_value("microsoftLauncherDockPresenceAllowUserModification", self.microsoft_launcher_dock_presence_allow_user_modification)
        writer.write_enum_value("microsoftLauncherDockPresenceConfiguration", self.microsoft_launcher_dock_presence_configuration)
        writer.write_bool_value("microsoftLauncherFeedAllowUserModification", self.microsoft_launcher_feed_allow_user_modification)
        writer.write_bool_value("microsoftLauncherFeedEnabled", self.microsoft_launcher_feed_enabled)
        writer.write_enum_value("microsoftLauncherSearchBarPlacementConfiguration", self.microsoft_launcher_search_bar_placement_configuration)
        writer.write_bool_value("networkEscapeHatchAllowed", self.network_escape_hatch_allowed)
        writer.write_bool_value("nfcBlockOutgoingBeam", self.nfc_block_outgoing_beam)
        writer.write_bool_value("passwordBlockKeyguard", self.password_block_keyguard)
        writer.write_collection_of_enum_values("passwordBlockKeyguardFeatures", self.password_block_keyguard_features)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinimumLetterCharacters", self.password_minimum_letter_characters)
        writer.write_int_value("passwordMinimumLowerCaseCharacters", self.password_minimum_lower_case_characters)
        writer.write_int_value("passwordMinimumNonLetterCharacters", self.password_minimum_non_letter_characters)
        writer.write_int_value("passwordMinimumNumericCharacters", self.password_minimum_numeric_characters)
        writer.write_int_value("passwordMinimumSymbolCharacters", self.password_minimum_symbol_characters)
        writer.write_int_value("passwordMinimumUpperCaseCharacters", self.password_minimum_upper_case_characters)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordCountToBlock", self.password_previous_password_count_to_block)
        writer.write_enum_value("passwordRequireUnlock", self.password_require_unlock)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("personalProfileAppsAllowInstallFromUnknownSources", self.personal_profile_apps_allow_install_from_unknown_sources)
        writer.write_bool_value("personalProfileCameraBlocked", self.personal_profile_camera_blocked)
        writer.write_collection_of_object_values("personalProfilePersonalApplications", self.personal_profile_personal_applications)
        writer.write_enum_value("personalProfilePlayStoreMode", self.personal_profile_play_store_mode)
        writer.write_bool_value("personalProfileScreenCaptureBlocked", self.personal_profile_screen_capture_blocked)
        writer.write_enum_value("playStoreMode", self.play_store_mode)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("securityCommonCriteriaModeEnabled", self.security_common_criteria_mode_enabled)
        writer.write_bool_value("securityDeveloperSettingsEnabled", self.security_developer_settings_enabled)
        writer.write_bool_value("securityRequireVerifyApps", self.security_require_verify_apps)
        writer.write_bool_value("shareDeviceLocationDisabled", self.share_device_location_disabled)
        writer.write_object_value("shortHelpText", self.short_help_text)
        writer.write_bool_value("statusBarBlocked", self.status_bar_blocked)
        writer.write_collection_of_enum_values("stayOnModes", self.stay_on_modes)
        writer.write_bool_value("storageAllowUsb", self.storage_allow_usb)
        writer.write_bool_value("storageBlockExternalMedia", self.storage_block_external_media)
        writer.write_bool_value("storageBlockUsbFileTransfer", self.storage_block_usb_file_transfer)
        writer.write_collection_of_object_values("systemUpdateFreezePeriods", self.system_update_freeze_periods)
        writer.write_enum_value("systemUpdateInstallType", self.system_update_install_type)
        writer.write_int_value("systemUpdateWindowEndMinutesAfterMidnight", self.system_update_window_end_minutes_after_midnight)
        writer.write_int_value("systemUpdateWindowStartMinutesAfterMidnight", self.system_update_window_start_minutes_after_midnight)
        writer.write_bool_value("systemWindowsBlocked", self.system_windows_blocked)
        writer.write_bool_value("usersBlockAdd", self.users_block_add)
        writer.write_bool_value("usersBlockRemove", self.users_block_remove)
        writer.write_bool_value("volumeBlockAdjustment", self.volume_block_adjustment)
        writer.write_bool_value("vpnAlwaysOnLockdownMode", self.vpn_always_on_lockdown_mode)
        writer.write_str_value("vpnAlwaysOnPackageIdentifier", self.vpn_always_on_package_identifier)
        writer.write_bool_value("wifiBlockEditConfigurations", self.wifi_block_edit_configurations)
        writer.write_bool_value("wifiBlockEditPolicyDefinedConfigurations", self.wifi_block_edit_policy_defined_configurations)
        writer.write_int_value("workProfilePasswordExpirationDays", self.work_profile_password_expiration_days)
        writer.write_int_value("workProfilePasswordMinimumLength", self.work_profile_password_minimum_length)
        writer.write_int_value("workProfilePasswordMinimumLetterCharacters", self.work_profile_password_minimum_letter_characters)
        writer.write_int_value("workProfilePasswordMinimumLowerCaseCharacters", self.work_profile_password_minimum_lower_case_characters)
        writer.write_int_value("workProfilePasswordMinimumNonLetterCharacters", self.work_profile_password_minimum_non_letter_characters)
        writer.write_int_value("workProfilePasswordMinimumNumericCharacters", self.work_profile_password_minimum_numeric_characters)
        writer.write_int_value("workProfilePasswordMinimumSymbolCharacters", self.work_profile_password_minimum_symbol_characters)
        writer.write_int_value("workProfilePasswordMinimumUpperCaseCharacters", self.work_profile_password_minimum_upper_case_characters)
        writer.write_int_value("workProfilePasswordPreviousPasswordCountToBlock", self.work_profile_password_previous_password_count_to_block)
        writer.write_enum_value("workProfilePasswordRequireUnlock", self.work_profile_password_require_unlock)
        writer.write_enum_value("workProfilePasswordRequiredType", self.work_profile_password_required_type)
        writer.write_int_value("workProfilePasswordSignInFailureCountBeforeFactoryReset", self.work_profile_password_sign_in_failure_count_before_factory_reset)
    

