from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_data_connector import ApiDataConnector

from .api_data_connector import ApiDataConnector

@dataclass
class OneRosterApiDataConnector(ApiDataConnector, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.oneRosterApiDataConnector"
    # The API version of the OneRoster source. Example: 1.1, 1.2
    api_version: Optional[str] = None
    # Indicates whether the user specified to import optional contacts data.
    is_contacts_enabled: Optional[bool] = None
    # Indicates whether the user specified to import optional demographics data.
    is_demographics_enabled: Optional[bool] = None
    # Indicates whether the user specified to import optional flags data.
    is_flags_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OneRosterApiDataConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OneRosterApiDataConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OneRosterApiDataConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .api_data_connector import ApiDataConnector

        from .api_data_connector import ApiDataConnector

        fields: dict[str, Callable[[Any], None]] = {
            "apiVersion": lambda n : setattr(self, 'api_version', n.get_str_value()),
            "isContactsEnabled": lambda n : setattr(self, 'is_contacts_enabled', n.get_bool_value()),
            "isDemographicsEnabled": lambda n : setattr(self, 'is_demographics_enabled', n.get_bool_value()),
            "isFlagsEnabled": lambda n : setattr(self, 'is_flags_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("apiVersion", self.api_version)
        writer.write_bool_value("isContactsEnabled", self.is_contacts_enabled)
        writer.write_bool_value("isDemographicsEnabled", self.is_demographics_enabled)
        writer.write_bool_value("isFlagsEnabled", self.is_flags_enabled)
    

