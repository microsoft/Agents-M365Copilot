from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_catalog_resource_type import AccessReviewCatalogResourceType
    from .access_review_resource_scope import AccessReviewResourceScope

from .access_review_resource_scope import AccessReviewResourceScope

@dataclass
class AccessReviewCatalogScope(AccessReviewResourceScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewCatalogScope"
    # The additionalCatalogResourceTypes property
    additional_catalog_resource_types: Optional[AccessReviewCatalogResourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewCatalogScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewCatalogScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewCatalogScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_catalog_resource_type import AccessReviewCatalogResourceType
        from .access_review_resource_scope import AccessReviewResourceScope

        from .access_review_catalog_resource_type import AccessReviewCatalogResourceType
        from .access_review_resource_scope import AccessReviewResourceScope

        fields: dict[str, Callable[[Any], None]] = {
            "additionalCatalogResourceTypes": lambda n : setattr(self, 'additional_catalog_resource_types', n.get_collection_of_enum_values(AccessReviewCatalogResourceType)),
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
        writer.write_enum_value("additionalCatalogResourceTypes", self.additional_catalog_resource_types)
    

