from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration
    from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
    from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class DeviceEnrollmentPlatformRestrictionConfiguration(DeviceEnrollmentConfiguration, Parsable):
    """
    Device Enrollment Configuration that restricts the types of devices a user can enroll for a single platform
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceEnrollmentPlatformRestrictionConfiguration"
    # Restrictions based on platform, platform operating system version, and device ownership
    platform_restriction: Optional[DeviceEnrollmentPlatformRestriction] = None
    # This enum indicates the platform type for which the enrollment restriction applies.
    platform_type: Optional[EnrollmentRestrictionPlatformType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceEnrollmentPlatformRestrictionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestrictionConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceEnrollmentPlatformRestrictionConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
        from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
        from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

        fields: dict[str, Callable[[Any], None]] = {
            "platformRestriction": lambda n : setattr(self, 'platform_restriction', n.get_object_value(DeviceEnrollmentPlatformRestriction)),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(EnrollmentRestrictionPlatformType)),
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
        writer.write_object_value("platformRestriction", self.platform_restriction)
        writer.write_enum_value("platformType", self.platform_type)
    

