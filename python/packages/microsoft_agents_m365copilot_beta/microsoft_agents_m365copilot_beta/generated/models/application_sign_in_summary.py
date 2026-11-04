from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ApplicationSignInSummary(Entity, Parsable):
    # Name of the application that the user signed into.
    app_display_name: Optional[str] = None
    # Count of failed sign-ins made by the application.
    failed_sign_in_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Percentage of successful sign-ins made by the application.
    success_percentage: Optional[float] = None
    # Count of successful sign-ins made by the application.
    successful_sign_in_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationSignInSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationSignInSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationSignInSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "failedSignInCount": lambda n : setattr(self, 'failed_sign_in_count', n.get_int_value()),
            "successPercentage": lambda n : setattr(self, 'success_percentage', n.get_float_value()),
            "successfulSignInCount": lambda n : setattr(self, 'successful_sign_in_count', n.get_int_value()),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_int_value("failedSignInCount", self.failed_sign_in_count)
        writer.write_float_value("successPercentage", self.success_percentage)
        writer.write_int_value("successfulSignInCount", self.successful_sign_in_count)
    

