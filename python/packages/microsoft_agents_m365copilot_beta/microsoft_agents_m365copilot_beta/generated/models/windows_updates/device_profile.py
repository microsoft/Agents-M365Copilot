from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .hotpatch_readiness import HotpatchReadiness
    from .os_status import OsStatus

from ..entity import Entity

@dataclass
class DeviceProfile(Entity, Parsable):
    # The Microsoft Entra device identifier. Read-only.
    azure_ad_device_id: Optional[str] = None
    # The hardware model of the device. Read-only.
    device_model: Optional[str] = None
    # The device name. Read-only.
    device_name: Optional[str] = None
    # The hotpatchReadiness property
    hotpatch_readiness: Optional[HotpatchReadiness] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Windows build installed on the device. Read-only.
    os_build: Optional[str] = None
    # The osStatus property
    os_status: Optional[OsStatus] = None
    # The Windows version installed on the device. Read-only.
    os_version: Optional[str] = None
    # The device serial number. Read-only.
    serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .hotpatch_readiness import HotpatchReadiness
        from .os_status import OsStatus

        from ..entity import Entity
        from .hotpatch_readiness import HotpatchReadiness
        from .os_status import OsStatus

        fields: dict[str, Callable[[Any], None]] = {
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "hotpatchReadiness": lambda n : setattr(self, 'hotpatch_readiness', n.get_enum_value(HotpatchReadiness)),
            "osBuild": lambda n : setattr(self, 'os_build', n.get_str_value()),
            "osStatus": lambda n : setattr(self, 'os_status', n.get_enum_value(OsStatus)),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
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
        writer.write_enum_value("hotpatchReadiness", self.hotpatch_readiness)
        writer.write_enum_value("osStatus", self.os_status)
    

