from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .organizational_branding_theme_localization import OrganizationalBrandingThemeLocalization

from .entity import Entity

@dataclass
class OrganizationalBrandingTheme(Entity, Parsable):
    # Indicates whether the theme is set as the default branding theme for the entire tenant and includes all applications within the tenant. When set to true, this theme is automatically applied to any application that does not have a specific theme assigned. This property is useful for enforcing consistent branding across multiple apps without configuring each one individually. Optional.
    is_default_theme: Optional[bool] = None
    # Represents a locale-based branding theme.
    localizations: Optional[list[OrganizationalBrandingThemeLocalization]] = None
    # The name of the branding theme. Up to 120 characters. Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationalBrandingTheme:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBrandingTheme
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationalBrandingTheme()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .organizational_branding_theme_localization import OrganizationalBrandingThemeLocalization

        from .entity import Entity
        from .organizational_branding_theme_localization import OrganizationalBrandingThemeLocalization

        fields: dict[str, Callable[[Any], None]] = {
            "isDefaultTheme": lambda n : setattr(self, 'is_default_theme', n.get_bool_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(OrganizationalBrandingThemeLocalization)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_bool_value("isDefaultTheme", self.is_default_theme)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_str_value("name", self.name)
    

