from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_device import AuthenticationMethodDevice
    from .hardware_oath_token_hash_function import HardwareOathTokenHashFunction
    from .hardware_oath_token_status import HardwareOathTokenStatus
    from .identity import Identity
    from .user import User

from .authentication_method_device import AuthenticationMethodDevice

@dataclass
class HardwareOathTokenAuthenticationMethodDevice(AuthenticationMethodDevice, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.hardwareOathTokenAuthenticationMethodDevice"
    # Assign the hardware OATH token to a user.
    assign_to: Optional[User] = None
    # User the token is assigned to. Nullable. Supports $filter (eq).
    assigned_to: Optional[Identity] = None
    # Hash function of the hardrware token. The possible values are: hmacsha1 or hmacsha256. Default value is: hmacsha1. Supports $filter (eq).
    hash_function: Optional[HardwareOathTokenHashFunction] = None
    # The date and time the authentication method was last used by the user. Read-only. Optional. This optional value is null if the authentication method doesn't populate it. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_used_date_time: Optional[datetime.datetime] = None
    # Manufacturer name of the hardware token. Supports $filter (eq).
    manufacturer: Optional[str] = None
    # Model name of the hardware token. Supports $filter (eq).
    model: Optional[str] = None
    # Secret key of the specific hardware token, provided by the vendor.
    secret_key: Optional[str] = None
    # Serial number of the specific hardware token, often found on the back of the device. Supports $select and $filter (eq).
    serial_number: Optional[str] = None
    # Status of the hardware OATH token.The possible values are: available, assigned, activated, failedActivation. Supports $filter(eq).
    status: Optional[HardwareOathTokenStatus] = None
    # Refresh interval of the 6-digit verification code, in seconds. The possible values are: 30 or 60. Supports $filter (eq).
    time_interval_in_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwareOathTokenAuthenticationMethodDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareOathTokenAuthenticationMethodDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwareOathTokenAuthenticationMethodDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_device import AuthenticationMethodDevice
        from .hardware_oath_token_hash_function import HardwareOathTokenHashFunction
        from .hardware_oath_token_status import HardwareOathTokenStatus
        from .identity import Identity
        from .user import User

        from .authentication_method_device import AuthenticationMethodDevice
        from .hardware_oath_token_hash_function import HardwareOathTokenHashFunction
        from .hardware_oath_token_status import HardwareOathTokenStatus
        from .identity import Identity
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "assignTo": lambda n : setattr(self, 'assign_to', n.get_object_value(User)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(Identity)),
            "hashFunction": lambda n : setattr(self, 'hash_function', n.get_enum_value(HardwareOathTokenHashFunction)),
            "lastUsedDateTime": lambda n : setattr(self, 'last_used_date_time', n.get_datetime_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "secretKey": lambda n : setattr(self, 'secret_key', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(HardwareOathTokenStatus)),
            "timeIntervalInSeconds": lambda n : setattr(self, 'time_interval_in_seconds', n.get_int_value()),
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
        writer.write_object_value("assignTo", self.assign_to)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_enum_value("hashFunction", self.hash_function)
        writer.write_datetime_value("lastUsedDateTime", self.last_used_date_time)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("secretKey", self.secret_key)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("timeIntervalInSeconds", self.time_interval_in_seconds)
    

