from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CertificateConnectorSetting(AdditionalDataHolder, Parsable):
    """
    Certificate connector settings.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Certificate expire time
    cert_expiry_time: Optional[datetime.datetime] = None
    # Version of certificate connector
    connector_version: Optional[str] = None
    # Certificate connector enrollment error
    enrollment_error: Optional[str] = None
    # Last time certificate connector connected
    last_connector_connection_time: Optional[datetime.datetime] = None
    # Version of last uploaded certificate connector
    last_upload_version: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Certificate connector status
    status: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateConnectorSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateConnectorSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateConnectorSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "certExpiryTime": lambda n : setattr(self, 'cert_expiry_time', n.get_datetime_value()),
            "connectorVersion": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "enrollmentError": lambda n : setattr(self, 'enrollment_error', n.get_str_value()),
            "lastConnectorConnectionTime": lambda n : setattr(self, 'last_connector_connection_time', n.get_datetime_value()),
            "lastUploadVersion": lambda n : setattr(self, 'last_upload_version', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
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
        writer.write_datetime_value("certExpiryTime", self.cert_expiry_time)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_str_value("enrollmentError", self.enrollment_error)
        writer.write_datetime_value("lastConnectorConnectionTime", self.last_connector_connection_time)
        writer.write_int_value("lastUploadVersion", self.last_upload_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

