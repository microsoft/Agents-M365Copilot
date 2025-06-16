from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, Union

from kiota_abstractions.serialization import (
    AdditionalDataHolder,
    Parsable,
    ParseNode,
    SerializationWriter,
)
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton


@dataclass
class SearchSensitivityLabelInfo(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a sensitivityLabel.This model is shared with the CCS retrieval API and search where it is already unhidden.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The color property
    color: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The isEncrypted property
    is_encrypted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # The sensitivityLabelId property
    sensitivity_label_id: Optional[str] = None
    # The tooltip property
    tooltip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchSensitivityLabelInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchSensitivityLabelInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchSensitivityLabelInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sensitivityLabelId": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
            "tooltip": lambda n : setattr(self, 'tooltip', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

