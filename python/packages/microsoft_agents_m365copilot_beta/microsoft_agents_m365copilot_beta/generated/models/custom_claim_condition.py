from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .claim_condition_user_type import ClaimConditionUserType
    from .custom_claim_condition_base import CustomClaimConditionBase

from .custom_claim_condition_base import CustomClaimConditionBase

@dataclass
class CustomClaimCondition(CustomClaimConditionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customClaimCondition"
    # A list of groups (GUIDs) to which the user/application must be a member for this condition to be applied.
    member_of: Optional[list[str]] = None
    # The type of user this condition applies to. The possible values are: any, members, allGuests, aadGuests, externalGuests, unknownFutureValue.
    user_type: Optional[ClaimConditionUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomClaimCondition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomClaimCondition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomClaimCondition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .claim_condition_user_type import ClaimConditionUserType
        from .custom_claim_condition_base import CustomClaimConditionBase

        from .claim_condition_user_type import ClaimConditionUserType
        from .custom_claim_condition_base import CustomClaimConditionBase

        fields: dict[str, Callable[[Any], None]] = {
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_primitive_values(str)),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(ClaimConditionUserType)),
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
        writer.write_collection_of_primitive_values("memberOf", self.member_of)
        writer.write_enum_value("userType", self.user_type)
    

