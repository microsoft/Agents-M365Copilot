from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .allow_file_response_action import AllowFileResponseAction
    from .block_file_response_action import BlockFileResponseAction
    from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction
    from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction
    from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction
    from .disable_user_response_action import DisableUserResponseAction
    from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction
    from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction
    from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction
    from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction
    from .hard_delete_response_action import HardDeleteResponseAction
    from .incident_task_response_action import IncidentTaskResponseAction
    from .initiate_investigation_response_action import InitiateInvestigationResponseAction
    from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction
    from .isolate_device_response_action import IsolateDeviceResponseAction
    from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction
    from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction
    from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction
    from .move_to_inbox_response_action import MoveToInboxResponseAction
    from .move_to_junk_response_action import MoveToJunkResponseAction
    from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction
    from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction
    from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction
    from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction
    from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction
    from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction
    from .soft_delete_response_action import SoftDeleteResponseAction
    from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction
    from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction
    from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction
    from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

@dataclass
class ResponseAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.allowFileResponseAction".casefold():
            from .allow_file_response_action import AllowFileResponseAction

            return AllowFileResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.blockFileResponseAction".casefold():
            from .block_file_response_action import BlockFileResponseAction

            return BlockFileResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.collectInvestigationPackageIncidentTaskResponseAction".casefold():
            from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction

            return CollectInvestigationPackageIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.collectInvestigationPackageResponseAction".casefold():
            from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction

            return CollectInvestigationPackageResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.disableUserIncidentTaskResponseAction".casefold():
            from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction

            return DisableUserIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.disableUserResponseAction".casefold():
            from .disable_user_response_action import DisableUserResponseAction

            return DisableUserResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.enableUserIncidentTaskResponseAction".casefold():
            from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction

            return EnableUserIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.forceUserPasswordResetIncidentTaskResponseAction".casefold():
            from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction

            return ForceUserPasswordResetIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.forceUserPasswordResetResponseAction".casefold():
            from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction

            return ForceUserPasswordResetResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hardDeleteEmailIncidentTaskResponseAction".casefold():
            from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction

            return HardDeleteEmailIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hardDeleteResponseAction".casefold():
            from .hard_delete_response_action import HardDeleteResponseAction

            return HardDeleteResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.incidentTaskResponseAction".casefold():
            from .incident_task_response_action import IncidentTaskResponseAction

            return IncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.initiateInvestigationResponseAction".casefold():
            from .initiate_investigation_response_action import InitiateInvestigationResponseAction

            return InitiateInvestigationResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.isolateDeviceIncidentTaskResponseAction".casefold():
            from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction

            return IsolateDeviceIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.isolateDeviceResponseAction".casefold():
            from .isolate_device_response_action import IsolateDeviceResponseAction

            return IsolateDeviceResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.markUserAsCompromisedIncidentTaskResponseAction".casefold():
            from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction

            return MarkUserAsCompromisedIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.markUserAsCompromisedResponseAction".casefold():
            from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction

            return MarkUserAsCompromisedResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.moveToDeletedItemsResponseAction".casefold():
            from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction

            return MoveToDeletedItemsResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.moveToInboxResponseAction".casefold():
            from .move_to_inbox_response_action import MoveToInboxResponseAction

            return MoveToInboxResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.moveToJunkResponseAction".casefold():
            from .move_to_junk_response_action import MoveToJunkResponseAction

            return MoveToJunkResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.requireSignInIncidentTaskResponseAction".casefold():
            from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction

            return RequireSignInIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.restrictAppExecutionIncidentTaskResponseAction".casefold():
            from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction

            return RestrictAppExecutionIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.restrictAppExecutionResponseAction".casefold():
            from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction

            return RestrictAppExecutionResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.runAntivirusScanIncidentTaskResponseAction".casefold():
            from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction

            return RunAntivirusScanIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.runAntivirusScanResponseAction".casefold():
            from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction

            return RunAntivirusScanResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.softDeleteIncidentTaskResponseAction".casefold():
            from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction

            return SoftDeleteIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.softDeleteResponseAction".casefold():
            from .soft_delete_response_action import SoftDeleteResponseAction

            return SoftDeleteResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.stopAndQuarantineFileIncidentTaskResponseAction".casefold():
            from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction

            return StopAndQuarantineFileIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.stopAndQuarantineFileResponseAction".casefold():
            from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction

            return StopAndQuarantineFileResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unIsolateDeviceIncidentTaskResponseAction".casefold():
            from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction

            return UnIsolateDeviceIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unRestrictAppExecutionIncidentTaskResponseAction".casefold():
            from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

            return UnRestrictAppExecutionIncidentTaskResponseAction()
        return ResponseAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .allow_file_response_action import AllowFileResponseAction
        from .block_file_response_action import BlockFileResponseAction
        from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction
        from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction
        from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction
        from .disable_user_response_action import DisableUserResponseAction
        from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction
        from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction
        from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction
        from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction
        from .hard_delete_response_action import HardDeleteResponseAction
        from .incident_task_response_action import IncidentTaskResponseAction
        from .initiate_investigation_response_action import InitiateInvestigationResponseAction
        from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction
        from .isolate_device_response_action import IsolateDeviceResponseAction
        from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction
        from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction
        from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction
        from .move_to_inbox_response_action import MoveToInboxResponseAction
        from .move_to_junk_response_action import MoveToJunkResponseAction
        from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction
        from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction
        from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction
        from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction
        from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction
        from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction
        from .soft_delete_response_action import SoftDeleteResponseAction
        from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction
        from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction
        from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction
        from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

        from .allow_file_response_action import AllowFileResponseAction
        from .block_file_response_action import BlockFileResponseAction
        from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction
        from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction
        from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction
        from .disable_user_response_action import DisableUserResponseAction
        from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction
        from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction
        from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction
        from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction
        from .hard_delete_response_action import HardDeleteResponseAction
        from .incident_task_response_action import IncidentTaskResponseAction
        from .initiate_investigation_response_action import InitiateInvestigationResponseAction
        from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction
        from .isolate_device_response_action import IsolateDeviceResponseAction
        from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction
        from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction
        from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction
        from .move_to_inbox_response_action import MoveToInboxResponseAction
        from .move_to_junk_response_action import MoveToJunkResponseAction
        from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction
        from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction
        from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction
        from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction
        from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction
        from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction
        from .soft_delete_response_action import SoftDeleteResponseAction
        from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction
        from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction
        from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction
        from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

