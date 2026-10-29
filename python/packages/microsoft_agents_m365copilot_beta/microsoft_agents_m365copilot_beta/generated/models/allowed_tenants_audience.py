from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sign_in_audience_restrictions_base import SignInAudienceRestrictionsBase

from .sign_in_audience_restrictions_base import SignInAudienceRestrictionsBase

@dataclass
class AllowedTenantsAudience(SignInAudienceRestrictionsBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.allowedTenantsAudience"
    # The list of Entra tenant IDs where the application can be used as either a client application or a resource application (API). This property must contain at least one value and can't include more than 20 values. The tenant ID where the application is registered may be included, but is not required (see isHomeTenantAllowed). Required.
    allowed_tenant_ids: Optional[list[str]] = None
    # Whether the tenant where the application is registered is allowed. Currently, only true is supported. Default is true.
    is_home_tenant_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AllowedTenantsAudience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AllowedTenantsAudience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AllowedTenantsAudience()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sign_in_audience_restrictions_base import SignInAudienceRestrictionsBase

        from .sign_in_audience_restrictions_base import SignInAudienceRestrictionsBase

        fields: dict[str, Callable[[Any], None]] = {
            "allowedTenantIds": lambda n : setattr(self, 'allowed_tenant_ids', n.get_collection_of_primitive_values(str)),
            "isHomeTenantAllowed": lambda n : setattr(self, 'is_home_tenant_allowed', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("allowedTenantIds", self.allowed_tenant_ids)
        writer.write_bool_value("isHomeTenantAllowed", self.is_home_tenant_allowed)
    

