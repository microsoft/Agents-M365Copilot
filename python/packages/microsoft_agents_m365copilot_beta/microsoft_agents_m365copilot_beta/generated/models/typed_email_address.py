from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_address import EmailAddress
    from .email_type import EmailType

from .email_address import EmailAddress

@dataclass
class TypedEmailAddress(EmailAddress, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.typedEmailAddress"
    # To specify a custom type of email address, set type to other, and assign otherLabel to a custom string. For example, you may use a specific email address for your volunteer activities. Set type to other, and set otherLabel to a custom string such as Volunteer work.
    other_label: Optional[str] = None
    # The type of email address. The possible values are: unknown, work, personal, main, other. The default value is unknown, which means address has not been set as a specific type.
    type: Optional[EmailType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TypedEmailAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TypedEmailAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TypedEmailAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_address import EmailAddress
        from .email_type import EmailType

        from .email_address import EmailAddress
        from .email_type import EmailType

        fields: dict[str, Callable[[Any], None]] = {
            "otherLabel": lambda n : setattr(self, 'other_label', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(EmailType)),
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
        writer.write_str_value("otherLabel", self.other_label)
        writer.write_enum_value("type", self.type)
    

