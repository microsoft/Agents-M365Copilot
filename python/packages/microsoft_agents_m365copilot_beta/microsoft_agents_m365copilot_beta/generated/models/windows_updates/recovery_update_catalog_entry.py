from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .product_revision import ProductRevision
    from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

@dataclass
class RecoveryUpdateCatalogEntry(SoftwareUpdateCatalogEntry, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.recoveryUpdateCatalogEntry"
    # The catalog name. Read-only.
    catalog_name: Optional[str] = None
    # A collection of product revisions associated with the update.
    product_revisions: Optional[list[ProductRevision]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecoveryUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecoveryUpdateCatalogEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecoveryUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .product_revision import ProductRevision
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        from .product_revision import ProductRevision
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        fields: dict[str, Callable[[Any], None]] = {
            "catalogName": lambda n : setattr(self, 'catalog_name', n.get_str_value()),
            "productRevisions": lambda n : setattr(self, 'product_revisions', n.get_collection_of_object_values(ProductRevision)),
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
        writer.write_str_value("catalogName", self.catalog_name)
        writer.write_collection_of_object_values("productRevisions", self.product_revisions)
    

