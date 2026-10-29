from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExceptionInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The isFalsePositive property
    is_false_positive: Optional[bool] = None
    # The justification property
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The ruleIds property
    rule_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExceptionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExceptionInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExceptionInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isFalsePositive": lambda n : setattr(self, 'is_false_positive', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "ruleIds": lambda n : setattr(self, 'rule_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("isFalsePositive", self.is_false_positive)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("reason", self.reason)
        writer.write_collection_of_primitive_values("ruleIds", self.rule_ids)
        writer.write_additional_data_value(self.additional_data)
    

