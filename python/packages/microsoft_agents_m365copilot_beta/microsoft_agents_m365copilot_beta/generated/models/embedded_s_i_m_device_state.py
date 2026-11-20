from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .embedded_s_i_m_device_state_value import EmbeddedSIMDeviceStateValue
    from .entity import Entity

from .entity import Entity

@dataclass
class EmbeddedSIMDeviceState(Entity, Parsable):
    """
    Describes the embedded SIM activation code deployment state in relation to a device.
    """
    # The time the embedded SIM device status was created. Generated service side.
    created_date_time: Optional[datetime.datetime] = None
    # Device name to which the subscription was provisioned e.g. DESKTOP-JOE
    device_name: Optional[str] = None
    # The time the embedded SIM device last checked in. Updated service side.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The time the embedded SIM device status was last modified. Updated service side.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Describes the various states for an embedded SIM activation code.
    state: Optional[EmbeddedSIMDeviceStateValue] = None
    # String description of the provisioning state.
    state_details: Optional[str] = None
    # The Universal Integrated Circuit Card Identifier (UICCID) identifying the hardware onto which a profile is to be deployed.
    universal_integrated_circuit_card_identifier: Optional[str] = None
    # Username which the subscription was provisioned to e.g. joe@contoso.com
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmbeddedSIMDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedSIMDeviceState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmbeddedSIMDeviceState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .embedded_s_i_m_device_state_value import EmbeddedSIMDeviceStateValue
        from .entity import Entity

        from .embedded_s_i_m_device_state_value import EmbeddedSIMDeviceStateValue
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(EmbeddedSIMDeviceStateValue)),
            "stateDetails": lambda n : setattr(self, 'state_details', n.get_str_value()),
            "universalIntegratedCircuitCardIdentifier": lambda n : setattr(self, 'universal_integrated_circuit_card_identifier', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("stateDetails", self.state_details)
        writer.write_str_value("universalIntegratedCircuitCardIdentifier", self.universal_integrated_circuit_card_identifier)
        writer.write_str_value("userName", self.user_name)
    

