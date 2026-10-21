from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
    from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
    from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
    from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
    from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
    from .entity import Entity
    from .error_code import ErrorCode
    from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
    from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
    from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
    from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
    from .mobile_app_policy_set_item import MobileAppPolicySetItem
    from .policy_set_status import PolicySetStatus
    from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
    from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
    from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem

from .entity import Entity

@dataclass
class PolicySetItem(Entity, Parsable):
    """
    A class containing the properties used for PolicySet Item.
    """
    # Creation time of the PolicySetItem.
    created_date_time: Optional[datetime.datetime] = None
    # DisplayName of the PolicySetItem.
    display_name: Optional[str] = None
    # The errorCode property
    error_code: Optional[ErrorCode] = None
    # Tags of the guided deployment
    guided_deployment_tags: Optional[list[str]] = None
    # policySetType of the PolicySetItem.
    item_type: Optional[str] = None
    # Last modified time of the PolicySetItem.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # PayloadId of the PolicySetItem.
    payload_id: Optional[str] = None
    # The enum to specify the status of PolicySet.
    status: Optional[PolicySetStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicySetItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyPolicySetItem".casefold():
            from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem

            return DeviceCompliancePolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationPolicySetItem".casefold():
            from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem

            return DeviceConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationPolicyPolicySetItem".casefold():
            from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem

            return DeviceManagementConfigurationPolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptPolicySetItem".casefold():
            from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem

            return DeviceManagementScriptPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem".casefold():
            from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem

            return EnrollmentRestrictionsConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem".casefold():
            from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem

            return IosLobAppProvisioningConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtectionPolicySetItem".casefold():
            from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem

            return ManagedAppProtectionPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationPolicySetItem".casefold():
            from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem

            return ManagedDeviceMobileAppConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicyPolicySetItem".casefold():
            from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem

            return MdmWindowsInformationProtectionPolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppPolicySetItem".casefold():
            from .mobile_app_policy_set_item import MobileAppPolicySetItem

            return MobileAppPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfigurationPolicySetItem".casefold():
            from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem

            return TargetedManagedAppConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem".casefold():
            from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem

            return Windows10EnrollmentCompletionPageConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfilePolicySetItem".casefold():
            from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem

            return WindowsAutopilotDeploymentProfilePolicySetItem()
        return PolicySetItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
        from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
        from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
        from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
        from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
        from .entity import Entity
        from .error_code import ErrorCode
        from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
        from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
        from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
        from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
        from .mobile_app_policy_set_item import MobileAppPolicySetItem
        from .policy_set_status import PolicySetStatus
        from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
        from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
        from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem

        from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
        from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
        from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
        from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
        from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
        from .entity import Entity
        from .error_code import ErrorCode
        from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
        from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
        from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
        from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
        from .mobile_app_policy_set_item import MobileAppPolicySetItem
        from .policy_set_status import PolicySetStatus
        from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
        from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
        from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(ErrorCode)),
            "guidedDeploymentTags": lambda n : setattr(self, 'guided_deployment_tags', n.get_collection_of_primitive_values(str)),
            "itemType": lambda n : setattr(self, 'item_type', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PolicySetStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_collection_of_primitive_values("guidedDeploymentTags", self.guided_deployment_tags)
        writer.write_str_value("itemType", self.item_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("status", self.status)
    

