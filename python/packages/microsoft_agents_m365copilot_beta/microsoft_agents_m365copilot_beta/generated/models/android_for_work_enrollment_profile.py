from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mime_content import MimeContent

from .entity import Entity

@dataclass
class AndroidForWorkEnrollmentProfile(Entity, Parsable):
    """
    Enrollment Profile used to enroll COSU devices using Google's Cloud Management.
    """
    # Tenant GUID the enrollment profile belongs to.
    account_id: Optional[str] = None
    # Date time the enrollment profile was created.
    created_date_time: Optional[datetime.datetime] = None
    # Description for the enrollment profile.
    description: Optional[str] = None
    # Display name for the enrollment profile.
    display_name: Optional[str] = None
    # Total number of Android devices that have enrolled using this enrollment profile.
    enrolled_device_count: Optional[int] = None
    # Date time the enrollment profile was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # String used to generate a QR code for the token.
    qr_code_content: Optional[str] = None
    # String used to generate a QR code for the token.
    qr_code_image: Optional[MimeContent] = None
    # Date time the most recently created token will expire.
    token_expiration_date_time: Optional[datetime.datetime] = None
    # Value of the most recently created token for this enrollment profile.
    token_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkEnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkEnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mime_content import MimeContent

        from .entity import Entity
        from .mime_content import MimeContent

        fields: dict[str, Callable[[Any], None]] = {
            "accountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolledDeviceCount": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "qrCodeContent": lambda n : setattr(self, 'qr_code_content', n.get_str_value()),
            "qrCodeImage": lambda n : setattr(self, 'qr_code_image', n.get_object_value(MimeContent)),
            "tokenExpirationDateTime": lambda n : setattr(self, 'token_expiration_date_time', n.get_datetime_value()),
            "tokenValue": lambda n : setattr(self, 'token_value', n.get_str_value()),
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
        writer.write_str_value("accountId", self.account_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("qrCodeContent", self.qr_code_content)
        writer.write_object_value("qrCodeImage", self.qr_code_image)
        writer.write_datetime_value("tokenExpirationDateTime", self.token_expiration_date_time)
        writer.write_str_value("tokenValue", self.token_value)
    

