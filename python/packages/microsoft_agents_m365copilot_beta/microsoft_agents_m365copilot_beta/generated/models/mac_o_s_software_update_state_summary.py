from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
    from .mac_o_s_software_update_state import MacOSSoftwareUpdateState

from .entity import Entity

@dataclass
class MacOSSoftwareUpdateStateSummary(Entity, Parsable):
    """
    MacOS software update state summary for a device and user
    """
    # Human readable name of the software update
    display_name: Optional[str] = None
    # Last date time the report for this device and product key was updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Product key of the software update.
    product_key: Optional[str] = None
    # MacOS Software Update State
    state: Optional[MacOSSoftwareUpdateState] = None
    # MacOS Software Update Category
    update_category: Optional[MacOSSoftwareUpdateCategory] = None
    # Version of the software update
    update_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSSoftwareUpdateStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSoftwareUpdateStateSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSSoftwareUpdateStateSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
        from .mac_o_s_software_update_state import MacOSSoftwareUpdateState

        from .entity import Entity
        from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
        from .mac_o_s_software_update_state import MacOSSoftwareUpdateState

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MacOSSoftwareUpdateState)),
            "updateCategory": lambda n : setattr(self, 'update_category', n.get_enum_value(MacOSSoftwareUpdateCategory)),
            "updateVersion": lambda n : setattr(self, 'update_version', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("productKey", self.product_key)
        writer.write_enum_value("state", self.state)
        writer.write_enum_value("updateCategory", self.update_category)
        writer.write_str_value("updateVersion", self.update_version)
    

