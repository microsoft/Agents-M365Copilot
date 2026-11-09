from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_catalog_package import MobileAppCatalogPackage
    from .win32_lob_app import Win32LobApp

from .win32_lob_app import Win32LobApp

@dataclass
class Win32CatalogApp(Win32LobApp, Parsable):
    """
    A mobileApp that is based on a referenced application in a Win32CatalogApp repository
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32CatalogApp"
    # The latest available catalog package the app is upgradeable to. This property is read-only.
    latest_upgrade_catalog_package: Optional[MobileAppCatalogPackage] = None
    # The mobileAppCatalogPackageId property references the mobileAppCatalogPackage entity which contains information about an application catalog package that can be deployed to Intune-managed devices
    mobile_app_catalog_package_id: Optional[str] = None
    # The current catalog package the app is synced from. This property is read-only.
    referenced_catalog_package: Optional[MobileAppCatalogPackage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32CatalogApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32CatalogApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32CatalogApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .win32_lob_app import Win32LobApp

        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .win32_lob_app import Win32LobApp

        fields: dict[str, Callable[[Any], None]] = {
            "latestUpgradeCatalogPackage": lambda n : setattr(self, 'latest_upgrade_catalog_package', n.get_object_value(MobileAppCatalogPackage)),
            "mobileAppCatalogPackageId": lambda n : setattr(self, 'mobile_app_catalog_package_id', n.get_str_value()),
            "referencedCatalogPackage": lambda n : setattr(self, 'referenced_catalog_package', n.get_object_value(MobileAppCatalogPackage)),
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
        writer.write_object_value("latestUpgradeCatalogPackage", self.latest_upgrade_catalog_package)
        writer.write_str_value("mobileAppCatalogPackageId", self.mobile_app_catalog_package_id)
        writer.write_object_value("referencedCatalogPackage", self.referenced_catalog_package)
    

