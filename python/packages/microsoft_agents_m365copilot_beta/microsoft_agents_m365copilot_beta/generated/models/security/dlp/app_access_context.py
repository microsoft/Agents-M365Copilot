from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AppAccessContext(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The aadSessionId property
    aad_session_id: Optional[str] = None
    # The apiId property
    api_id: Optional[str] = None
    # The clientAppId property
    client_app_id: Optional[str] = None
    # The clientAppName property
    client_app_name: Optional[str] = None
    # The correlationId property
    correlation_id: Optional[str] = None
    # The issuedAtDate property
    issued_at_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The uniqueTokenId property
    unique_token_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppAccessContext:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppAccessContext
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppAccessContext()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "aadSessionId": lambda n : setattr(self, 'aad_session_id', n.get_str_value()),
            "apiId": lambda n : setattr(self, 'api_id', n.get_str_value()),
            "clientAppId": lambda n : setattr(self, 'client_app_id', n.get_str_value()),
            "clientAppName": lambda n : setattr(self, 'client_app_name', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "issuedAtDate": lambda n : setattr(self, 'issued_at_date', n.get_date_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uniqueTokenId": lambda n : setattr(self, 'unique_token_id', n.get_str_value()),
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
        writer.write_str_value("aadSessionId", self.aad_session_id)
        writer.write_str_value("apiId", self.api_id)
        writer.write_str_value("clientAppId", self.client_app_id)
        writer.write_str_value("clientAppName", self.client_app_name)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_date_value("issuedAtDate", self.issued_at_date)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("uniqueTokenId", self.unique_token_id)
        writer.write_additional_data_value(self.additional_data)
    

