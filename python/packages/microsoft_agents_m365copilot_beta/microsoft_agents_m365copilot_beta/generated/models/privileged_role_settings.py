from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class PrivilegedRoleSettings(Entity, Parsable):
    # The approvalOnElevation property
    approval_on_elevation: Optional[bool] = None
    # The approverIds property
    approver_ids: Optional[list[str]] = None
    # The elevationDuration property
    elevation_duration: Optional[datetime.timedelta] = None
    # The isMfaOnElevationConfigurable property
    is_mfa_on_elevation_configurable: Optional[bool] = None
    # The lastGlobalAdmin property
    last_global_admin: Optional[bool] = None
    # The maxElavationDuration property
    max_elavation_duration: Optional[datetime.timedelta] = None
    # The mfaOnElevation property
    mfa_on_elevation: Optional[bool] = None
    # The minElevationDuration property
    min_elevation_duration: Optional[datetime.timedelta] = None
    # The notificationToUserOnElevation property
    notification_to_user_on_elevation: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ticketingInfoOnElevation property
    ticketing_info_on_elevation: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedRoleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedRoleSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "approvalOnElevation": lambda n : setattr(self, 'approval_on_elevation', n.get_bool_value()),
            "approverIds": lambda n : setattr(self, 'approver_ids', n.get_collection_of_primitive_values(str)),
            "elevationDuration": lambda n : setattr(self, 'elevation_duration', n.get_timedelta_value()),
            "isMfaOnElevationConfigurable": lambda n : setattr(self, 'is_mfa_on_elevation_configurable', n.get_bool_value()),
            "lastGlobalAdmin": lambda n : setattr(self, 'last_global_admin', n.get_bool_value()),
            "maxElavationDuration": lambda n : setattr(self, 'max_elavation_duration', n.get_timedelta_value()),
            "mfaOnElevation": lambda n : setattr(self, 'mfa_on_elevation', n.get_bool_value()),
            "minElevationDuration": lambda n : setattr(self, 'min_elevation_duration', n.get_timedelta_value()),
            "notificationToUserOnElevation": lambda n : setattr(self, 'notification_to_user_on_elevation', n.get_bool_value()),
            "ticketingInfoOnElevation": lambda n : setattr(self, 'ticketing_info_on_elevation', n.get_bool_value()),
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
        writer.write_bool_value("approvalOnElevation", self.approval_on_elevation)
        writer.write_collection_of_primitive_values("approverIds", self.approver_ids)
        writer.write_timedelta_value("elevationDuration", self.elevation_duration)
        writer.write_bool_value("isMfaOnElevationConfigurable", self.is_mfa_on_elevation_configurable)
        writer.write_bool_value("lastGlobalAdmin", self.last_global_admin)
        writer.write_timedelta_value("maxElavationDuration", self.max_elavation_duration)
        writer.write_bool_value("mfaOnElevation", self.mfa_on_elevation)
        writer.write_timedelta_value("minElevationDuration", self.min_elevation_duration)
        writer.write_bool_value("notificationToUserOnElevation", self.notification_to_user_on_elevation)
        writer.write_bool_value("ticketingInfoOnElevation", self.ticketing_info_on_elevation)
    

