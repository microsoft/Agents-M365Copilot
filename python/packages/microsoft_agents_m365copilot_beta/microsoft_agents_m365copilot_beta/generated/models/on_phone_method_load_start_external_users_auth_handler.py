from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .on_phone_method_load_start_handler import OnPhoneMethodLoadStartHandler
    from .phone_options import PhoneOptions

from .on_phone_method_load_start_handler import OnPhoneMethodLoadStartHandler

@dataclass
class OnPhoneMethodLoadStartExternalUsersAuthHandler(OnPhoneMethodLoadStartHandler, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onPhoneMethodLoadStartExternalUsersAuthHandler"
    # The smsOptions property
    sms_options: Optional[PhoneOptions] = None
    # The voiceOptions property
    voice_options: Optional[PhoneOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPhoneMethodLoadStartExternalUsersAuthHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPhoneMethodLoadStartExternalUsersAuthHandler
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPhoneMethodLoadStartExternalUsersAuthHandler()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .on_phone_method_load_start_handler import OnPhoneMethodLoadStartHandler
        from .phone_options import PhoneOptions

        from .on_phone_method_load_start_handler import OnPhoneMethodLoadStartHandler
        from .phone_options import PhoneOptions

        fields: dict[str, Callable[[Any], None]] = {
            "smsOptions": lambda n : setattr(self, 'sms_options', n.get_object_value(PhoneOptions)),
            "voiceOptions": lambda n : setattr(self, 'voice_options', n.get_object_value(PhoneOptions)),
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
        writer.write_object_value("smsOptions", self.sms_options)
        writer.write_object_value("voiceOptions", self.voice_options)
    

