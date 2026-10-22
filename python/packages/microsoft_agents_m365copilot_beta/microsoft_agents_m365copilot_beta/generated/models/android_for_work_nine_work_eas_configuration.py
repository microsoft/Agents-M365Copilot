from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

@dataclass
class AndroidForWorkNineWorkEasConfiguration(AndroidForWorkEasEmailProfileBase, Parsable):
    """
    By providing configurations in this profile you can instruct the Nine Work email client on Android For Work devices to communicate with an Exchange server and get email, contacts, calendar, tasks, and notes. Furthermore, you can also specify how much email to sync and how often the device should sync.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkNineWorkEasConfiguration"
    # Toggles syncing the calendar. If set to false the calendar is turned off on the device.
    sync_calendar: Optional[bool] = None
    # Toggles syncing contacts. If set to false contacts are turned off on the device.
    sync_contacts: Optional[bool] = None
    # Toggles syncing tasks. If set to false tasks are turned off on the device.
    sync_tasks: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkNineWorkEasConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkNineWorkEasConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkNineWorkEasConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

        from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

        fields: dict[str, Callable[[Any], None]] = {
            "syncCalendar": lambda n : setattr(self, 'sync_calendar', n.get_bool_value()),
            "syncContacts": lambda n : setattr(self, 'sync_contacts', n.get_bool_value()),
            "syncTasks": lambda n : setattr(self, 'sync_tasks', n.get_bool_value()),
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
        writer.write_bool_value("syncCalendar", self.sync_calendar)
        writer.write_bool_value("syncContacts", self.sync_contacts)
        writer.write_bool_value("syncTasks", self.sync_tasks)
    

