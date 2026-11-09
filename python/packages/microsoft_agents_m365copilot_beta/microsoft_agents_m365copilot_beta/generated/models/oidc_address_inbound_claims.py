from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OidcAddressInboundClaims(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Country name.
    country: Optional[str] = None
    # City or locality.
    locality: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Zip code or postal code.
    postal_code: Optional[str] = None
    # Country name.
    region: Optional[str] = None
    # Full mailing address, formatted for display or use on a mailing label. This field MAY contain multiple lines, separated by newlines. Newlines can be represented either as a carriage return/line feed pair ('/r/n') or as a single line feed character ('/n').
    street_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OidcAddressInboundClaims:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OidcAddressInboundClaims
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OidcAddressInboundClaims()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "locality": lambda n : setattr(self, 'locality', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "street_address": lambda n : setattr(self, 'street_address', n.get_str_value()),
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
        writer.write_str_value("country", self.country)
        writer.write_str_value("locality", self.locality)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("postal_code", self.postal_code)
        writer.write_str_value("region", self.region)
        writer.write_str_value("street_address", self.street_address)
        writer.write_additional_data_value(self.additional_data)
    

