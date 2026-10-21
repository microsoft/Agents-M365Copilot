from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_privacy import GroupPrivacy
    from .label_action_base import LabelActionBase

from .label_action_base import LabelActionBase

@dataclass
class ProtectGroup(LabelActionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.protectGroup"
    # The allowEmailFromGuestUsers property
    allow_email_from_guest_users: Optional[bool] = None
    # The allowGuestUsers property
    allow_guest_users: Optional[bool] = None
    # The privacy property
    privacy: Optional[GroupPrivacy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProtectGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_privacy import GroupPrivacy
        from .label_action_base import LabelActionBase

        from .group_privacy import GroupPrivacy
        from .label_action_base import LabelActionBase

        fields: dict[str, Callable[[Any], None]] = {
            "allowEmailFromGuestUsers": lambda n : setattr(self, 'allow_email_from_guest_users', n.get_bool_value()),
            "allowGuestUsers": lambda n : setattr(self, 'allow_guest_users', n.get_bool_value()),
            "privacy": lambda n : setattr(self, 'privacy', n.get_enum_value(GroupPrivacy)),
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
        writer.write_bool_value("allowEmailFromGuestUsers", self.allow_email_from_guest_users)
        writer.write_bool_value("allowGuestUsers", self.allow_guest_users)
        writer.write_enum_value("privacy", self.privacy)
    

