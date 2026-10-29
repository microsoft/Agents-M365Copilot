from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
    from .apple_owner_type_enrollment_type import AppleOwnerTypeEnrollmentType
    from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
    from .device_platform_type import DevicePlatformType
    from .entity import Entity

from .entity import Entity

@dataclass
class AppleUserInitiatedEnrollmentProfile(Entity, Parsable):
    """
    The enrollmentProfile resource represents a collection of configurations which must be provided pre-enrollment to enable enrolling certain devices whose identities have been pre-staged. Pre-staged device identities are assigned to this type of profile to apply the profile's configurations at enrollment of the corresponding device.
    """
    # The list of assignments for this profile.
    assignments: Optional[list[AppleEnrollmentProfileAssignment]] = None
    # List of available enrollment type options
    available_enrollment_type_options: Optional[list[AppleOwnerTypeEnrollmentType]] = None
    # Profile creation time
    created_date_time: Optional[datetime.datetime] = None
    # The defaultEnrollmentType property
    default_enrollment_type: Optional[AppleUserInitiatedEnrollmentType] = None
    # Description of the profile
    description: Optional[str] = None
    # Name of the profile
    display_name: Optional[str] = None
    # Profile last modified time
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types.
    platform: Optional[DevicePlatformType] = None
    # Priority, 0 is highest
    priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppleUserInitiatedEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleUserInitiatedEnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppleUserInitiatedEnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
        from .apple_owner_type_enrollment_type import AppleOwnerTypeEnrollmentType
        from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
        from .device_platform_type import DevicePlatformType
        from .entity import Entity

        from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
        from .apple_owner_type_enrollment_type import AppleOwnerTypeEnrollmentType
        from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
        from .device_platform_type import DevicePlatformType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(AppleEnrollmentProfileAssignment)),
            "availableEnrollmentTypeOptions": lambda n : setattr(self, 'available_enrollment_type_options', n.get_collection_of_object_values(AppleOwnerTypeEnrollmentType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultEnrollmentType": lambda n : setattr(self, 'default_enrollment_type', n.get_enum_value(AppleUserInitiatedEnrollmentType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(DevicePlatformType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("availableEnrollmentTypeOptions", self.available_enrollment_type_options)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("defaultEnrollmentType", self.default_enrollment_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platform", self.platform)
        writer.write_int_value("priority", self.priority)
    

