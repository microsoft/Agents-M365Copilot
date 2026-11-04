from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AuthenticationAppDeviceDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The version of the client authentication app used during the authentication step.
    app_version: Optional[str] = None
    # The name of the client authentication app used during the authentication step.
    client_app: Optional[str] = None
    # ID of the device used during the authentication step.
    device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operating system running on the device used for the authentication step.
    operating_system: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationAppDeviceDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAppDeviceDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationAppDeviceDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "appVersion": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "clientApp": lambda n : setattr(self, 'client_app', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
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
        writer.write_str_value("appVersion", self.app_version)
        writer.write_str_value("clientApp", self.client_app)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_additional_data_value(self.additional_data)
    

