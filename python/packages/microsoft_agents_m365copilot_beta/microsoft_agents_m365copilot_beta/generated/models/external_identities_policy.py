from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class ExternalIdentitiesPolicy(PolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalIdentitiesPolicy"
    # Reserved for future use.
    allow_deleted_identities_data_removal: Optional[bool] = None
    # Defines whether external users can leave the guest tenant. If set to false, self-service controls are disabled, and the admin of the guest tenant must manually remove the external user from the guest tenant. When the external user leaves the tenant, their data in the guest tenant is first soft-deleted then permanently deleted in 30 days.
    allow_external_identities_to_leave: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalIdentitiesPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalIdentitiesPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalIdentitiesPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_base import PolicyBase

        from .policy_base import PolicyBase

        fields: dict[str, Callable[[Any], None]] = {
            "allowDeletedIdentitiesDataRemoval": lambda n : setattr(self, 'allow_deleted_identities_data_removal', n.get_bool_value()),
            "allowExternalIdentitiesToLeave": lambda n : setattr(self, 'allow_external_identities_to_leave', n.get_bool_value()),
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
        writer.write_bool_value("allowDeletedIdentitiesDataRemoval", self.allow_deleted_identities_data_removal)
        writer.write_bool_value("allowExternalIdentitiesToLeave", self.allow_external_identities_to_leave)
    

