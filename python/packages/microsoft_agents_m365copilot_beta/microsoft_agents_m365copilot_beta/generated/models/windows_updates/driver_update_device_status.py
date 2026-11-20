from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .device_client_state import DeviceClientState
    from .device_client_substate import DeviceClientSubstate
    from .device_service_state import DeviceServiceState
    from .device_service_substate import DeviceServiceSubstate

from ..entity import Entity

@dataclass
class DriverUpdateDeviceStatus(Entity, Parsable):
    # The Microsoft Entra identifier of the device. Read-only.
    aad_device_id: Optional[str] = None
    # The clientState property
    client_state: Optional[DeviceClientState] = None
    # The clientSubstate property
    client_substate: Optional[DeviceClientSubstate] = None
    # The device name. Read-only.
    device_name: Optional[str] = None
    # The date and time of the latest status event. Read-only.
    last_event_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the driver update policy. Read-only.
    policy_id: Optional[str] = None
    # The display name of the driver update policy. Read-only.
    policy_name: Optional[str] = None
    # The identifier of the Windows Autopatch ring. Read-only.
    ring_id: Optional[str] = None
    # The display name of the Windows Autopatch ring. Read-only.
    ring_name: Optional[str] = None
    # The serviceState property
    service_state: Optional[DeviceServiceState] = None
    # The serviceSubstate property
    service_substate: Optional[DeviceServiceSubstate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriverUpdateDeviceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriverUpdateDeviceStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriverUpdateDeviceStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .device_client_state import DeviceClientState
        from .device_client_substate import DeviceClientSubstate
        from .device_service_state import DeviceServiceState
        from .device_service_substate import DeviceServiceSubstate

        from ..entity import Entity
        from .device_client_state import DeviceClientState
        from .device_client_substate import DeviceClientSubstate
        from .device_service_state import DeviceServiceState
        from .device_service_substate import DeviceServiceSubstate

        fields: dict[str, Callable[[Any], None]] = {
            "aadDeviceId": lambda n : setattr(self, 'aad_device_id', n.get_str_value()),
            "clientState": lambda n : setattr(self, 'client_state', n.get_enum_value(DeviceClientState)),
            "clientSubstate": lambda n : setattr(self, 'client_substate', n.get_enum_value(DeviceClientSubstate)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "lastEventDateTime": lambda n : setattr(self, 'last_event_date_time', n.get_datetime_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "ringId": lambda n : setattr(self, 'ring_id', n.get_str_value()),
            "ringName": lambda n : setattr(self, 'ring_name', n.get_str_value()),
            "serviceState": lambda n : setattr(self, 'service_state', n.get_enum_value(DeviceServiceState)),
            "serviceSubstate": lambda n : setattr(self, 'service_substate', n.get_enum_value(DeviceServiceSubstate)),
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
        writer.write_enum_value("clientState", self.client_state)
        writer.write_enum_value("clientSubstate", self.client_substate)
        writer.write_enum_value("serviceState", self.service_state)
        writer.write_enum_value("serviceSubstate", self.service_substate)
    

