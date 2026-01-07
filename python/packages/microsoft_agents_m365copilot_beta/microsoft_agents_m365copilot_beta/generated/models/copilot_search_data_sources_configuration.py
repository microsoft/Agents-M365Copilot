from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .one_drive_data_source_configuration import OneDriveDataSourceConfiguration

@dataclass
class CopilotSearchDataSourcesConfiguration(AdditionalDataHolder, Parsable):
    """
    Specifies which data sources to include in the search and optional filters for each.If omitted, the query runs across all supported Microsoft data sources by default.Each data source key can include a filter expression to narrow results and a list of metadata fields to retrieve for that source.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Configuration for searching OneDrive for Business content.
    one_drive: Optional[OneDriveDataSourceConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotSearchDataSourcesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotSearchDataSourcesConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotSearchDataSourcesConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .one_drive_data_source_configuration import OneDriveDataSourceConfiguration

        from .one_drive_data_source_configuration import OneDriveDataSourceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oneDrive": lambda n : setattr(self, 'one_drive', n.get_object_value(OneDriveDataSourceConfiguration)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("oneDrive", self.one_drive)
        writer.write_additional_data_value(self.additional_data)
    

