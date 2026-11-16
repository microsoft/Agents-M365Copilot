from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_field_rules import PlannerFieldRules
    from .planner_property_rule import PlannerPropertyRule

from .planner_property_rule import PlannerPropertyRule

@dataclass
class PlannerTaskPropertyRule(PlannerPropertyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.plannerTaskPropertyRule"
    # Rules and restrictions for applied categories. This value doesn't currently support overrides. Accepted values for the default rule and individual overrides are allow, block.
    applied_categories: Optional[PlannerFieldRules] = None
    # Rules and restrictions for approval. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are: allow, add, remove, block.
    approval_attachment: Optional[PlannerFieldRules] = None
    # Rules and restrictions for assignments. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, addSelf, addOther, remove, removeSelf, removeOther, block.
    assignments: Optional[PlannerFieldRules] = None
    # Rules and restrictions for checklist. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, update, check, reorder, block.
    check_lists: Optional[PlannerFieldRules] = None
    # Rules and restrictions for completion requirements of the task. Accepted values are allow, add, remove, edit, and block.
    completion_requirements: Optional[list[str]] = None
    # Rules and restrictions for deleting the task. Accepted values are allow and block.
    delete: Optional[list[str]] = None
    # Rules and restrictions for changing the due date of the task. Accepted values are allow and block.
    due_date: Optional[list[str]] = None
    # Rules and restrictions for forms. Allowed overrides are userCreated and applicationCreated. The following are the accepted values for the default rule and individual overrides: allow, add, addResponse, remove, update, block.
    forms: Optional[PlannerFieldRules] = None
    # Rules and restrictions for moving the task between buckets or plans. Accepted values are allow, moveBetweenPlans, moveBetweenBuckets, and block.
    move: Optional[list[str]] = None
    # Rules and restrictions for changing the notes of the task. Accepted values are allow and block.
    notes: Optional[list[str]] = None
    # Rules and restrictions for changing the order of the task. Accepted values are allow and block.
    order: Optional[list[str]] = None
    # Rules and restrictions for changing the completion percentage of the task. Accepted values are allow, setToComplete, overrideRequirements, setToNotStarted, setToInProgress, and block.
    percent_complete: Optional[list[str]] = None
    # Rules and restrictions for changing the preview type of the task. Accepted values are allow and block.
    preview_type: Optional[list[str]] = None
    # Rules and restrictions for changing the priority of the task. Accepted values are allow and block.
    priority: Optional[list[str]] = None
    # Rules and restrictions for references. Allowed overrides are userCreated and applicationCreated. Accepted values for the default rule and individual overrides are allow, add, remove, block.
    references: Optional[PlannerFieldRules] = None
    # Rules and restrictions for changing the start date of the task. Accepted values are allow and block.
    start_date: Optional[list[str]] = None
    # Rules and restrictions for changing the title of the task. Accepted values are allow and block.
    title: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskPropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskPropertyRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskPropertyRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_field_rules import PlannerFieldRules
        from .planner_property_rule import PlannerPropertyRule

        from .planner_field_rules import PlannerFieldRules
        from .planner_property_rule import PlannerPropertyRule

        fields: dict[str, Callable[[Any], None]] = {
            "appliedCategories": lambda n : setattr(self, 'applied_categories', n.get_object_value(PlannerFieldRules)),
            "approvalAttachment": lambda n : setattr(self, 'approval_attachment', n.get_object_value(PlannerFieldRules)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(PlannerFieldRules)),
            "checkLists": lambda n : setattr(self, 'check_lists', n.get_object_value(PlannerFieldRules)),
            "completionRequirements": lambda n : setattr(self, 'completion_requirements', n.get_collection_of_primitive_values(str)),
            "delete": lambda n : setattr(self, 'delete', n.get_collection_of_primitive_values(str)),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_collection_of_primitive_values(str)),
            "forms": lambda n : setattr(self, 'forms', n.get_object_value(PlannerFieldRules)),
            "move": lambda n : setattr(self, 'move', n.get_collection_of_primitive_values(str)),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_primitive_values(str)),
            "order": lambda n : setattr(self, 'order', n.get_collection_of_primitive_values(str)),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_collection_of_primitive_values(str)),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_collection_of_primitive_values(str)),
            "priority": lambda n : setattr(self, 'priority', n.get_collection_of_primitive_values(str)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(PlannerFieldRules)),
            "startDate": lambda n : setattr(self, 'start_date', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("appliedCategories", self.applied_categories)
        writer.write_object_value("approvalAttachment", self.approval_attachment)
        writer.write_object_value("assignments", self.assignments)
        writer.write_object_value("checkLists", self.check_lists)
        writer.write_collection_of_primitive_values("completionRequirements", self.completion_requirements)
        writer.write_collection_of_primitive_values("delete", self.delete)
        writer.write_collection_of_primitive_values("dueDate", self.due_date)
        writer.write_object_value("forms", self.forms)
        writer.write_collection_of_primitive_values("move", self.move)
        writer.write_collection_of_primitive_values("notes", self.notes)
        writer.write_collection_of_primitive_values("order", self.order)
        writer.write_collection_of_primitive_values("percentComplete", self.percent_complete)
        writer.write_collection_of_primitive_values("previewType", self.preview_type)
        writer.write_collection_of_primitive_values("priority", self.priority)
        writer.write_object_value("references", self.references)
        writer.write_collection_of_primitive_values("startDate", self.start_date)
        writer.write_collection_of_primitive_values("title", self.title)
    

