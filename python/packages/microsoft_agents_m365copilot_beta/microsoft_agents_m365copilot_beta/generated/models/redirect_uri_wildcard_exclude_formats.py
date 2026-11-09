from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RedirectUriWildcardExcludeFormats(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # When true, blocks the use of wildcards in the path portion of redirect URIs. When false, allows wildcards in paths.
    exclude_wildcards_in_path: Optional[bool] = None
    # Collection of domain names where wildcards in the path portion of redirect URIs are blocked. Accepts only valid host names (no wildcards) as defined in RFC 3986 §3.2.2. For example, login.microsoft.com or contoso.com.
    exclude_wildcards_in_path_with_domains: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectUriWildcardExcludeFormats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectUriWildcardExcludeFormats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectUriWildcardExcludeFormats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "excludeWildcardsInPath": lambda n : setattr(self, 'exclude_wildcards_in_path', n.get_bool_value()),
            "excludeWildcardsInPathWithDomains": lambda n : setattr(self, 'exclude_wildcards_in_path_with_domains', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("excludeWildcardsInPath", self.exclude_wildcards_in_path)
        writer.write_collection_of_primitive_values("excludeWildcardsInPathWithDomains", self.exclude_wildcards_in_path_with_domains)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

