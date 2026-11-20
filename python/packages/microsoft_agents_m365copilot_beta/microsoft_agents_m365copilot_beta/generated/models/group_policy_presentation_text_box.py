from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

@dataclass
class GroupPolicyPresentationTextBox(GroupPolicyUploadedPresentation, Parsable):
    """
    Represents an ADMX textBox element and an ADMX text element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyPresentationTextBox"
    # Localized default string displayed in the text box. The default value is empty.
    default_value: Optional[str] = None
    # An unsigned integer that specifies the maximum number of text characters. Default value is 1023.
    max_length: Optional[int] = None
    # Requirement to enter a value in the text box. Default value is false.
    required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentationTextBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationTextBox
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationTextBox()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "maxLength": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
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
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_int_value("maxLength", self.max_length)
        writer.write_bool_value("required", self.required)
    

