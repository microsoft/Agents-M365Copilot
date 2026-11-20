from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FraudProtectionDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The providerErrorMessages property
    provider_error_messages: Optional[list[str]] = None
    # The providerHttpStatusCodes property
    provider_http_status_codes: Optional[list[int]] = None
    # The providerName property
    provider_name: Optional[str] = None
    # The providerResponseTimes property
    provider_response_times: Optional[list[int]] = None
    # The providerSessionId property
    provider_session_id: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The verdict property
    verdict: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FraudProtectionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FraudProtectionDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FraudProtectionDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "providerErrorMessages": lambda n : setattr(self, 'provider_error_messages', n.get_collection_of_primitive_values(str)),
            "providerHttpStatusCodes": lambda n : setattr(self, 'provider_http_status_codes', n.get_collection_of_primitive_values(int)),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "providerResponseTimes": lambda n : setattr(self, 'provider_response_times', n.get_collection_of_primitive_values(int)),
            "providerSessionId": lambda n : setattr(self, 'provider_session_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "verdict": lambda n : setattr(self, 'verdict', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("providerErrorMessages", self.provider_error_messages)
        writer.write_collection_of_primitive_values("providerHttpStatusCodes", self.provider_http_status_codes)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_collection_of_primitive_values("providerResponseTimes", self.provider_response_times)
        writer.write_str_value("providerSessionId", self.provider_session_id)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("verdict", self.verdict)
        writer.write_additional_data_value(self.additional_data)
    

