from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aad_source import AadSource
    from .aws_source import AwsSource
    from .azure_source import AzureSource
    from .gsuite_source import GsuiteSource
    from .unknown_source import UnknownSource

@dataclass
class AuthorizationSystemIdentitySource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Type of identity provider. Read-only.
    identity_provider_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizationSystemIdentitySource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystemIdentitySource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadSource".casefold():
            from .aad_source import AadSource

            return AadSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsSource".casefold():
            from .aws_source import AwsSource

            return AwsSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureSource".casefold():
            from .azure_source import AzureSource

            return AzureSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gsuiteSource".casefold():
            from .gsuite_source import GsuiteSource

            return GsuiteSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unknownSource".casefold():
            from .unknown_source import UnknownSource

            return UnknownSource()
        return AuthorizationSystemIdentitySource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aad_source import AadSource
        from .aws_source import AwsSource
        from .azure_source import AzureSource
        from .gsuite_source import GsuiteSource
        from .unknown_source import UnknownSource

        from .aad_source import AadSource
        from .aws_source import AwsSource
        from .azure_source import AzureSource
        from .gsuite_source import GsuiteSource
        from .unknown_source import UnknownSource

        fields: dict[str, Callable[[Any], None]] = {
            "identityProviderType": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
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
        writer.write_str_value("identityProviderType", self.identity_provider_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

