from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings
    from .win_get_app_install_time_settings import WinGetAppInstallTimeSettings
    from .win_get_app_notification import WinGetAppNotification
    from .win_get_app_restart_settings import WinGetAppRestartSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class WinGetAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign a WinGet app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.winGetAppAssignmentSettings"
    # The install time settings to apply for this app assignment.
    install_time_settings: Optional[WinGetAppInstallTimeSettings] = None
    # Contains value for notification status.
    notifications: Optional[WinGetAppNotification] = None
    # The reboot settings to apply for this app assignment.
    restart_settings: Optional[WinGetAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WinGetAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WinGetAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WinGetAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .win_get_app_install_time_settings import WinGetAppInstallTimeSettings
        from .win_get_app_notification import WinGetAppNotification
        from .win_get_app_restart_settings import WinGetAppRestartSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .win_get_app_install_time_settings import WinGetAppInstallTimeSettings
        from .win_get_app_notification import WinGetAppNotification
        from .win_get_app_restart_settings import WinGetAppRestartSettings

        fields: dict[str, Callable[[Any], None]] = {
            "installTimeSettings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(WinGetAppInstallTimeSettings)),
            "notifications": lambda n : setattr(self, 'notifications', n.get_enum_value(WinGetAppNotification)),
            "restartSettings": lambda n : setattr(self, 'restart_settings', n.get_object_value(WinGetAppRestartSettings)),
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
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notifications", self.notifications)
        writer.write_object_value("restartSettings", self.restart_settings)
    

