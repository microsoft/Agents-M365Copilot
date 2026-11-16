from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_state import ActionState
    from .device_action_category import DeviceActionCategory
    from .entity import Entity
    from .remote_action import RemoteAction

from .entity import Entity

@dataclass
class RemoteActionAudit(Entity, Parsable):
    """
    Report of remote actions initiated on the devices belonging to a certain tenant.
    """
    # Remote actions Intune supports.
    action: Optional[RemoteAction] = None
    # The actionState property
    action_state: Optional[ActionState] = None
    # BulkAction ID
    bulk_device_action_id: Optional[str] = None
    # Enum type used for DeviceActionCategory
    device_action_category: Optional[DeviceActionCategory] = None
    # Intune device name.
    device_display_name: Optional[str] = None
    # IMEI of the device.
    device_i_m_e_i: Optional[str] = None
    # Upn of the device owner.
    device_owner_user_principal_name: Optional[str] = None
    # User who initiated the device action, format is UPN.
    initiated_by_user_principal_name: Optional[str] = None
    # Action target.
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time when the action was issued, given in UTC.
    request_date_time: Optional[datetime.datetime] = None
    # [deprecated] Please use InitiatedByUserPrincipalName instead.
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteActionAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteActionAudit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteActionAudit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_state import ActionState
        from .device_action_category import DeviceActionCategory
        from .entity import Entity
        from .remote_action import RemoteAction

        from .action_state import ActionState
        from .device_action_category import DeviceActionCategory
        from .entity import Entity
        from .remote_action import RemoteAction

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(RemoteAction)),
            "actionState": lambda n : setattr(self, 'action_state', n.get_enum_value(ActionState)),
            "bulkDeviceActionId": lambda n : setattr(self, 'bulk_device_action_id', n.get_str_value()),
            "deviceActionCategory": lambda n : setattr(self, 'device_action_category', n.get_enum_value(DeviceActionCategory)),
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "deviceIMEI": lambda n : setattr(self, 'device_i_m_e_i', n.get_str_value()),
            "deviceOwnerUserPrincipalName": lambda n : setattr(self, 'device_owner_user_principal_name', n.get_str_value()),
            "initiatedByUserPrincipalName": lambda n : setattr(self, 'initiated_by_user_principal_name', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_str_value("bulkDeviceActionId", self.bulk_device_action_id)
        writer.write_enum_value("deviceActionCategory", self.device_action_category)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceIMEI", self.device_i_m_e_i)
        writer.write_str_value("deviceOwnerUserPrincipalName", self.device_owner_user_principal_name)
        writer.write_str_value("initiatedByUserPrincipalName", self.initiated_by_user_principal_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_str_value("userName", self.user_name)
    

