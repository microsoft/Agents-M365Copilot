from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings
    from .windows_auto_update_catalog_app_delivery_optimization_priority import WindowsAutoUpdateCatalogAppDeliveryOptimizationPriority
    from .windows_auto_update_catalog_app_install_time_settings import WindowsAutoUpdateCatalogAppInstallTimeSettings
    from .windows_auto_update_catalog_app_notification_type import WindowsAutoUpdateCatalogAppNotificationType
    from .windows_auto_update_catalog_app_restart_settings import WindowsAutoUpdateCatalogAppRestartSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class WindowsAutoUpdateCatalogAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains per-group deployment configuration for a windowsAutoUpdateCatalogApp. These settings control the end-user experience when the app is deployed to a specific group—including whether notifications are shown, how delivery bandwidth is used, when the app must be installed by, and how the device coordinates restarts afterward.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsAutoUpdateCatalogAppAssignmentSettings"
    # Indicates the delivery optimization download priority level for app content. This controls whether the download uses background bandwidth (minimal impact on other network activity) or foreground bandwidth (prioritized download at the expense of other network traffic).
    delivery_optimization_priority: Optional[WindowsAutoUpdateCatalogAppDeliveryOptimizationPriority] = None
    # Specifies the deadline by which the app must be installed on the device. When null, the app is offered for immediate installation with no enforced deadline.
    install_time_settings: Optional[WindowsAutoUpdateCatalogAppInstallTimeSettings] = None
    # Indicates which notifications the Intune management extension displays to the end user during the app installation and restart lifecycle on managed devices.
    notification_type: Optional[WindowsAutoUpdateCatalogAppNotificationType] = None
    # Specifies the restart coordination behavior after the app is installed—including how long to wait before restarting, when to show a countdown, and how long the user can snooze. When null, no restart coordination is applied (the device may still restart based on the app's deviceRestartBehavior setting). Note: the service accepts restart settings regardless of the app's deviceRestartBehavior value; the device agent determines which settings are actually honored at runtime.
    restart_settings: Optional[WindowsAutoUpdateCatalogAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAutoUpdateCatalogAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutoUpdateCatalogAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsAutoUpdateCatalogAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .windows_auto_update_catalog_app_delivery_optimization_priority import WindowsAutoUpdateCatalogAppDeliveryOptimizationPriority
        from .windows_auto_update_catalog_app_install_time_settings import WindowsAutoUpdateCatalogAppInstallTimeSettings
        from .windows_auto_update_catalog_app_notification_type import WindowsAutoUpdateCatalogAppNotificationType
        from .windows_auto_update_catalog_app_restart_settings import WindowsAutoUpdateCatalogAppRestartSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .windows_auto_update_catalog_app_delivery_optimization_priority import WindowsAutoUpdateCatalogAppDeliveryOptimizationPriority
        from .windows_auto_update_catalog_app_install_time_settings import WindowsAutoUpdateCatalogAppInstallTimeSettings
        from .windows_auto_update_catalog_app_notification_type import WindowsAutoUpdateCatalogAppNotificationType
        from .windows_auto_update_catalog_app_restart_settings import WindowsAutoUpdateCatalogAppRestartSettings

        fields: dict[str, Callable[[Any], None]] = {
            "deliveryOptimizationPriority": lambda n : setattr(self, 'delivery_optimization_priority', n.get_enum_value(WindowsAutoUpdateCatalogAppDeliveryOptimizationPriority)),
            "installTimeSettings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(WindowsAutoUpdateCatalogAppInstallTimeSettings)),
            "notificationType": lambda n : setattr(self, 'notification_type', n.get_enum_value(WindowsAutoUpdateCatalogAppNotificationType)),
            "restartSettings": lambda n : setattr(self, 'restart_settings', n.get_object_value(WindowsAutoUpdateCatalogAppRestartSettings)),
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
        writer.write_enum_value("deliveryOptimizationPriority", self.delivery_optimization_priority)
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notificationType", self.notification_type)
        writer.write_object_value("restartSettings", self.restart_settings)
    

