from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_person import BookingPerson
    from .phone import Phone
    from .physical_address import PhysicalAddress

from .booking_person import BookingPerson

@dataclass
class BookingCustomer(BookingPerson, Parsable):
    """
    Represents a customer of the business.
    """
    # Addresses associated with the customer, including home, business and other addresses.
    addresses: Optional[list[PhysicalAddress]] = None
    # The date, time, and timezone when the customer was created.
    created_date_time: Optional[datetime.datetime] = None
    # The date, time, and timezone when the customer was last updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Phone numbers associated with the customer, including home, business and mobile numbers.
    phones: Optional[list[Phone]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingCustomer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingCustomer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_person import BookingPerson
        from .phone import Phone
        from .physical_address import PhysicalAddress

        from .booking_person import BookingPerson
        from .phone import Phone
        from .physical_address import PhysicalAddress

        fields: dict[str, Callable[[Any], None]] = {
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(PhysicalAddress)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
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
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_object_values("phones", self.phones)
    

