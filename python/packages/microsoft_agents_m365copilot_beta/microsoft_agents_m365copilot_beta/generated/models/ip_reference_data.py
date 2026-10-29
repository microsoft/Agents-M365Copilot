from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IpReferenceData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The asn property
    asn: Optional[int] = None
    # The city property
    city: Optional[str] = None
    # The countryOrRegionCode property
    country_or_region_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organization property
    organization: Optional[str] = None
    # The state property
    state: Optional[str] = None
    # The vendor property
    vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpReferenceData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpReferenceData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpReferenceData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "asn": lambda n : setattr(self, 'asn', n.get_int_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryOrRegionCode": lambda n : setattr(self, 'country_or_region_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
        writer.write_int_value("asn", self.asn)
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegionCode", self.country_or_region_code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("state", self.state)
        writer.write_str_value("vendor", self.vendor)
        writer.write_additional_data_value(self.additional_data)
    

