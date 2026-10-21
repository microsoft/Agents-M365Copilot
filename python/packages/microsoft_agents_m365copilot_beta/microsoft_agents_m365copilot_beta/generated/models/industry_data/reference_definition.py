from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class ReferenceDefinition(Entity, Parsable):
    # The code value for the definition that must be unique within the referenceType.
    code: Optional[str] = None
    # The date and time when the definition was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # A human-readable representation of the reference code value for display in a user interface.
    display_name: Optional[str] = None
    # Indicates whether the definition is disabled.
    is_disabled: Optional[bool] = None
    # The date and time when the definition was most recently changed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The categorical type for a collection of enumerated values.
    reference_type: Optional[str] = None
    # The index that specifies the order in which to present the definition to the user. Must be unique within the referenceType.
    sort_index: Optional[int] = None
    # The standards body or organization source which defined the code.
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReferenceDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReferenceDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "referenceType": lambda n : setattr(self, 'reference_type', n.get_str_value()),
            "sortIndex": lambda n : setattr(self, 'sort_index', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_str_value("referenceType", self.reference_type)
        writer.write_int_value("sortIndex", self.sort_index)
    

