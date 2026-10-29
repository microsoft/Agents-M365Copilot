from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .device import Device

from .authentication_method import AuthenticationMethod

@dataclass
class PasswordlessMicrosoftAuthenticatorAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.passwordlessMicrosoftAuthenticatorAuthenticationMethod"
    # The timestamp when this method was registered to the user.
    creation_date_time: Optional[datetime.datetime] = None
    # The device property
    device: Optional[Device] = None
    # The display name of the mobile device as given by the user.
    display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordlessMicrosoftAuthenticatorAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordlessMicrosoftAuthenticatorAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordlessMicrosoftAuthenticatorAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .device import Device

        from .authentication_method import AuthenticationMethod
        from .device import Device

        fields: dict[str, Callable[[Any], None]] = {
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Device)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("device", self.device)
        writer.write_str_value("displayName", self.display_name)
    

