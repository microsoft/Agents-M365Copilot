from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

@dataclass
class GroupPolicyPresentationCheckBox(GroupPolicyUploadedPresentation, Parsable):
    """
    Represents an ADMX checkBox element and an ADMX boolean element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyPresentationCheckBox"
    # Default value for the check box. The default value is false.
    default_checked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentationCheckBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationCheckBox
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationCheckBox()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: dict[str, Callable[[Any], None]] = {
            "defaultChecked": lambda n : setattr(self, 'default_checked', n.get_bool_value()),
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
        writer.write_bool_value("defaultChecked", self.default_checked)
    

