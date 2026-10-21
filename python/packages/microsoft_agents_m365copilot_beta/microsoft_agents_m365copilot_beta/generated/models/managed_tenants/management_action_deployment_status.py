from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .management_action_status import ManagementActionStatus
    from .workload_action_deployment_status import WorkloadActionDeploymentStatus

@dataclass
class ManagementActionDeploymentStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The identifier for the management action. Required. Read-only.
    management_action_id: Optional[str] = None
    # The management template identifier that was used to generate the management action. Required. Read-only.
    management_template_id: Optional[str] = None
    # The managementTemplateVersion property
    management_template_version: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ManagementActionStatus] = None
    # The collection of workload action deployment statues for the given management action. Optional.
    workload_action_deployment_statuses: Optional[list[WorkloadActionDeploymentStatus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementActionDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementActionDeploymentStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementActionDeploymentStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .management_action_status import ManagementActionStatus
        from .workload_action_deployment_status import WorkloadActionDeploymentStatus

        from .management_action_status import ManagementActionStatus
        from .workload_action_deployment_status import WorkloadActionDeploymentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "managementActionId": lambda n : setattr(self, 'management_action_id', n.get_str_value()),
            "managementTemplateId": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "managementTemplateVersion": lambda n : setattr(self, 'management_template_version', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ManagementActionStatus)),
            "workloadActionDeploymentStatuses": lambda n : setattr(self, 'workload_action_deployment_statuses', n.get_collection_of_object_values(WorkloadActionDeploymentStatus)),
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
        writer.write_str_value("managementActionId", self.management_action_id)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_int_value("managementTemplateVersion", self.management_template_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("workloadActionDeploymentStatuses", self.workload_action_deployment_statuses)
        writer.write_additional_data_value(self.additional_data)
    

