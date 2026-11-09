from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_filter import ConditionalAccessFilter

@dataclass
class ConditionalAccessDevices(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Filter that defines the dynamic-device-syntax rule to include/exclude devices. A filter can use device properties (such as extension attributes) to include/exclude them. Cannot be set if includeDevices or excludeDevices is set.
    device_filter: Optional[ConditionalAccessFilter] = None
    # States excluded from the scope of the policy. Possible values: Compliant, DomainJoined.
    exclude_device_states: Optional[list[str]] = None
    # States excluded from the scope of the policy. Possible values: Compliant, DomainJoined. Cannot be set if deviceFIlter is set.
    exclude_devices: Optional[list[str]] = None
    # States in the scope of the policy. All is the only allowed value.
    include_device_states: Optional[list[str]] = None
    # States in the scope of the policy. All is the only allowed value. Cannot be set if deviceFilter is set.
    include_devices: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessDevices:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessDevices
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessDevices()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_filter import ConditionalAccessFilter

        from .conditional_access_filter import ConditionalAccessFilter

        fields: dict[str, Callable[[Any], None]] = {
            "deviceFilter": lambda n : setattr(self, 'device_filter', n.get_object_value(ConditionalAccessFilter)),
            "excludeDeviceStates": lambda n : setattr(self, 'exclude_device_states', n.get_collection_of_primitive_values(str)),
            "excludeDevices": lambda n : setattr(self, 'exclude_devices', n.get_collection_of_primitive_values(str)),
            "includeDeviceStates": lambda n : setattr(self, 'include_device_states', n.get_collection_of_primitive_values(str)),
            "includeDevices": lambda n : setattr(self, 'include_devices', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("deviceFilter", self.device_filter)
        writer.write_collection_of_primitive_values("excludeDeviceStates", self.exclude_device_states)
        writer.write_collection_of_primitive_values("excludeDevices", self.exclude_devices)
        writer.write_collection_of_primitive_values("includeDeviceStates", self.include_device_states)
        writer.write_collection_of_primitive_values("includeDevices", self.include_devices)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

