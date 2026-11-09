from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting
    from .cloud_pc_disaster_recovery_type import CloudPcDisasterRecoveryType

@dataclass
class CloudPcCrossRegionDisasterRecoverySetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # True if an end user is allowed to set up cross-region disaster recovery for Cloud PC; otherwise, false. The default value is false. This property is deprecated and will no longer be supported effective February 11, 2025. For scenarios where crossRegionDisasterRecoveryEnabled is true, set disasterRecoveryType to crossRegion. For scenarios where crossRegionDisasterRecoveryEnabled is false,  set disasterRecoveryType to notconfigured.
    cross_region_disaster_recovery_enabled: Optional[bool] = None
    # Indicates the network settings of the Cloud PC during a cross-region disaster recovery operation.
    disaster_recovery_network_setting: Optional[CloudPcDisasterRecoveryNetworkSetting] = None
    # Indicates the type of disaster recovery to perform when a disaster occurs on the user's Cloud PC. The possible values are: notConfigured, crossRegion, premium, unknownFutureValue. The default value is notConfigured.
    disaster_recovery_type: Optional[CloudPcDisasterRecoveryType] = None
    # Indicates whether Windows 365 maintain the cross-region disaster recovery function generated restore points. If true, the Windows 365 stored restore points; false indicates that Windows 365 doesn't generate or keep the restore point from the original Cloud PC. If a disaster occurs, the new Cloud PC can only be provisioned using the initial image. This limitation can result in the loss of some user data on the original Cloud PC. The default value is false.
    maintain_cross_region_restore_point_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the client allows the end user to initiate a disaster recovery activation. True indicates that the client includes the option for the end user to activate Backup Cloud PC. When false, the end user doesn't have the option to activate disaster recovery. The default value is false. Currently, only premium disaster recovery is supported.
    user_initiated_disaster_recovery_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcCrossRegionDisasterRecoverySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcCrossRegionDisasterRecoverySetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcCrossRegionDisasterRecoverySetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting
        from .cloud_pc_disaster_recovery_type import CloudPcDisasterRecoveryType

        from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting
        from .cloud_pc_disaster_recovery_type import CloudPcDisasterRecoveryType

        fields: dict[str, Callable[[Any], None]] = {
            "crossRegionDisasterRecoveryEnabled": lambda n : setattr(self, 'cross_region_disaster_recovery_enabled', n.get_bool_value()),
            "disasterRecoveryNetworkSetting": lambda n : setattr(self, 'disaster_recovery_network_setting', n.get_object_value(CloudPcDisasterRecoveryNetworkSetting)),
            "disasterRecoveryType": lambda n : setattr(self, 'disaster_recovery_type', n.get_enum_value(CloudPcDisasterRecoveryType)),
            "maintainCrossRegionRestorePointEnabled": lambda n : setattr(self, 'maintain_cross_region_restore_point_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userInitiatedDisasterRecoveryAllowed": lambda n : setattr(self, 'user_initiated_disaster_recovery_allowed', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("crossRegionDisasterRecoveryEnabled", self.cross_region_disaster_recovery_enabled)
        writer.write_object_value("disasterRecoveryNetworkSetting", self.disaster_recovery_network_setting)
        writer.write_enum_value("disasterRecoveryType", self.disaster_recovery_type)
        writer.write_bool_value("maintainCrossRegionRestorePointEnabled", self.maintain_cross_region_restore_point_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("userInitiatedDisasterRecoveryAllowed", self.user_initiated_disaster_recovery_allowed)
        writer.write_additional_data_value(self.additional_data)
    

