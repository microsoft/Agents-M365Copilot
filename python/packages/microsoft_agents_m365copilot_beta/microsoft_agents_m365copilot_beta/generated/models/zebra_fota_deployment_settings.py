from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .zebra_fota_network_type import ZebraFotaNetworkType
    from .zebra_fota_schedule_mode import ZebraFotaScheduleMode
    from .zebra_fota_update_type import ZebraFotaUpdateType

@dataclass
class ZebraFotaDeploymentSettings(AdditionalDataHolder, Parsable):
    """
    The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Minimum battery level (%) required for both download and installation. Default: -1 (System defaults). Maximum is 100.
    battery_rule_minimum_battery_level_percentage: Optional[int] = None
    # Flag indicating if charger is required. When set to false, the client can install updates whether the device is in or out of the charger. Applied only for installation. Defaults to false.
    battery_rule_require_charger: Optional[bool] = None
    # Deploy update for devices with this model only.
    device_model: Optional[str] = None
    # Represents various network types for Zebra FOTA deployment.
    download_rule_network_type: Optional[ZebraFotaNetworkType] = None
    # Date and time in the device time zone when the download will start (e.g., `2018-07-25T10:20:32`). The default value is UTC now and the maximum is 10 days from deployment creation.
    download_rule_start_date_time: Optional[datetime.datetime] = None
    # A description provided by Zebra for the the firmware artifact to update the device to (e.g.: `LifeGuard Update 120 (released 29-June-2022)`.
    firmware_target_artifact_description: Optional[str] = None
    # Deployment's Board Support Package (BSP. E.g.: '01.18.02.00'). Required only for custom update type.
    firmware_target_board_support_package_version: Optional[str] = None
    # Target OS Version (e.g.: '8.1.0'). Required only for custom update type.
    firmware_target_os_version: Optional[str] = None
    # Target patch name (e.g.: 'U06'). Required only for custom update type.
    firmware_target_patch: Optional[str] = None
    # Date and time in device time zone when the install will start. Default - download startDate if configured, otherwise defaults to NOW. Ignored when deployment update type was set to auto.
    install_rule_start_date_time: Optional[datetime.datetime] = None
    # Time of day after which the install cannot start. Possible range is 00:30:00 to 23:59:59. Should be greater than 'installRuleWindowStartTime' by 30 mins. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 23:59:59. Respected for all values of update type, including AUTO.
    install_rule_window_end_time: Optional[datetime.time] = None
    # Time of day (00:00:00 - 23:30:00) when installation should begin. The time is expressed in a 24-hour format, as hh:mm, and is in the device time zone. Default - 00:00:00. Respected for all values of update type, including AUTO.
    install_rule_window_start_time: Optional[datetime.time] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Maximum 28 days. Default is 28 days. Sequence of dates are: 1) Download start date. 2) Install start date. 3) Schedule end date. If any of the values are not provided, the date provided in the preceding step of the sequence is used. If no values are provided, the string value of the current UTC is used.
    schedule_duration_in_days: Optional[int] = None
    # Represents various schedule modes for Zebra FOTA deployment.
    schedule_mode: Optional[ZebraFotaScheduleMode] = None
    # This attribute indicates the deployment time offset (e.g.`180` represents an offset of `+03:00`, and `-270` represents an offset of `-04:30`). The time offset is the time timezone where the devices are located. The deployment start and end data uses this timezone
    time_zone_offset_in_minutes: Optional[int] = None
    # Represents various update types for Zebra FOTA deployment.
    update_type: Optional[ZebraFotaUpdateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ZebraFotaDeploymentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeploymentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ZebraFotaDeploymentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .zebra_fota_network_type import ZebraFotaNetworkType
        from .zebra_fota_schedule_mode import ZebraFotaScheduleMode
        from .zebra_fota_update_type import ZebraFotaUpdateType

        from .zebra_fota_network_type import ZebraFotaNetworkType
        from .zebra_fota_schedule_mode import ZebraFotaScheduleMode
        from .zebra_fota_update_type import ZebraFotaUpdateType

        fields: dict[str, Callable[[Any], None]] = {
            "batteryRuleMinimumBatteryLevelPercentage": lambda n : setattr(self, 'battery_rule_minimum_battery_level_percentage', n.get_int_value()),
            "batteryRuleRequireCharger": lambda n : setattr(self, 'battery_rule_require_charger', n.get_bool_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "downloadRuleNetworkType": lambda n : setattr(self, 'download_rule_network_type', n.get_enum_value(ZebraFotaNetworkType)),
            "downloadRuleStartDateTime": lambda n : setattr(self, 'download_rule_start_date_time', n.get_datetime_value()),
            "firmwareTargetArtifactDescription": lambda n : setattr(self, 'firmware_target_artifact_description', n.get_str_value()),
            "firmwareTargetBoardSupportPackageVersion": lambda n : setattr(self, 'firmware_target_board_support_package_version', n.get_str_value()),
            "firmwareTargetOsVersion": lambda n : setattr(self, 'firmware_target_os_version', n.get_str_value()),
            "firmwareTargetPatch": lambda n : setattr(self, 'firmware_target_patch', n.get_str_value()),
            "installRuleStartDateTime": lambda n : setattr(self, 'install_rule_start_date_time', n.get_datetime_value()),
            "installRuleWindowEndTime": lambda n : setattr(self, 'install_rule_window_end_time', n.get_time_value()),
            "installRuleWindowStartTime": lambda n : setattr(self, 'install_rule_window_start_time', n.get_time_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduleDurationInDays": lambda n : setattr(self, 'schedule_duration_in_days', n.get_int_value()),
            "scheduleMode": lambda n : setattr(self, 'schedule_mode', n.get_enum_value(ZebraFotaScheduleMode)),
            "timeZoneOffsetInMinutes": lambda n : setattr(self, 'time_zone_offset_in_minutes', n.get_int_value()),
            "updateType": lambda n : setattr(self, 'update_type', n.get_enum_value(ZebraFotaUpdateType)),
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
        writer.write_int_value("batteryRuleMinimumBatteryLevelPercentage", self.battery_rule_minimum_battery_level_percentage)
        writer.write_bool_value("batteryRuleRequireCharger", self.battery_rule_require_charger)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_enum_value("downloadRuleNetworkType", self.download_rule_network_type)
        writer.write_datetime_value("downloadRuleStartDateTime", self.download_rule_start_date_time)
        writer.write_str_value("firmwareTargetArtifactDescription", self.firmware_target_artifact_description)
        writer.write_str_value("firmwareTargetBoardSupportPackageVersion", self.firmware_target_board_support_package_version)
        writer.write_str_value("firmwareTargetOsVersion", self.firmware_target_os_version)
        writer.write_str_value("firmwareTargetPatch", self.firmware_target_patch)
        writer.write_datetime_value("installRuleStartDateTime", self.install_rule_start_date_time)
        writer.write_time_value("installRuleWindowEndTime", self.install_rule_window_end_time)
        writer.write_time_value("installRuleWindowStartTime", self.install_rule_window_start_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("scheduleDurationInDays", self.schedule_duration_in_days)
        writer.write_enum_value("scheduleMode", self.schedule_mode)
        writer.write_int_value("timeZoneOffsetInMinutes", self.time_zone_offset_in_minutes)
        writer.write_enum_value("updateType", self.update_type)
        writer.write_additional_data_value(self.additional_data)
    

