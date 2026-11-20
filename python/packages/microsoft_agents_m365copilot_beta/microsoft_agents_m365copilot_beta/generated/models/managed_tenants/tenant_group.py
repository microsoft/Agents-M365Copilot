from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .management_action_info import ManagementActionInfo
    from .management_intent_info import ManagementIntentInfo

from ..entity import Entity

@dataclass
class TenantGroup(Entity, Parsable):
    # A flag indicating whether all managed tenant are included in the tenant group. Required. Read-only.
    all_tenants_included: Optional[bool] = None
    # The display name for the tenant group. Optional. Read-only.
    display_name: Optional[str] = None
    # The collection of management action associated with the tenant group. Optional. Read-only.
    management_actions: Optional[list[ManagementActionInfo]] = None
    # The collection of management intents associated with the tenant group. Optional. Read-only.
    management_intents: Optional[list[ManagementIntentInfo]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of managed tenant identifiers include in the tenant group. Optional. Read-only.
    tenant_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .management_action_info import ManagementActionInfo
        from .management_intent_info import ManagementIntentInfo

        from ..entity import Entity
        from .management_action_info import ManagementActionInfo
        from .management_intent_info import ManagementIntentInfo

        fields: dict[str, Callable[[Any], None]] = {
            "allTenantsIncluded": lambda n : setattr(self, 'all_tenants_included', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "managementActions": lambda n : setattr(self, 'management_actions', n.get_collection_of_object_values(ManagementActionInfo)),
            "managementIntents": lambda n : setattr(self, 'management_intents', n.get_collection_of_object_values(ManagementIntentInfo)),
            "tenantIds": lambda n : setattr(self, 'tenant_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("allTenantsIncluded", self.all_tenants_included)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("managementActions", self.management_actions)
        writer.write_collection_of_object_values("managementIntents", self.management_intents)
        writer.write_collection_of_primitive_values("tenantIds", self.tenant_ids)
    

