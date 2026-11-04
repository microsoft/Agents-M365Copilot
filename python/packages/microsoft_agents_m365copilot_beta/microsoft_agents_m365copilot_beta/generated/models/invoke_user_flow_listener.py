from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_listener import AuthenticationListener
    from .b2x_identity_user_flow import B2xIdentityUserFlow

from .authentication_listener import AuthenticationListener

@dataclass
class InvokeUserFlowListener(AuthenticationListener, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.invokeUserFlowListener"
    # The user flow that is invoked when this action executes.
    user_flow: Optional[B2xIdentityUserFlow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvokeUserFlowListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvokeUserFlowListener
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvokeUserFlowListener()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_listener import AuthenticationListener
        from .b2x_identity_user_flow import B2xIdentityUserFlow

        from .authentication_listener import AuthenticationListener
        from .b2x_identity_user_flow import B2xIdentityUserFlow

        fields: dict[str, Callable[[Any], None]] = {
            "userFlow": lambda n : setattr(self, 'user_flow', n.get_object_value(B2xIdentityUserFlow)),
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
        writer.write_object_value("userFlow", self.user_flow)
    

