from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_data import AlertData
    from .alert_data_reference_string import AlertDataReferenceString
    from .alert_severity import AlertSeverity
    from .alert_status import AlertStatus
    from .managed_tenant_alert_log import ManagedTenantAlertLog
    from .managed_tenant_alert_rule import ManagedTenantAlertRule
    from .managed_tenant_api_notification import ManagedTenantApiNotification
    from .managed_tenant_email_notification import ManagedTenantEmailNotification

from ..entity import Entity

@dataclass
class ManagedTenantAlert(Entity, Parsable):
    # The alertData property
    alert_data: Optional[AlertData] = None
    # The alertDataReferenceStrings property
    alert_data_reference_strings: Optional[list[AlertDataReferenceString]] = None
    # The alertLogs property
    alert_logs: Optional[list[ManagedTenantAlertLog]] = None
    # The alertRule property
    alert_rule: Optional[ManagedTenantAlertRule] = None
    # The alertRuleDisplayName property
    alert_rule_display_name: Optional[str] = None
    # The apiNotifications property
    api_notifications: Optional[list[ManagedTenantApiNotification]] = None
    # The assignedToUserId property
    assigned_to_user_id: Optional[str] = None
    # The correlationCount property
    correlation_count: Optional[int] = None
    # The correlationId property
    correlation_id: Optional[str] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The emailNotifications property
    email_notifications: Optional[list[ManagedTenantEmailNotification]] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The message property
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # The status property
    status: Optional[AlertStatus] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedTenantAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedTenantAlert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_data import AlertData
        from .alert_data_reference_string import AlertDataReferenceString
        from .alert_severity import AlertSeverity
        from .alert_status import AlertStatus
        from .managed_tenant_alert_log import ManagedTenantAlertLog
        from .managed_tenant_alert_rule import ManagedTenantAlertRule
        from .managed_tenant_api_notification import ManagedTenantApiNotification
        from .managed_tenant_email_notification import ManagedTenantEmailNotification

        from ..entity import Entity
        from .alert_data import AlertData
        from .alert_data_reference_string import AlertDataReferenceString
        from .alert_severity import AlertSeverity
        from .alert_status import AlertStatus
        from .managed_tenant_alert_log import ManagedTenantAlertLog
        from .managed_tenant_alert_rule import ManagedTenantAlertRule
        from .managed_tenant_api_notification import ManagedTenantApiNotification
        from .managed_tenant_email_notification import ManagedTenantEmailNotification

        fields: dict[str, Callable[[Any], None]] = {
            "alertData": lambda n : setattr(self, 'alert_data', n.get_object_value(AlertData)),
            "alertDataReferenceStrings": lambda n : setattr(self, 'alert_data_reference_strings', n.get_collection_of_object_values(AlertDataReferenceString)),
            "alertLogs": lambda n : setattr(self, 'alert_logs', n.get_collection_of_object_values(ManagedTenantAlertLog)),
            "alertRule": lambda n : setattr(self, 'alert_rule', n.get_object_value(ManagedTenantAlertRule)),
            "alertRuleDisplayName": lambda n : setattr(self, 'alert_rule_display_name', n.get_str_value()),
            "apiNotifications": lambda n : setattr(self, 'api_notifications', n.get_collection_of_object_values(ManagedTenantApiNotification)),
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "correlationCount": lambda n : setattr(self, 'correlation_count', n.get_int_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "emailNotifications": lambda n : setattr(self, 'email_notifications', n.get_collection_of_object_values(ManagedTenantEmailNotification)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AlertStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_object_value("alertData", self.alert_data)
        writer.write_collection_of_object_values("alertDataReferenceStrings", self.alert_data_reference_strings)
        writer.write_collection_of_object_values("alertLogs", self.alert_logs)
        writer.write_object_value("alertRule", self.alert_rule)
        writer.write_str_value("alertRuleDisplayName", self.alert_rule_display_name)
        writer.write_collection_of_object_values("apiNotifications", self.api_notifications)
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_int_value("correlationCount", self.correlation_count)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("emailNotifications", self.email_notifications)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("title", self.title)
    

