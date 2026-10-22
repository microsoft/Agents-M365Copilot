from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_bulk_action_status import CloudPcBulkActionStatus
    from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
    from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
    from .cloud_pc_bulk_disaster_recovery import CloudPcBulkDisasterRecovery
    from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
    from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
    from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
    from .cloud_pc_bulk_move import CloudPcBulkMove
    from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
    from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
    from .cloud_pc_bulk_reinstall_agent import CloudPcBulkReinstallAgent
    from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
    from .cloud_pc_bulk_resize import CloudPcBulkResize
    from .cloud_pc_bulk_restart import CloudPcBulkRestart
    from .cloud_pc_bulk_restore import CloudPcBulkRestore
    from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
    from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcBulkAction(Entity, Parsable):
    # Run summary of this bulk action.
    action_summary: Optional[CloudPcBulkActionSummary] = None
    # The cloudPcIds property
    cloud_pc_ids: Optional[list[str]] = None
    # The date and time when the bulk action was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Name of the bulk action.
    display_name: Optional[str] = None
    # Indicates the user principal name (UPN) of the user who initiated this bulk action. Read-only.
    initiated_by_user_principal_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the bulk action is scheduled according to the maintenance window. When true, the bulk action uses the maintenance window to schedule the action; false means that the bulk action doesn't use the maintenance window. The default value is false.
    scheduled_during_maintenance_window: Optional[bool] = None
    # Indicates the status of bulk actions. Possible values are pending, succeeded, failed, unknownFutureValue. The default value is pending. Read-only.
    status: Optional[CloudPcBulkActionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcBulkAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkCreateSnapshot".casefold():
            from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot

            return CloudPcBulkCreateSnapshot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkDisasterRecovery".casefold():
            from .cloud_pc_bulk_disaster_recovery import CloudPcBulkDisasterRecovery

            return CloudPcBulkDisasterRecovery()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailback".casefold():
            from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback

            return CloudPcBulkDisasterRecoveryFailback()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailover".casefold():
            from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover

            return CloudPcBulkDisasterRecoveryFailover()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkModifyDiskEncryptionType".casefold():
            from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType

            return CloudPcBulkModifyDiskEncryptionType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkMove".casefold():
            from .cloud_pc_bulk_move import CloudPcBulkMove

            return CloudPcBulkMove()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkPowerOff".casefold():
            from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff

            return CloudPcBulkPowerOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkPowerOn".casefold():
            from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn

            return CloudPcBulkPowerOn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkReinstallAgent".casefold():
            from .cloud_pc_bulk_reinstall_agent import CloudPcBulkReinstallAgent

            return CloudPcBulkReinstallAgent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkReprovision".casefold():
            from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision

            return CloudPcBulkReprovision()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkResize".casefold():
            from .cloud_pc_bulk_resize import CloudPcBulkResize

            return CloudPcBulkResize()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkRestart".casefold():
            from .cloud_pc_bulk_restart import CloudPcBulkRestart

            return CloudPcBulkRestart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkRestore".casefold():
            from .cloud_pc_bulk_restore import CloudPcBulkRestore

            return CloudPcBulkRestore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkSetReviewStatus".casefold():
            from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus

            return CloudPcBulkSetReviewStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcBulkTroubleshoot".casefold():
            from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot

            return CloudPcBulkTroubleshoot()
        return CloudPcBulkAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_bulk_action_status import CloudPcBulkActionStatus
        from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
        from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
        from .cloud_pc_bulk_disaster_recovery import CloudPcBulkDisasterRecovery
        from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
        from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
        from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
        from .cloud_pc_bulk_move import CloudPcBulkMove
        from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
        from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
        from .cloud_pc_bulk_reinstall_agent import CloudPcBulkReinstallAgent
        from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
        from .cloud_pc_bulk_resize import CloudPcBulkResize
        from .cloud_pc_bulk_restart import CloudPcBulkRestart
        from .cloud_pc_bulk_restore import CloudPcBulkRestore
        from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
        from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
        from .entity import Entity

        from .cloud_pc_bulk_action_status import CloudPcBulkActionStatus
        from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
        from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
        from .cloud_pc_bulk_disaster_recovery import CloudPcBulkDisasterRecovery
        from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
        from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
        from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
        from .cloud_pc_bulk_move import CloudPcBulkMove
        from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
        from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
        from .cloud_pc_bulk_reinstall_agent import CloudPcBulkReinstallAgent
        from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
        from .cloud_pc_bulk_resize import CloudPcBulkResize
        from .cloud_pc_bulk_restart import CloudPcBulkRestart
        from .cloud_pc_bulk_restore import CloudPcBulkRestore
        from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
        from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "actionSummary": lambda n : setattr(self, 'action_summary', n.get_object_value(CloudPcBulkActionSummary)),
            "cloudPcIds": lambda n : setattr(self, 'cloud_pc_ids', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "initiatedByUserPrincipalName": lambda n : setattr(self, 'initiated_by_user_principal_name', n.get_str_value()),
            "scheduledDuringMaintenanceWindow": lambda n : setattr(self, 'scheduled_during_maintenance_window', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcBulkActionStatus)),
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
        writer.write_object_value("actionSummary", self.action_summary)
        writer.write_collection_of_primitive_values("cloudPcIds", self.cloud_pc_ids)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("initiatedByUserPrincipalName", self.initiated_by_user_principal_name)
        writer.write_bool_value("scheduledDuringMaintenanceWindow", self.scheduled_during_maintenance_window)
        writer.write_enum_value("status", self.status)
    

