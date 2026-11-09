from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
    from .dep_profile_admin_account_password_rotation_setting import DepProfileAdminAccountPasswordRotationSetting

from .dep_enrollment_base_profile import DepEnrollmentBaseProfile

@dataclass
class DepMacOSEnrollmentProfile(DepEnrollmentBaseProfile, Parsable):
    """
    The DepMacOSEnrollmentProfile resource represents an Apple Device Enrollment Program (DEP) enrollment profile specific to macOS configuration. This type of profile must be assigned to Apple DEP serial numbers before the corresponding devices can enroll via DEP.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.depMacOSEnrollmentProfile"
    # Indicates if Accessibility screen is disabled
    accessibility_screen_disabled: Optional[bool] = None
    # Indicates what the full name for the admin account is
    admin_account_full_name: Optional[str] = None
    # Indicates what the password for the admin account is
    admin_account_password: Optional[str] = None
    # Indicates what the user name for the admin account is
    admin_account_user_name: Optional[str] = None
    # Indicates if Setup Assistant will automatically advance through its screen
    auto_advance_setup_enabled: Optional[bool] = None
    # Indicates if UnlockWithWatch screen is disabled
    auto_unlock_with_watch_disabled: Optional[bool] = None
    # Indicates if iCloud Documents and Desktop screen is disabled
    choose_your_lock_screen_disabled: Optional[bool] = None
    # Settings for local admin account password automatic rotation.
    dep_profile_admin_account_password_rotation_setting: Optional[DepProfileAdminAccountPasswordRotationSetting] = None
    # Indicates whether Setup Assistant will auto populate the primary account information
    dont_auto_populate_primary_account_info: Optional[bool] = None
    # Indicates whether the user will enable blockediting
    enable_restrict_editing: Optional[bool] = None
    # Indicates if file vault is disabled
    file_vault_disabled: Optional[bool] = None
    # Indicates whether the admin account should be hidded or not
    hide_admin_account: Optional[bool] = None
    # Indicates if iCloud Analytics screen is disabled
    i_cloud_diagnostics_disabled: Optional[bool] = None
    # Indicates if iCloud Documents and Desktop screen is disabled
    i_cloud_storage_disabled: Optional[bool] = None
    # Indicates if Passcode setup pane is disabled
    pass_code_disabled: Optional[bool] = None
    # Indicates what the full name for the primary account is
    primary_account_full_name: Optional[str] = None
    # Indicates what the account name for the primary account is
    primary_account_user_name: Optional[str] = None
    # Indicates if registration is disabled
    registration_disabled: Optional[bool] = None
    # Indicates if the device is network-tethered to run the command
    request_requires_network_tether: Optional[bool] = None
    # Indicates whether Setup Assistant will set the account as a regular user
    set_primary_setup_account_as_regular_user: Optional[bool] = None
    # Indicates whether Setup Assistant will skip the user interface for primary account setup
    skip_primary_setup_account_creation: Optional[bool] = None
    # Indicates whether Platform SSO is used as part of device enrollment during Setup Assistant. When TRUE, Platform SSO is used in device enrollment during Setup Assistant. When FALSE Platform SSO is not used in enrollment during Setup Assistant. Note: This value cannot be TRUE when configurationWebUrl is TRUE.
    use_platform_s_s_o_during_setup_assistant: Optional[bool] = None
    # Indicates if zoom setup pane is disabled
    zoom_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepMacOSEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepMacOSEnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepMacOSEnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .dep_profile_admin_account_password_rotation_setting import DepProfileAdminAccountPasswordRotationSetting

        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .dep_profile_admin_account_password_rotation_setting import DepProfileAdminAccountPasswordRotationSetting

        fields: dict[str, Callable[[Any], None]] = {
            "accessibilityScreenDisabled": lambda n : setattr(self, 'accessibility_screen_disabled', n.get_bool_value()),
            "adminAccountFullName": lambda n : setattr(self, 'admin_account_full_name', n.get_str_value()),
            "adminAccountPassword": lambda n : setattr(self, 'admin_account_password', n.get_str_value()),
            "adminAccountUserName": lambda n : setattr(self, 'admin_account_user_name', n.get_str_value()),
            "autoAdvanceSetupEnabled": lambda n : setattr(self, 'auto_advance_setup_enabled', n.get_bool_value()),
            "autoUnlockWithWatchDisabled": lambda n : setattr(self, 'auto_unlock_with_watch_disabled', n.get_bool_value()),
            "chooseYourLockScreenDisabled": lambda n : setattr(self, 'choose_your_lock_screen_disabled', n.get_bool_value()),
            "depProfileAdminAccountPasswordRotationSetting": lambda n : setattr(self, 'dep_profile_admin_account_password_rotation_setting', n.get_object_value(DepProfileAdminAccountPasswordRotationSetting)),
            "dontAutoPopulatePrimaryAccountInfo": lambda n : setattr(self, 'dont_auto_populate_primary_account_info', n.get_bool_value()),
            "enableRestrictEditing": lambda n : setattr(self, 'enable_restrict_editing', n.get_bool_value()),
            "fileVaultDisabled": lambda n : setattr(self, 'file_vault_disabled', n.get_bool_value()),
            "hideAdminAccount": lambda n : setattr(self, 'hide_admin_account', n.get_bool_value()),
            "iCloudDiagnosticsDisabled": lambda n : setattr(self, 'i_cloud_diagnostics_disabled', n.get_bool_value()),
            "iCloudStorageDisabled": lambda n : setattr(self, 'i_cloud_storage_disabled', n.get_bool_value()),
            "passCodeDisabled": lambda n : setattr(self, 'pass_code_disabled', n.get_bool_value()),
            "primaryAccountFullName": lambda n : setattr(self, 'primary_account_full_name', n.get_str_value()),
            "primaryAccountUserName": lambda n : setattr(self, 'primary_account_user_name', n.get_str_value()),
            "registrationDisabled": lambda n : setattr(self, 'registration_disabled', n.get_bool_value()),
            "requestRequiresNetworkTether": lambda n : setattr(self, 'request_requires_network_tether', n.get_bool_value()),
            "setPrimarySetupAccountAsRegularUser": lambda n : setattr(self, 'set_primary_setup_account_as_regular_user', n.get_bool_value()),
            "skipPrimarySetupAccountCreation": lambda n : setattr(self, 'skip_primary_setup_account_creation', n.get_bool_value()),
            "usePlatformSSODuringSetupAssistant": lambda n : setattr(self, 'use_platform_s_s_o_during_setup_assistant', n.get_bool_value()),
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
        writer.write_bool_value("accessibilityScreenDisabled", self.accessibility_screen_disabled)
        writer.write_str_value("adminAccountFullName", self.admin_account_full_name)
        writer.write_str_value("adminAccountPassword", self.admin_account_password)
        writer.write_str_value("adminAccountUserName", self.admin_account_user_name)
        writer.write_bool_value("autoAdvanceSetupEnabled", self.auto_advance_setup_enabled)
        writer.write_bool_value("autoUnlockWithWatchDisabled", self.auto_unlock_with_watch_disabled)
        writer.write_bool_value("chooseYourLockScreenDisabled", self.choose_your_lock_screen_disabled)
        writer.write_object_value("depProfileAdminAccountPasswordRotationSetting", self.dep_profile_admin_account_password_rotation_setting)
        writer.write_bool_value("dontAutoPopulatePrimaryAccountInfo", self.dont_auto_populate_primary_account_info)
        writer.write_bool_value("enableRestrictEditing", self.enable_restrict_editing)
        writer.write_bool_value("fileVaultDisabled", self.file_vault_disabled)
        writer.write_bool_value("hideAdminAccount", self.hide_admin_account)
        writer.write_bool_value("iCloudDiagnosticsDisabled", self.i_cloud_diagnostics_disabled)
        writer.write_bool_value("iCloudStorageDisabled", self.i_cloud_storage_disabled)
        writer.write_bool_value("passCodeDisabled", self.pass_code_disabled)
        writer.write_str_value("primaryAccountFullName", self.primary_account_full_name)
        writer.write_str_value("primaryAccountUserName", self.primary_account_user_name)
        writer.write_bool_value("registrationDisabled", self.registration_disabled)
        writer.write_bool_value("requestRequiresNetworkTether", self.request_requires_network_tether)
        writer.write_bool_value("setPrimarySetupAccountAsRegularUser", self.set_primary_setup_account_as_regular_user)
        writer.write_bool_value("skipPrimarySetupAccountCreation", self.skip_primary_setup_account_creation)
        writer.write_bool_value("usePlatformSSODuringSetupAssistant", self.use_platform_s_s_o_during_setup_assistant)
        writer.write_bool_value("zoomDisabled", self.zoom_disabled)
    

