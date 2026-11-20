from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IdJagIdentifierUriConfiguration(AdditionalDataHolder, Parsable):
    """
    Identifier URIs classified for the ID-JAG protocol. Each value must also exist exactly in the application's top-level identifierUris. Clearing this classification doesn't remove top-level identifierUris; complete deletion requires removing the URI from identifierUris and every referencing protocol classification in the same Application PATCH. Must use HTTPS; api://, wildcards, query strings, fragments, and explicit ports 80 or 443 are not supported. Other explicit ports remain significant. Values are compared using Unicode code-point equality without URI normalization.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Required and non-null when ID-JAG identifier URI configuration is supplied. Application identifier URIs opted into outbound ID-JAG. Must exactly match values in top-level identifierUris in the prospective final state. Explicit ports 80 and 443 are rejected; other ports remain significant. An empty collection normalizes the parent to null without changing top-level identifierUris.
    uris: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdJagIdentifierUriConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdJagIdentifierUriConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdJagIdentifierUriConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uris": lambda n : setattr(self, 'uris', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("uris", self.uris)
        writer.write_additional_data_value(self.additional_data)
    

