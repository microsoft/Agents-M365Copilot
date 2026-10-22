from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceEnrollmentPlatformRestriction(AdditionalDataHolder, Parsable):
    """
    Platform specific enrollment restrictions
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of blocked Manufacturers.
    blocked_manufacturers: Optional[list[str]] = None
    # Collection of blocked Skus.
    blocked_skus: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Max OS version supported
    os_maximum_version: Optional[str] = None
    # Min OS version supported
    os_minimum_version: Optional[str] = None
    # Block personally owned devices from enrolling
    personal_device_enrollment_blocked: Optional[bool] = None
    # Block the platform from enrolling
    platform_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceEnrollmentPlatformRestriction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestriction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceEnrollmentPlatformRestriction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "blockedManufacturers": lambda n : setattr(self, 'blocked_manufacturers', n.get_collection_of_primitive_values(str)),
            "blockedSkus": lambda n : setattr(self, 'blocked_skus', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "personalDeviceEnrollmentBlocked": lambda n : setattr(self, 'personal_device_enrollment_blocked', n.get_bool_value()),
            "platformBlocked": lambda n : setattr(self, 'platform_blocked', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("blockedManufacturers", self.blocked_manufacturers)
        writer.write_collection_of_primitive_values("blockedSkus", self.blocked_skus)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("personalDeviceEnrollmentBlocked", self.personal_device_enrollment_blocked)
        writer.write_bool_value("platformBlocked", self.platform_blocked)
        writer.write_additional_data_value(self.additional_data)
    

