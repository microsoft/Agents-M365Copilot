from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_quality_update_product_build_version_detail import WindowsQualityUpdateProductBuildVersionDetail
    from .windows_quality_update_product_knowledge_base_article import WindowsQualityUpdateProductKnowledgeBaseArticle

@dataclass
class WindowsQualityUpdateCatalogProductRevision(AdditionalDataHolder, Parsable):
    """
    The operating system product revisions that are released as part of this quality update.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The display name of the windows quality update catalog product revision. For example, 'Windows 11, version 22H2, build 22621.4112'. Read-only
    display_name: Optional[str] = None
    # Represents a knowledge base (KB) article.
    knowledge_base_article: Optional[WindowsQualityUpdateProductKnowledgeBaseArticle] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the build version details of a product revision that is associated with a quality update.
    os_build: Optional[WindowsQualityUpdateProductBuildVersionDetail] = None
    # The product name of the windows quality update catalog product revision. For example, 'Windows 11'. Read-only
    product_name: Optional[str] = None
    # The date and time when the windows quality update catalog product revision was released. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. Read-only
    release_date_time: Optional[datetime.datetime] = None
    # The version name of the windows quality update catalog product revision. For example, '22H2'. Read-only
    version_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateCatalogProductRevision:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateCatalogProductRevision
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateCatalogProductRevision()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_quality_update_product_build_version_detail import WindowsQualityUpdateProductBuildVersionDetail
        from .windows_quality_update_product_knowledge_base_article import WindowsQualityUpdateProductKnowledgeBaseArticle

        from .windows_quality_update_product_build_version_detail import WindowsQualityUpdateProductBuildVersionDetail
        from .windows_quality_update_product_knowledge_base_article import WindowsQualityUpdateProductKnowledgeBaseArticle

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "knowledgeBaseArticle": lambda n : setattr(self, 'knowledge_base_article', n.get_object_value(WindowsQualityUpdateProductKnowledgeBaseArticle)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osBuild": lambda n : setattr(self, 'os_build', n.get_object_value(WindowsQualityUpdateProductBuildVersionDetail)),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "versionName": lambda n : setattr(self, 'version_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("knowledgeBaseArticle", self.knowledge_base_article)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("osBuild", self.os_build)
        writer.write_str_value("productName", self.product_name)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_str_value("versionName", self.version_name)
        writer.write_additional_data_value(self.additional_data)
    

