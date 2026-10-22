from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_app_scope import CustomAppScope
    from .rbac_application_multiple import RbacApplicationMultiple

from .rbac_application_multiple import RbacApplicationMultiple

@dataclass
class UnifiedRbacApplicationMultiple(RbacApplicationMultiple, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.unifiedRbacApplicationMultiple"
    # Represents the resources that the principal has been granted access.
    custom_app_scopes: Optional[list[CustomAppScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRbacApplicationMultiple:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacApplicationMultiple
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRbacApplicationMultiple()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_app_scope import CustomAppScope
        from .rbac_application_multiple import RbacApplicationMultiple

        from .custom_app_scope import CustomAppScope
        from .rbac_application_multiple import RbacApplicationMultiple

        fields: dict[str, Callable[[Any], None]] = {
            "customAppScopes": lambda n : setattr(self, 'custom_app_scopes', n.get_collection_of_object_values(CustomAppScope)),
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
        writer.write_collection_of_object_values("customAppScopes", self.custom_app_scopes)
    

