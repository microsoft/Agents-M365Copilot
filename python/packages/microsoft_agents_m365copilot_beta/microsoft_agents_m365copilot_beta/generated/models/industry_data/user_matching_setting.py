from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identifier_type_reference_value import IdentifierTypeReferenceValue
    from .role_group import RoleGroup
    from .user_match_target_reference_value import UserMatchTargetReferenceValue

@dataclass
class UserMatchingSetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The RefUserMatchTarget for matching a user from the source with a Microsoft Entra user object.
    match_target: Optional[UserMatchTargetReferenceValue] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority order to apply when a user has multiple RefRole codes assigned.
    priority_order: Optional[int] = None
    # The roleGroup property
    role_group: Optional[RoleGroup] = None
    # The sourceIdentifier property
    source_identifier: Optional[IdentifierTypeReferenceValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserMatchingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserMatchingSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserMatchingSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .role_group import RoleGroup
        from .user_match_target_reference_value import UserMatchTargetReferenceValue

        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .role_group import RoleGroup
        from .user_match_target_reference_value import UserMatchTargetReferenceValue

        fields: dict[str, Callable[[Any], None]] = {
            "matchTarget": lambda n : setattr(self, 'match_target', n.get_object_value(UserMatchTargetReferenceValue)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priorityOrder": lambda n : setattr(self, 'priority_order', n.get_int_value()),
            "roleGroup": lambda n : setattr(self, 'role_group', n.get_object_value(RoleGroup)),
            "sourceIdentifier": lambda n : setattr(self, 'source_identifier', n.get_object_value(IdentifierTypeReferenceValue)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("matchTarget", self.match_target)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priorityOrder", self.priority_order)
        writer.write_object_value("roleGroup", self.role_group)
        writer.write_object_value("sourceIdentifier", self.source_identifier)
        writer.write_additional_data_value(self.additional_data)
    

