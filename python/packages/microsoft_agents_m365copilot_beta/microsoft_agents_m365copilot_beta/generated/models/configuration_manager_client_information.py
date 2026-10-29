from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ConfigurationManagerClientInformation(AdditionalDataHolder, Parsable):
    """
    Configuration Manager client information synced from SCCM
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Configuration Manager Client Id from SCCM
    client_identifier: Optional[str] = None
    # Configuration Manager Client version from SCCM
    client_version: Optional[str] = None
    # Configuration Manager Client blocked status from SCCM
    is_blocked: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationManagerClientInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerClientInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationManagerClientInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "clientIdentifier": lambda n : setattr(self, 'client_identifier', n.get_str_value()),
            "clientVersion": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "isBlocked": lambda n : setattr(self, 'is_blocked', n.get_bool_value()),
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
        writer.write_str_value("clientIdentifier", self.client_identifier)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_bool_value("isBlocked", self.is_blocked)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

