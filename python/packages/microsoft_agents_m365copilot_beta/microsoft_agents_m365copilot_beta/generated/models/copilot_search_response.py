from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_search_hit import CopilotSearchHit

@dataclass
class CopilotSearchResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The nextLink property
    next_link: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The searchHits property
    search_hits: Optional[list[CopilotSearchHit]] = None
    # The totalCount property
    total_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotSearchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotSearchResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotSearchResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_search_hit import CopilotSearchHit

        from .copilot_search_hit import CopilotSearchHit

        fields: dict[str, Callable[[Any], None]] = {
            "nextLink": lambda n : setattr(self, 'next_link', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "searchHits": lambda n : setattr(self, 'search_hits', n.get_collection_of_object_values(CopilotSearchHit)),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
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
        writer.write_str_value("nextLink", self.next_link)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("searchHits", self.search_hits)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_additional_data_value(self.additional_data)
    

