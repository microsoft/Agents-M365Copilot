from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edge_home_button_hidden import EdgeHomeButtonHidden
    from .edge_home_button_loads_start_page import EdgeHomeButtonLoadsStartPage
    from .edge_home_button_opens_custom_u_r_l import EdgeHomeButtonOpensCustomURL
    from .edge_home_button_opens_new_tab import EdgeHomeButtonOpensNewTab

@dataclass
class EdgeHomeButtonConfiguration(AdditionalDataHolder, Parsable):
    """
    The home button configuration base class used to identify the available options
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdgeHomeButtonConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeHomeButtonConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonHidden".casefold():
            from .edge_home_button_hidden import EdgeHomeButtonHidden

            return EdgeHomeButtonHidden()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonLoadsStartPage".casefold():
            from .edge_home_button_loads_start_page import EdgeHomeButtonLoadsStartPage

            return EdgeHomeButtonLoadsStartPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonOpensCustomURL".casefold():
            from .edge_home_button_opens_custom_u_r_l import EdgeHomeButtonOpensCustomURL

            return EdgeHomeButtonOpensCustomURL()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edgeHomeButtonOpensNewTab".casefold():
            from .edge_home_button_opens_new_tab import EdgeHomeButtonOpensNewTab

            return EdgeHomeButtonOpensNewTab()
        return EdgeHomeButtonConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .edge_home_button_hidden import EdgeHomeButtonHidden
        from .edge_home_button_loads_start_page import EdgeHomeButtonLoadsStartPage
        from .edge_home_button_opens_custom_u_r_l import EdgeHomeButtonOpensCustomURL
        from .edge_home_button_opens_new_tab import EdgeHomeButtonOpensNewTab

        from .edge_home_button_hidden import EdgeHomeButtonHidden
        from .edge_home_button_loads_start_page import EdgeHomeButtonLoadsStartPage
        from .edge_home_button_opens_custom_u_r_l import EdgeHomeButtonOpensCustomURL
        from .edge_home_button_opens_new_tab import EdgeHomeButtonOpensNewTab

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

