from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsRemoteConnection(Entity, Parsable):
    """
    The user experience analytics remote connection entity. The report will be retired on December 31, 2024. You can start using the Cloud PC connection quality report now via https://learn.microsoft.com/windows-365/enterprise/report-cloud-pc-connection-quality.
    """
    # The sign in failure percentage of Cloud PC Device. Valid values 0 to 100
    cloud_pc_failure_percentage: Optional[float] = None
    # The round tip time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
    cloud_pc_round_trip_time: Optional[float] = None
    # The sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
    cloud_pc_sign_in_time: Optional[float] = None
    # The core boot time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
    core_boot_time: Optional[float] = None
    # The core sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
    core_sign_in_time: Optional[float] = None
    # The count of remote connection. Valid values 0 to 2147483647
    device_count: Optional[int] = None
    # The id of the device.
    device_id: Optional[str] = None
    # The name of the device.
    device_name: Optional[str] = None
    # The user experience analytics manufacturer.
    manufacturer: Optional[str] = None
    # The user experience analytics device model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remote sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
    remote_sign_in_time: Optional[float] = None
    # The user experience analytics userPrincipalName.
    user_principal_name: Optional[str] = None
    # The user experience analytics virtual network.
    virtual_network: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsRemoteConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsRemoteConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsRemoteConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "cloudPcFailurePercentage": lambda n : setattr(self, 'cloud_pc_failure_percentage', n.get_float_value()),
            "cloudPcRoundTripTime": lambda n : setattr(self, 'cloud_pc_round_trip_time', n.get_float_value()),
            "cloudPcSignInTime": lambda n : setattr(self, 'cloud_pc_sign_in_time', n.get_float_value()),
            "coreBootTime": lambda n : setattr(self, 'core_boot_time', n.get_float_value()),
            "coreSignInTime": lambda n : setattr(self, 'core_sign_in_time', n.get_float_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "remoteSignInTime": lambda n : setattr(self, 'remote_sign_in_time', n.get_float_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "virtualNetwork": lambda n : setattr(self, 'virtual_network', n.get_str_value()),
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
        writer.write_float_value("cloudPcFailurePercentage", self.cloud_pc_failure_percentage)
        writer.write_float_value("cloudPcRoundTripTime", self.cloud_pc_round_trip_time)
        writer.write_float_value("cloudPcSignInTime", self.cloud_pc_sign_in_time)
        writer.write_float_value("coreBootTime", self.core_boot_time)
        writer.write_float_value("coreSignInTime", self.core_sign_in_time)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("remoteSignInTime", self.remote_sign_in_time)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("virtualNetwork", self.virtual_network)
    

