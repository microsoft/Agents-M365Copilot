from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_definition import GroupPolicyDefinition
    from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
    from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
    from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
    from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
    from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
    from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
    from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
    from .group_policy_presentation_text import GroupPolicyPresentationText
    from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .entity import Entity

@dataclass
class GroupPolicyPresentation(Entity, Parsable):
    """
    The base entity for the display presentation of any of the additional options in a group policy definition.
    """
    # The group policy definition associated with the presentation.
    definition: Optional[GroupPolicyDefinition] = None
    # Localized text label for any presentation entity. The default value is empty.
    label: Optional[str] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationCheckBox".casefold():
            from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox

            return GroupPolicyPresentationCheckBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationComboBox".casefold():
            from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox

            return GroupPolicyPresentationComboBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationDecimalTextBox".casefold():
            from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox

            return GroupPolicyPresentationDecimalTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationDropdownList".casefold():
            from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList

            return GroupPolicyPresentationDropdownList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationListBox".casefold():
            from .group_policy_presentation_list_box import GroupPolicyPresentationListBox

            return GroupPolicyPresentationListBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox".casefold():
            from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox

            return GroupPolicyPresentationLongDecimalTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationMultiTextBox".casefold():
            from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox

            return GroupPolicyPresentationMultiTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationText".casefold():
            from .group_policy_presentation_text import GroupPolicyPresentationText

            return GroupPolicyPresentationText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationTextBox".casefold():
            from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

            return GroupPolicyPresentationTextBox()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyUploadedPresentation".casefold():
            from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

            return GroupPolicyUploadedPresentation()
        return GroupPolicyPresentation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
        from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
        from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
        from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
        from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
        from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
        from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
        from .group_policy_presentation_text import GroupPolicyPresentationText
        from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .entity import Entity
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
        from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
        from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
        from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
        from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
        from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
        from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
        from .group_policy_presentation_text import GroupPolicyPresentationText
        from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(GroupPolicyDefinition)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("label", self.label)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

