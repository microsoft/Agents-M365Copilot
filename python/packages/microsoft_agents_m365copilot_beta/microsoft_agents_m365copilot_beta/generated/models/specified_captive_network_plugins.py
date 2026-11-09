from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SpecifiedCaptiveNetworkPlugins(AdditionalDataHolder, Parsable):
    """
    Specifies all the Captive network plugins allowed during the IKEv2 AlwaysOn VPN connection
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
    allowed_bundle_identifiers: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecifiedCaptiveNetworkPlugins:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecifiedCaptiveNetworkPlugins
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpecifiedCaptiveNetworkPlugins()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowedBundleIdentifiers": lambda n : setattr(self, 'allowed_bundle_identifiers', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedBundleIdentifiers", self.allowed_bundle_identifiers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

