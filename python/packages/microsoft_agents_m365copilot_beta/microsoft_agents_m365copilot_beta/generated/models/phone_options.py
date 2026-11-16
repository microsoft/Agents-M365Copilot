from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneOptions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A read-only, Microsoft-defined list of regions that already enable MFA. For more information, see the following list of countries.
    default_regions: Optional[list[int]] = None
    # A numbers-only set representing the region telecom codes to prevent or disable the telephony service. Validates against current International Subscriber Dialing (ISD) country codes where the maximum code length is 4. Values must be non-null.
    exclude_regions: Optional[list[int]] = None
    # A numbers-only set representing the country codes that can be manually added to enable telephony service in those regions, in addition to the list of countries that are already enabled. For more information about regions that require opt in, see Regions that need to opt in for MFA telephony verification. Validates against current International Subscriber Dialing (ISD) country codes where the maximum code length is 4. Values must be positive integers and can't overlap with 'excludeRegions'.
    include_additional_regions: Optional[list[int]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "defaultRegions": lambda n : setattr(self, 'default_regions', n.get_collection_of_primitive_values(int)),
            "excludeRegions": lambda n : setattr(self, 'exclude_regions', n.get_collection_of_primitive_values(int)),
            "includeAdditionalRegions": lambda n : setattr(self, 'include_additional_regions', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("defaultRegions", self.default_regions)
        writer.write_collection_of_primitive_values("excludeRegions", self.exclude_regions)
        writer.write_collection_of_primitive_values("includeAdditionalRegions", self.include_additional_regions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

