from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_app_device_threat_level import ManagedAppDeviceThreatLevel
    from .managed_app_policy import ManagedAppPolicy
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_remediation_action import ManagedAppRemediationAction
    from .managed_mobile_app import ManagedMobileApp
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
    from .windows_managed_app_clipboard_sharing_level import WindowsManagedAppClipboardSharingLevel
    from .windows_managed_app_data_transfer_level import WindowsManagedAppDataTransferLevel
    from .windows_managed_app_data_transfer_locations import WindowsManagedAppDataTransferLocations

from .managed_app_policy import ManagedAppPolicy

@dataclass
class WindowsManagedAppProtection(ManagedAppPolicy, Parsable):
    """
    Policy used to configure detailed management settings targeted to specific security groups and for a specified set of apps on a Windows device
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsManagedAppProtection"
    # Windows MAM data transfer locations
    allowed_inbound_data_transfer_source_apps: Optional[WindowsManagedAppDataTransferLocations] = None
    # Data can be transferred from/to these classes of apps
    allowed_inbound_data_transfer_sources: Optional[WindowsManagedAppDataTransferLevel] = None
    # Represents the level to which the device's clipboard may be shared between apps
    allowed_outbound_clipboard_sharing_level: Optional[WindowsManagedAppClipboardSharingLevel] = None
    # Windows MAM data transfer locations
    allowed_outbound_data_transfer_destination_apps: Optional[WindowsManagedAppDataTransferLocations] = None
    # Data can be transferred from/to these classes of apps
    allowed_outbound_data_transfer_destinations: Optional[WindowsManagedAppDataTransferLevel] = None
    # If set, it will specify what action to take in the case where the user is unable to checkin because their authentication token is invalid. This happens when the user is deleted or disabled in AAD. Some possible values are block or wipe. If this property is not set, no action will be taken. Possible values are: block, wipe, warn, blockWhenSettingIsSupported.
    app_action_if_unable_to_authenticate_user: Optional[ManagedAppRemediationAction] = None
    # List of apps to which the policy is deployed.
    apps: Optional[list[ManagedMobileApp]] = None
    # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
    assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = None
    # Indicates the total number of applications for which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # When TRUE, indicates that the policy is deployed to some inclusion groups. When FALSE, indicates that the policy is not deployed to any inclusion groups. Default value is FALSE.
    is_assigned: Optional[bool] = None
    # The maxium threat level allowed for an app to be compliant.
    maximum_allowed_device_threat_level: Optional[ManagedAppDeviceThreatLevel] = None
    # Versions bigger than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    maximum_required_os_version: Optional[str] = None
    # Versions bigger than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    maximum_warning_os_version: Optional[str] = None
    # Versions bigger than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    maximum_wipe_os_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_required_app_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_required_os_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_required_sdk_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_warning_app_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_warning_os_version: Optional[str] = None
    # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    minimum_wipe_app_version: Optional[str] = None
    # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    minimum_wipe_os_version: Optional[str] = None
    # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    minimum_wipe_sdk_version: Optional[str] = None
    # An admin initiated action to be applied on a managed app.
    mobile_threat_defense_remediation_action: Optional[ManagedAppRemediationAction] = None
    # The period after which access is checked when the device is not connected to the internet. For example, PT5M indicates that the interval is 5 minutes in duration. A timespan value of PT0S indicates that access will be blocked immediately when the device is not connected to the internet.
    period_offline_before_access_check: Optional[datetime.timedelta] = None
    # The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped. For example, P5D indicates that the interval is 5 days in duration. A timespan value of PT0S indicates that managed data will never be wiped when the device is not connected to the internet.
    period_offline_before_wipe_is_enforced: Optional[datetime.timedelta] = None
    # When TRUE, indicates that printing is blocked from managed apps. When FALSE, indicates that printing is allowed from managed apps. Default value is FALSE.
    print_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsManagedAppProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsManagedAppProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_device_threat_level import ManagedAppDeviceThreatLevel
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_remediation_action import ManagedAppRemediationAction
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .windows_managed_app_clipboard_sharing_level import WindowsManagedAppClipboardSharingLevel
        from .windows_managed_app_data_transfer_level import WindowsManagedAppDataTransferLevel
        from .windows_managed_app_data_transfer_locations import WindowsManagedAppDataTransferLocations

        from .managed_app_device_threat_level import ManagedAppDeviceThreatLevel
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_remediation_action import ManagedAppRemediationAction
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .windows_managed_app_clipboard_sharing_level import WindowsManagedAppClipboardSharingLevel
        from .windows_managed_app_data_transfer_level import WindowsManagedAppDataTransferLevel
        from .windows_managed_app_data_transfer_locations import WindowsManagedAppDataTransferLocations

        fields: dict[str, Callable[[Any], None]] = {
            "allowedInboundDataTransferSourceApps": lambda n : setattr(self, 'allowed_inbound_data_transfer_source_apps', n.get_collection_of_enum_values(WindowsManagedAppDataTransferLocations)),
            "allowedInboundDataTransferSources": lambda n : setattr(self, 'allowed_inbound_data_transfer_sources', n.get_enum_value(WindowsManagedAppDataTransferLevel)),
            "allowedOutboundClipboardSharingLevel": lambda n : setattr(self, 'allowed_outbound_clipboard_sharing_level', n.get_enum_value(WindowsManagedAppClipboardSharingLevel)),
            "allowedOutboundDataTransferDestinationApps": lambda n : setattr(self, 'allowed_outbound_data_transfer_destination_apps', n.get_collection_of_enum_values(WindowsManagedAppDataTransferLocations)),
            "allowedOutboundDataTransferDestinations": lambda n : setattr(self, 'allowed_outbound_data_transfer_destinations', n.get_enum_value(WindowsManagedAppDataTransferLevel)),
            "appActionIfUnableToAuthenticateUser": lambda n : setattr(self, 'app_action_if_unable_to_authenticate_user', n.get_enum_value(ManagedAppRemediationAction)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TargetedManagedAppPolicyAssignment)),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "maximumAllowedDeviceThreatLevel": lambda n : setattr(self, 'maximum_allowed_device_threat_level', n.get_enum_value(ManagedAppDeviceThreatLevel)),
            "maximumRequiredOsVersion": lambda n : setattr(self, 'maximum_required_os_version', n.get_str_value()),
            "maximumWarningOsVersion": lambda n : setattr(self, 'maximum_warning_os_version', n.get_str_value()),
            "maximumWipeOsVersion": lambda n : setattr(self, 'maximum_wipe_os_version', n.get_str_value()),
            "minimumRequiredAppVersion": lambda n : setattr(self, 'minimum_required_app_version', n.get_str_value()),
            "minimumRequiredOsVersion": lambda n : setattr(self, 'minimum_required_os_version', n.get_str_value()),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimumWarningAppVersion": lambda n : setattr(self, 'minimum_warning_app_version', n.get_str_value()),
            "minimumWarningOsVersion": lambda n : setattr(self, 'minimum_warning_os_version', n.get_str_value()),
            "minimumWipeAppVersion": lambda n : setattr(self, 'minimum_wipe_app_version', n.get_str_value()),
            "minimumWipeOsVersion": lambda n : setattr(self, 'minimum_wipe_os_version', n.get_str_value()),
            "minimumWipeSdkVersion": lambda n : setattr(self, 'minimum_wipe_sdk_version', n.get_str_value()),
            "mobileThreatDefenseRemediationAction": lambda n : setattr(self, 'mobile_threat_defense_remediation_action', n.get_enum_value(ManagedAppRemediationAction)),
            "periodOfflineBeforeAccessCheck": lambda n : setattr(self, 'period_offline_before_access_check', n.get_timedelta_value()),
            "periodOfflineBeforeWipeIsEnforced": lambda n : setattr(self, 'period_offline_before_wipe_is_enforced', n.get_timedelta_value()),
            "printBlocked": lambda n : setattr(self, 'print_blocked', n.get_bool_value()),
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
        writer.write_enum_value("allowedInboundDataTransferSourceApps", self.allowed_inbound_data_transfer_source_apps)
        writer.write_enum_value("allowedInboundDataTransferSources", self.allowed_inbound_data_transfer_sources)
        writer.write_enum_value("allowedOutboundClipboardSharingLevel", self.allowed_outbound_clipboard_sharing_level)
        writer.write_enum_value("allowedOutboundDataTransferDestinationApps", self.allowed_outbound_data_transfer_destination_apps)
        writer.write_enum_value("allowedOutboundDataTransferDestinations", self.allowed_outbound_data_transfer_destinations)
        writer.write_enum_value("appActionIfUnableToAuthenticateUser", self.app_action_if_unable_to_authenticate_user)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_enum_value("maximumAllowedDeviceThreatLevel", self.maximum_allowed_device_threat_level)
        writer.write_str_value("maximumRequiredOsVersion", self.maximum_required_os_version)
        writer.write_str_value("maximumWarningOsVersion", self.maximum_warning_os_version)
        writer.write_str_value("maximumWipeOsVersion", self.maximum_wipe_os_version)
        writer.write_str_value("minimumRequiredAppVersion", self.minimum_required_app_version)
        writer.write_str_value("minimumRequiredOsVersion", self.minimum_required_os_version)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
        writer.write_str_value("minimumWarningAppVersion", self.minimum_warning_app_version)
        writer.write_str_value("minimumWarningOsVersion", self.minimum_warning_os_version)
        writer.write_str_value("minimumWipeAppVersion", self.minimum_wipe_app_version)
        writer.write_str_value("minimumWipeOsVersion", self.minimum_wipe_os_version)
        writer.write_str_value("minimumWipeSdkVersion", self.minimum_wipe_sdk_version)
        writer.write_enum_value("mobileThreatDefenseRemediationAction", self.mobile_threat_defense_remediation_action)
        writer.write_timedelta_value("periodOfflineBeforeAccessCheck", self.period_offline_before_access_check)
        writer.write_timedelta_value("periodOfflineBeforeWipeIsEnforced", self.period_offline_before_wipe_is_enforced)
        writer.write_bool_value("printBlocked", self.print_blocked)
    

