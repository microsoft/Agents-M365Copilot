from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app import MobileApp
    from .win_get_app_install_experience import WinGetAppInstallExperience

from .mobile_app import MobileApp

@dataclass
class WinGetApp(MobileApp, Parsable):
    """
    A MobileApp that is based on a referenced application in a WinGet repository.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.winGetApp"
    # The install experience settings associated with this application, which are used to ensure the desired install experiences on the target device are taken into account. This includes the account type (System or User) that actions should be run as on target devices. Required at creation time.
    install_experience: Optional[WinGetAppInstallExperience] = None
    # Hash of package metadata properties used to validate that the application matches the metadata in the source repository.
    manifest_hash: Optional[str] = None
    # The PackageIdentifier from the WinGet source repository REST API. This also maps to the Id when using the WinGet client command line application. Required at creation time, cannot be modified on existing objects.
    package_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WinGetApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WinGetApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WinGetApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app import MobileApp
        from .win_get_app_install_experience import WinGetAppInstallExperience

        from .mobile_app import MobileApp
        from .win_get_app_install_experience import WinGetAppInstallExperience

        fields: dict[str, Callable[[Any], None]] = {
            "installExperience": lambda n : setattr(self, 'install_experience', n.get_object_value(WinGetAppInstallExperience)),
            "manifestHash": lambda n : setattr(self, 'manifest_hash', n.get_str_value()),
            "packageIdentifier": lambda n : setattr(self, 'package_identifier', n.get_str_value()),
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
        writer.write_object_value("installExperience", self.install_experience)
        writer.write_str_value("manifestHash", self.manifest_hash)
        writer.write_str_value("packageIdentifier", self.package_identifier)
    

