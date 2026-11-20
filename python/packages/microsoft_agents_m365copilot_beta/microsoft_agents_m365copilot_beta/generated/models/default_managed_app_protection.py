from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_safety_net_apps_verification_type import AndroidManagedAppSafetyNetAppsVerificationType
    from .android_managed_app_safety_net_device_attestation_type import AndroidManagedAppSafetyNetDeviceAttestationType
    from .android_managed_app_safety_net_evaluation_type import AndroidManagedAppSafetyNetEvaluationType
    from .key_value_pair import KeyValuePair
    from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_protection import ManagedAppProtection
    from .managed_app_remediation_action import ManagedAppRemediationAction
    from .managed_mobile_app import ManagedMobileApp

from .managed_app_protection import ManagedAppProtection

@dataclass
class DefaultManagedAppProtection(ManagedAppProtection, Parsable):
    """
    Policy used to configure detailed management settings for a specified set of apps for all users not targeted by a TargetedManagedAppProtection Policy
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.defaultManagedAppProtection"
    # Indicates  if content sync for widgets is allowed for iOS on App Protection Policies
    allow_widget_content_sync: Optional[bool] = None
    # Semicolon seperated list of device manufacturers allowed, as a string, for the managed app to work. (Android only)
    allowed_android_device_manufacturers: Optional[str] = None
    # List of device models allowed, as a string, for the managed app to work. (Android Only)
    allowed_android_device_models: Optional[list[str]] = None
    # Semicolon seperated list of device models allowed, as a string, for the managed app to work. (iOS Only)
    allowed_ios_device_models: Optional[str] = None
    # Defines a managed app behavior, either block or warn, if the user is clocked out (non-working time). Possible values are: block, wipe, warn, blockWhenSettingIsSupported.
    app_action_if_account_is_clocked_out: Optional[ManagedAppRemediationAction] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_android_device_manufacturer_not_allowed: Optional[ManagedAppRemediationAction] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_android_device_model_not_allowed: Optional[ManagedAppRemediationAction] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_android_safety_net_apps_verification_failed: Optional[ManagedAppRemediationAction] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_android_safety_net_device_attestation_failed: Optional[ManagedAppRemediationAction] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_device_lock_not_set: Optional[ManagedAppRemediationAction] = None
    # If the device does not have a passcode of high complexity or higher, trigger the stored action. Possible values are: block, wipe, warn, blockWhenSettingIsSupported.
    app_action_if_device_passcode_complexity_less_than_high: Optional[ManagedAppRemediationAction] = None
    # If the device does not have a passcode of low complexity or higher, trigger the stored action. Possible values are: block, wipe, warn, blockWhenSettingIsSupported.
    app_action_if_device_passcode_complexity_less_than_low: Optional[ManagedAppRemediationAction] = None
    # If the device does not have a passcode of medium complexity or higher, trigger the stored action. Possible values are: block, wipe, warn, blockWhenSettingIsSupported.
    app_action_if_device_passcode_complexity_less_than_medium: Optional[ManagedAppRemediationAction] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_ios_device_model_not_allowed: Optional[ManagedAppRemediationAction] = None
    # Represents the level to which app data is encrypted for managed apps
    app_data_encryption_type: Optional[ManagedAppDataEncryptionType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[list[ManagedMobileApp]] = None
    # Indicates whether use of the biometric authentication is allowed in place of a pin if PinRequired is set to True. (Android Only)
    biometric_authentication_blocked: Optional[bool] = None
    # Maximum number of days Company Portal update can be deferred on the device or app access will be blocked.
    block_after_company_portal_update_deferral_in_days: Optional[int] = None
    # Whether the app should connect to the configured VPN on launch (Android only).
    connect_to_vpn_on_launch: Optional[bool] = None
    # Friendly name of the preferred custom browser to open weblink on Android. (Android only)
    custom_browser_display_name: Optional[str] = None
    # Unique identifier of a custom browser to open weblink on Android. (Android only)
    custom_browser_package_id: Optional[str] = None
    # A custom browser protocol to open weblink on iOS. (iOS only)
    custom_browser_protocol: Optional[str] = None
    # Friendly name of a custom dialer app to click-to-open a phone number on Android.
    custom_dialer_app_display_name: Optional[str] = None
    # PackageId of a custom dialer app to click-to-open a phone number on Android.
    custom_dialer_app_package_id: Optional[str] = None
    # Protocol of a custom dialer app to click-to-open a phone number on iOS, for example, skype:.
    custom_dialer_app_protocol: Optional[str] = None
    # A set of string key and string value pairs to be sent to the affected users, unalterned by this service
    custom_settings: Optional[list[KeyValuePair]] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # Defines if any kind of lock must be required on device. (android only)
    device_lock_required: Optional[bool] = None
    # When this setting is enabled, app level encryption is disabled if device level encryption is enabled. (Android only)
    disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
    # Disable protection of data transferred to other apps through IOS OpenIn option. This setting is only allowed to be True when AllowedOutboundDataTransferDestinations is set to ManagedApps. (iOS Only)
    disable_protection_of_managed_outbound_open_in_data: Optional[bool] = None
    # Indicates whether managed-app data should be encrypted. (Android only)
    encrypt_app_data: Optional[bool] = None
    # Android App packages in this list will be exempt from the policy and will be able to receive data from managed apps. (Android only)
    exempted_app_packages: Optional[list[KeyValuePair]] = None
    # iOS Apps in this list will be exempt from the policy and will be able to receive data from managed apps. (iOS Only)
    exempted_app_protocols: Optional[list[KeyValuePair]] = None
    # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True. (iOS Only)
    face_id_blocked: Optional[bool] = None
    # Defines if open-in operation is supported from the managed app to the filesharing locations selected. This setting only applies when AllowedOutboundDataTransferDestinations is set to ManagedApps and DisableProtectionOfManagedOutboundOpenInData is set to False. (iOS Only)
    filter_open_in_to_only_managed_apps: Optional[bool] = None
    # Indicate to the client to enable both biometrics and fingerprints for the app.
    fingerprint_and_biometric_enabled: Optional[bool] = None
    # When a specific app redirection is enforced by protectedMessagingRedirectAppType in an App Protection Policy, this value defines the app name which are allowed to be used.
    messaging_redirect_app_display_name: Optional[str] = None
    # When a specific app redirection is enforced by protectedMessagingRedirectAppType in an App Protection Policy, this value defines the app package ids which are allowed to be used.
    messaging_redirect_app_package_id: Optional[str] = None
    # When a specific app redirection is enforced by protectedMessagingRedirectAppType in an App Protection Policy, this value defines the app url redirect schemes which are allowed to be used.
    messaging_redirect_app_url_scheme: Optional[str] = None
    # Minimum version of the Company portal that must be installed on the device or app access will be blocked
    minimum_required_company_portal_version: Optional[str] = None
    # Define the oldest required Android security patch level a user can have to gain secure access to the app. (Android only)
    minimum_required_patch_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. (iOS Only)
    minimum_required_sdk_version: Optional[str] = None
    # Minimum version of the Company portal that must be installed on the device or the user will receive a warning
    minimum_warning_company_portal_version: Optional[str] = None
    # Define the oldest recommended Android security patch level a user can have for secure access to the app. (Android only)
    minimum_warning_patch_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data. (iOS only)
    minimum_warning_sdk_version: Optional[str] = None
    # Minimum version of the Company portal that must be installed on the device or the company data on the app will be wiped
    minimum_wipe_company_portal_version: Optional[str] = None
    # Android security patch level  less than or equal to the specified value will wipe the managed app and the associated company data. (Android only)
    minimum_wipe_patch_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_wipe_sdk_version: Optional[str] = None
    # Protect incoming data from unknown source. This setting is only allowed to be True when AllowedInboundDataTransferSources is set to AllApps. (iOS Only)
    protect_inbound_data_from_unknown_sources: Optional[bool] = None
    # Require user to apply Class 3 Biometrics on their Android device.
    require_class3_biometrics: Optional[bool] = None
    # A PIN prompt will override biometric prompts if class 3 biometrics are updated on the device.
    require_pin_after_biometric_change: Optional[bool] = None
    # An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
    required_android_safety_net_apps_verification_type: Optional[AndroidManagedAppSafetyNetAppsVerificationType] = None
    # An admin enforced Android SafetyNet Device Attestation requirement on a managed app.
    required_android_safety_net_device_attestation_type: Optional[AndroidManagedAppSafetyNetDeviceAttestationType] = None
    # An admin enforced Android SafetyNet evaluation type requirement on a managed app.
    required_android_safety_net_evaluation_type: Optional[AndroidManagedAppSafetyNetEvaluationType] = None
    # Indicates whether screen capture is blocked. (Android only)
    screen_capture_blocked: Optional[bool] = None
    # Defines if third party keyboards are allowed while accessing a managed app. (iOS Only)
    third_party_keyboards_blocked: Optional[bool] = None
    # Maximum number of days Company Portal update can be deferred on the device or the user will receive the warning
    warn_after_company_portal_update_deferral_in_days: Optional[int] = None
    # Maximum number of days Company Portal update can be deferred on the device or the company data on the app will be wiped
    wipe_after_company_portal_update_deferral_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DefaultManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultManagedAppProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DefaultManagedAppProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_safety_net_apps_verification_type import AndroidManagedAppSafetyNetAppsVerificationType
        from .android_managed_app_safety_net_device_attestation_type import AndroidManagedAppSafetyNetDeviceAttestationType
        from .android_managed_app_safety_net_evaluation_type import AndroidManagedAppSafetyNetEvaluationType
        from .key_value_pair import KeyValuePair
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_app_remediation_action import ManagedAppRemediationAction
        from .managed_mobile_app import ManagedMobileApp

        from .android_managed_app_safety_net_apps_verification_type import AndroidManagedAppSafetyNetAppsVerificationType
        from .android_managed_app_safety_net_device_attestation_type import AndroidManagedAppSafetyNetDeviceAttestationType
        from .android_managed_app_safety_net_evaluation_type import AndroidManagedAppSafetyNetEvaluationType
        from .key_value_pair import KeyValuePair
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_app_remediation_action import ManagedAppRemediationAction
        from .managed_mobile_app import ManagedMobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "allowWidgetContentSync": lambda n : setattr(self, 'allow_widget_content_sync', n.get_bool_value()),
            "allowedAndroidDeviceManufacturers": lambda n : setattr(self, 'allowed_android_device_manufacturers', n.get_str_value()),
            "allowedAndroidDeviceModels": lambda n : setattr(self, 'allowed_android_device_models', n.get_collection_of_primitive_values(str)),
            "allowedIosDeviceModels": lambda n : setattr(self, 'allowed_ios_device_models', n.get_str_value()),
            "appActionIfAccountIsClockedOut": lambda n : setattr(self, 'app_action_if_account_is_clocked_out', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfAndroidDeviceManufacturerNotAllowed": lambda n : setattr(self, 'app_action_if_android_device_manufacturer_not_allowed', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfAndroidDeviceModelNotAllowed": lambda n : setattr(self, 'app_action_if_android_device_model_not_allowed', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfAndroidSafetyNetAppsVerificationFailed": lambda n : setattr(self, 'app_action_if_android_safety_net_apps_verification_failed', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfAndroidSafetyNetDeviceAttestationFailed": lambda n : setattr(self, 'app_action_if_android_safety_net_device_attestation_failed', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfDeviceLockNotSet": lambda n : setattr(self, 'app_action_if_device_lock_not_set', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfDevicePasscodeComplexityLessThanHigh": lambda n : setattr(self, 'app_action_if_device_passcode_complexity_less_than_high', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfDevicePasscodeComplexityLessThanLow": lambda n : setattr(self, 'app_action_if_device_passcode_complexity_less_than_low', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfDevicePasscodeComplexityLessThanMedium": lambda n : setattr(self, 'app_action_if_device_passcode_complexity_less_than_medium', n.get_enum_value(ManagedAppRemediationAction)),
            "appActionIfIosDeviceModelNotAllowed": lambda n : setattr(self, 'app_action_if_ios_device_model_not_allowed', n.get_enum_value(ManagedAppRemediationAction)),
            "appDataEncryptionType": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "biometricAuthenticationBlocked": lambda n : setattr(self, 'biometric_authentication_blocked', n.get_bool_value()),
            "blockAfterCompanyPortalUpdateDeferralInDays": lambda n : setattr(self, 'block_after_company_portal_update_deferral_in_days', n.get_int_value()),
            "connectToVpnOnLaunch": lambda n : setattr(self, 'connect_to_vpn_on_launch', n.get_bool_value()),
            "customBrowserDisplayName": lambda n : setattr(self, 'custom_browser_display_name', n.get_str_value()),
            "customBrowserPackageId": lambda n : setattr(self, 'custom_browser_package_id', n.get_str_value()),
            "customBrowserProtocol": lambda n : setattr(self, 'custom_browser_protocol', n.get_str_value()),
            "customDialerAppDisplayName": lambda n : setattr(self, 'custom_dialer_app_display_name', n.get_str_value()),
            "customDialerAppPackageId": lambda n : setattr(self, 'custom_dialer_app_package_id', n.get_str_value()),
            "customDialerAppProtocol": lambda n : setattr(self, 'custom_dialer_app_protocol', n.get_str_value()),
            "customSettings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(KeyValuePair)),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "deviceLockRequired": lambda n : setattr(self, 'device_lock_required', n.get_bool_value()),
            "disableAppEncryptionIfDeviceEncryptionIsEnabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "disableProtectionOfManagedOutboundOpenInData": lambda n : setattr(self, 'disable_protection_of_managed_outbound_open_in_data', n.get_bool_value()),
            "encryptAppData": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "exemptedAppPackages": lambda n : setattr(self, 'exempted_app_packages', n.get_collection_of_object_values(KeyValuePair)),
            "exemptedAppProtocols": lambda n : setattr(self, 'exempted_app_protocols', n.get_collection_of_object_values(KeyValuePair)),
            "faceIdBlocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "filterOpenInToOnlyManagedApps": lambda n : setattr(self, 'filter_open_in_to_only_managed_apps', n.get_bool_value()),
            "fingerprintAndBiometricEnabled": lambda n : setattr(self, 'fingerprint_and_biometric_enabled', n.get_bool_value()),
            "messagingRedirectAppDisplayName": lambda n : setattr(self, 'messaging_redirect_app_display_name', n.get_str_value()),
            "messagingRedirectAppPackageId": lambda n : setattr(self, 'messaging_redirect_app_package_id', n.get_str_value()),
            "messagingRedirectAppUrlScheme": lambda n : setattr(self, 'messaging_redirect_app_url_scheme', n.get_str_value()),
            "minimumRequiredCompanyPortalVersion": lambda n : setattr(self, 'minimum_required_company_portal_version', n.get_str_value()),
            "minimumRequiredPatchVersion": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimumWarningCompanyPortalVersion": lambda n : setattr(self, 'minimum_warning_company_portal_version', n.get_str_value()),
            "minimumWarningPatchVersion": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "minimumWarningSdkVersion": lambda n : setattr(self, 'minimum_warning_sdk_version', n.get_str_value()),
            "minimumWipeCompanyPortalVersion": lambda n : setattr(self, 'minimum_wipe_company_portal_version', n.get_str_value()),
            "minimumWipePatchVersion": lambda n : setattr(self, 'minimum_wipe_patch_version', n.get_str_value()),
            "minimumWipeSdkVersion": lambda n : setattr(self, 'minimum_wipe_sdk_version', n.get_str_value()),
            "protectInboundDataFromUnknownSources": lambda n : setattr(self, 'protect_inbound_data_from_unknown_sources', n.get_bool_value()),
            "requireClass3Biometrics": lambda n : setattr(self, 'require_class3_biometrics', n.get_bool_value()),
            "requirePinAfterBiometricChange": lambda n : setattr(self, 'require_pin_after_biometric_change', n.get_bool_value()),
            "requiredAndroidSafetyNetAppsVerificationType": lambda n : setattr(self, 'required_android_safety_net_apps_verification_type', n.get_enum_value(AndroidManagedAppSafetyNetAppsVerificationType)),
            "requiredAndroidSafetyNetDeviceAttestationType": lambda n : setattr(self, 'required_android_safety_net_device_attestation_type', n.get_enum_value(AndroidManagedAppSafetyNetDeviceAttestationType)),
            "requiredAndroidSafetyNetEvaluationType": lambda n : setattr(self, 'required_android_safety_net_evaluation_type', n.get_enum_value(AndroidManagedAppSafetyNetEvaluationType)),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "thirdPartyKeyboardsBlocked": lambda n : setattr(self, 'third_party_keyboards_blocked', n.get_bool_value()),
            "warnAfterCompanyPortalUpdateDeferralInDays": lambda n : setattr(self, 'warn_after_company_portal_update_deferral_in_days', n.get_int_value()),
            "wipeAfterCompanyPortalUpdateDeferralInDays": lambda n : setattr(self, 'wipe_after_company_portal_update_deferral_in_days', n.get_int_value()),
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
        writer.write_bool_value("allowWidgetContentSync", self.allow_widget_content_sync)
        writer.write_str_value("allowedAndroidDeviceManufacturers", self.allowed_android_device_manufacturers)
        writer.write_collection_of_primitive_values("allowedAndroidDeviceModels", self.allowed_android_device_models)
        writer.write_str_value("allowedIosDeviceModels", self.allowed_ios_device_models)
        writer.write_enum_value("appActionIfAccountIsClockedOut", self.app_action_if_account_is_clocked_out)
        writer.write_enum_value("appActionIfAndroidDeviceManufacturerNotAllowed", self.app_action_if_android_device_manufacturer_not_allowed)
        writer.write_enum_value("appActionIfAndroidDeviceModelNotAllowed", self.app_action_if_android_device_model_not_allowed)
        writer.write_enum_value("appActionIfAndroidSafetyNetAppsVerificationFailed", self.app_action_if_android_safety_net_apps_verification_failed)
        writer.write_enum_value("appActionIfAndroidSafetyNetDeviceAttestationFailed", self.app_action_if_android_safety_net_device_attestation_failed)
        writer.write_enum_value("appActionIfDeviceLockNotSet", self.app_action_if_device_lock_not_set)
        writer.write_enum_value("appActionIfDevicePasscodeComplexityLessThanHigh", self.app_action_if_device_passcode_complexity_less_than_high)
        writer.write_enum_value("appActionIfDevicePasscodeComplexityLessThanLow", self.app_action_if_device_passcode_complexity_less_than_low)
        writer.write_enum_value("appActionIfDevicePasscodeComplexityLessThanMedium", self.app_action_if_device_passcode_complexity_less_than_medium)
        writer.write_enum_value("appActionIfIosDeviceModelNotAllowed", self.app_action_if_ios_device_model_not_allowed)
        writer.write_enum_value("appDataEncryptionType", self.app_data_encryption_type)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_bool_value("biometricAuthenticationBlocked", self.biometric_authentication_blocked)
        writer.write_int_value("blockAfterCompanyPortalUpdateDeferralInDays", self.block_after_company_portal_update_deferral_in_days)
        writer.write_bool_value("connectToVpnOnLaunch", self.connect_to_vpn_on_launch)
        writer.write_str_value("customBrowserDisplayName", self.custom_browser_display_name)
        writer.write_str_value("customBrowserPackageId", self.custom_browser_package_id)
        writer.write_str_value("customBrowserProtocol", self.custom_browser_protocol)
        writer.write_str_value("customDialerAppDisplayName", self.custom_dialer_app_display_name)
        writer.write_str_value("customDialerAppPackageId", self.custom_dialer_app_package_id)
        writer.write_str_value("customDialerAppProtocol", self.custom_dialer_app_protocol)
        writer.write_collection_of_object_values("customSettings", self.custom_settings)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("deviceLockRequired", self.device_lock_required)
        writer.write_bool_value("disableAppEncryptionIfDeviceEncryptionIsEnabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("disableProtectionOfManagedOutboundOpenInData", self.disable_protection_of_managed_outbound_open_in_data)
        writer.write_bool_value("encryptAppData", self.encrypt_app_data)
        writer.write_collection_of_object_values("exemptedAppPackages", self.exempted_app_packages)
        writer.write_collection_of_object_values("exemptedAppProtocols", self.exempted_app_protocols)
        writer.write_bool_value("faceIdBlocked", self.face_id_blocked)
        writer.write_bool_value("filterOpenInToOnlyManagedApps", self.filter_open_in_to_only_managed_apps)
        writer.write_bool_value("fingerprintAndBiometricEnabled", self.fingerprint_and_biometric_enabled)
        writer.write_str_value("messagingRedirectAppDisplayName", self.messaging_redirect_app_display_name)
        writer.write_str_value("messagingRedirectAppPackageId", self.messaging_redirect_app_package_id)
        writer.write_str_value("messagingRedirectAppUrlScheme", self.messaging_redirect_app_url_scheme)
        writer.write_str_value("minimumRequiredCompanyPortalVersion", self.minimum_required_company_portal_version)
        writer.write_str_value("minimumRequiredPatchVersion", self.minimum_required_patch_version)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
        writer.write_str_value("minimumWarningCompanyPortalVersion", self.minimum_warning_company_portal_version)
        writer.write_str_value("minimumWarningPatchVersion", self.minimum_warning_patch_version)
        writer.write_str_value("minimumWarningSdkVersion", self.minimum_warning_sdk_version)
        writer.write_str_value("minimumWipeCompanyPortalVersion", self.minimum_wipe_company_portal_version)
        writer.write_str_value("minimumWipePatchVersion", self.minimum_wipe_patch_version)
        writer.write_str_value("minimumWipeSdkVersion", self.minimum_wipe_sdk_version)
        writer.write_bool_value("protectInboundDataFromUnknownSources", self.protect_inbound_data_from_unknown_sources)
        writer.write_bool_value("requireClass3Biometrics", self.require_class3_biometrics)
        writer.write_bool_value("requirePinAfterBiometricChange", self.require_pin_after_biometric_change)
        writer.write_enum_value("requiredAndroidSafetyNetAppsVerificationType", self.required_android_safety_net_apps_verification_type)
        writer.write_enum_value("requiredAndroidSafetyNetDeviceAttestationType", self.required_android_safety_net_device_attestation_type)
        writer.write_enum_value("requiredAndroidSafetyNetEvaluationType", self.required_android_safety_net_evaluation_type)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("thirdPartyKeyboardsBlocked", self.third_party_keyboards_blocked)
        writer.write_int_value("warnAfterCompanyPortalUpdateDeferralInDays", self.warn_after_company_portal_update_deferral_in_days)
        writer.write_int_value("wipeAfterCompanyPortalUpdateDeferralInDays", self.wipe_after_company_portal_update_deferral_in_days)
    

