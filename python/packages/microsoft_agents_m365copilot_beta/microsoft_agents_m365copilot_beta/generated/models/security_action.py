from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .key_value_pair import KeyValuePair
    from .operation_status import OperationStatus
    from .result_info import ResultInfo
    from .security_action_state import SecurityActionState
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class SecurityAction(Entity, Parsable):
    # Reason for invoking this action.
    action_reason: Optional[str] = None
    # The Application ID of the calling application that submitted (POST) the action. The appId should be extracted from the auth token and not entered manually by the calling application.
    app_id: Optional[str] = None
    # Azure tenant ID of the entity to determine which tenant the entity belongs to (multi-tenancy support). The azureTenantId should be extracted from the auth token and not entered manually by the calling application.
    azure_tenant_id: Optional[str] = None
    # Unique client context string. Can have a maximum of 256 characters.
    client_context: Optional[str] = None
    # Timestamp when the action was completed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    completed_date_time: Optional[datetime.datetime] = None
    # Timestamp when the action is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Error info when the action fails.
    error_info: Optional[ResultInfo] = None
    # Timestamp when this action was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_action_date_time: Optional[datetime.datetime] = None
    # Action name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of parameters (key-value pairs) necessary to invoke the action, for example, URL or fileHash to block.). Required.
    parameters: Optional[list[KeyValuePair]] = None
    # Collection of securityActionState to keep the history of an action.
    states: Optional[list[SecurityActionState]] = None
    # Status of the action. The possible values are: NotStarted, Running, Completed, Failed.
    status: Optional[OperationStatus] = None
    # The user principal name of the signed-in user that submitted  (POST) the action. The user should be extracted from the auth token and not entered manually by the calling application.
    user: Optional[str] = None
    # Complex Type containing details about the Security product/service vendor, provider, and sub-provider (for example, vendor=Microsoft; provider=Windows Defender ATP; sub-provider=AppLocker).
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .operation_status import OperationStatus
        from .result_info import ResultInfo
        from .security_action_state import SecurityActionState
        from .security_vendor_information import SecurityVendorInformation

        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .operation_status import OperationStatus
        from .result_info import ResultInfo
        from .security_action_state import SecurityActionState
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "actionReason": lambda n : setattr(self, 'action_reason', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "errorInfo": lambda n : setattr(self, 'error_info', n.get_object_value(ResultInfo)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(KeyValuePair)),
            "states": lambda n : setattr(self, 'states', n.get_collection_of_object_values(SecurityActionState)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OperationStatus)),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
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
        writer.write_str_value("actionReason", self.action_reason)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_str_value("clientContext", self.client_context)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("errorInfo", self.error_info)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_collection_of_object_values("states", self.states)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("user", self.user)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

