from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

from .authentication_method import AuthenticationMethod

@dataclass
class HardwareOathAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.hardwareOathAuthenticationMethod"
    # Exposes the hardware OATH method in the directory.
    device: Optional[HardwareOathTokenAuthenticationMethodDevice] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwareOathAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareOathAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwareOathAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

        from .authentication_method import AuthenticationMethod
        from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

        fields: dict[str, Callable[[Any], None]] = {
            "device": lambda n : setattr(self, 'device', n.get_object_value(HardwareOathTokenAuthenticationMethodDevice)),
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
        writer.write_object_value("device", self.device)
    

