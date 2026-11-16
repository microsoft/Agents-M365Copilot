from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ZebraFotaArtifact(Entity, Parsable):
    """
    Describes a single artifact for a specific device model.
    """
    # The version of the Board Support Package (BSP. E.g.: 01.18.02.00)
    board_support_package_version: Optional[str] = None
    # Artifact description. (e.g.: `LifeGuard Update 98 (released 24-September-2021)
    description: Optional[str] = None
    # Applicable device model (e.g.: TC8300)
    device_model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Artifact OS version (e.g.: 8.1.0)
    os_version: Optional[str] = None
    # Artifact patch version (e.g.: U00)
    patch_version: Optional[str] = None
    # Artifact release notes URL (e.g.: https://www.zebra.com/<filename.pdf>)
    release_notes_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ZebraFotaArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaArtifact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ZebraFotaArtifact()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "boardSupportPackageVersion": lambda n : setattr(self, 'board_support_package_version', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "patchVersion": lambda n : setattr(self, 'patch_version', n.get_str_value()),
            "releaseNotesUrl": lambda n : setattr(self, 'release_notes_url', n.get_str_value()),
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
        writer.write_str_value("boardSupportPackageVersion", self.board_support_package_version)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("patchVersion", self.patch_version)
        writer.write_str_value("releaseNotesUrl", self.release_notes_url)
    

