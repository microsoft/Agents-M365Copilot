from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_user_attributes import AdditionalUserAttributes
    from .additional_user_options import AdditionalUserOptions

@dataclass
class UserManagementOptions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The different attribute choices for the users to be provisioned. The possible values are: userGradeLevel, userNumber, unknownFutureValue.
    additional_attributes: Optional[list[AdditionalUserAttributes]] = None
    # The additionalOptions property
    additional_options: Optional[AdditionalUserOptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserManagementOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserManagementOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserManagementOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .additional_user_attributes import AdditionalUserAttributes
        from .additional_user_options import AdditionalUserOptions

        from .additional_user_attributes import AdditionalUserAttributes
        from .additional_user_options import AdditionalUserOptions

        fields: dict[str, Callable[[Any], None]] = {
            "additionalAttributes": lambda n : setattr(self, 'additional_attributes', n.get_collection_of_enum_values(AdditionalUserAttributes)),
            "additionalOptions": lambda n : setattr(self, 'additional_options', n.get_object_value(AdditionalUserOptions)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_enum_values("additionalAttributes", self.additional_attributes)
        writer.write_object_value("additionalOptions", self.additional_options)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

