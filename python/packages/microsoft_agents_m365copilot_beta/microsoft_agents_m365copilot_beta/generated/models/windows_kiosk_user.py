from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup
    from .windows_kiosk_autologon import WindowsKioskAutologon
    from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup
    from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser
    from .windows_kiosk_local_group import WindowsKioskLocalGroup
    from .windows_kiosk_local_user import WindowsKioskLocalUser
    from .windows_kiosk_visitor import WindowsKioskVisitor

@dataclass
class WindowsKioskUser(AdditionalDataHolder, Parsable):
    """
    The user base class used to identify the account info for the kiosk configuration
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskActiveDirectoryGroup".casefold():
            from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup

            return WindowsKioskActiveDirectoryGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskAutologon".casefold():
            from .windows_kiosk_autologon import WindowsKioskAutologon

            return WindowsKioskAutologon()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskAzureADGroup".casefold():
            from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup

            return WindowsKioskAzureADGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskAzureADUser".casefold():
            from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser

            return WindowsKioskAzureADUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskLocalGroup".casefold():
            from .windows_kiosk_local_group import WindowsKioskLocalGroup

            return WindowsKioskLocalGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskLocalUser".casefold():
            from .windows_kiosk_local_user import WindowsKioskLocalUser

            return WindowsKioskLocalUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskVisitor".casefold():
            from .windows_kiosk_visitor import WindowsKioskVisitor

            return WindowsKioskVisitor()
        return WindowsKioskUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup
        from .windows_kiosk_autologon import WindowsKioskAutologon
        from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup
        from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser
        from .windows_kiosk_local_group import WindowsKioskLocalGroup
        from .windows_kiosk_local_user import WindowsKioskLocalUser
        from .windows_kiosk_visitor import WindowsKioskVisitor

        from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup
        from .windows_kiosk_autologon import WindowsKioskAutologon
        from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup
        from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser
        from .windows_kiosk_local_group import WindowsKioskLocalGroup
        from .windows_kiosk_local_user import WindowsKioskLocalUser
        from .windows_kiosk_visitor import WindowsKioskVisitor

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

