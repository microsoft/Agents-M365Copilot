from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mfa_type import MfaType

from .entity import Entity

@dataclass
class MfaUserCountMetric(Entity, Parsable):
    # The count property
    count: Optional[int] = None
    # The factDate property
    fact_date: Optional[datetime.date] = None
    # The mfaType property
    mfa_type: Optional[MfaType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MfaUserCountMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MfaUserCountMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MfaUserCountMetric()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mfa_type import MfaType

        from .entity import Entity
        from .mfa_type import MfaType

        fields: dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "mfaType": lambda n : setattr(self, 'mfa_type', n.get_enum_value(MfaType)),
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
        writer.write_int_value("count", self.count)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_enum_value("mfaType", self.mfa_type)
    

