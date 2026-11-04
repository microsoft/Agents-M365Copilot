from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

@dataclass
class GroupPolicyPresentationLongDecimalTextBox(GroupPolicyUploadedPresentation, Parsable):
    """
    Represents an ADMX longDecimalTextBox element and an ADMX longDecimal element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyPresentationLongDecimalTextBox"
    # An unsigned integer that specifies the initial value for the decimal text box. The default value is 1.
    default_value: Optional[int] = None
    # An unsigned long that specifies the maximum allowed value. The default value is 9999.
    max_value: Optional[int] = None
    # An unsigned long that specifies the minimum allowed value. The default value is 0.
    min_value: Optional[int] = None
    # Requirement to enter a value in the parameter box. The default value is false.
    required: Optional[bool] = None
    # If true, create a spin control; otherwise, create a text box for numeric entry. The default value is true.
    spin: Optional[bool] = None
    # An unsigned integer that specifies the increment of change for the spin control. The default value is 1.
    spin_step: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentationLongDecimalTextBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationLongDecimalTextBox
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationLongDecimalTextBox()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_int_value()),
            "maxValue": lambda n : setattr(self, 'max_value', n.get_int_value()),
            "minValue": lambda n : setattr(self, 'min_value', n.get_int_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "spin": lambda n : setattr(self, 'spin', n.get_bool_value()),
            "spinStep": lambda n : setattr(self, 'spin_step', n.get_int_value()),
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
        writer.write_int_value("defaultValue", self.default_value)
        writer.write_int_value("maxValue", self.max_value)
        writer.write_int_value("minValue", self.min_value)
        writer.write_bool_value("required", self.required)
        writer.write_bool_value("spin", self.spin)
        writer.write_int_value("spinStep", self.spin_step)
    

