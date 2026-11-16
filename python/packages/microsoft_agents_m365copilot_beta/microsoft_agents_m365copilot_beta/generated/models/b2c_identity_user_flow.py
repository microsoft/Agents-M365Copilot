from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_provider import IdentityProvider
    from .identity_provider_base import IdentityProviderBase
    from .identity_user_flow import IdentityUserFlow
    from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
    from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
    from .user_flow_language_configuration import UserFlowLanguageConfiguration

from .identity_user_flow import IdentityUserFlow

@dataclass
class B2cIdentityUserFlow(IdentityUserFlow, Parsable):
    # Configuration for enabling an API connector for use as part of the user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
    api_connector_configuration: Optional[UserFlowApiConnectorConfiguration] = None
    # Indicates the default language of the b2cIdentityUserFlow that is used when no ui_locale tag is specified in the request. This field is RFC 5646 compliant.
    default_language_tag: Optional[str] = None
    # The identity providers included in the user flow.
    identity_providers: Optional[list[IdentityProvider]] = None
    # The property that determines whether language customization is enabled within the B2C user flow. Language customization is not enabled by default for B2C user flows.
    is_language_customization_enabled: Optional[bool] = None
    # The languages supported for customization within the user flow. Language customization is not enabled by default in B2C user flows.
    languages: Optional[list[UserFlowLanguageConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user attribute assignments included in the user flow.
    user_attribute_assignments: Optional[list[IdentityUserFlowAttributeAssignment]] = None
    # The identity providers included in the user flow.
    user_flow_identity_providers: Optional[list[IdentityProviderBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> B2cIdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: B2cIdentityUserFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return B2cIdentityUserFlow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_provider import IdentityProvider
        from .identity_provider_base import IdentityProviderBase
        from .identity_user_flow import IdentityUserFlow
        from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
        from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
        from .user_flow_language_configuration import UserFlowLanguageConfiguration

        from .identity_provider import IdentityProvider
        from .identity_provider_base import IdentityProviderBase
        from .identity_user_flow import IdentityUserFlow
        from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
        from .user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
        from .user_flow_language_configuration import UserFlowLanguageConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "apiConnectorConfiguration": lambda n : setattr(self, 'api_connector_configuration', n.get_object_value(UserFlowApiConnectorConfiguration)),
            "defaultLanguageTag": lambda n : setattr(self, 'default_language_tag', n.get_str_value()),
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(IdentityProvider)),
            "isLanguageCustomizationEnabled": lambda n : setattr(self, 'is_language_customization_enabled', n.get_bool_value()),
            "languages": lambda n : setattr(self, 'languages', n.get_collection_of_object_values(UserFlowLanguageConfiguration)),
            "userAttributeAssignments": lambda n : setattr(self, 'user_attribute_assignments', n.get_collection_of_object_values(IdentityUserFlowAttributeAssignment)),
            "userFlowIdentityProviders": lambda n : setattr(self, 'user_flow_identity_providers', n.get_collection_of_object_values(IdentityProviderBase)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("apiConnectorConfiguration", self.api_connector_configuration)
        writer.write_str_value("defaultLanguageTag", self.default_language_tag)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_bool_value("isLanguageCustomizationEnabled", self.is_language_customization_enabled)
        writer.write_collection_of_object_values("languages", self.languages)
        writer.write_collection_of_object_values("userAttributeAssignments", self.user_attribute_assignments)
        writer.write_collection_of_object_values("userFlowIdentityProviders", self.user_flow_identity_providers)
    

