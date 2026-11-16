from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .forwarding_category import ForwardingCategory
    from .forwarding_rule import ForwardingRule
    from .networking_protocol import NetworkingProtocol

from .forwarding_rule import ForwardingRule

@dataclass
class M365ForwardingRule(ForwardingRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.m365ForwardingRule"
    # The category property
    category: Optional[ForwardingCategory] = None
    # The port(s) used by a forwarding rule for Microsoft 365 traffic are specified to determine the specific network port(s) through which the Microsoft 365 traffic is directed and forwarded.
    ports: Optional[list[str]] = None
    # The protocol property
    protocol: Optional[NetworkingProtocol] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> M365ForwardingRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: M365ForwardingRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return M365ForwardingRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .forwarding_category import ForwardingCategory
        from .forwarding_rule import ForwardingRule
        from .networking_protocol import NetworkingProtocol

        from .forwarding_category import ForwardingCategory
        from .forwarding_rule import ForwardingRule
        from .networking_protocol import NetworkingProtocol

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ForwardingCategory)),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(NetworkingProtocol)),
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
        writer.write_enum_value("category", self.category)
        writer.write_collection_of_primitive_values("ports", self.ports)
        writer.write_enum_value("protocol", self.protocol)
    

