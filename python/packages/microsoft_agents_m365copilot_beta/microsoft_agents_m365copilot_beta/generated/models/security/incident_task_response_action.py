from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction
    from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction
    from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction
    from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction
    from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction
    from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction
    from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction
    from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction
    from .response_action import ResponseAction
    from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction
    from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction
    from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction
    from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction
    from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction
    from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

from .response_action import ResponseAction

@dataclass
class IncidentTaskResponseAction(ResponseAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.incidentTaskResponseAction"
    # Required. The identifier value for the response action. This value is specific to the type of action being performed.
    identifier_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IncidentTaskResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IncidentTaskResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.collectInvestigationPackageIncidentTaskResponseAction".casefold():
            from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction

            return CollectInvestigationPackageIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.disableUserIncidentTaskResponseAction".casefold():
            from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction

            return DisableUserIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.enableUserIncidentTaskResponseAction".casefold():
            from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction

            return EnableUserIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.forceUserPasswordResetIncidentTaskResponseAction".casefold():
            from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction

            return ForceUserPasswordResetIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hardDeleteEmailIncidentTaskResponseAction".casefold():
            from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction

            return HardDeleteEmailIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.isolateDeviceIncidentTaskResponseAction".casefold():
            from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction

            return IsolateDeviceIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.markUserAsCompromisedIncidentTaskResponseAction".casefold():
            from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction

            return MarkUserAsCompromisedIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.requireSignInIncidentTaskResponseAction".casefold():
            from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction

            return RequireSignInIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.restrictAppExecutionIncidentTaskResponseAction".casefold():
            from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction

            return RestrictAppExecutionIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.runAntivirusScanIncidentTaskResponseAction".casefold():
            from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction

            return RunAntivirusScanIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.softDeleteIncidentTaskResponseAction".casefold():
            from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction

            return SoftDeleteIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.stopAndQuarantineFileIncidentTaskResponseAction".casefold():
            from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction

            return StopAndQuarantineFileIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unIsolateDeviceIncidentTaskResponseAction".casefold():
            from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction

            return UnIsolateDeviceIncidentTaskResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unRestrictAppExecutionIncidentTaskResponseAction".casefold():
            from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

            return UnRestrictAppExecutionIncidentTaskResponseAction()
        return IncidentTaskResponseAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction
        from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction
        from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction
        from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction
        from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction
        from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction
        from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction
        from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction
        from .response_action import ResponseAction
        from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction
        from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction
        from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction
        from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction
        from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction
        from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

        from .collect_investigation_package_incident_task_response_action import CollectInvestigationPackageIncidentTaskResponseAction
        from .disable_user_incident_task_response_action import DisableUserIncidentTaskResponseAction
        from .enable_user_incident_task_response_action import EnableUserIncidentTaskResponseAction
        from .force_user_password_reset_incident_task_response_action import ForceUserPasswordResetIncidentTaskResponseAction
        from .hard_delete_email_incident_task_response_action import HardDeleteEmailIncidentTaskResponseAction
        from .isolate_device_incident_task_response_action import IsolateDeviceIncidentTaskResponseAction
        from .mark_user_as_compromised_incident_task_response_action import MarkUserAsCompromisedIncidentTaskResponseAction
        from .require_sign_in_incident_task_response_action import RequireSignInIncidentTaskResponseAction
        from .response_action import ResponseAction
        from .restrict_app_execution_incident_task_response_action import RestrictAppExecutionIncidentTaskResponseAction
        from .run_antivirus_scan_incident_task_response_action import RunAntivirusScanIncidentTaskResponseAction
        from .soft_delete_incident_task_response_action import SoftDeleteIncidentTaskResponseAction
        from .stop_and_quarantine_file_incident_task_response_action import StopAndQuarantineFileIncidentTaskResponseAction
        from .un_isolate_device_incident_task_response_action import UnIsolateDeviceIncidentTaskResponseAction
        from .un_restrict_app_execution_incident_task_response_action import UnRestrictAppExecutionIncidentTaskResponseAction

        fields: dict[str, Callable[[Any], None]] = {
            "identifierValue": lambda n : setattr(self, 'identifier_value', n.get_str_value()),
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
        writer.write_str_value("identifierValue", self.identifier_value)
    

