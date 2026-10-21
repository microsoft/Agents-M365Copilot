from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_privacy_data_access_level import WindowsPrivacyDataAccessLevel
    from .windows_privacy_data_category import WindowsPrivacyDataCategory

from .entity import Entity

@dataclass
class WindowsPrivacyDataAccessControlItem(Entity, Parsable):
    """
    Specify access control level per privacy data category
    """
    # Determine the access level to specific Windows privacy data category.
    access_level: Optional[WindowsPrivacyDataAccessLevel] = None
    # The Package Family Name of a Windows app. When set, the access level applies to the specified application.
    app_display_name: Optional[str] = None
    # The Package Family Name of a Windows app. When set, the access level applies to the specified application.
    app_package_family_name: Optional[str] = None
    # Windows privacy data category specifier for privacy data access.
    data_category: Optional[WindowsPrivacyDataCategory] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPrivacyDataAccessControlItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPrivacyDataAccessControlItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPrivacyDataAccessControlItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_privacy_data_access_level import WindowsPrivacyDataAccessLevel
        from .windows_privacy_data_category import WindowsPrivacyDataCategory

        from .entity import Entity
        from .windows_privacy_data_access_level import WindowsPrivacyDataAccessLevel
        from .windows_privacy_data_category import WindowsPrivacyDataCategory

        fields: dict[str, Callable[[Any], None]] = {
            "accessLevel": lambda n : setattr(self, 'access_level', n.get_enum_value(WindowsPrivacyDataAccessLevel)),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appPackageFamilyName": lambda n : setattr(self, 'app_package_family_name', n.get_str_value()),
            "dataCategory": lambda n : setattr(self, 'data_category', n.get_enum_value(WindowsPrivacyDataCategory)),
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
        writer.write_enum_value("accessLevel", self.access_level)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appPackageFamilyName", self.app_package_family_name)
        writer.write_enum_value("dataCategory", self.data_category)
    

