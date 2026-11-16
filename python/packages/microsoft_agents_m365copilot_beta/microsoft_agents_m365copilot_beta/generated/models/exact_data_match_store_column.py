from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExactDataMatchStoreColumn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ignoredDelimiters property
    ignored_delimiters: Optional[list[str]] = None
    # The isCaseInsensitive property
    is_case_insensitive: Optional[bool] = None
    # The isSearchable property
    is_searchable: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExactDataMatchStoreColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExactDataMatchStoreColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExactDataMatchStoreColumn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "ignoredDelimiters": lambda n : setattr(self, 'ignored_delimiters', n.get_collection_of_primitive_values(str)),
            "isCaseInsensitive": lambda n : setattr(self, 'is_case_insensitive', n.get_bool_value()),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("ignoredDelimiters", self.ignored_delimiters)
        writer.write_bool_value("isCaseInsensitive", self.is_case_insensitive)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

