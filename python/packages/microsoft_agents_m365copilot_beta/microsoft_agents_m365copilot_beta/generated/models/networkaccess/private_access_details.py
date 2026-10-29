from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_type import AccessType
    from .connection_status import ConnectionStatus
    from .third_party_token_details import ThirdPartyTokenDetails

@dataclass
class PrivateAccessDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Type of accessed application. Access type options: QuickAccess, PrivateAccess.
    access_type: Optional[AccessType] = None
    # The unique identifier for Application segment ID from Azure AD.
    app_segment_id: Optional[str] = None
    # Status of a connection. Status options: Open, Active, Closed.
    connection_status: Optional[ConnectionStatus] = None
    # Private access connector ID.
    connector_id: Optional[str] = None
    # Private access connector IP address.
    connector_ip: Optional[str] = None
    # Private access connector name.
    connector_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Region where the request was processed by the backend service.
    processing_region: Optional[str] = None
    # Details about third-party tokens used in the transaction.
    third_party_token_details: Optional[ThirdPartyTokenDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivateAccessDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivateAccessDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivateAccessDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_type import AccessType
        from .connection_status import ConnectionStatus
        from .third_party_token_details import ThirdPartyTokenDetails

        from .access_type import AccessType
        from .connection_status import ConnectionStatus
        from .third_party_token_details import ThirdPartyTokenDetails

        fields: dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(AccessType)),
            "appSegmentId": lambda n : setattr(self, 'app_segment_id', n.get_str_value()),
            "connectionStatus": lambda n : setattr(self, 'connection_status', n.get_enum_value(ConnectionStatus)),
            "connectorId": lambda n : setattr(self, 'connector_id', n.get_str_value()),
            "connectorIp": lambda n : setattr(self, 'connector_ip', n.get_str_value()),
            "connectorName": lambda n : setattr(self, 'connector_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processingRegion": lambda n : setattr(self, 'processing_region', n.get_str_value()),
            "thirdPartyTokenDetails": lambda n : setattr(self, 'third_party_token_details', n.get_object_value(ThirdPartyTokenDetails)),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("appSegmentId", self.app_segment_id)
        writer.write_enum_value("connectionStatus", self.connection_status)
        writer.write_str_value("connectorId", self.connector_id)
        writer.write_str_value("connectorIp", self.connector_ip)
        writer.write_str_value("connectorName", self.connector_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("processingRegion", self.processing_region)
        writer.write_object_value("thirdPartyTokenDetails", self.third_party_token_details)
        writer.write_additional_data_value(self.additional_data)
    

