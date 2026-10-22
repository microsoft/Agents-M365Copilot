from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_driver_update_profile_inventory_sync_state import WindowsDriverUpdateProfileInventorySyncState

@dataclass
class WindowsDriverUpdateProfileInventorySyncStatus(AdditionalDataHolder, Parsable):
    """
    A complex type to store the status of a driver and firmware profile inventory sync. The status includes the last successful sync date time and the state of the last sync.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Windows DnF update inventory sync state.
    driver_inventory_sync_state: Optional[WindowsDriverUpdateProfileInventorySyncState] = None
    # The last successful sync date and time in UTC.
    last_successful_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDriverUpdateProfileInventorySyncStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDriverUpdateProfileInventorySyncStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDriverUpdateProfileInventorySyncStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_driver_update_profile_inventory_sync_state import WindowsDriverUpdateProfileInventorySyncState

        from .windows_driver_update_profile_inventory_sync_state import WindowsDriverUpdateProfileInventorySyncState

        fields: dict[str, Callable[[Any], None]] = {
            "driverInventorySyncState": lambda n : setattr(self, 'driver_inventory_sync_state', n.get_enum_value(WindowsDriverUpdateProfileInventorySyncState)),
            "lastSuccessfulSyncDateTime": lambda n : setattr(self, 'last_successful_sync_date_time', n.get_datetime_value()),
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
        writer.write_enum_value("driverInventorySyncState", self.driver_inventory_sync_state)
        writer.write_datetime_value("lastSuccessfulSyncDateTime", self.last_successful_sync_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

