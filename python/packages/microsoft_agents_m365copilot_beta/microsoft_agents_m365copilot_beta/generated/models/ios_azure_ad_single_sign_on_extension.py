from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_single_sign_on_extension import IosSingleSignOnExtension
    from .key_typed_value_pair import KeyTypedValuePair

from .ios_single_sign_on_extension import IosSingleSignOnExtension

@dataclass
class IosAzureAdSingleSignOnExtension(IosSingleSignOnExtension, Parsable):
    """
    Represents an Azure AD-type Single Sign-On extension profile for iOS devices.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosAzureAdSingleSignOnExtension"
    # An optional list of additional bundle IDs allowed to use the AAD extension for single sign-on.
    bundle_id_access_control_list: Optional[list[str]] = None
    # Gets or sets a list of typed key-value pairs used to configure Credential-type profiles. This collection can contain a maximum of 500 elements.
    configurations: Optional[list[KeyTypedValuePair]] = None
    # Enables or disables shared device mode.
    enable_shared_device_mode: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosAzureAdSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosAzureAdSingleSignOnExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosAzureAdSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ios_single_sign_on_extension import IosSingleSignOnExtension
        from .key_typed_value_pair import KeyTypedValuePair

        from .ios_single_sign_on_extension import IosSingleSignOnExtension
        from .key_typed_value_pair import KeyTypedValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "bundleIdAccessControlList": lambda n : setattr(self, 'bundle_id_access_control_list', n.get_collection_of_primitive_values(str)),
            "configurations": lambda n : setattr(self, 'configurations', n.get_collection_of_object_values(KeyTypedValuePair)),
            "enableSharedDeviceMode": lambda n : setattr(self, 'enable_shared_device_mode', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("bundleIdAccessControlList", self.bundle_id_access_control_list)
        writer.write_collection_of_object_values("configurations", self.configurations)
        writer.write_bool_value("enableSharedDeviceMode", self.enable_shared_device_mode)
    

