from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OnPremisesSipInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the user is currently enabled for on-premises Skype for Business.
    is_sip_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates a fully qualified DNS name of the Microsoft Online Communications Server deployment.
    sip_deployment_location: Optional[str] = None
    # Serves as a unique identifier for each user on the on-premises Skype for Business.
    sip_primary_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesSipInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesSipInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesSipInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isSipEnabled": lambda n : setattr(self, 'is_sip_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sipDeploymentLocation": lambda n : setattr(self, 'sip_deployment_location', n.get_str_value()),
            "sipPrimaryAddress": lambda n : setattr(self, 'sip_primary_address', n.get_str_value()),
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
        writer.write_bool_value("isSipEnabled", self.is_sip_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sipDeploymentLocation", self.sip_deployment_location)
        writer.write_str_value("sipPrimaryAddress", self.sip_primary_address)
        writer.write_additional_data_value(self.additional_data)
    

