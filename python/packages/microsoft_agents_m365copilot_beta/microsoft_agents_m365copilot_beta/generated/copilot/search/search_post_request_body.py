from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.copilot_search_data_sources_configuration import CopilotSearchDataSourcesConfiguration

@dataclass
class SearchPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies which data sources to include in the search and optional filters for each.If omitted, the query runs across all supported Microsoft data sources by default.Each data source key can include a filter expression to narrow results and a list of metadata fields to retrieve for that source.
    data_sources: Optional[CopilotSearchDataSourcesConfiguration] = None
    # The pageSize property
    page_size: Optional[int] = None
    # The query property
    query: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...models.copilot_search_data_sources_configuration import CopilotSearchDataSourcesConfiguration

        from ...models.copilot_search_data_sources_configuration import CopilotSearchDataSourcesConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "dataSources": lambda n : setattr(self, 'data_sources', n.get_object_value(CopilotSearchDataSourcesConfiguration)),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
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
        writer.write_object_value("dataSources", self.data_sources)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_str_value("query", self.query)
        writer.write_additional_data_value(self.additional_data)
    

