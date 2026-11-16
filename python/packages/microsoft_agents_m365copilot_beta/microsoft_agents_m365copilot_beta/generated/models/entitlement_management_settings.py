from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class EntitlementManagementSettings(Entity, Parsable):
    # If externalUserLifecycleAction is BlockSignInAndDelete, the number of days after an external user is blocked from sign in before their account is deleted.
    days_until_external_user_deleted_after_blocked: Optional[int] = None
    # One of None, BlockSignIn, or BlockSignInAndDelete.
    external_user_lifecycle_action: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntitlementManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagementSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagementSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "daysUntilExternalUserDeletedAfterBlocked": lambda n : setattr(self, 'days_until_external_user_deleted_after_blocked', n.get_int_value()),
            "externalUserLifecycleAction": lambda n : setattr(self, 'external_user_lifecycle_action', n.get_str_value()),
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
        writer.write_int_value("daysUntilExternalUserDeletedAfterBlocked", self.days_until_external_user_deleted_after_blocked)
        writer.write_str_value("externalUserLifecycleAction", self.external_user_lifecycle_action)
    

