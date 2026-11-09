from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ip_destination import IpDestination

from .ip_destination import IpDestination

@dataclass
class IpRange(IpDestination, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.ipRange"
    # Specifies the starting IP address of the IP range.
    begin_address: Optional[str] = None
    # Specifies the ending IP address of the IP range.
    end_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpRange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpRange()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ip_destination import IpDestination

        from .ip_destination import IpDestination

        fields: dict[str, Callable[[Any], None]] = {
            "beginAddress": lambda n : setattr(self, 'begin_address', n.get_str_value()),
            "endAddress": lambda n : setattr(self, 'end_address', n.get_str_value()),
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
        writer.write_str_value("beginAddress", self.begin_address)
        writer.write_str_value("endAddress", self.end_address)
    

