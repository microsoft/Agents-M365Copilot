from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_quality_update_cadence import WindowsQualityUpdateCadence
    from .windows_quality_update_catalog_product_revision import WindowsQualityUpdateCatalogProductRevision
    from .windows_quality_update_category import WindowsQualityUpdateCategory
    from .windows_quality_update_cve_severity_information import WindowsQualityUpdateCveSeverityInformation
    from .windows_update_catalog_item import WindowsUpdateCatalogItem

from .windows_update_catalog_item import WindowsUpdateCatalogItem

@dataclass
class WindowsQualityUpdateCatalogItem(WindowsUpdateCatalogItem, Parsable):
    """
    Windows update catalog item entity
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsQualityUpdateCatalogItem"
    # Windows quality update category
    classification: Optional[WindowsQualityUpdateCategory] = None
    # CVE information for catalog items
    cve_severity_information: Optional[WindowsQualityUpdateCveSeverityInformation] = None
    # When TRUE, indicates that the quality updates qualify for expedition. When FALSE, indicates the quality updates do not quality for expedition. Default value is FALSE. Read-only
    is_expeditable: Optional[bool] = None
    # Identifies the knowledge base article associated with the Windows quality update catalog item. Read-only
    kb_article_id: Optional[str] = None
    # The operating system product revisions that are released as part of this quality update. Read-only.
    product_revisions: Optional[list[WindowsQualityUpdateCatalogProductRevision]] = None
    # The publishing cadence of the quality update. Possible values are: monthly, outOfBand. This property cannot be modified and is automatically populated when the catalog is created.
    quality_update_cadence: Optional[WindowsQualityUpdateCadence] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateCatalogItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateCatalogItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateCatalogItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_quality_update_cadence import WindowsQualityUpdateCadence
        from .windows_quality_update_catalog_product_revision import WindowsQualityUpdateCatalogProductRevision
        from .windows_quality_update_category import WindowsQualityUpdateCategory
        from .windows_quality_update_cve_severity_information import WindowsQualityUpdateCveSeverityInformation
        from .windows_update_catalog_item import WindowsUpdateCatalogItem

        from .windows_quality_update_cadence import WindowsQualityUpdateCadence
        from .windows_quality_update_catalog_product_revision import WindowsQualityUpdateCatalogProductRevision
        from .windows_quality_update_category import WindowsQualityUpdateCategory
        from .windows_quality_update_cve_severity_information import WindowsQualityUpdateCveSeverityInformation
        from .windows_update_catalog_item import WindowsUpdateCatalogItem

        fields: dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(WindowsQualityUpdateCategory)),
            "cveSeverityInformation": lambda n : setattr(self, 'cve_severity_information', n.get_object_value(WindowsQualityUpdateCveSeverityInformation)),
            "isExpeditable": lambda n : setattr(self, 'is_expeditable', n.get_bool_value()),
            "kbArticleId": lambda n : setattr(self, 'kb_article_id', n.get_str_value()),
            "productRevisions": lambda n : setattr(self, 'product_revisions', n.get_collection_of_object_values(WindowsQualityUpdateCatalogProductRevision)),
            "qualityUpdateCadence": lambda n : setattr(self, 'quality_update_cadence', n.get_enum_value(WindowsQualityUpdateCadence)),
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
        writer.write_enum_value("classification", self.classification)
        writer.write_object_value("cveSeverityInformation", self.cve_severity_information)
        writer.write_bool_value("isExpeditable", self.is_expeditable)
        writer.write_str_value("kbArticleId", self.kb_article_id)
        writer.write_collection_of_object_values("productRevisions", self.product_revisions)
        writer.write_enum_value("qualityUpdateCadence", self.quality_update_cadence)
    

