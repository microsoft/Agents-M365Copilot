from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .qr_code import QrCode
    from .qr_pin import QrPin

from .authentication_method import AuthenticationMethod

@dataclass
class QrCodePinAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.qrCodePinAuthenticationMethod"
    # The PIN linked to the QR Code auth method of the user.
    pin: Optional[QrPin] = None
    # Standard QR code is primary QR code of the user with lifetime upto 395 days (13 months). There can be only one active standard QR code for the user.
    standard_q_r_code: Optional[QrCode] = None
    # Temporary QR code has lifetime up to 12 hours. It can be issued when the user doesn't have access to their standard QR code. There can be only one active temporary QR code for the user.
    temporary_q_r_code: Optional[QrCode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrCodePinAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrCodePinAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrCodePinAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .qr_code import QrCode
        from .qr_pin import QrPin

        from .authentication_method import AuthenticationMethod
        from .qr_code import QrCode
        from .qr_pin import QrPin

        fields: dict[str, Callable[[Any], None]] = {
            "pin": lambda n : setattr(self, 'pin', n.get_object_value(QrPin)),
            "standardQRCode": lambda n : setattr(self, 'standard_q_r_code', n.get_object_value(QrCode)),
            "temporaryQRCode": lambda n : setattr(self, 'temporary_q_r_code', n.get_object_value(QrCode)),
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
        writer.write_object_value("pin", self.pin)
        writer.write_object_value("standardQRCode", self.standard_q_r_code)
        writer.write_object_value("temporaryQRCode", self.temporary_q_r_code)
    

