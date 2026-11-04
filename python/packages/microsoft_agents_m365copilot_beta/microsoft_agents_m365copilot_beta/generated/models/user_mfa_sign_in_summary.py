from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserMfaSignInSummary(Entity, Parsable):
    # The date and time (UTC) for when the summary was aggregated for. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The total number of MFA sign-ins for the given day.
    multi_factor_sign_ins: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of non-MFA sign ins for the given day.
    single_factor_sign_ins: Optional[int] = None
    # The total number of sign-ins for the given day.
    total_sign_ins: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserMfaSignInSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserMfaSignInSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserMfaSignInSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "multiFactorSignIns": lambda n : setattr(self, 'multi_factor_sign_ins', n.get_int_value()),
            "singleFactorSignIns": lambda n : setattr(self, 'single_factor_sign_ins', n.get_int_value()),
            "totalSignIns": lambda n : setattr(self, 'total_sign_ins', n.get_int_value()),
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
        writer.write_int_value("multiFactorSignIns", self.multi_factor_sign_ins)
        writer.write_int_value("singleFactorSignIns", self.single_factor_sign_ins)
        writer.write_int_value("totalSignIns", self.total_sign_ins)
    

