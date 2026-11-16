from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item_category import ItemCategory
    from .picture import Picture

@dataclass
class Item(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The baseUnitOfMeasureId property
    base_unit_of_measure_id: Optional[UUID] = None
    # The blocked property
    blocked: Optional[bool] = None
    # The displayName property
    display_name: Optional[str] = None
    # The gtin property
    gtin: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The inventory property
    inventory: Optional[float] = None
    # The itemCategory property
    item_category: Optional[ItemCategory] = None
    # The itemCategoryCode property
    item_category_code: Optional[str] = None
    # The itemCategoryId property
    item_category_id: Optional[UUID] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The number property
    number: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The picture property
    picture: Optional[list[Picture]] = None
    # The priceIncludesTax property
    price_includes_tax: Optional[bool] = None
    # The taxGroupCode property
    tax_group_code: Optional[str] = None
    # The taxGroupId property
    tax_group_id: Optional[UUID] = None
    # The type property
    type: Optional[str] = None
    # The unitCost property
    unit_cost: Optional[float] = None
    # The unitPrice property
    unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Item:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Item
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Item()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_category import ItemCategory
        from .picture import Picture

        from .item_category import ItemCategory
        from .picture import Picture

        fields: dict[str, Callable[[Any], None]] = {
            "baseUnitOfMeasureId": lambda n : setattr(self, 'base_unit_of_measure_id', n.get_uuid_value()),
            "blocked": lambda n : setattr(self, 'blocked', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "gtin": lambda n : setattr(self, 'gtin', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "inventory": lambda n : setattr(self, 'inventory', n.get_float_value()),
            "itemCategory": lambda n : setattr(self, 'item_category', n.get_object_value(ItemCategory)),
            "itemCategoryCode": lambda n : setattr(self, 'item_category_code', n.get_str_value()),
            "itemCategoryId": lambda n : setattr(self, 'item_category_id', n.get_uuid_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "picture": lambda n : setattr(self, 'picture', n.get_collection_of_object_values(Picture)),
            "priceIncludesTax": lambda n : setattr(self, 'price_includes_tax', n.get_bool_value()),
            "taxGroupCode": lambda n : setattr(self, 'tax_group_code', n.get_str_value()),
            "taxGroupId": lambda n : setattr(self, 'tax_group_id', n.get_uuid_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "unitCost": lambda n : setattr(self, 'unit_cost', n.get_float_value()),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
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
        writer.write_uuid_value("baseUnitOfMeasureId", self.base_unit_of_measure_id)
        writer.write_bool_value("blocked", self.blocked)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("gtin", self.gtin)
        writer.write_uuid_value("id", self.id)
        writer.write_float_value("inventory", self.inventory)
        writer.write_object_value("itemCategory", self.item_category)
        writer.write_str_value("itemCategoryCode", self.item_category_code)
        writer.write_uuid_value("itemCategoryId", self.item_category_id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("number", self.number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("picture", self.picture)
        writer.write_bool_value("priceIncludesTax", self.price_includes_tax)
        writer.write_str_value("taxGroupCode", self.tax_group_code)
        writer.write_uuid_value("taxGroupId", self.tax_group_id)
        writer.write_str_value("type", self.type)
        writer.write_float_value("unitCost", self.unit_cost)
        writer.write_float_value("unitPrice", self.unit_price)
        writer.write_additional_data_value(self.additional_data)
    

