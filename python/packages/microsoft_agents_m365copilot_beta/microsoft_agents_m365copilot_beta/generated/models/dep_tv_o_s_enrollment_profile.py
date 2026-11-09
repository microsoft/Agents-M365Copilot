from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enrollment_profile import EnrollmentProfile

from .enrollment_profile import EnrollmentProfile

@dataclass
class DepTvOSEnrollmentProfile(EnrollmentProfile, Parsable):
    """
    The depTvOSEnrollmentProfile resource represents an Apple Device Enrollment Program (DEP) enrollment profile specific to Apple TV device configuration. This type of profile must be assigned to Apple TV devices before the devices can enroll via DEP. However, This entity type will only be used as a navigation property to fetch the display name of the profile while getting the exitsing depOnboardingSetting entity, it won't support any operations, as the new entity is supported in device configuration(DCV2) graph calls
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.depTvOSEnrollmentProfile"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepTvOSEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepTvOSEnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepTvOSEnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enrollment_profile import EnrollmentProfile

        from .enrollment_profile import EnrollmentProfile

        fields: dict[str, Callable[[Any], None]] = {
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
    

