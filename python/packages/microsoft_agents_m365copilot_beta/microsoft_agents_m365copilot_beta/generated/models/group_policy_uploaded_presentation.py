from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_presentation import GroupPolicyPresentation
    from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
    from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
    from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
    from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
    from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
    from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
    from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
    from .group_policy_presentation_text import GroupPolicyPresentationText
    from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

from .group_policy_presentation import GroupPolicyPresentation

@dataclass
class GroupPolicyUploadedPresentation(GroupPolicyPresentation, Parsable):
    """
    Represents an ADMX checkBox element and an ADMX boolean element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyUploadedPresentation"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyUploadedPresentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedPresentation
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
        return GroupPolicyUploadedPresentation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
        from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
        from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
        from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
        from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
        from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
        from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
        from .group_policy_presentation_text import GroupPolicyPresentationText
        from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_presentation_check_box import GroupPolicyPresentationCheckBox
        from .group_policy_presentation_combo_box import GroupPolicyPresentationComboBox
        from .group_policy_presentation_decimal_text_box import GroupPolicyPresentationDecimalTextBox
        from .group_policy_presentation_dropdown_list import GroupPolicyPresentationDropdownList
        from .group_policy_presentation_list_box import GroupPolicyPresentationListBox
        from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox
        from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox
        from .group_policy_presentation_text import GroupPolicyPresentationText
        from .group_policy_presentation_text_box import GroupPolicyPresentationTextBox

        fields: dict[str, Callable[[Any], None]] = {
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
    

