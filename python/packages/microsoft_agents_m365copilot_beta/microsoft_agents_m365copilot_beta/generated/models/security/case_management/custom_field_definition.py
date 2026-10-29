from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .date_time_custom_field_definition import DateTimeCustomFieldDefinition
    from .number_custom_field_definition import NumberCustomFieldDefinition
    from .options_custom_field_definition import OptionsCustomFieldDefinition
    from .string_custom_field_definition import StringCustomFieldDefinition

from ...entity import Entity

@dataclass
class CustomFieldDefinition(Entity, Parsable):
    # The field description. Supports $filter and $orderby.
    description: Optional[str] = None
    # The field label shown on the case form. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # true if the field is disabled; otherwise, false. Supports $filter and $orderby.
    is_disabled: Optional[bool] = None
    # true if a value is required for this field; otherwise, false. Supports $filter and $orderby.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomFieldDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomFieldDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.dateTimeCustomFieldDefinition".casefold():
            from .date_time_custom_field_definition import DateTimeCustomFieldDefinition

            return DateTimeCustomFieldDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.numberCustomFieldDefinition".casefold():
            from .number_custom_field_definition import NumberCustomFieldDefinition

            return NumberCustomFieldDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.optionsCustomFieldDefinition".casefold():
            from .options_custom_field_definition import OptionsCustomFieldDefinition

            return OptionsCustomFieldDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.stringCustomFieldDefinition".casefold():
            from .string_custom_field_definition import StringCustomFieldDefinition

            return StringCustomFieldDefinition()
        return CustomFieldDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .date_time_custom_field_definition import DateTimeCustomFieldDefinition
        from .number_custom_field_definition import NumberCustomFieldDefinition
        from .options_custom_field_definition import OptionsCustomFieldDefinition
        from .string_custom_field_definition import StringCustomFieldDefinition

        from ...entity import Entity
        from .date_time_custom_field_definition import DateTimeCustomFieldDefinition
        from .number_custom_field_definition import NumberCustomFieldDefinition
        from .options_custom_field_definition import OptionsCustomFieldDefinition
        from .string_custom_field_definition import StringCustomFieldDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_bool_value("isRequired", self.is_required)
    

