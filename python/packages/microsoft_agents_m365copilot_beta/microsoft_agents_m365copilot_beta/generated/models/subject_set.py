from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_governance.all_excluding_agent_builder_platforms_subject_set import AllExcludingAgentBuilderPlatformsSubjectSet
    from .identity_governance.all_excluding_groups_subject_set import AllExcludingGroupsSubjectSet
    from .identity_governance.all_excluding_specific_objects_subject_set import AllExcludingSpecificObjectsSubjectSet
    from .identity_governance.group_based_subject_set import GroupBasedSubjectSet
    from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
    from .identity_governance.selected_objects_subject_set import SelectedObjectsSubjectSet

@dataclass
class SubjectSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.allExcludingAgentBuilderPlatformsSubjectSet".casefold():
            from .identity_governance.all_excluding_agent_builder_platforms_subject_set import AllExcludingAgentBuilderPlatformsSubjectSet

            return AllExcludingAgentBuilderPlatformsSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.allExcludingGroupsSubjectSet".casefold():
            from .identity_governance.all_excluding_groups_subject_set import AllExcludingGroupsSubjectSet

            return AllExcludingGroupsSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.allExcludingSpecificObjectsSubjectSet".casefold():
            from .identity_governance.all_excluding_specific_objects_subject_set import AllExcludingSpecificObjectsSubjectSet

            return AllExcludingSpecificObjectsSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.groupBasedSubjectSet".casefold():
            from .identity_governance.group_based_subject_set import GroupBasedSubjectSet

            return GroupBasedSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.ruleBasedSubjectSet".casefold():
            from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet

            return RuleBasedSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.selectedObjectsSubjectSet".casefold():
            from .identity_governance.selected_objects_subject_set import SelectedObjectsSubjectSet

            return SelectedObjectsSubjectSet()
        return SubjectSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_governance.all_excluding_agent_builder_platforms_subject_set import AllExcludingAgentBuilderPlatformsSubjectSet
        from .identity_governance.all_excluding_groups_subject_set import AllExcludingGroupsSubjectSet
        from .identity_governance.all_excluding_specific_objects_subject_set import AllExcludingSpecificObjectsSubjectSet
        from .identity_governance.group_based_subject_set import GroupBasedSubjectSet
        from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
        from .identity_governance.selected_objects_subject_set import SelectedObjectsSubjectSet

        from .identity_governance.all_excluding_agent_builder_platforms_subject_set import AllExcludingAgentBuilderPlatformsSubjectSet
        from .identity_governance.all_excluding_groups_subject_set import AllExcludingGroupsSubjectSet
        from .identity_governance.all_excluding_specific_objects_subject_set import AllExcludingSpecificObjectsSubjectSet
        from .identity_governance.group_based_subject_set import GroupBasedSubjectSet
        from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
        from .identity_governance.selected_objects_subject_set import SelectedObjectsSubjectSet

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
    

