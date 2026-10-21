from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_source_filter import AuthenticationSourceFilter
    from .entity import Entity
    from .invoke_user_flow_listener import InvokeUserFlowListener

from .entity import Entity

@dataclass
class AuthenticationListener(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority of the listener. Determines the order of evaluation when an event has multiple listeners. The priority is evaluated from low to high.
    priority: Optional[int] = None
    # Filter based on the source of the authentication that is used to determine whether the listener is evaluated, and is currently limited to evaluations based on application the user is authenticating to.
    source_filter: Optional[AuthenticationSourceFilter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationListener
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invokeUserFlowListener".casefold():
            from .invoke_user_flow_listener import InvokeUserFlowListener

            return InvokeUserFlowListener()
        return AuthenticationListener()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_source_filter import AuthenticationSourceFilter
        from .entity import Entity
        from .invoke_user_flow_listener import InvokeUserFlowListener

        from .authentication_source_filter import AuthenticationSourceFilter
        from .entity import Entity
        from .invoke_user_flow_listener import InvokeUserFlowListener

        fields: dict[str, Callable[[Any], None]] = {
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sourceFilter": lambda n : setattr(self, 'source_filter', n.get_object_value(AuthenticationSourceFilter)),
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
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("sourceFilter", self.source_filter)
    

