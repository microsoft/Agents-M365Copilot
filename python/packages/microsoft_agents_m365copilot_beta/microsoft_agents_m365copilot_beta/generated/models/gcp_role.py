from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .gcp_role_type import GcpRoleType
    from .gcp_scope import GcpScope

from .entity import Entity

@dataclass
class GcpRole(Entity, Parsable):
    # The name of the GCP role. Supports $filter and (eq,contains).
    display_name: Optional[str] = None
    # The ID of the GCP role as defined by GCP. Alternate key.
    external_id: Optional[str] = None
    # The gcpRoleType property
    gcp_role_type: Optional[GcpRoleType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resources that an identity assigned this GCP role can perform actions on. Supports $filter and (eq).
    scopes: Optional[list[GcpScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpRole
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GcpRole()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .gcp_role_type import GcpRoleType
        from .gcp_scope import GcpScope

        from .entity import Entity
        from .gcp_role_type import GcpRoleType
        from .gcp_scope import GcpScope

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "gcpRoleType": lambda n : setattr(self, 'gcp_role_type', n.get_enum_value(GcpRoleType)),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_object_values(GcpScope)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_enum_value("gcpRoleType", self.gcp_role_type)
        writer.write_collection_of_object_values("scopes", self.scopes)
    

