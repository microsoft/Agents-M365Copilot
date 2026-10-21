from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class QrCodePinAuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.qrCodePinAuthenticationMethodConfiguration"
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[AuthenticationMethodTarget]] = None
    # A memorized alphanumeric secret code. Minimum length is 8 as per NIST 800-63B and can't be longer than 20 digits.
    pin_length: Optional[int] = None
    # The maximum value is 395 days and the default value is 365 days.
    standard_q_r_code_lifetime_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrCodePinAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrCodePinAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrCodePinAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget

        fields: dict[str, Callable[[Any], None]] = {
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
            "pinLength": lambda n : setattr(self, 'pin_length', n.get_int_value()),
            "standardQRCodeLifetimeInDays": lambda n : setattr(self, 'standard_q_r_code_lifetime_in_days', n.get_int_value()),
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
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_int_value("pinLength", self.pin_length)
        writer.write_int_value("standardQRCodeLifetimeInDays", self.standard_q_r_code_lifetime_in_days)
    

