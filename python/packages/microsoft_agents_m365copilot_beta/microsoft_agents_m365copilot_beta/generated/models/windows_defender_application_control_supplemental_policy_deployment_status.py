from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
    from .windows_defender_application_control_supplemental_policy_statuses import WindowsDefenderApplicationControlSupplementalPolicyStatuses

from .entity import Entity

@dataclass
class WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus(Entity, Parsable):
    """
    Contains properties for the deployment state of a WindowsDefenderApplicationControl supplemental policy for a device.
    """
    # Enum values for the various WindowsDefenderApplicationControl supplemental policy deployment statuses.
    deployment_status: Optional[WindowsDefenderApplicationControlSupplementalPolicyStatuses] = None
    # Device ID.
    device_id: Optional[str] = None
    # Device name.
    device_name: Optional[str] = None
    # Last sync date time.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Windows OS Version Description.
    os_description: Optional[str] = None
    # Windows OS Version.
    os_version: Optional[str] = None
    # The navigation link to the WindowsDefenderApplicationControl supplemental policy.
    policy: Optional[WindowsDefenderApplicationControlSupplementalPolicy] = None
    # Human readable version of the WindowsDefenderApplicationControl supplemental policy.
    policy_version: Optional[str] = None
    # The name of the user of this device.
    user_name: Optional[str] = None
    # User Principal Name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
        from .windows_defender_application_control_supplemental_policy_statuses import WindowsDefenderApplicationControlSupplementalPolicyStatuses

        from .entity import Entity
        from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
        from .windows_defender_application_control_supplemental_policy_statuses import WindowsDefenderApplicationControlSupplementalPolicyStatuses

        fields: dict[str, Callable[[Any], None]] = {
            "deploymentStatus": lambda n : setattr(self, 'deployment_status', n.get_enum_value(WindowsDefenderApplicationControlSupplementalPolicyStatuses)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(WindowsDefenderApplicationControlSupplementalPolicy)),
            "policyVersion": lambda n : setattr(self, 'policy_version', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("deploymentStatus", self.deployment_status)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyVersion", self.policy_version)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

