from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .network_type import NetworkType

@dataclass
class NetworkLocationDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Provides the name of the network used when signing in.
    network_names: Optional[list[str]] = None
    # Provides the type of network used when signing in. The possible values are: intranet, extranet, namedNetwork, trusted, unknownFutureValue.
    network_type: Optional[NetworkType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkLocationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkLocationDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkLocationDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .network_type import NetworkType

        from .network_type import NetworkType

        fields: dict[str, Callable[[Any], None]] = {
            "networkNames": lambda n : setattr(self, 'network_names', n.get_collection_of_primitive_values(str)),
            "networkType": lambda n : setattr(self, 'network_type', n.get_enum_value(NetworkType)),
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
        writer.write_collection_of_primitive_values("networkNames", self.network_names)
        writer.write_enum_value("networkType", self.network_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

