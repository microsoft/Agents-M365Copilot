from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .product_revision import ProductRevision
    from .quality_update_cadence import QualityUpdateCadence
    from .quality_update_classification import QualityUpdateClassification
    from .quality_update_cve_severity_information import QualityUpdateCveSeverityInformation
    from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

@dataclass
class QualityUpdateCatalogEntry(SoftwareUpdateCatalogEntry, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry"
    # The catalog name of the content. Read-only.
    catalog_name: Optional[str] = None
    # Severity information of the Common Vulnerabilities and Exposures associated with the content.
    cve_severity_information: Optional[QualityUpdateCveSeverityInformation] = None
    # Indicates whether the content can be deployed as an expedited quality update. Read-only.
    is_expeditable: Optional[bool] = None
    # The operating system product revisions that are released as part of this quality update.
    product_revisions: Optional[list[ProductRevision]] = None
    # The publishing cadence of the quality update. The possible values are: monthly, outOfBand, unknownFutureValue. Read-only.
    quality_update_cadence: Optional[QualityUpdateCadence] = None
    # The qualityUpdateClassification property
    quality_update_classification: Optional[QualityUpdateClassification] = None
    # The short name of the content. Read-only.
    short_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QualityUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QualityUpdateCatalogEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QualityUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .product_revision import ProductRevision
        from .quality_update_cadence import QualityUpdateCadence
        from .quality_update_classification import QualityUpdateClassification
        from .quality_update_cve_severity_information import QualityUpdateCveSeverityInformation
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        from .product_revision import ProductRevision
        from .quality_update_cadence import QualityUpdateCadence
        from .quality_update_classification import QualityUpdateClassification
        from .quality_update_cve_severity_information import QualityUpdateCveSeverityInformation
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        fields: dict[str, Callable[[Any], None]] = {
            "catalogName": lambda n : setattr(self, 'catalog_name', n.get_str_value()),
            "cveSeverityInformation": lambda n : setattr(self, 'cve_severity_information', n.get_object_value(QualityUpdateCveSeverityInformation)),
            "isExpeditable": lambda n : setattr(self, 'is_expeditable', n.get_bool_value()),
            "productRevisions": lambda n : setattr(self, 'product_revisions', n.get_collection_of_object_values(ProductRevision)),
            "qualityUpdateCadence": lambda n : setattr(self, 'quality_update_cadence', n.get_enum_value(QualityUpdateCadence)),
            "qualityUpdateClassification": lambda n : setattr(self, 'quality_update_classification', n.get_enum_value(QualityUpdateClassification)),
            "shortName": lambda n : setattr(self, 'short_name', n.get_str_value()),
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
        writer.write_object_value("cveSeverityInformation", self.cve_severity_information)
        writer.write_bool_value("isExpeditable", self.is_expeditable)
        writer.write_collection_of_object_values("productRevisions", self.product_revisions)
        writer.write_enum_value("qualityUpdateCadence", self.quality_update_cadence)
        writer.write_enum_value("qualityUpdateClassification", self.quality_update_classification)
        writer.write_str_value("shortName", self.short_name)
    

