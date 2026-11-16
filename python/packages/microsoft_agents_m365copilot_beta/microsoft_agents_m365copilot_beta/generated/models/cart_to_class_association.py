from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CartToClassAssociation(Entity, Parsable):
    """
    CartToClassAssociation for associating device carts with classrooms.
    """
    # Identifiers of classrooms to be associated with device carts.
    classroom_ids: Optional[list[str]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Admin provided description of the CartToClassAssociation.
    description: Optional[str] = None
    # Identifiers of device carts to be associated with classes.
    device_cart_ids: Optional[list[str]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Version of the CartToClassAssociation.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CartToClassAssociation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CartToClassAssociation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CartToClassAssociation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "classroomIds": lambda n : setattr(self, 'classroom_ids', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceCartIds": lambda n : setattr(self, 'device_cart_ids', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("classroomIds", self.classroom_ids)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("deviceCartIds", self.device_cart_ids)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("version", self.version)
    

