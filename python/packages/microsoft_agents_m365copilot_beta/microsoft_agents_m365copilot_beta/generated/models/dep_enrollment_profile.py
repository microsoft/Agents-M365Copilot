from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enrollment_profile import EnrollmentProfile
    from .i_tunes_pairing_mode import ITunesPairingMode
    from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

from .enrollment_profile import EnrollmentProfile

@dataclass
class DepEnrollmentProfile(EnrollmentProfile, Parsable):
    """
    The depEnrollmentProfile resource represents an Apple Device Enrollment Program (DEP) enrollment profile. This type of profile must be assigned to Apple DEP serial numbers before the corresponding devices can enroll via DEP.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.depEnrollmentProfile"
    # Indicates if Apple id setup pane is disabled
    apple_id_disabled: Optional[bool] = None
    # Indicates if Apple pay setup pane is disabled
    apple_pay_disabled: Optional[bool] = None
    # Indicates if the device will need to wait for configured confirmation
    await_device_configured_confirmation: Optional[bool] = None
    # Indicates if diagnostics setup pane is disabled
    diagnostics_disabled: Optional[bool] = None
    # This indicates whether the device is to be enrolled in a mode which enables multi user scenarios. Only applicable in shared iPads.
    enable_shared_i_pad: Optional[bool] = None
    # The iTunesPairingMode property
    i_tunes_pairing_mode: Optional[ITunesPairingMode] = None
    # Indicates if this is the default profile
    is_default: Optional[bool] = None
    # Indicates if the profile is mandatory
    is_mandatory: Optional[bool] = None
    # Indicates if Location service setup pane is disabled
    location_disabled: Optional[bool] = None
    # Indicates if Mac OS file vault is disabled
    mac_o_s_file_vault_disabled: Optional[bool] = None
    # Indicates if Mac OS registration is disabled
    mac_o_s_registration_disabled: Optional[bool] = None
    # Management certificates for Apple Configurator
    management_certificates: Optional[list[ManagementCertificateWithThumbprint]] = None
    # Indicates if Passcode setup pane is disabled
    pass_code_disabled: Optional[bool] = None
    # Indicates if the profile removal option is disabled
    profile_removal_disabled: Optional[bool] = None
    # Indicates if Restore setup pane is blocked
    restore_blocked: Optional[bool] = None
    # Indicates if Restore from Android is disabled
    restore_from_android_disabled: Optional[bool] = None
    # This specifies the maximum number of users that can use a shared iPad. Only applicable in shared iPad mode.
    shared_i_pad_maximum_user_count: Optional[int] = None
    # Indicates if siri setup pane is disabled
    siri_disabled: Optional[bool] = None
    # Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
    supervised_mode_enabled: Optional[bool] = None
    # Support department information
    support_department: Optional[str] = None
    # Support phone number
    support_phone_number: Optional[str] = None
    # Indicates if 'Terms and Conditions' setup pane is disabled
    terms_and_conditions_disabled: Optional[bool] = None
    # Indicates if touch id setup pane is disabled
    touch_id_disabled: Optional[bool] = None
    # Indicates if zoom setup pane is disabled
    zoom_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepEnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepEnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enrollment_profile import EnrollmentProfile
        from .i_tunes_pairing_mode import ITunesPairingMode
        from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

        from .enrollment_profile import EnrollmentProfile
        from .i_tunes_pairing_mode import ITunesPairingMode
        from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

        fields: dict[str, Callable[[Any], None]] = {
            "appleIdDisabled": lambda n : setattr(self, 'apple_id_disabled', n.get_bool_value()),
            "applePayDisabled": lambda n : setattr(self, 'apple_pay_disabled', n.get_bool_value()),
            "awaitDeviceConfiguredConfirmation": lambda n : setattr(self, 'await_device_configured_confirmation', n.get_bool_value()),
            "diagnosticsDisabled": lambda n : setattr(self, 'diagnostics_disabled', n.get_bool_value()),
            "enableSharedIPad": lambda n : setattr(self, 'enable_shared_i_pad', n.get_bool_value()),
            "iTunesPairingMode": lambda n : setattr(self, 'i_tunes_pairing_mode', n.get_enum_value(ITunesPairingMode)),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isMandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
            "locationDisabled": lambda n : setattr(self, 'location_disabled', n.get_bool_value()),
            "macOSFileVaultDisabled": lambda n : setattr(self, 'mac_o_s_file_vault_disabled', n.get_bool_value()),
            "macOSRegistrationDisabled": lambda n : setattr(self, 'mac_o_s_registration_disabled', n.get_bool_value()),
            "managementCertificates": lambda n : setattr(self, 'management_certificates', n.get_collection_of_object_values(ManagementCertificateWithThumbprint)),
            "passCodeDisabled": lambda n : setattr(self, 'pass_code_disabled', n.get_bool_value()),
            "profileRemovalDisabled": lambda n : setattr(self, 'profile_removal_disabled', n.get_bool_value()),
            "restoreBlocked": lambda n : setattr(self, 'restore_blocked', n.get_bool_value()),
            "restoreFromAndroidDisabled": lambda n : setattr(self, 'restore_from_android_disabled', n.get_bool_value()),
            "sharedIPadMaximumUserCount": lambda n : setattr(self, 'shared_i_pad_maximum_user_count', n.get_int_value()),
            "siriDisabled": lambda n : setattr(self, 'siri_disabled', n.get_bool_value()),
            "supervisedModeEnabled": lambda n : setattr(self, 'supervised_mode_enabled', n.get_bool_value()),
            "supportDepartment": lambda n : setattr(self, 'support_department', n.get_str_value()),
            "supportPhoneNumber": lambda n : setattr(self, 'support_phone_number', n.get_str_value()),
            "termsAndConditionsDisabled": lambda n : setattr(self, 'terms_and_conditions_disabled', n.get_bool_value()),
            "touchIdDisabled": lambda n : setattr(self, 'touch_id_disabled', n.get_bool_value()),
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
        writer.write_bool_value("appleIdDisabled", self.apple_id_disabled)
        writer.write_bool_value("applePayDisabled", self.apple_pay_disabled)
        writer.write_bool_value("awaitDeviceConfiguredConfirmation", self.await_device_configured_confirmation)
        writer.write_bool_value("diagnosticsDisabled", self.diagnostics_disabled)
        writer.write_bool_value("enableSharedIPad", self.enable_shared_i_pad)
        writer.write_enum_value("iTunesPairingMode", self.i_tunes_pairing_mode)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isMandatory", self.is_mandatory)
        writer.write_bool_value("locationDisabled", self.location_disabled)
        writer.write_bool_value("macOSFileVaultDisabled", self.mac_o_s_file_vault_disabled)
        writer.write_bool_value("macOSRegistrationDisabled", self.mac_o_s_registration_disabled)
        writer.write_collection_of_object_values("managementCertificates", self.management_certificates)
        writer.write_bool_value("passCodeDisabled", self.pass_code_disabled)
        writer.write_bool_value("profileRemovalDisabled", self.profile_removal_disabled)
        writer.write_bool_value("restoreBlocked", self.restore_blocked)
        writer.write_bool_value("restoreFromAndroidDisabled", self.restore_from_android_disabled)
        writer.write_int_value("sharedIPadMaximumUserCount", self.shared_i_pad_maximum_user_count)
        writer.write_bool_value("siriDisabled", self.siri_disabled)
        writer.write_bool_value("supervisedModeEnabled", self.supervised_mode_enabled)
        writer.write_str_value("supportDepartment", self.support_department)
        writer.write_str_value("supportPhoneNumber", self.support_phone_number)
        writer.write_bool_value("termsAndConditionsDisabled", self.terms_and_conditions_disabled)
        writer.write_bool_value("touchIdDisabled", self.touch_id_disabled)
        writer.write_bool_value("zoomDisabled", self.zoom_disabled)
    

