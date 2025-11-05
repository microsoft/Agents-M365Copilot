from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.artifact_type import ArtifactType

@dataclass
class GetArtifactsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The artifactTypes property
    artifact_types: Optional[list[ArtifactType]] = None
    # The maxResults property
    max_results: Optional[int] = None
    # The rangeInSec property
    range_in_sec: Optional[int] = None
    # The seedDateTime property
    seed_date_time: Optional[datetime.datetime] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetArtifactsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetArtifactsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetArtifactsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.artifact_type import ArtifactType

        from .......models.artifact_type import ArtifactType

        fields: dict[str, Callable[[Any], None]] = {
            "artifactTypes": lambda n : setattr(self, 'artifact_types', n.get_collection_of_enum_values(ArtifactType)),
            "maxResults": lambda n : setattr(self, 'max_results', n.get_int_value()),
            "rangeInSec": lambda n : setattr(self, 'range_in_sec', n.get_int_value()),
            "seedDateTime": lambda n : setattr(self, 'seed_date_time', n.get_datetime_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_collection_of_enum_values("artifactTypes", self.artifact_types)
        writer.write_int_value("maxResults", self.max_results)
        writer.write_int_value("rangeInSec", self.range_in_sec)
        writer.write_datetime_value("seedDateTime", self.seed_date_time)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

