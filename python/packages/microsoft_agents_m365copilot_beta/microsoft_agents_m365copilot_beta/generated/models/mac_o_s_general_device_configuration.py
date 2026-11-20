from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_list_item import AppListItem
    from .app_list_type import AppListType
    from .device_configuration import DeviceConfiguration
    from .mac_o_s_privacy_access_control_item import MacOSPrivacyAccessControlItem
    from .mac_o_s_software_update_delay_policy import MacOSSoftwareUpdateDelayPolicy
    from .required_password_type import RequiredPasswordType

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSGeneralDeviceConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the macOSGeneralDeviceConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSGeneralDeviceConfiguration"
    # When TRUE, activation lock is allowed when the devices is in the supervised mode. When FALSE, activation lock is not allowed. Default is false.
    activation_lock_when_supervised_allowed: Optional[bool] = None
    # Yes prevents users from adding friends to Game Center. Available for devices running macOS versions 10.13 and later.
    adding_game_center_friends_blocked: Optional[bool] = None
    # Indicates whether or not to allow AirDrop.
    air_drop_blocked: Optional[bool] = None
    # Indicates whether or to block users from unlocking their Mac with Apple Watch.
    apple_watch_block_auto_unlock: Optional[bool] = None
    # Indicates whether or not to block the user from accessing the camera of the device.
    camera_blocked: Optional[bool] = None
    # Indicates whether or not to allow remote screen observation by Classroom app. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
    classroom_app_block_remote_screen_observation: Optional[bool] = None
    # Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
    classroom_app_force_unprompted_screen_observation: Optional[bool] = None
    # Indicates whether or not to automatically give permission to the teacher's requests, without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
    classroom_force_automatically_join_classes: Optional[bool] = None
    # Indicates whether a student enrolled in an unmanaged course via Classroom will be required to request permission from the teacher when attempting to leave the course. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
    classroom_force_request_permission_to_leave_classes: Optional[bool] = None
    # Indicates whether or not to allow the teacher to lock apps or the device without prompting the student. Requires MDM enrollment via Apple School Manager or Apple Business Manager.
    classroom_force_unprompted_app_and_device_lock: Optional[bool] = None
    # Possible values of the compliance app list.
    compliant_app_list_type: Optional[AppListType] = None
    # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
    compliant_apps_list: Optional[list[AppListItem]] = None
    # Indicates whether or not to allow content caching.
    content_caching_blocked: Optional[bool] = None
    # Indicates whether or not to block definition lookup.
    definition_lookup_blocked: Optional[bool] = None
    # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
    email_in_domain_suffixes: Optional[list[str]] = None
    # TRUE disables the reset option on supervised devices. FALSE enables the reset option on supervised devices. Available for devices running macOS versions 12.0 and later.
    erase_content_and_settings_blocked: Optional[bool] = None
    # Yes disables Game Center, and the Game Center icon is removed from the Home screen. Available for devices running macOS versions 10.13 and later.
    game_center_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from continuing work that they started on a MacOS device on another iOS or MacOS device (MacOS 10.15 or later).
    i_cloud_block_activity_continuation: Optional[bool] = None
    # Indicates whether or not to block iCloud from syncing contacts.
    i_cloud_block_address_book: Optional[bool] = None
    # Indicates whether or not to block iCloud from syncing bookmarks.
    i_cloud_block_bookmarks: Optional[bool] = None
    # Indicates whether or not to block iCloud from syncing calendars.
    i_cloud_block_calendar: Optional[bool] = None
    # Indicates whether or not to block iCloud document sync.
    i_cloud_block_document_sync: Optional[bool] = None
    # Indicates whether or not to block iCloud from syncing mail.
    i_cloud_block_mail: Optional[bool] = None
    # Indicates whether or not to block iCloud from syncing notes.
    i_cloud_block_notes: Optional[bool] = None
    # Indicates whether or not to block iCloud Photo Library.
    i_cloud_block_photo_library: Optional[bool] = None
    # Indicates whether or not to block iCloud from syncing reminders.
    i_cloud_block_reminders: Optional[bool] = None
    # When TRUE the synchronization of cloud desktop and documents is blocked. When FALSE, synchronization of the cloud desktop and documents are allowed. Available for devices running macOS 10.12.4 and later.
    i_cloud_desktop_and_documents_blocked: Optional[bool] = None
    # iCloud private relay is an iCloud+ service that prevents networks and servers from monitoring a person's activity across the internet. By blocking iCloud private relay, Apple will not encrypt the traffic leaving the device. Available for devices running macOS 12 and later.
    i_cloud_private_relay_blocked: Optional[bool] = None
    # Indicates whether or not to block files from being transferred using iTunes.
    i_tunes_block_file_sharing: Optional[bool] = None
    # Indicates whether or not to block Music service and revert Music app to classic mode.
    i_tunes_block_music_service: Optional[bool] = None
    # Indicates whether or not to block the user from using dictation input.
    keyboard_block_dictation: Optional[bool] = None
    # Indicates whether or not iCloud keychain synchronization is blocked (macOS 10.12 and later).
    keychain_block_cloud_sync: Optional[bool] = None
    # TRUE prevents multiplayer gaming when using Game Center. FALSE allows multiplayer gaming when using Game Center. Available for devices running macOS versions 10.13 and later.
    multiplayer_gaming_blocked: Optional[bool] = None
    # Indicates whether or not to block sharing passwords with the AirDrop passwords feature.
    password_block_air_drop_sharing: Optional[bool] = None
    # Indicates whether or not to block the AutoFill Passwords feature.
    password_block_auto_fill: Optional[bool] = None
    # Indicates whether or not to block fingerprint unlock.
    password_block_fingerprint_unlock: Optional[bool] = None
    # Indicates whether or not to allow passcode modification.
    password_block_modification: Optional[bool] = None
    # Indicates whether or not to block requesting passwords from nearby devices.
    password_block_proximity_requests: Optional[bool] = None
    # Block simple passwords.
    password_block_simple: Optional[bool] = None
    # Number of days before the password expires.
    password_expiration_days: Optional[int] = None
    # The number of allowed failed attempts to enter the passcode at the device's lock screen. Valid values 2 to 11
    password_maximum_attempt_count: Optional[int] = None
    # Number of character sets a password must contain. Valid values 0 to 4
    password_minimum_character_set_count: Optional[int] = None
    # Minimum length of passwords.
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity required before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Minutes of inactivity required before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # The number of minutes before the login is reset after the maximum number of unsuccessful login attempts is reached.
    password_minutes_until_failed_login_reset: Optional[int] = None
    # Number of previous passwords to block.
    password_previous_password_block_count: Optional[int] = None
    # Whether or not to require a password.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # List of privacy preference policy controls. This collection can contain a maximum of 10000 elements.
    privacy_access_controls: Optional[list[MacOSPrivacyAccessControlItem]] = None
    # Indicates whether or not to block the user from using Auto fill in Safari.
    safari_block_autofill: Optional[bool] = None
    # Indicates whether or not to block the user from taking Screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Specify the number of days (1-90) to delay visibility of major OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
    software_update_major_o_s_deferred_install_delay_in_days: Optional[int] = None
    # Specify the number of days (1-90) to delay visibility of minor OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
    software_update_minor_o_s_deferred_install_delay_in_days: Optional[int] = None
    # Specify the number of days (1-90) to delay visibility of non-OS software updates. Available for devices running macOS versions 11.3 and later. Valid values 0 to 90
    software_update_non_o_s_deferred_install_delay_in_days: Optional[int] = None
    # Sets how many days a software update will be delyed for a supervised device. Valid values 0 to 90
    software_updates_enforced_delay_in_days: Optional[int] = None
    # Indicates whether or not to block Spotlight from returning any results from an Internet search.
    spotlight_block_internet_results: Optional[bool] = None
    # Maximum hours after which the user must enter their password to unlock the device instead of using Touch ID. Available for devices running macOS 12 and later. Valid values 0 to 2147483647
    touch_id_timeout_in_hours: Optional[int] = None
    # Determines whether to delay OS and/or app updates for macOS. Possible values are: none, delayOSUpdateVisibility, delayAppUpdateVisibility, unknownFutureValue, delayMajorOsUpdateVisibility.
    update_delay_policy: Optional[MacOSSoftwareUpdateDelayPolicy] = None
    # TRUE prevents the wallpaper from being changed. FALSE allows the wallpaper to be changed. Available for devices running macOS versions 10.13 and later.
    wallpaper_modification_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_privacy_access_control_item import MacOSPrivacyAccessControlItem
        from .mac_o_s_software_update_delay_policy import MacOSSoftwareUpdateDelayPolicy
        from .required_password_type import RequiredPasswordType

        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_privacy_access_control_item import MacOSPrivacyAccessControlItem
        from .mac_o_s_software_update_delay_policy import MacOSSoftwareUpdateDelayPolicy
        from .required_password_type import RequiredPasswordType

        fields: dict[str, Callable[[Any], None]] = {
            "activationLockWhenSupervisedAllowed": lambda n : setattr(self, 'activation_lock_when_supervised_allowed', n.get_bool_value()),
            "addingGameCenterFriendsBlocked": lambda n : setattr(self, 'adding_game_center_friends_blocked', n.get_bool_value()),
            "airDropBlocked": lambda n : setattr(self, 'air_drop_blocked', n.get_bool_value()),
            "appleWatchBlockAutoUnlock": lambda n : setattr(self, 'apple_watch_block_auto_unlock', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "classroomAppBlockRemoteScreenObservation": lambda n : setattr(self, 'classroom_app_block_remote_screen_observation', n.get_bool_value()),
            "classroomAppForceUnpromptedScreenObservation": lambda n : setattr(self, 'classroom_app_force_unprompted_screen_observation', n.get_bool_value()),
            "classroomForceAutomaticallyJoinClasses": lambda n : setattr(self, 'classroom_force_automatically_join_classes', n.get_bool_value()),
            "classroomForceRequestPermissionToLeaveClasses": lambda n : setattr(self, 'classroom_force_request_permission_to_leave_classes', n.get_bool_value()),
            "classroomForceUnpromptedAppAndDeviceLock": lambda n : setattr(self, 'classroom_force_unprompted_app_and_device_lock', n.get_bool_value()),
            "compliantAppListType": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(AppListType)),
            "compliantAppsList": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(AppListItem)),
            "contentCachingBlocked": lambda n : setattr(self, 'content_caching_blocked', n.get_bool_value()),
            "definitionLookupBlocked": lambda n : setattr(self, 'definition_lookup_blocked', n.get_bool_value()),
            "emailInDomainSuffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "eraseContentAndSettingsBlocked": lambda n : setattr(self, 'erase_content_and_settings_blocked', n.get_bool_value()),
            "gameCenterBlocked": lambda n : setattr(self, 'game_center_blocked', n.get_bool_value()),
            "iCloudBlockActivityContinuation": lambda n : setattr(self, 'i_cloud_block_activity_continuation', n.get_bool_value()),
            "iCloudBlockAddressBook": lambda n : setattr(self, 'i_cloud_block_address_book', n.get_bool_value()),
            "iCloudBlockBookmarks": lambda n : setattr(self, 'i_cloud_block_bookmarks', n.get_bool_value()),
            "iCloudBlockCalendar": lambda n : setattr(self, 'i_cloud_block_calendar', n.get_bool_value()),
            "iCloudBlockDocumentSync": lambda n : setattr(self, 'i_cloud_block_document_sync', n.get_bool_value()),
            "iCloudBlockMail": lambda n : setattr(self, 'i_cloud_block_mail', n.get_bool_value()),
            "iCloudBlockNotes": lambda n : setattr(self, 'i_cloud_block_notes', n.get_bool_value()),
            "iCloudBlockPhotoLibrary": lambda n : setattr(self, 'i_cloud_block_photo_library', n.get_bool_value()),
            "iCloudBlockReminders": lambda n : setattr(self, 'i_cloud_block_reminders', n.get_bool_value()),
            "iCloudDesktopAndDocumentsBlocked": lambda n : setattr(self, 'i_cloud_desktop_and_documents_blocked', n.get_bool_value()),
            "iCloudPrivateRelayBlocked": lambda n : setattr(self, 'i_cloud_private_relay_blocked', n.get_bool_value()),
            "iTunesBlockFileSharing": lambda n : setattr(self, 'i_tunes_block_file_sharing', n.get_bool_value()),
            "iTunesBlockMusicService": lambda n : setattr(self, 'i_tunes_block_music_service', n.get_bool_value()),
            "keyboardBlockDictation": lambda n : setattr(self, 'keyboard_block_dictation', n.get_bool_value()),
            "keychainBlockCloudSync": lambda n : setattr(self, 'keychain_block_cloud_sync', n.get_bool_value()),
            "multiplayerGamingBlocked": lambda n : setattr(self, 'multiplayer_gaming_blocked', n.get_bool_value()),
            "passwordBlockAirDropSharing": lambda n : setattr(self, 'password_block_air_drop_sharing', n.get_bool_value()),
            "passwordBlockAutoFill": lambda n : setattr(self, 'password_block_auto_fill', n.get_bool_value()),
            "passwordBlockFingerprintUnlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "passwordBlockModification": lambda n : setattr(self, 'password_block_modification', n.get_bool_value()),
            "passwordBlockProximityRequests": lambda n : setattr(self, 'password_block_proximity_requests', n.get_bool_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMaximumAttemptCount": lambda n : setattr(self, 'password_maximum_attempt_count', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordMinutesUntilFailedLoginReset": lambda n : setattr(self, 'password_minutes_until_failed_login_reset', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "privacyAccessControls": lambda n : setattr(self, 'privacy_access_controls', n.get_collection_of_object_values(MacOSPrivacyAccessControlItem)),
            "safariBlockAutofill": lambda n : setattr(self, 'safari_block_autofill', n.get_bool_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "softwareUpdateMajorOSDeferredInstallDelayInDays": lambda n : setattr(self, 'software_update_major_o_s_deferred_install_delay_in_days', n.get_int_value()),
            "softwareUpdateMinorOSDeferredInstallDelayInDays": lambda n : setattr(self, 'software_update_minor_o_s_deferred_install_delay_in_days', n.get_int_value()),
            "softwareUpdateNonOSDeferredInstallDelayInDays": lambda n : setattr(self, 'software_update_non_o_s_deferred_install_delay_in_days', n.get_int_value()),
            "softwareUpdatesEnforcedDelayInDays": lambda n : setattr(self, 'software_updates_enforced_delay_in_days', n.get_int_value()),
            "spotlightBlockInternetResults": lambda n : setattr(self, 'spotlight_block_internet_results', n.get_bool_value()),
            "touchIdTimeoutInHours": lambda n : setattr(self, 'touch_id_timeout_in_hours', n.get_int_value()),
            "updateDelayPolicy": lambda n : setattr(self, 'update_delay_policy', n.get_collection_of_enum_values(MacOSSoftwareUpdateDelayPolicy)),
            "wallpaperModificationBlocked": lambda n : setattr(self, 'wallpaper_modification_blocked', n.get_bool_value()),
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
        writer.write_bool_value("activationLockWhenSupervisedAllowed", self.activation_lock_when_supervised_allowed)
        writer.write_bool_value("addingGameCenterFriendsBlocked", self.adding_game_center_friends_blocked)
        writer.write_bool_value("airDropBlocked", self.air_drop_blocked)
        writer.write_bool_value("appleWatchBlockAutoUnlock", self.apple_watch_block_auto_unlock)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("classroomAppBlockRemoteScreenObservation", self.classroom_app_block_remote_screen_observation)
        writer.write_bool_value("classroomAppForceUnpromptedScreenObservation", self.classroom_app_force_unprompted_screen_observation)
        writer.write_bool_value("classroomForceAutomaticallyJoinClasses", self.classroom_force_automatically_join_classes)
        writer.write_bool_value("classroomForceRequestPermissionToLeaveClasses", self.classroom_force_request_permission_to_leave_classes)
        writer.write_bool_value("classroomForceUnpromptedAppAndDeviceLock", self.classroom_force_unprompted_app_and_device_lock)
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_bool_value("contentCachingBlocked", self.content_caching_blocked)
        writer.write_bool_value("definitionLookupBlocked", self.definition_lookup_blocked)
        writer.write_collection_of_primitive_values("emailInDomainSuffixes", self.email_in_domain_suffixes)
        writer.write_bool_value("eraseContentAndSettingsBlocked", self.erase_content_and_settings_blocked)
        writer.write_bool_value("gameCenterBlocked", self.game_center_blocked)
        writer.write_bool_value("iCloudBlockActivityContinuation", self.i_cloud_block_activity_continuation)
        writer.write_bool_value("iCloudBlockAddressBook", self.i_cloud_block_address_book)
        writer.write_bool_value("iCloudBlockBookmarks", self.i_cloud_block_bookmarks)
        writer.write_bool_value("iCloudBlockCalendar", self.i_cloud_block_calendar)
        writer.write_bool_value("iCloudBlockDocumentSync", self.i_cloud_block_document_sync)
        writer.write_bool_value("iCloudBlockMail", self.i_cloud_block_mail)
        writer.write_bool_value("iCloudBlockNotes", self.i_cloud_block_notes)
        writer.write_bool_value("iCloudBlockPhotoLibrary", self.i_cloud_block_photo_library)
        writer.write_bool_value("iCloudBlockReminders", self.i_cloud_block_reminders)
        writer.write_bool_value("iCloudDesktopAndDocumentsBlocked", self.i_cloud_desktop_and_documents_blocked)
        writer.write_bool_value("iCloudPrivateRelayBlocked", self.i_cloud_private_relay_blocked)
        writer.write_bool_value("iTunesBlockFileSharing", self.i_tunes_block_file_sharing)
        writer.write_bool_value("iTunesBlockMusicService", self.i_tunes_block_music_service)
        writer.write_bool_value("keyboardBlockDictation", self.keyboard_block_dictation)
        writer.write_bool_value("keychainBlockCloudSync", self.keychain_block_cloud_sync)
        writer.write_bool_value("multiplayerGamingBlocked", self.multiplayer_gaming_blocked)
        writer.write_bool_value("passwordBlockAirDropSharing", self.password_block_air_drop_sharing)
        writer.write_bool_value("passwordBlockAutoFill", self.password_block_auto_fill)
        writer.write_bool_value("passwordBlockFingerprintUnlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("passwordBlockModification", self.password_block_modification)
        writer.write_bool_value("passwordBlockProximityRequests", self.password_block_proximity_requests)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMaximumAttemptCount", self.password_maximum_attempt_count)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordMinutesUntilFailedLoginReset", self.password_minutes_until_failed_login_reset)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_collection_of_object_values("privacyAccessControls", self.privacy_access_controls)
        writer.write_bool_value("safariBlockAutofill", self.safari_block_autofill)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_int_value("softwareUpdateMajorOSDeferredInstallDelayInDays", self.software_update_major_o_s_deferred_install_delay_in_days)
        writer.write_int_value("softwareUpdateMinorOSDeferredInstallDelayInDays", self.software_update_minor_o_s_deferred_install_delay_in_days)
        writer.write_int_value("softwareUpdateNonOSDeferredInstallDelayInDays", self.software_update_non_o_s_deferred_install_delay_in_days)
        writer.write_int_value("softwareUpdatesEnforcedDelayInDays", self.software_updates_enforced_delay_in_days)
        writer.write_bool_value("spotlightBlockInternetResults", self.spotlight_block_internet_results)
        writer.write_int_value("touchIdTimeoutInHours", self.touch_id_timeout_in_hours)
        writer.write_enum_value("updateDelayPolicy", self.update_delay_policy)
        writer.write_bool_value("wallpaperModificationBlocked", self.wallpaper_modification_blocked)
    

