from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .discovery_source import DiscoverySource
    from .enrollment_state import EnrollmentState
    from .entity import Entity
    from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
    from .platform import Platform

from .entity import Entity

@dataclass
class ImportedAppleDeviceIdentity(Entity, Parsable):
    """
    The importedAppleDeviceIdentity resource represents the imported device identity of an Apple device .
    """
    # Created Date Time of the device
    created_date_time: Optional[datetime.datetime] = None
    # The description of the device
    description: Optional[str] = None
    # The discoverySource property
    discovery_source: Optional[DiscoverySource] = None
    # The enrollmentState property
    enrollment_state: Optional[EnrollmentState] = None
    # Indicates if the device is deleted from Apple Business Manager
    is_deleted: Optional[bool] = None
    # Indicates if the Apple device is supervised.
    is_supervised: Optional[bool] = None
    # Last Contacted Date Time of the device
    last_contacted_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform: Optional[Platform] = None
    # The time enrollment profile was assigned to the device
    requested_enrollment_profile_assignment_date_time: Optional[datetime.datetime] = None
    # Enrollment profile Id admin intends to apply to the device during next enrollment
    requested_enrollment_profile_id: Optional[str] = None
    # Device serial number
    serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportedAppleDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportedAppleDeviceIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedAppleDeviceIdentityResult".casefold():
            from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult

            return ImportedAppleDeviceIdentityResult()
        return ImportedAppleDeviceIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .discovery_source import DiscoverySource
        from .enrollment_state import EnrollmentState
        from .entity import Entity
        from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
        from .platform import Platform

        from .discovery_source import DiscoverySource
        from .enrollment_state import EnrollmentState
        from .entity import Entity
        from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
        from .platform import Platform

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoverySource": lambda n : setattr(self, 'discovery_source', n.get_enum_value(DiscoverySource)),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(EnrollmentState)),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "isSupervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "lastContactedDateTime": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(Platform)),
            "requestedEnrollmentProfileAssignmentDateTime": lambda n : setattr(self, 'requested_enrollment_profile_assignment_date_time', n.get_datetime_value()),
            "requestedEnrollmentProfileId": lambda n : setattr(self, 'requested_enrollment_profile_id', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("discoverySource", self.discovery_source)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_bool_value("isSupervised", self.is_supervised)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_enum_value("platform", self.platform)
        writer.write_datetime_value("requestedEnrollmentProfileAssignmentDateTime", self.requested_enrollment_profile_assignment_date_time)
        writer.write_str_value("requestedEnrollmentProfileId", self.requested_enrollment_profile_id)
        writer.write_str_value("serialNumber", self.serial_number)
    

