from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_log_operation_type import ActivityLogOperationType
    from .activity_log_result_status import ActivityLogResultStatus
    from .activity_log_severity import ActivityLogSeverity
    from .backup_policy_activity_log import BackupPolicyActivityLog
    from .dynamic_rule_activity_log import DynamicRuleActivityLog
    from .entity import Entity
    from .offboarding_activity_log import OffboardingActivityLog
    from .public_error import PublicError
    from .restore_task_activity_log import RestoreTaskActivityLog
    from .service_type import ServiceType

from .entity import Entity

@dataclass
class ActivityLogBase(Entity, Parsable):
    # The activityType property
    activity_type: Optional[ActivityLogOperationType] = None
    # Contains error details if an error occurred while processing this activity.
    error: Optional[PublicError] = None
    # Timestamp of activity completion.
    event_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity of the person who performed the activity.
    performed_by: Optional[str] = None
    # The resultStatus property
    result_status: Optional[ActivityLogResultStatus] = None
    # The serviceType property
    service_type: Optional[ServiceType] = None
    # The severity property
    severity: Optional[ActivityLogSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivityLogBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivityLogBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.backupPolicyActivityLog".casefold():
            from .backup_policy_activity_log import BackupPolicyActivityLog

            return BackupPolicyActivityLog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dynamicRuleActivityLog".casefold():
            from .dynamic_rule_activity_log import DynamicRuleActivityLog

            return DynamicRuleActivityLog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offboardingActivityLog".casefold():
            from .offboarding_activity_log import OffboardingActivityLog

            return OffboardingActivityLog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restoreTaskActivityLog".casefold():
            from .restore_task_activity_log import RestoreTaskActivityLog

            return RestoreTaskActivityLog()
        return ActivityLogBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_log_operation_type import ActivityLogOperationType
        from .activity_log_result_status import ActivityLogResultStatus
        from .activity_log_severity import ActivityLogSeverity
        from .backup_policy_activity_log import BackupPolicyActivityLog
        from .dynamic_rule_activity_log import DynamicRuleActivityLog
        from .entity import Entity
        from .offboarding_activity_log import OffboardingActivityLog
        from .public_error import PublicError
        from .restore_task_activity_log import RestoreTaskActivityLog
        from .service_type import ServiceType

        from .activity_log_operation_type import ActivityLogOperationType
        from .activity_log_result_status import ActivityLogResultStatus
        from .activity_log_severity import ActivityLogSeverity
        from .backup_policy_activity_log import BackupPolicyActivityLog
        from .dynamic_rule_activity_log import DynamicRuleActivityLog
        from .entity import Entity
        from .offboarding_activity_log import OffboardingActivityLog
        from .public_error import PublicError
        from .restore_task_activity_log import RestoreTaskActivityLog
        from .service_type import ServiceType

        fields: dict[str, Callable[[Any], None]] = {
            "activityType": lambda n : setattr(self, 'activity_type', n.get_enum_value(ActivityLogOperationType)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "performedBy": lambda n : setattr(self, 'performed_by', n.get_str_value()),
            "resultStatus": lambda n : setattr(self, 'result_status', n.get_enum_value(ActivityLogResultStatus)),
            "serviceType": lambda n : setattr(self, 'service_type', n.get_enum_value(ServiceType)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(ActivityLogSeverity)),
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
        writer.write_enum_value("activityType", self.activity_type)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("performedBy", self.performed_by)
        writer.write_enum_value("resultStatus", self.result_status)
        writer.write_enum_value("serviceType", self.service_type)
        writer.write_enum_value("severity", self.severity)
    

