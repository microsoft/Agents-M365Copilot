from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_scope_operator import DeviceScopeOperator
    from .device_scope_parameter import DeviceScopeParameter
    from .device_scope_status import DeviceScopeStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDeviceScope(Entity, Parsable):
    """
    The user experience analytics device scope entity contains device scope configuration values use to apply filtering on the endpoint analytics reports.
    """
    # Indicates the creation date and time for the custom device scope.
    created_date_time: Optional[datetime.datetime] = None
    # The name of the user experience analytics device Scope configuration.
    device_scope_name: Optional[str] = None
    # Indicates whether a device scope is enabled or disabled. When TRUE, the device scope is enabled. When FALSE, the device scope is disabled. Default value is FALSE.
    enabled: Optional[bool] = None
    # Indicates whether the device scope configuration is built-in or custom. When TRUE, the device scope configuration is built-in. When FALSE, the device scope configuration is custom. Default value is FALSE.
    is_built_in: Optional[bool] = None
    # Indicates the last updated date and time for the custom device scope.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device scope configuration query operator. Possible values are: equals, notEquals, contains, notContains, greaterThan, lessThan. Default value: equals.
    operator: Optional[DeviceScopeOperator] = None
    # The unique identifier of the person (admin) who created the device scope configuration.
    owner_id: Optional[str] = None
    # Device scope configuration parameter. It will be expend in future to add more parameter. Eg: device scope parameter can be OS version, Disk Type, Device manufacturer, device model or Scope tag. Default value: scopeTag.
    parameter: Optional[DeviceScopeParameter] = None
    # Indicates the device scope status after the device scope has been enabled. Possible values are: none, computing, insufficientData or completed. Default value is none.
    status: Optional[DeviceScopeStatus] = None
    # The device scope configuration query clause value.
    value: Optional[str] = None
    # The unique identifier for a user device scope tag Id used for the creation of device scope configuration.
    value_object_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsDeviceScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_scope_operator import DeviceScopeOperator
        from .device_scope_parameter import DeviceScopeParameter
        from .device_scope_status import DeviceScopeStatus
        from .entity import Entity

        from .device_scope_operator import DeviceScopeOperator
        from .device_scope_parameter import DeviceScopeParameter
        from .device_scope_status import DeviceScopeStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceScopeName": lambda n : setattr(self, 'device_scope_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(DeviceScopeOperator)),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_str_value()),
            "parameter": lambda n : setattr(self, 'parameter', n.get_enum_value(DeviceScopeParameter)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DeviceScopeStatus)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "valueObjectId": lambda n : setattr(self, 'value_object_id', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceScopeName", self.device_scope_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("ownerId", self.owner_id)
        writer.write_enum_value("parameter", self.parameter)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("value", self.value)
        writer.write_str_value("valueObjectId", self.value_object_id)
    

