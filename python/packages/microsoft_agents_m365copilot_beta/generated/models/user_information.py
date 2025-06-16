from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, Union

from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter

if TYPE_CHECKING:
    from .access_scope import AccessScope
    from .key_value_pair import KeyValuePair
    from .message_user_role import MessageUserRole
    from .user_identity import UserIdentity

from .user_identity import UserIdentity


@dataclass
class UserInformation(UserIdentity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userInformation"
    # The accessScope property
    access_scope: Optional[AccessScope] = None
    # The customAttributes property
    custom_attributes: Optional[list[KeyValuePair]] = None
    # The role property
    role: Optional[MessageUserRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_scope import AccessScope
        from .key_value_pair import KeyValuePair
        from .message_user_role import MessageUserRole
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "accessScope": lambda n : setattr(self, 'access_scope', n.get_enum_value(AccessScope)),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(KeyValuePair)),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MessageUserRole)),
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
        writer.write_enum_value("accessScope", self.access_scope)
        writer.write_collection_of_object_values("customAttributes", self.custom_attributes)
        writer.write_enum_value("role", self.role)
    

