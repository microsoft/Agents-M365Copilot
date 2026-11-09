from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair

@dataclass
class CloudPcStatusDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # More information about the Cloud PC status. For example, 'additionalInformation': ['{'@odata.type': 'microsoft.graph.keyValuePair','name': 'retriable','value': true }] '
    additional_information: Optional[list[KeyValuePair]] = None
    # The error/warning code associated with the Cloud PC status. Example: 'code': 'internalServerError'.
    code: Optional[str] = None
    # The status message associated with error code. Example: 'message': 'There was an internal server error. Please contact support xxx.'.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcStatusDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcStatusDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcStatusDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_value_pair import KeyValuePair

        from .key_value_pair import KeyValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_collection_of_object_values(KeyValuePair)),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
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
        writer.write_collection_of_object_values("additionalInformation", self.additional_information)
        writer.write_str_value("code", self.code)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

