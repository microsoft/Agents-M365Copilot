from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RestoreArtifactDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of artifacts that failed to be restored during the restore operation.
    failed_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of artifacts that were successfully restored during the restore operation.
    restored_count: Optional[int] = None
    # The total number of artifacts included in the restore operation.
    total_artifacts_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreArtifactDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreArtifactDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestoreArtifactDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restoredCount": lambda n : setattr(self, 'restored_count', n.get_int_value()),
            "totalArtifactsCount": lambda n : setattr(self, 'total_artifacts_count', n.get_int_value()),
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
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("restoredCount", self.restored_count)
        writer.write_int_value("totalArtifactsCount", self.total_artifacts_count)
        writer.write_additional_data_value(self.additional_data)
    

