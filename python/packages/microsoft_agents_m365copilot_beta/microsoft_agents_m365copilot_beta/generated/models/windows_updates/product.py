from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .edition import Edition
    from .known_issue import KnownIssue
    from .product_revision import ProductRevision

from ..entity import Entity

@dataclass
class Product(Entity, Parsable):
    # Represents an edition of a particular Windows product.
    editions: Optional[list[Edition]] = None
    # The friendly names of the product. For example, Version 22H2 (OS build 22621). Read-only.
    friendly_names: Optional[list[str]] = None
    # The name of the product group. For example, Windows 11. Read-only.
    group_name: Optional[str] = None
    # Represents a known issue related to a Windows product.
    known_issues: Optional[list[KnownIssue]] = None
    # The name of the product. For example, Windows 11, version 22H2. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a product revision.
    revisions: Optional[list[ProductRevision]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Product:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Product
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Product()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .edition import Edition
        from .known_issue import KnownIssue
        from .product_revision import ProductRevision

        from ..entity import Entity
        from .edition import Edition
        from .known_issue import KnownIssue
        from .product_revision import ProductRevision

        fields: dict[str, Callable[[Any], None]] = {
            "editions": lambda n : setattr(self, 'editions', n.get_collection_of_object_values(Edition)),
            "friendlyNames": lambda n : setattr(self, 'friendly_names', n.get_collection_of_primitive_values(str)),
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "knownIssues": lambda n : setattr(self, 'known_issues', n.get_collection_of_object_values(KnownIssue)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "revisions": lambda n : setattr(self, 'revisions', n.get_collection_of_object_values(ProductRevision)),
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
        writer.write_collection_of_object_values("editions", self.editions)
        writer.write_collection_of_primitive_values("friendlyNames", self.friendly_names)
        writer.write_str_value("groupName", self.group_name)
        writer.write_collection_of_object_values("knownIssues", self.known_issues)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("revisions", self.revisions)
    

