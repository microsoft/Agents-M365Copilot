from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enrollment_state import EnrollmentState
    from .entity import Entity
    from .imported_device_identity_result import ImportedDeviceIdentityResult
    from .imported_device_identity_type import ImportedDeviceIdentityType
    from .platform import Platform

from .entity import Entity

@dataclass
class ImportedDeviceIdentity(Entity, Parsable):
    """
    The importedDeviceIdentity resource represents a unique hardware identity of a device that has been pre-staged for pre-enrollment configuration.
    """
    # Created Date Time of the device
    created_date_time: Optional[datetime.datetime] = None
    # The description of the device
    description: Optional[str] = None
    # The enrollmentState property
    enrollment_state: Optional[EnrollmentState] = None
    # Imported Device Identifier
    imported_device_identifier: Optional[str] = None
    # The importedDeviceIdentityType property
    imported_device_identity_type: Optional[ImportedDeviceIdentityType] = None
    # Last Contacted Date Time of the device
    last_contacted_date_time: Optional[datetime.datetime] = None
    # Last Modified DateTime of the description
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform: Optional[Platform] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportedDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportedDeviceIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedDeviceIdentityResult".casefold():
            from .imported_device_identity_result import ImportedDeviceIdentityResult

            return ImportedDeviceIdentityResult()
        return ImportedDeviceIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enrollment_state import EnrollmentState
        from .entity import Entity
        from .imported_device_identity_result import ImportedDeviceIdentityResult
        from .imported_device_identity_type import ImportedDeviceIdentityType
        from .platform import Platform

        from .enrollment_state import EnrollmentState
        from .entity import Entity
        from .imported_device_identity_result import ImportedDeviceIdentityResult
        from .imported_device_identity_type import ImportedDeviceIdentityType
        from .platform import Platform

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(EnrollmentState)),
            "importedDeviceIdentifier": lambda n : setattr(self, 'imported_device_identifier', n.get_str_value()),
            "importedDeviceIdentityType": lambda n : setattr(self, 'imported_device_identity_type', n.get_enum_value(ImportedDeviceIdentityType)),
            "lastContactedDateTime": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(Platform)),
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
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_str_value("importedDeviceIdentifier", self.imported_device_identifier)
        writer.write_enum_value("importedDeviceIdentityType", self.imported_device_identity_type)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platform", self.platform)
    

