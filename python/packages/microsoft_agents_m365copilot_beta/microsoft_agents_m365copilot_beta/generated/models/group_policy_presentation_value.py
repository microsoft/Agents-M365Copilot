from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_definition_value import GroupPolicyDefinitionValue
    from .group_policy_presentation import GroupPolicyPresentation
    from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
    from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
    from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
    from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
    from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
    from .group_policy_presentation_value_text import GroupPolicyPresentationValueText

from .entity import Entity

@dataclass
class GroupPolicyPresentationValue(Entity, Parsable):
    """
    The base presentation value entity that stores the value for a single group policy presentation.
    """
    # The date and time the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # The group policy definition value associated with the presentation value.
    definition_value: Optional[GroupPolicyDefinitionValue] = None
    # The date and time the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The group policy presentation associated with the presentation value.
    presentation: Optional[GroupPolicyPresentation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentationValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueBoolean".casefold():
            from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean

            return GroupPolicyPresentationValueBoolean()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueDecimal".casefold():
            from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal

            return GroupPolicyPresentationValueDecimal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueList".casefold():
            from .group_policy_presentation_value_list import GroupPolicyPresentationValueList

            return GroupPolicyPresentationValueList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueLongDecimal".casefold():
            from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal

            return GroupPolicyPresentationValueLongDecimal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueMultiText".casefold():
            from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText

            return GroupPolicyPresentationValueMultiText()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyPresentationValueText".casefold():
            from .group_policy_presentation_value_text import GroupPolicyPresentationValueText

            return GroupPolicyPresentationValueText()
        return GroupPolicyPresentationValue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_definition_value import GroupPolicyDefinitionValue
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
        from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
        from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
        from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
        from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
        from .group_policy_presentation_value_text import GroupPolicyPresentationValueText

        from .entity import Entity
        from .group_policy_definition_value import GroupPolicyDefinitionValue
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
        from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
        from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
        from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
        from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
        from .group_policy_presentation_value_text import GroupPolicyPresentationValueText

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definitionValue": lambda n : setattr(self, 'definition_value', n.get_object_value(GroupPolicyDefinitionValue)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "presentation": lambda n : setattr(self, 'presentation', n.get_object_value(GroupPolicyPresentation)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definitionValue", self.definition_value)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("presentation", self.presentation)
    

