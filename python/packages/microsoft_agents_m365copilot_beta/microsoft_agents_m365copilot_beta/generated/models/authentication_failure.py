from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_failure_reason_code import AuthenticationFailureReasonCode
    from .entity import Entity

from .entity import Entity

@dataclass
class AuthenticationFailure(Entity, Parsable):
    # The count property
    count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The reasonCode property
    reason_code: Optional[AuthenticationFailureReasonCode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationFailure:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationFailure
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationFailure()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_failure_reason_code import AuthenticationFailureReasonCode
        from .entity import Entity

        from .authentication_failure_reason_code import AuthenticationFailureReasonCode
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "reasonCode": lambda n : setattr(self, 'reason_code', n.get_enum_value(AuthenticationFailureReasonCode)),
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
        writer.write_int_value("count", self.count)
        writer.write_str_value("reason", self.reason)
        writer.write_enum_value("reasonCode", self.reason_code)
    

