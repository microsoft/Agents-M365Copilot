from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .security_baseline_compliance_state import SecurityBaselineComplianceState

from .entity import Entity

@dataclass
class SecurityBaselineDeviceState(Entity, Parsable):
    """
    The security baseline compliance state summary of the security baseline for a device.
    """
    # Display name of the device
    device_display_name: Optional[str] = None
    # Last modified date time of the policy report
    last_reported_date_time: Optional[datetime.datetime] = None
    # Intune device id
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Security Baseline Compliance State
    state: Optional[SecurityBaselineComplianceState] = None
    # User Principal Name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineDeviceState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineDeviceState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .security_baseline_compliance_state import SecurityBaselineComplianceState

        from .entity import Entity
        from .security_baseline_compliance_state import SecurityBaselineComplianceState

        fields: dict[str, Callable[[Any], None]] = {
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "lastReportedDateTime": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SecurityBaselineComplianceState)),
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
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

