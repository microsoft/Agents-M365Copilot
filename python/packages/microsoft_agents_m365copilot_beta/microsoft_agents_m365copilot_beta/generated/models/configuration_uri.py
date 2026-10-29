from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .uri_usage_type import UriUsageType

@dataclass
class ConfigurationUri(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The single sign-on mode that the URI is configured for. The possible values are: saml, password.
    applies_to_single_sign_on_mode: Optional[str] = None
    # The various formats that the URI should follow.
    examples: Optional[list[str]] = None
    # Indicates whether this URI is required for the single sign-on configuration.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The usage property
    usage: Optional[UriUsageType] = None
    # The suggested values for the URI. Developers may need to customize these values for their tenant.
    values: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationUri:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationUri
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationUri()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .uri_usage_type import UriUsageType

        from .uri_usage_type import UriUsageType

        fields: dict[str, Callable[[Any], None]] = {
            "appliesToSingleSignOnMode": lambda n : setattr(self, 'applies_to_single_sign_on_mode', n.get_str_value()),
            "examples": lambda n : setattr(self, 'examples', n.get_collection_of_primitive_values(str)),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "usage": lambda n : setattr(self, 'usage', n.get_enum_value(UriUsageType)),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("appliesToSingleSignOnMode", self.applies_to_single_sign_on_mode)
        writer.write_collection_of_primitive_values("examples", self.examples)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("usage", self.usage)
        writer.write_collection_of_primitive_values("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    

