from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsAutoUpdateCatalogAppRestartSettings(AdditionalDataHolder, Parsable):
    """
    Specifies how the device coordinates a restart after the app is installed. These settings control the grace period before a restart is initiated, when the user sees a countdown notification, and how long the user can defer the restart by snoozing. When null, no restart coordination is applied (the device may still restart based on the app's deviceRestartBehavior setting).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of minutes before the scheduled restart at which a countdown notification is displayed to the user. Must be between 1 and the value of gracePeriodInMinutes. This countdown is non-dismissible and warns the user that a restart is imminent. For example, a value of 15 means the countdown appears 15 minutes before the restart.
    countdown_display_before_restart_in_minutes: Optional[int] = None
    # The number of minutes the device waits after app installation before initiating a restart. During this period, the user can continue working and save their documents. For example, a value of 1440 means the device waits 24 hours before restarting.
    grace_period_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of minutes by which the user can defer (snooze) the restart notification each time they press the snooze button. When null, the snooze option is not available and the user cannot defer the restart. For example, a value of 240 allows the user to defer the restart by 4 hours each time.
    restart_notification_snooze_duration_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAutoUpdateCatalogAppRestartSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutoUpdateCatalogAppRestartSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsAutoUpdateCatalogAppRestartSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "countdownDisplayBeforeRestartInMinutes": lambda n : setattr(self, 'countdown_display_before_restart_in_minutes', n.get_int_value()),
            "gracePeriodInMinutes": lambda n : setattr(self, 'grace_period_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restartNotificationSnoozeDurationInMinutes": lambda n : setattr(self, 'restart_notification_snooze_duration_in_minutes', n.get_int_value()),
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
        writer.write_int_value("countdownDisplayBeforeRestartInMinutes", self.countdown_display_before_restart_in_minutes)
        writer.write_int_value("gracePeriodInMinutes", self.grace_period_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("restartNotificationSnoozeDurationInMinutes", self.restart_notification_snooze_duration_in_minutes)
        writer.write_additional_data_value(self.additional_data)
    

