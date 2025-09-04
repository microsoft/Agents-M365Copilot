from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_identity import UserIdentity

from .user_identity import UserIdentity

@dataclass
class AuditUserIdentity(UserIdentity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.auditUserIdentity"
    # For user sign ins, the identifier of the tenant that the user is a member of.
    home_tenant_id: Optional[str] = None
    # For user sign ins, the name of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Microsoft Entra ID to show the tenant content.
    home_tenant_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditUserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditUserIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditUserIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_identity import UserIdentity

        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "homeTenantId": lambda n : setattr(self, 'home_tenant_id', n.get_str_value()),
            "homeTenantName": lambda n : setattr(self, 'home_tenant_name', n.get_str_value()),
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
        writer.write_str_value("homeTenantId", self.home_tenant_id)
        writer.write_str_value("homeTenantName", self.home_tenant_name)
    

