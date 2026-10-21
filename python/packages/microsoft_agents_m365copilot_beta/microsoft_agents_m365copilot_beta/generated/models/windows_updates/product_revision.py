from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .build_version_details import BuildVersionDetails
    from .catalog_entry import CatalogEntry
    from .knowledge_base_article import KnowledgeBaseArticle

from ..entity import Entity

@dataclass
class ProductRevision(Entity, Parsable):
    # The catalogEntry property
    catalog_entry: Optional[CatalogEntry] = None
    # The display name of the content. Read-only.
    display_name: Optional[str] = None
    # True indicates that the content is hotpatchable; otherwise, false. For more information, see Deploy a hotpatch quality update using Windows Autopatch. Read-only.
    is_hotpatch_update: Optional[bool] = None
    # The knowledge base article associated with the product revision.
    knowledge_base_article: Optional[KnowledgeBaseArticle] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The osBuild property
    os_build: Optional[BuildVersionDetails] = None
    # The product of the revision. The possible values are: Windows 10, Windows 11. Read-only.
    product: Optional[str] = None
    # The release date for the content. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    release_date_time: Optional[datetime.datetime] = None
    # The version of the feature update. Read-only.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProductRevision:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProductRevision
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProductRevision()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .build_version_details import BuildVersionDetails
        from .catalog_entry import CatalogEntry
        from .knowledge_base_article import KnowledgeBaseArticle

        from ..entity import Entity
        from .build_version_details import BuildVersionDetails
        from .catalog_entry import CatalogEntry
        from .knowledge_base_article import KnowledgeBaseArticle

        fields: dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(CatalogEntry)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isHotpatchUpdate": lambda n : setattr(self, 'is_hotpatch_update', n.get_bool_value()),
            "knowledgeBaseArticle": lambda n : setattr(self, 'knowledge_base_article', n.get_object_value(KnowledgeBaseArticle)),
            "osBuild": lambda n : setattr(self, 'os_build', n.get_object_value(BuildVersionDetails)),
            "product": lambda n : setattr(self, 'product', n.get_str_value()),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isHotpatchUpdate", self.is_hotpatch_update)
        writer.write_object_value("knowledgeBaseArticle", self.knowledge_base_article)
        writer.write_object_value("osBuild", self.os_build)
        writer.write_str_value("product", self.product)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_str_value("version", self.version)
    

