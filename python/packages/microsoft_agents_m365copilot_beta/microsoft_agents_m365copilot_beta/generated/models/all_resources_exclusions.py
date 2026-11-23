from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_action_exclusion import UserActionExclusion

@dataclass
class AllResourcesExclusions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The user-action exclusions and their states. Supply the complete desired collection when updating it. Not nullable.
    user_action_exclusions: Optional[list[UserActionExclusion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AllResourcesExclusions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AllResourcesExclusions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AllResourcesExclusions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_action_exclusion import UserActionExclusion

        from .user_action_exclusion import UserActionExclusion

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userActionExclusions": lambda n : setattr(self, 'user_action_exclusions', n.get_collection_of_object_values(UserActionExclusion)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("userActionExclusions", self.user_action_exclusions)
        writer.write_additional_data_value(self.additional_data)
    

