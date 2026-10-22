from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .managed_device_architecture import ManagedDeviceArchitecture
    from .managed_device_windows_operating_system_edition import ManagedDeviceWindowsOperatingSystemEdition
    from .managed_device_windows_operating_system_update import ManagedDeviceWindowsOperatingSystemUpdate

from .entity import Entity

@dataclass
class ManagedDeviceWindowsOperatingSystemImage(Entity, Parsable):
    """
    This entity defines different Windows Operating System products, like 'Windows 11 22H1', 'Windows 11 22H2' etc., along with their available configurations.
    """
    # Indicates the available Quality/Security updates for a specific Windows product version (example: Windows 11 22H1), for upto last 3 Patch Tuesdays . This value in the API response would be updated 2-3 days after every Patch Tuesday. Supports: $filter, $select, $top, $skip. Read-only.
    available_updates: Optional[list[ManagedDeviceWindowsOperatingSystemUpdate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the list of architectures supported by the image. E.g. ['ARM64','X86']. Supports: $filter, $select, $top, $skip. Read-only.
    supported_architectures: Optional[list[ManagedDeviceArchitecture]] = None
    # Indicates the list of editions supported by the image along with their support dates. Supports: $filter, $select, $top, $skip. Read-only.
    supported_editions: Optional[list[ManagedDeviceWindowsOperatingSystemEdition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceWindowsOperatingSystemImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceWindowsOperatingSystemImage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceWindowsOperatingSystemImage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .managed_device_architecture import ManagedDeviceArchitecture
        from .managed_device_windows_operating_system_edition import ManagedDeviceWindowsOperatingSystemEdition
        from .managed_device_windows_operating_system_update import ManagedDeviceWindowsOperatingSystemUpdate

        from .entity import Entity
        from .managed_device_architecture import ManagedDeviceArchitecture
        from .managed_device_windows_operating_system_edition import ManagedDeviceWindowsOperatingSystemEdition
        from .managed_device_windows_operating_system_update import ManagedDeviceWindowsOperatingSystemUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "availableUpdates": lambda n : setattr(self, 'available_updates', n.get_collection_of_object_values(ManagedDeviceWindowsOperatingSystemUpdate)),
            "supportedArchitectures": lambda n : setattr(self, 'supported_architectures', n.get_collection_of_enum_values(ManagedDeviceArchitecture)),
            "supportedEditions": lambda n : setattr(self, 'supported_editions', n.get_collection_of_object_values(ManagedDeviceWindowsOperatingSystemEdition)),
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
        writer.write_collection_of_object_values("availableUpdates", self.available_updates)
        writer.write_collection_of_enum_values("supportedArchitectures", self.supported_architectures)
        writer.write_collection_of_object_values("supportedEditions", self.supported_editions)
    

