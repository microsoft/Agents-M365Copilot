from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .transcript_payload import TranscriptPayload

@dataclass
class GetArtifactsResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The nextLink property
    next_link: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The payloads property
    payloads: Optional[list[TranscriptPayload]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetArtifactsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetArtifactsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetArtifactsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .transcript_payload import TranscriptPayload

        from .transcript_payload import TranscriptPayload

        fields: dict[str, Callable[[Any], None]] = {
            "nextLink": lambda n : setattr(self, 'next_link', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payloads": lambda n : setattr(self, 'payloads', n.get_collection_of_object_values(TranscriptPayload)),
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
        writer.write_collection_of_object_values("payloads", self.payloads)
        writer.write_additional_data_value(self.additional_data)
    

