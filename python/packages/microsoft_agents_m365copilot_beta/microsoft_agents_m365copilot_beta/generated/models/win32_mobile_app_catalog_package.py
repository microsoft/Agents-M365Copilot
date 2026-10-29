from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_catalog_package import MobileAppCatalogPackage
    from .windows_architecture import WindowsArchitecture

from .mobile_app_catalog_package import MobileAppCatalogPackage

@dataclass
class Win32MobileAppCatalogPackage(MobileAppCatalogPackage, Parsable):
    """
    win32MobileAppCatalogPackage extends mobileAppCatalogPackage by providing information necessary for the creation of a win32CatalogApp instance.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32MobileAppCatalogPackage"
    # Contains properties for Windows architecture.
    applicable_architectures: Optional[WindowsArchitecture] = None
    # The product branch name, which is a specific subset of product functionality as defined by the publisher (example: "Fabrikam for Business (x64)"). A specific product will have one or more branchDisplayNames. Read-only. Supports $filter, $search, $select. This property is read-only.
    branch_display_name: Optional[str] = None
    # The identifier of a specific branch irrespective of version, or other attributes. This id is associated with the branchDisplayName. Read-only. This property is read-only.
    branch_id: Optional[str] = None
    # One or more locale(s) supported by the branch. Value is a two-letter ISO 639 language tags with optional two-letter subtags (example: en-US, ko, de, de-DE), or mul to indicate multi-language. Read-only. This property is read-only.
    locales: Optional[list[str]] = None
    # Indicates whether the package is capable to auto-update to latest when software/application updates are available. When TRUE, it indicates it is an auto-updating application. When FALSE, it indicates that it is not an auto-updating application. This property is read-only.
    package_auto_update_capable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32MobileAppCatalogPackage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32MobileAppCatalogPackage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32MobileAppCatalogPackage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .windows_architecture import WindowsArchitecture

        from .mobile_app_catalog_package import MobileAppCatalogPackage
        from .windows_architecture import WindowsArchitecture

        fields: dict[str, Callable[[Any], None]] = {
            "applicableArchitectures": lambda n : setattr(self, 'applicable_architectures', n.get_collection_of_enum_values(WindowsArchitecture)),
            "branchDisplayName": lambda n : setattr(self, 'branch_display_name', n.get_str_value()),
            "branchId": lambda n : setattr(self, 'branch_id', n.get_str_value()),
            "locales": lambda n : setattr(self, 'locales', n.get_collection_of_primitive_values(str)),
            "packageAutoUpdateCapable": lambda n : setattr(self, 'package_auto_update_capable', n.get_bool_value()),
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
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
    

