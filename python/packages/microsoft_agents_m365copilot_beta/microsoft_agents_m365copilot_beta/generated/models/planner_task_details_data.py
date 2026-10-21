from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .planner_base_approval_attachment import PlannerBaseApprovalAttachment
    from .planner_checklist_items import PlannerChecklistItems
    from .planner_external_references import PlannerExternalReferences
    from .planner_forms_dictionary import PlannerFormsDictionary
    from .planner_preview_type import PlannerPreviewType
    from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails

@dataclass
class PlannerTaskDetailsData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Detailed information about the approval that is attached to the task.
    approval_attachment: Optional[PlannerBaseApprovalAttachment] = None
    # The collection of checklist items on the task.
    checklist: Optional[PlannerChecklistItems] = None
    # Contains detailed information about requirements on the task.
    completion_requirements: Optional[PlannerTaskCompletionRequirementDetails] = None
    # Description of the task.
    description: Optional[str] = None
    # The collection of forms associated with the task.
    forms: Optional[PlannerFormsDictionary] = None
    # Rich text description of the task for use by applications that support HTML content.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The previewType property
    preview_type: Optional[PlannerPreviewType] = None
    # The collection of references on the task.
    references: Optional[PlannerExternalReferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskDetailsData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskDetailsData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskDetailsData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .planner_base_approval_attachment import PlannerBaseApprovalAttachment
        from .planner_checklist_items import PlannerChecklistItems
        from .planner_external_references import PlannerExternalReferences
        from .planner_forms_dictionary import PlannerFormsDictionary
        from .planner_preview_type import PlannerPreviewType
        from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails

        from .item_body import ItemBody
        from .planner_base_approval_attachment import PlannerBaseApprovalAttachment
        from .planner_checklist_items import PlannerChecklistItems
        from .planner_external_references import PlannerExternalReferences
        from .planner_forms_dictionary import PlannerFormsDictionary
        from .planner_preview_type import PlannerPreviewType
        from .planner_task_completion_requirement_details import PlannerTaskCompletionRequirementDetails

        fields: dict[str, Callable[[Any], None]] = {
            "approvalAttachment": lambda n : setattr(self, 'approval_attachment', n.get_object_value(PlannerBaseApprovalAttachment)),
            "checklist": lambda n : setattr(self, 'checklist', n.get_object_value(PlannerChecklistItems)),
            "completionRequirements": lambda n : setattr(self, 'completion_requirements', n.get_object_value(PlannerTaskCompletionRequirementDetails)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "forms": lambda n : setattr(self, 'forms', n.get_object_value(PlannerFormsDictionary)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(PlannerPreviewType)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(PlannerExternalReferences)),
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
        writer.write_object_value("approvalAttachment", self.approval_attachment)
        writer.write_object_value("checklist", self.checklist)
        writer.write_object_value("completionRequirements", self.completion_requirements)
        writer.write_str_value("description", self.description)
        writer.write_object_value("forms", self.forms)
        writer.write_object_value("notes", self.notes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_object_value("references", self.references)
        writer.write_additional_data_value(self.additional_data)
    

