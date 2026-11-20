from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .qr_code_image_details import QrCodeImageDetails

from .entity import Entity

@dataclass
class QrCode(Entity, Parsable):
    # The date and time when the QR code was created.
    created_date_time: Optional[datetime.datetime] = None
    # Temporary QR code lifetime is between 1-12 hours. Standard QR code lifetime is in days and max. is 395 days (13 months) and default value is 365 days (12 months).
    expire_date_time: Optional[datetime.datetime] = None
    # The QR code image's raw data that is returned when a standard or temporary QR code is created.
    image: Optional[QrCodeImageDetails] = None
    # The date and time when the QR code was last used for a successful sign-in.
    last_used_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the QR code becomes active and available to use.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrCode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrCode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .qr_code_image_details import QrCodeImageDetails

        from .entity import Entity
        from .qr_code_image_details import QrCodeImageDetails

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expireDateTime": lambda n : setattr(self, 'expire_date_time', n.get_datetime_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(QrCodeImageDetails)),
            "lastUsedDateTime": lambda n : setattr(self, 'last_used_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("expireDateTime", self.expire_date_time)
        writer.write_object_value("image", self.image)
        writer.write_datetime_value("lastUsedDateTime", self.last_used_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

