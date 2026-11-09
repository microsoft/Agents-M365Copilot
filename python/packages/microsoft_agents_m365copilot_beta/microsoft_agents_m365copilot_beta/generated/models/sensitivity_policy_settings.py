from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sensitivity_label_target import SensitivityLabelTarget

from .entity import Entity

@dataclass
class SensitivityPolicySettings(Entity, Parsable):
    # The applicableTo property
    applicable_to: Optional[SensitivityLabelTarget] = None
    # The downgradeSensitivityRequiresJustification property
    downgrade_sensitivity_requires_justification: Optional[bool] = None
    # The helpWebUrl property
    help_web_url: Optional[str] = None
    # The isMandatory property
    is_mandatory: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensitivityPolicySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityPolicySettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensitivityPolicySettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sensitivity_label_target import SensitivityLabelTarget

        from .entity import Entity
        from .sensitivity_label_target import SensitivityLabelTarget

        fields: dict[str, Callable[[Any], None]] = {
            "applicableTo": lambda n : setattr(self, 'applicable_to', n.get_collection_of_enum_values(SensitivityLabelTarget)),
            "downgradeSensitivityRequiresJustification": lambda n : setattr(self, 'downgrade_sensitivity_requires_justification', n.get_bool_value()),
            "helpWebUrl": lambda n : setattr(self, 'help_web_url', n.get_str_value()),
            "isMandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
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
        writer.write_enum_value("applicableTo", self.applicable_to)
        writer.write_bool_value("downgradeSensitivityRequiresJustification", self.downgrade_sensitivity_requires_justification)
        writer.write_str_value("helpWebUrl", self.help_web_url)
        writer.write_bool_value("isMandatory", self.is_mandatory)
    

