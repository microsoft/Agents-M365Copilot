from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .mac_o_s_kernel_extension import MacOSKernelExtension
    from .mac_o_s_system_extension import MacOSSystemExtension
    from .mac_o_s_system_extension_type_mapping import MacOSSystemExtensionTypeMapping

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSExtensionsConfiguration(DeviceConfiguration, Parsable):
    """
    MacOS extensions configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSExtensionsConfiguration"
    # All kernel extensions validly signed by the team identifiers in this list will be allowed to load.
    kernel_extension_allowed_team_identifiers: Optional[list[str]] = None
    # If set to true, users can approve additional kernel extensions not explicitly allowed by configurations profiles.
    kernel_extension_overrides_allowed: Optional[bool] = None
    # A list of kernel extensions that will be allowed to load. . This collection can contain a maximum of 500 elements.
    kernel_extensions_allowed: Optional[list[MacOSKernelExtension]] = None
    # Gets or sets a list of allowed macOS system extensions. This collection can contain a maximum of 500 elements.
    system_extensions_allowed: Optional[list[MacOSSystemExtension]] = None
    # Gets or sets a list of allowed team identifiers. Any system extension signed with any of the specified team identifiers will be approved.
    system_extensions_allowed_team_identifiers: Optional[list[str]] = None
    # Gets or sets a list of allowed macOS system extension types. This collection can contain a maximum of 500 elements.
    system_extensions_allowed_types: Optional[list[MacOSSystemExtensionTypeMapping]] = None
    # Gets or sets whether to allow the user to approve additional system extensions not explicitly allowed by configuration profiles.
    system_extensions_block_override: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSExtensionsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSExtensionsConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSExtensionsConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_kernel_extension import MacOSKernelExtension
        from .mac_o_s_system_extension import MacOSSystemExtension
        from .mac_o_s_system_extension_type_mapping import MacOSSystemExtensionTypeMapping

        from .device_configuration import DeviceConfiguration
        from .mac_o_s_kernel_extension import MacOSKernelExtension
        from .mac_o_s_system_extension import MacOSSystemExtension
        from .mac_o_s_system_extension_type_mapping import MacOSSystemExtensionTypeMapping

        fields: dict[str, Callable[[Any], None]] = {
            "kernelExtensionAllowedTeamIdentifiers": lambda n : setattr(self, 'kernel_extension_allowed_team_identifiers', n.get_collection_of_primitive_values(str)),
            "kernelExtensionOverridesAllowed": lambda n : setattr(self, 'kernel_extension_overrides_allowed', n.get_bool_value()),
            "kernelExtensionsAllowed": lambda n : setattr(self, 'kernel_extensions_allowed', n.get_collection_of_object_values(MacOSKernelExtension)),
            "systemExtensionsAllowed": lambda n : setattr(self, 'system_extensions_allowed', n.get_collection_of_object_values(MacOSSystemExtension)),
            "systemExtensionsAllowedTeamIdentifiers": lambda n : setattr(self, 'system_extensions_allowed_team_identifiers', n.get_collection_of_primitive_values(str)),
            "systemExtensionsAllowedTypes": lambda n : setattr(self, 'system_extensions_allowed_types', n.get_collection_of_object_values(MacOSSystemExtensionTypeMapping)),
            "systemExtensionsBlockOverride": lambda n : setattr(self, 'system_extensions_block_override', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("kernelExtensionAllowedTeamIdentifiers", self.kernel_extension_allowed_team_identifiers)
        writer.write_bool_value("kernelExtensionOverridesAllowed", self.kernel_extension_overrides_allowed)
        writer.write_collection_of_object_values("kernelExtensionsAllowed", self.kernel_extensions_allowed)
        writer.write_collection_of_object_values("systemExtensionsAllowed", self.system_extensions_allowed)
        writer.write_collection_of_primitive_values("systemExtensionsAllowedTeamIdentifiers", self.system_extensions_allowed_team_identifiers)
        writer.write_collection_of_object_values("systemExtensionsAllowedTypes", self.system_extensions_allowed_types)
        writer.write_bool_value("systemExtensionsBlockOverride", self.system_extensions_block_override)
    

