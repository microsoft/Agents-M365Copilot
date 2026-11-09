from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .embedded_s_i_m_activation_code import EmbeddedSIMActivationCode
    from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
    from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
    from .entity import Entity

from .entity import Entity

@dataclass
class EmbeddedSIMActivationCodePool(Entity, Parsable):
    """
    A pool represents a group of embedded SIM activation codes.
    """
    # The total count of activation codes which belong to this pool.
    activation_code_count: Optional[int] = None
    # The activation codes which belong to this pool. This navigation property is used to post activation codes to Intune but cannot be used to read activation codes from Intune.
    activation_codes: Optional[list[EmbeddedSIMActivationCode]] = None
    # Navigational property to a list of targets to which this pool is assigned.
    assignments: Optional[list[EmbeddedSIMActivationCodePoolAssignment]] = None
    # The time the embedded SIM activation code pool was created. Generated service side.
    created_date_time: Optional[datetime.datetime] = None
    # Navigational property to a list of device states for this pool.
    device_states: Optional[list[EmbeddedSIMDeviceState]] = None
    # The admin defined name of the embedded SIM activation code pool.
    display_name: Optional[str] = None
    # The time the embedded SIM activation code pool was last modified. Updated service side.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmbeddedSIMActivationCodePool:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedSIMActivationCodePool
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmbeddedSIMActivationCodePool()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .embedded_s_i_m_activation_code import EmbeddedSIMActivationCode
        from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
        from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
        from .entity import Entity

        from .embedded_s_i_m_activation_code import EmbeddedSIMActivationCode
        from .embedded_s_i_m_activation_code_pool_assignment import EmbeddedSIMActivationCodePoolAssignment
        from .embedded_s_i_m_device_state import EmbeddedSIMDeviceState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activationCodeCount": lambda n : setattr(self, 'activation_code_count', n.get_int_value()),
            "activationCodes": lambda n : setattr(self, 'activation_codes', n.get_collection_of_object_values(EmbeddedSIMActivationCode)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(EmbeddedSIMActivationCodePoolAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(EmbeddedSIMDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
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
        writer.write_int_value("activationCodeCount", self.activation_code_count)
        writer.write_collection_of_object_values("activationCodes", self.activation_codes)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

