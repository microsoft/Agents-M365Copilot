from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, Union

from kiota_abstractions.serialization import (
    AdditionalDataHolder,
    Parsable,
    ParseNode,
    SerializationWriter,
)
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton

if TYPE_CHECKING:
    from ...models.retrieval_data_source import RetrievalDataSource

@dataclass
class RetrievalPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The dataSource property
    data_source: Optional[RetrievalDataSource] = None
    # The filterExpression property
    filter_expression: Optional[str] = None
    # The maximumNumberOfResults property
    maximum_number_of_results: Optional[int] = None
    # The queryString property
    query_string: Optional[str] = None
    # The resourceMetadata property
    resource_metadata: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetrievalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetrievalPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetrievalPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...models.retrieval_data_source import RetrievalDataSource

        fields: dict[str, Callable[[Any], None]] = {
            "dataSource": lambda n : setattr(self, 'data_source', n.get_enum_value(RetrievalDataSource)),
            "filterExpression": lambda n : setattr(self, 'filter_expression', n.get_str_value()),
            "maximumNumberOfResults": lambda n : setattr(self, 'maximum_number_of_results', n.get_int_value()),
            "queryString": lambda n : setattr(self, 'query_string', n.get_str_value()),
            "resourceMetadata": lambda n : setattr(self, 'resource_metadata', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("dataSource", self.data_source)
        writer.write_str_value("filterExpression", self.filter_expression)
        writer.write_int_value("maximumNumberOfResults", self.maximum_number_of_results)
        writer.write_str_value("queryString", self.query_string)
        writer.write_collection_of_primitive_values("resourceMetadata", self.resource_metadata)
        writer.write_additional_data_value(self.additional_data)
    

