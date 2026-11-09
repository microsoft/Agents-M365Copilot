from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .onboarding_status import OnboardingStatus

from ..entity import Entity

@dataclass
class TenantStatus(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Reflects a message to the user if there's an error.
    onboarding_error_message: Optional[str] = None
    # The onboardingStatus property
    onboarding_status: Optional[OnboardingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .onboarding_status import OnboardingStatus

        from ..entity import Entity
        from .onboarding_status import OnboardingStatus

        fields: dict[str, Callable[[Any], None]] = {
            "onboardingErrorMessage": lambda n : setattr(self, 'onboarding_error_message', n.get_str_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(OnboardingStatus)),
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
        writer.write_str_value("onboardingErrorMessage", self.onboarding_error_message)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
    

