from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_update_status import WindowsUpdateStatus

from .entity import Entity

@dataclass
class WindowsUpdateState(Entity, Parsable):
    # Device display name.
    device_display_name: Optional[str] = None
    # The id of the device.
    device_id: Optional[str] = None
    # The current feature update version of the device.
    feature_update_version: Optional[str] = None
    # The date time that the Windows Update Agent did a successful scan.
    last_scan_date_time: Optional[datetime.datetime] = None
    # Last date time that the device sync with with Microsoft Intune.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Quality Update Version of the device.
    quality_update_version: Optional[str] = None
    # Windows update for business configuration device states
    status: Optional[WindowsUpdateStatus] = None
    # The id of the user.
    user_id: Optional[str] = None
    # User principal name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsUpdateState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsUpdateState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_update_status import WindowsUpdateStatus

        from .entity import Entity
        from .windows_update_status import WindowsUpdateStatus

        fields: dict[str, Callable[[Any], None]] = {
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "featureUpdateVersion": lambda n : setattr(self, 'feature_update_version', n.get_str_value()),
            "lastScanDateTime": lambda n : setattr(self, 'last_scan_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "qualityUpdateVersion": lambda n : setattr(self, 'quality_update_version', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(WindowsUpdateStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("featureUpdateVersion", self.feature_update_version)
        writer.write_datetime_value("lastScanDateTime", self.last_scan_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("qualityUpdateVersion", self.quality_update_version)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

