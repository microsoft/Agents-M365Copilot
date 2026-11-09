from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .teamwork_active_peripherals import TeamworkActivePeripherals

from .entity import Entity

@dataclass
class TeamworkDeviceActivity(Entity, Parsable):
    # The active peripheral devices attached to the device.
    active_peripherals: Optional[TeamworkActivePeripherals] = None
    # Identity of the user who created the device activity document.
    created_by: Optional[IdentitySet] = None
    # The UTC date and time when the device activity document was created.
    created_date_time: Optional[datetime.datetime] = None
    # Identity of the user who last modified the device activity details.
    last_modified_by: Optional[IdentitySet] = None
    # The UTC date and time when the device activity detail was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDeviceActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDeviceActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_active_peripherals import TeamworkActivePeripherals

        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_active_peripherals import TeamworkActivePeripherals

        fields: dict[str, Callable[[Any], None]] = {
            "activePeripherals": lambda n : setattr(self, 'active_peripherals', n.get_object_value(TeamworkActivePeripherals)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("activePeripherals", self.active_peripherals)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

