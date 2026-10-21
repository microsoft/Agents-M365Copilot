from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_typed_value_pair import KeyTypedValuePair
    from .single_sign_on_extension import SingleSignOnExtension

from .single_sign_on_extension import SingleSignOnExtension

@dataclass
class RedirectSingleSignOnExtension(SingleSignOnExtension, Parsable):
    """
    Represents an Apple Single Sign-On Extension.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.redirectSingleSignOnExtension"
    # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
    configurations: Optional[list[KeyTypedValuePair]] = None
    # Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
    extension_identifier: Optional[str] = None
    # Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
    team_identifier: Optional[str] = None
    # One or more URL prefixes of identity providers on whose behalf the app extension performs single sign-on. URLs must begin with http:// or https://. All URL prefixes must be unique for all profiles.
    url_prefixes: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectSingleSignOnExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_typed_value_pair import KeyTypedValuePair
        from .single_sign_on_extension import SingleSignOnExtension

        from .key_typed_value_pair import KeyTypedValuePair
        from .single_sign_on_extension import SingleSignOnExtension

        fields: dict[str, Callable[[Any], None]] = {
            "configurations": lambda n : setattr(self, 'configurations', n.get_collection_of_object_values(KeyTypedValuePair)),
            "extensionIdentifier": lambda n : setattr(self, 'extension_identifier', n.get_str_value()),
            "teamIdentifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
            "urlPrefixes": lambda n : setattr(self, 'url_prefixes', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("configurations", self.configurations)
        writer.write_str_value("extensionIdentifier", self.extension_identifier)
        writer.write_str_value("teamIdentifier", self.team_identifier)
        writer.write_collection_of_primitive_values("urlPrefixes", self.url_prefixes)
    

