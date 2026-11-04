from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
    from .i_tunes_pairing_mode import ITunesPairingMode
    from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

from .dep_enrollment_base_profile import DepEnrollmentBaseProfile

@dataclass
class DepIOSEnrollmentProfile(DepEnrollmentBaseProfile, Parsable):
    """
    The DepIOSEnrollmentProfile resource represents an Apple Device Enrollment Program (DEP) enrollment profile specific to iOS configuration. This type of profile must be assigned to Apple DEP serial numbers before the corresponding devices can enroll via DEP.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.depIOSEnrollmentProfile"
    # Indicates if Apperance screen is disabled
    appearance_screen_disabled: Optional[bool] = None
    # Indicates if the device will need to wait for configured confirmation
    await_device_configured_confirmation: Optional[bool] = None
    # Carrier URL for activating device eSIM.
    carrier_activation_url: Optional[str] = None
    # If set, indicates which Vpp token should be used to deploy the Company Portal w/ device licensing. 'enableAuthenticationViaCompanyPortal' must be set in order for this property to be set.
    company_portal_vpp_token_id: Optional[str] = None
    # Indicates if Device To Device Migration is disabled
    device_to_device_migration_disabled: Optional[bool] = None
    # This indicates whether the device is to be enrolled in a mode which enables multi user scenarios. Only applicable in shared iPads.
    enable_shared_i_pad: Optional[bool] = None
    # Tells the device to enable single app mode and apply app-lock during enrollment. Default is false. 'enableAuthenticationViaCompanyPortal' and 'companyPortalVppTokenId' must be set for this property to be set.
    enable_single_app_enrollment_mode: Optional[bool] = None
    # Indicates if Express Language screen is disabled
    express_language_screen_disabled: Optional[bool] = None
    # Indicates if temporary sessions is enabled
    force_temporary_session: Optional[bool] = None
    # Indicates if home button sensitivity screen is disabled
    home_button_screen_disabled: Optional[bool] = None
    # Indicates if iMessage and FaceTime screen is disabled
    i_message_and_face_time_screen_disabled: Optional[bool] = None
    # The iTunesPairingMode property
    i_tunes_pairing_mode: Optional[ITunesPairingMode] = None
    # Management certificates for Apple Configurator
    management_certificates: Optional[list[ManagementCertificateWithThumbprint]] = None
    # Indicates if onboarding setup screen is disabled
    on_boarding_screen_disabled: Optional[bool] = None
    # Indicates if Passcode setup pane is disabled
    pass_code_disabled: Optional[bool] = None
    # Indicates timeout before locked screen requires the user to enter the device passocde to unlock it
    passcode_lock_grace_period_in_seconds: Optional[int] = None
    # Indicates if Preferred language screen is disabled
    preferred_language_screen_disabled: Optional[bool] = None
    # Indicates if Weclome screen is disabled
    restore_completed_screen_disabled: Optional[bool] = None
    # Indicates if Restore from Android is disabled
    restore_from_android_disabled: Optional[bool] = None
    # This specifies the maximum number of users that can use a shared iPad. Only applicable in shared iPad mode.
    shared_i_pad_maximum_user_count: Optional[int] = None
    # Indicates if the SIMSetup screen is disabled
    sim_setup_screen_disabled: Optional[bool] = None
    # Indicates if the mandatory sofware update screen is disabled
    software_update_screen_disabled: Optional[bool] = None
    # Indicates timeout of temporary session
    temporary_session_timeout_in_seconds: Optional[int] = None
    # Indicates if Weclome screen is disabled
    update_complete_screen_disabled: Optional[bool] = None
    # Indicates timeout of temporary session
    user_session_timeout_in_seconds: Optional[int] = None
    # Indicates that this apple device is designated to support 'shared device mode' scenarios. This is distinct from the 'shared iPad' scenario. See https://learn.microsoft.com/mem/intune/enrollment/device-enrollment-shared-ios
    userless_shared_aad_mode_enabled: Optional[bool] = None
    # Indicates if the watch migration screen is disabled
    watch_migration_screen_disabled: Optional[bool] = None
    # Indicates if Weclome screen is disabled
    welcome_screen_disabled: Optional[bool] = None
    # Indicates if zoom setup pane is disabled
    zoom_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepIOSEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepIOSEnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepIOSEnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .i_tunes_pairing_mode import ITunesPairingMode
        from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .i_tunes_pairing_mode import ITunesPairingMode
        from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

        fields: dict[str, Callable[[Any], None]] = {
            "appearanceScreenDisabled": lambda n : setattr(self, 'appearance_screen_disabled', n.get_bool_value()),
            "awaitDeviceConfiguredConfirmation": lambda n : setattr(self, 'await_device_configured_confirmation', n.get_bool_value()),
            "carrierActivationUrl": lambda n : setattr(self, 'carrier_activation_url', n.get_str_value()),
            "companyPortalVppTokenId": lambda n : setattr(self, 'company_portal_vpp_token_id', n.get_str_value()),
            "deviceToDeviceMigrationDisabled": lambda n : setattr(self, 'device_to_device_migration_disabled', n.get_bool_value()),
            "enableSharedIPad": lambda n : setattr(self, 'enable_shared_i_pad', n.get_bool_value()),
            "enableSingleAppEnrollmentMode": lambda n : setattr(self, 'enable_single_app_enrollment_mode', n.get_bool_value()),
            "expressLanguageScreenDisabled": lambda n : setattr(self, 'express_language_screen_disabled', n.get_bool_value()),
            "forceTemporarySession": lambda n : setattr(self, 'force_temporary_session', n.get_bool_value()),
            "homeButtonScreenDisabled": lambda n : setattr(self, 'home_button_screen_disabled', n.get_bool_value()),
            "iMessageAndFaceTimeScreenDisabled": lambda n : setattr(self, 'i_message_and_face_time_screen_disabled', n.get_bool_value()),
            "iTunesPairingMode": lambda n : setattr(self, 'i_tunes_pairing_mode', n.get_enum_value(ITunesPairingMode)),
            "managementCertificates": lambda n : setattr(self, 'management_certificates', n.get_collection_of_object_values(ManagementCertificateWithThumbprint)),
            "onBoardingScreenDisabled": lambda n : setattr(self, 'on_boarding_screen_disabled', n.get_bool_value()),
            "passCodeDisabled": lambda n : setattr(self, 'pass_code_disabled', n.get_bool_value()),
            "passcodeLockGracePeriodInSeconds": lambda n : setattr(self, 'passcode_lock_grace_period_in_seconds', n.get_int_value()),
            "preferredLanguageScreenDisabled": lambda n : setattr(self, 'preferred_language_screen_disabled', n.get_bool_value()),
            "restoreCompletedScreenDisabled": lambda n : setattr(self, 'restore_completed_screen_disabled', n.get_bool_value()),
            "restoreFromAndroidDisabled": lambda n : setattr(self, 'restore_from_android_disabled', n.get_bool_value()),
            "sharedIPadMaximumUserCount": lambda n : setattr(self, 'shared_i_pad_maximum_user_count', n.get_int_value()),
            "simSetupScreenDisabled": lambda n : setattr(self, 'sim_setup_screen_disabled', n.get_bool_value()),
            "softwareUpdateScreenDisabled": lambda n : setattr(self, 'software_update_screen_disabled', n.get_bool_value()),
            "temporarySessionTimeoutInSeconds": lambda n : setattr(self, 'temporary_session_timeout_in_seconds', n.get_int_value()),
            "updateCompleteScreenDisabled": lambda n : setattr(self, 'update_complete_screen_disabled', n.get_bool_value()),
            "userSessionTimeoutInSeconds": lambda n : setattr(self, 'user_session_timeout_in_seconds', n.get_int_value()),
            "userlessSharedAadModeEnabled": lambda n : setattr(self, 'userless_shared_aad_mode_enabled', n.get_bool_value()),
            "watchMigrationScreenDisabled": lambda n : setattr(self, 'watch_migration_screen_disabled', n.get_bool_value()),
            "welcomeScreenDisabled": lambda n : setattr(self, 'welcome_screen_disabled', n.get_bool_value()),
            "zoomDisabled": lambda n : setattr(self, 'zoom_disabled', n.get_bool_value()),
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
        writer.write_bool_value("appearanceScreenDisabled", self.appearance_screen_disabled)
        writer.write_bool_value("awaitDeviceConfiguredConfirmation", self.await_device_configured_confirmation)
        writer.write_str_value("carrierActivationUrl", self.carrier_activation_url)
        writer.write_str_value("companyPortalVppTokenId", self.company_portal_vpp_token_id)
        writer.write_bool_value("deviceToDeviceMigrationDisabled", self.device_to_device_migration_disabled)
        writer.write_bool_value("enableSharedIPad", self.enable_shared_i_pad)
        writer.write_bool_value("enableSingleAppEnrollmentMode", self.enable_single_app_enrollment_mode)
        writer.write_bool_value("expressLanguageScreenDisabled", self.express_language_screen_disabled)
        writer.write_bool_value("forceTemporarySession", self.force_temporary_session)
        writer.write_bool_value("homeButtonScreenDisabled", self.home_button_screen_disabled)
        writer.write_bool_value("iMessageAndFaceTimeScreenDisabled", self.i_message_and_face_time_screen_disabled)
        writer.write_enum_value("iTunesPairingMode", self.i_tunes_pairing_mode)
        writer.write_collection_of_object_values("managementCertificates", self.management_certificates)
        writer.write_bool_value("onBoardingScreenDisabled", self.on_boarding_screen_disabled)
        writer.write_bool_value("passCodeDisabled", self.pass_code_disabled)
        writer.write_int_value("passcodeLockGracePeriodInSeconds", self.passcode_lock_grace_period_in_seconds)
        writer.write_bool_value("preferredLanguageScreenDisabled", self.preferred_language_screen_disabled)
        writer.write_bool_value("restoreCompletedScreenDisabled", self.restore_completed_screen_disabled)
        writer.write_bool_value("restoreFromAndroidDisabled", self.restore_from_android_disabled)
        writer.write_int_value("sharedIPadMaximumUserCount", self.shared_i_pad_maximum_user_count)
        writer.write_bool_value("simSetupScreenDisabled", self.sim_setup_screen_disabled)
        writer.write_bool_value("softwareUpdateScreenDisabled", self.software_update_screen_disabled)
        writer.write_int_value("temporarySessionTimeoutInSeconds", self.temporary_session_timeout_in_seconds)
        writer.write_bool_value("updateCompleteScreenDisabled", self.update_complete_screen_disabled)
        writer.write_int_value("userSessionTimeoutInSeconds", self.user_session_timeout_in_seconds)
        writer.write_bool_value("userlessSharedAadModeEnabled", self.userless_shared_aad_mode_enabled)
        writer.write_bool_value("watchMigrationScreenDisabled", self.watch_migration_screen_disabled)
        writer.write_bool_value("welcomeScreenDisabled", self.welcome_screen_disabled)
        writer.write_bool_value("zoomDisabled", self.zoom_disabled)
    

