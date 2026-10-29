from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense

from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense

@dataclass
class IosVppAppAssignedDeviceLicense(IosVppAppAssignedLicense, Parsable):
    """
    iOS Volume Purchase Program device license assignment. This class does not support Create, Delete, or Update.
    """
    # The device name.
    device_name: Optional[str] = None
    # The managed device ID.
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosVppAppAssignedDeviceLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignedDeviceLicense
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosVppAppAssignedDeviceLicense()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense

        from .ios_vpp_app_assigned_license import IosVppAppAssignedLicense

        fields: dict[str, Callable[[Any], None]] = {
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
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
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
    

