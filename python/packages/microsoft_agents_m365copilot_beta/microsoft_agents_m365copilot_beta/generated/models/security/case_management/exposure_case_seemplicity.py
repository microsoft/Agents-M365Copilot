from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExposureCaseSeemplicity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The configurationId property
    configuration_id: Optional[str] = None
    # The configurationName property
    configuration_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The providerType property
    provider_type: Optional[str] = None
    # The syncStatus property
    sync_status: Optional[str] = None
    # The ticketCreationTime property
    ticket_creation_time: Optional[datetime.datetime] = None
    # The ticketId property
    ticket_id: Optional[str] = None
    # The ticketLink property
    ticket_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExposureCaseSeemplicity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExposureCaseSeemplicity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExposureCaseSeemplicity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "configurationId": lambda n : setattr(self, 'configuration_id', n.get_str_value()),
            "configurationName": lambda n : setattr(self, 'configuration_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "providerType": lambda n : setattr(self, 'provider_type', n.get_str_value()),
            "syncStatus": lambda n : setattr(self, 'sync_status', n.get_str_value()),
            "ticketCreationTime": lambda n : setattr(self, 'ticket_creation_time', n.get_datetime_value()),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_str_value()),
            "ticketLink": lambda n : setattr(self, 'ticket_link', n.get_str_value()),
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
        writer.write_str_value("configurationId", self.configuration_id)
        writer.write_str_value("configurationName", self.configuration_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("providerType", self.provider_type)
        writer.write_str_value("syncStatus", self.sync_status)
        writer.write_datetime_value("ticketCreationTime", self.ticket_creation_time)
        writer.write_str_value("ticketId", self.ticket_id)
        writer.write_str_value("ticketLink", self.ticket_link)
        writer.write_additional_data_value(self.additional_data)
    

