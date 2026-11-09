from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_typed_value_pair import KeyTypedValuePair
    from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension

from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension

@dataclass
class MacOSCredentialSingleSignOnExtension(MacOSSingleSignOnExtension, Parsable):
    """
    Represents a Credential-type Single Sign-On extension profile for macOS devices.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSCredentialSingleSignOnExtension"
    # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
    configurations: Optional[list[KeyTypedValuePair]] = None
    # Gets or sets a list of hosts or domain names for which the app extension performs SSO.
    domains: Optional[list[str]] = None
    # Gets or sets the bundle ID of the app extension that performs SSO for the specified URLs.
    extension_identifier: Optional[str] = None
    # Gets or sets the case-sensitive realm name for this profile.
    realm: Optional[str] = None
    # Gets or sets the team ID of the app extension that performs SSO for the specified URLs.
    team_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSCredentialSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCredentialSingleSignOnExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSCredentialSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_typed_value_pair import KeyTypedValuePair
        from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension

        from .key_typed_value_pair import KeyTypedValuePair
        from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension

        fields: dict[str, Callable[[Any], None]] = {
            "configurations": lambda n : setattr(self, 'configurations', n.get_collection_of_object_values(KeyTypedValuePair)),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "extensionIdentifier": lambda n : setattr(self, 'extension_identifier', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "teamIdentifier": lambda n : setattr(self, 'team_identifier', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_str_value("extensionIdentifier", self.extension_identifier)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("teamIdentifier", self.team_identifier)
    

