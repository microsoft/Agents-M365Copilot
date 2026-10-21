from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcAgentPoolScalingPolicy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The maximum number of Cloud PCs in the pool. The valid values are 1 to 900, and must be greater than or equal to minimumCount.
    maximum_count: Optional[int] = None
    # The minimum number of Cloud PCs in the pool. The valid values are 0 to 900, and must be less than or equal to maximumCount.
    minimum_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAgentPoolScalingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAgentPoolScalingPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAgentPoolScalingPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "maximumCount": lambda n : setattr(self, 'maximum_count', n.get_int_value()),
            "minimumCount": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("maximumCount", self.maximum_count)
        writer.write_int_value("minimumCount", self.minimum_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

