from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
    from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

@dataclass
class DeviceManagementExchangeAccessRule(AdditionalDataHolder, Parsable):
    """
    Device Access Rules in Exchange.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Access Level in Exchange.
    access_level: Optional[DeviceManagementExchangeAccessLevel] = None
    # Device Class which will be impacted by this rule.
    device_class: Optional[DeviceManagementExchangeDeviceClass] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementExchangeAccessRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeAccessRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementExchangeAccessRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
        from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

        from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
        from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

        fields: dict[str, Callable[[Any], None]] = {
            "accessLevel": lambda n : setattr(self, 'access_level', n.get_enum_value(DeviceManagementExchangeAccessLevel)),
            "deviceClass": lambda n : setattr(self, 'device_class', n.get_object_value(DeviceManagementExchangeDeviceClass)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("accessLevel", self.access_level)
        writer.write_object_value("deviceClass", self.device_class)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

