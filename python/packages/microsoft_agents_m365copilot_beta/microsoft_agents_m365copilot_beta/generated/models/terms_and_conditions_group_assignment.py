from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .terms_and_conditions import TermsAndConditions

from .entity import Entity

@dataclass
class TermsAndConditionsGroupAssignment(Entity, Parsable):
    """
    A termsAndConditionsGroupAssignment entity represents the assignment of a given Terms and Conditions (T&C) policy to a given group. Users in the group will be required to accept the terms in order to have devices enrolled into Intune.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier of a group that the T&C policy is assigned to.
    target_group_id: Optional[str] = None
    # Navigation link to the terms and conditions that are assigned.
    terms_and_conditions: Optional[TermsAndConditions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TermsAndConditionsGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditionsGroupAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TermsAndConditionsGroupAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .terms_and_conditions import TermsAndConditions

        from .entity import Entity
        from .terms_and_conditions import TermsAndConditions

        fields: dict[str, Callable[[Any], None]] = {
            "targetGroupId": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_object_value(TermsAndConditions)),
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
        writer.write_str_value("targetGroupId", self.target_group_id)
        writer.write_object_value("termsAndConditions", self.terms_and_conditions)
    

