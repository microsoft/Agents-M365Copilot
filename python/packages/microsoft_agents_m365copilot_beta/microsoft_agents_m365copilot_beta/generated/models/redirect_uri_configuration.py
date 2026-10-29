from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .redirect_uri_allowed_domain_configuration import RedirectUriAllowedDomainConfiguration
    from .redirect_uri_allowed_scheme_configuration import RedirectUriAllowedSchemeConfiguration
    from .redirect_uri_blocked_domain_configuration import RedirectUriBlockedDomainConfiguration
    from .redirect_uri_blocked_scheme_configuration import RedirectUriBlockedSchemeConfiguration
    from .redirect_uri_wildcard_configuration import RedirectUriWildcardConfiguration

@dataclass
class RedirectUriConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Configuration that specifies blocked domains for redirect URIs with global and platform-specific settings.
    uri_with_blocked_domain: Optional[RedirectUriBlockedDomainConfiguration] = None
    # Configuration that specifies blocked URI schemes for redirect URIs with global and platform-specific settings and exempt format patterns.
    uri_with_blocked_scheme: Optional[RedirectUriBlockedSchemeConfiguration] = None
    # Configuration that controls the use of wildcard patterns in redirect URIs with configurable exceptions.
    uri_with_wildcard: Optional[RedirectUriWildcardConfiguration] = None
    # Configuration that specifies allowed domains for redirect URIs with global and platform-specific settings.
    uri_without_allowed_domain: Optional[RedirectUriAllowedDomainConfiguration] = None
    # Configuration that specifies allowed URI schemes for redirect URIs with global and platform-specific settings.
    uri_without_allowed_scheme: Optional[RedirectUriAllowedSchemeConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectUriConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectUriConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectUriConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .redirect_uri_allowed_domain_configuration import RedirectUriAllowedDomainConfiguration
        from .redirect_uri_allowed_scheme_configuration import RedirectUriAllowedSchemeConfiguration
        from .redirect_uri_blocked_domain_configuration import RedirectUriBlockedDomainConfiguration
        from .redirect_uri_blocked_scheme_configuration import RedirectUriBlockedSchemeConfiguration
        from .redirect_uri_wildcard_configuration import RedirectUriWildcardConfiguration

        from .redirect_uri_allowed_domain_configuration import RedirectUriAllowedDomainConfiguration
        from .redirect_uri_allowed_scheme_configuration import RedirectUriAllowedSchemeConfiguration
        from .redirect_uri_blocked_domain_configuration import RedirectUriBlockedDomainConfiguration
        from .redirect_uri_blocked_scheme_configuration import RedirectUriBlockedSchemeConfiguration
        from .redirect_uri_wildcard_configuration import RedirectUriWildcardConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uriWithBlockedDomain": lambda n : setattr(self, 'uri_with_blocked_domain', n.get_object_value(RedirectUriBlockedDomainConfiguration)),
            "uriWithBlockedScheme": lambda n : setattr(self, 'uri_with_blocked_scheme', n.get_object_value(RedirectUriBlockedSchemeConfiguration)),
            "uriWithWildcard": lambda n : setattr(self, 'uri_with_wildcard', n.get_object_value(RedirectUriWildcardConfiguration)),
            "uriWithoutAllowedDomain": lambda n : setattr(self, 'uri_without_allowed_domain', n.get_object_value(RedirectUriAllowedDomainConfiguration)),
            "uriWithoutAllowedScheme": lambda n : setattr(self, 'uri_without_allowed_scheme', n.get_object_value(RedirectUriAllowedSchemeConfiguration)),
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
        writer.write_object_value("uriWithBlockedDomain", self.uri_with_blocked_domain)
        writer.write_object_value("uriWithBlockedScheme", self.uri_with_blocked_scheme)
        writer.write_object_value("uriWithWildcard", self.uri_with_wildcard)
        writer.write_object_value("uriWithoutAllowedDomain", self.uri_without_allowed_domain)
        writer.write_object_value("uriWithoutAllowedScheme", self.uri_without_allowed_scheme)
        writer.write_additional_data_value(self.additional_data)
    

