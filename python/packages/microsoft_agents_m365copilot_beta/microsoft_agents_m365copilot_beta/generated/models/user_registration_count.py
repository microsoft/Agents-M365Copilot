from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .registration_status_type import RegistrationStatusType

@dataclass
class UserRegistrationCount(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the registration count for your tenant.
    registration_count: Optional[int] = None
    # The registrationStatus property
    registration_status: Optional[RegistrationStatusType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserRegistrationCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationCount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserRegistrationCount()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .registration_status_type import RegistrationStatusType

        from .registration_status_type import RegistrationStatusType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "registrationCount": lambda n : setattr(self, 'registration_count', n.get_int_value()),
            "registrationStatus": lambda n : setattr(self, 'registration_status', n.get_enum_value(RegistrationStatusType)),
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
        writer.write_int_value("registrationCount", self.registration_count)
        writer.write_enum_value("registrationStatus", self.registration_status)
        writer.write_additional_data_value(self.additional_data)
    

