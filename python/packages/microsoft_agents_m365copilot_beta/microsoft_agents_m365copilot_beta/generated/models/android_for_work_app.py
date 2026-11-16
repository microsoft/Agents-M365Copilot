from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class AndroidForWorkApp(MobileApp, Parsable):
    """
    Contains properties and inherited properties for Android for Work (AFW) Apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkApp"
    # The Identity Name. This property is read-only.
    app_identifier: Optional[str] = None
    # The Play for Work Store app URL.
    app_store_url: Optional[str] = None
    # The package identifier. This property is read-only.
    package_id: Optional[str] = None
    # The total number of VPP licenses.
    total_license_count: Optional[int] = None
    # The number of VPP licenses in use.
    used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app import MobileApp

        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "appIdentifier": lambda n : setattr(self, 'app_identifier', n.get_str_value()),
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
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
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    

