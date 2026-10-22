from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsAssignedAccessProfile(Entity, Parsable):
    """
    Assigned Access profile for Windows.
    """
    # These are the only Windows Store Apps that will be available to launch from the Start menu.
    app_user_model_ids: Optional[list[str]] = None
    # These are the paths of the Desktop Apps that will be available on the Start menu and the only apps the user will be able to launch.
    desktop_app_paths: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
    profile_name: Optional[str] = None
    # This setting allows the admin to specify whether the Task Bar is shown or not.
    show_task_bar: Optional[bool] = None
    # Allows admins to override the default Start layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in Binary format.
    start_menu_layout_xml: Optional[bytes] = None
    # The user accounts that will be locked to this kiosk configuration.
    user_accounts: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAssignedAccessProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAssignedAccessProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsAssignedAccessProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "appUserModelIds": lambda n : setattr(self, 'app_user_model_ids', n.get_collection_of_primitive_values(str)),
            "desktopAppPaths": lambda n : setattr(self, 'desktop_app_paths', n.get_collection_of_primitive_values(str)),
            "profileName": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "showTaskBar": lambda n : setattr(self, 'show_task_bar', n.get_bool_value()),
            "startMenuLayoutXml": lambda n : setattr(self, 'start_menu_layout_xml', n.get_bytes_value()),
            "userAccounts": lambda n : setattr(self, 'user_accounts', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("appUserModelIds", self.app_user_model_ids)
        writer.write_collection_of_primitive_values("desktopAppPaths", self.desktop_app_paths)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_bool_value("showTaskBar", self.show_task_bar)
        writer.write_bytes_value("startMenuLayoutXml", self.start_menu_layout_xml)
        writer.write_collection_of_primitive_values("userAccounts", self.user_accounts)
    

