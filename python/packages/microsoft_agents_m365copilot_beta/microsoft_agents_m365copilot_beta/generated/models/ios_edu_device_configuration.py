from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .ios_edu_certificate_settings import IosEduCertificateSettings

from .device_configuration import DeviceConfiguration

@dataclass
class IosEduDeviceConfiguration(DeviceConfiguration, Parsable):
    """
    iOS Education device configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosEduDeviceConfiguration"
    # The Trusted Root and PFX certificates for Device
    device_certificate_settings: Optional[IosEduCertificateSettings] = None
    # The Trusted Root and PFX certificates for Student
    student_certificate_settings: Optional[IosEduCertificateSettings] = None
    # Trusted Root and PFX certificates for iOS EDU.
    teacher_certificate_settings: Optional[IosEduCertificateSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosEduDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosEduDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosEduDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .ios_edu_certificate_settings import IosEduCertificateSettings

        from .device_configuration import DeviceConfiguration
        from .ios_edu_certificate_settings import IosEduCertificateSettings

        fields: dict[str, Callable[[Any], None]] = {
            "deviceCertificateSettings": lambda n : setattr(self, 'device_certificate_settings', n.get_object_value(IosEduCertificateSettings)),
            "studentCertificateSettings": lambda n : setattr(self, 'student_certificate_settings', n.get_object_value(IosEduCertificateSettings)),
            "teacherCertificateSettings": lambda n : setattr(self, 'teacher_certificate_settings', n.get_object_value(IosEduCertificateSettings)),
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
        writer.write_object_value("deviceCertificateSettings", self.device_certificate_settings)
        writer.write_object_value("studentCertificateSettings", self.student_certificate_settings)
        writer.write_object_value("teacherCertificateSettings", self.teacher_certificate_settings)
    

