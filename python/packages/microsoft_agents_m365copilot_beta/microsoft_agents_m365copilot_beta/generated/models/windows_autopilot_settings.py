from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_autopilot_sync_status import WindowsAutopilotSyncStatus

from .entity import Entity

@dataclass
class WindowsAutopilotSettings(Entity, Parsable):
    """
    The windowsAutopilotSettings resource represents a Windows Autopilot Account to sync data with Windows device data sync service.
    """
    # Last data sync date time with DDS service.
    last_manual_sync_trigger_date_time: Optional[datetime.datetime] = None
    # Last data sync date time with DDS service.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The syncStatus property
    sync_status: Optional[WindowsAutopilotSyncStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAutopilotSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsAutopilotSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_autopilot_sync_status import WindowsAutopilotSyncStatus

        from .entity import Entity
        from .windows_autopilot_sync_status import WindowsAutopilotSyncStatus

        fields: dict[str, Callable[[Any], None]] = {
            "lastManualSyncTriggerDateTime": lambda n : setattr(self, 'last_manual_sync_trigger_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "syncStatus": lambda n : setattr(self, 'sync_status', n.get_enum_value(WindowsAutopilotSyncStatus)),
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
        writer.write_datetime_value("lastManualSyncTriggerDateTime", self.last_manual_sync_trigger_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("syncStatus", self.sync_status)
    

