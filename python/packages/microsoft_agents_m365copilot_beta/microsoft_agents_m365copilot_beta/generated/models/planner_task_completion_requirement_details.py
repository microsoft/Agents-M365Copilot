from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_approval_requirement import PlannerApprovalRequirement
    from .planner_checklist_requirement import PlannerChecklistRequirement
    from .planner_forms_requirement import PlannerFormsRequirement

@dataclass
class PlannerTaskCompletionRequirementDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information about the requirements of an approval.
    approval_requirement: Optional[PlannerApprovalRequirement] = None
    # Information about the requirements for completing the checklist.
    checklist_requirement: Optional[PlannerChecklistRequirement] = None
    # Information about the requirements for completing the forms.
    forms_requirement: Optional[PlannerFormsRequirement] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskCompletionRequirementDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskCompletionRequirementDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskCompletionRequirementDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_approval_requirement import PlannerApprovalRequirement
        from .planner_checklist_requirement import PlannerChecklistRequirement
        from .planner_forms_requirement import PlannerFormsRequirement

        from .planner_approval_requirement import PlannerApprovalRequirement
        from .planner_checklist_requirement import PlannerChecklistRequirement
        from .planner_forms_requirement import PlannerFormsRequirement

        fields: dict[str, Callable[[Any], None]] = {
            "approvalRequirement": lambda n : setattr(self, 'approval_requirement', n.get_object_value(PlannerApprovalRequirement)),
            "checklistRequirement": lambda n : setattr(self, 'checklist_requirement', n.get_object_value(PlannerChecklistRequirement)),
            "formsRequirement": lambda n : setattr(self, 'forms_requirement', n.get_object_value(PlannerFormsRequirement)),
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
        writer.write_object_value("approvalRequirement", self.approval_requirement)
        writer.write_object_value("checklistRequirement", self.checklist_requirement)
        writer.write_object_value("formsRequirement", self.forms_requirement)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

