from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OneDriveDataSourceConfiguration(AdditionalDataHolder, Parsable):
    """
    Configuration for searching OneDrive for Business content.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A KQL filter to apply only to OneDrive items. Use this to scope the OneDrive search to specific folders, file types, owners, etc. Supported filter fields include path, author, lastModifiedTime, fileType, title, filename, driveId, etc.
    filter_expression: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of metadata field names to return for OneDrive results (if available and marked retrievable in the schema). For example, title, author, lastModifiedTime, etc. can be requested to enrich the search hits.
    resource_metadata_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OneDriveDataSourceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OneDriveDataSourceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OneDriveDataSourceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "filterExpression": lambda n : setattr(self, 'filter_expression', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceMetadataNames": lambda n : setattr(self, 'resource_metadata_names', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("filterExpression", self.filter_expression)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("resourceMetadataNames", self.resource_metadata_names)
        writer.write_additional_data_value(self.additional_data)
    

