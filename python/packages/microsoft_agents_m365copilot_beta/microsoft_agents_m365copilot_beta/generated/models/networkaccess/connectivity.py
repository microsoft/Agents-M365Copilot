from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .branch_site import BranchSite
    from .remote_network import RemoteNetwork
    from .web_category import WebCategory

from ..entity import Entity

@dataclass
class Connectivity(Entity, Parsable):
    # The locations for connectivity. DEPRECATED AND TO BE RETIRED SOON. Use the remoteNetwork relationship and its associated APIs instead.
    branches: Optional[list[BranchSite]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The locations, such as branches, that are connected to Global Secure Access services through an IPsec tunnel.
    remote_networks: Optional[list[RemoteNetwork]] = None
    # The URL category.
    web_categories: Optional[list[WebCategory]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Connectivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Connectivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Connectivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .branch_site import BranchSite
        from .remote_network import RemoteNetwork
        from .web_category import WebCategory

        from ..entity import Entity
        from .branch_site import BranchSite
        from .remote_network import RemoteNetwork
        from .web_category import WebCategory

        fields: dict[str, Callable[[Any], None]] = {
            "branches": lambda n : setattr(self, 'branches', n.get_collection_of_object_values(BranchSite)),
            "remoteNetworks": lambda n : setattr(self, 'remote_networks', n.get_collection_of_object_values(RemoteNetwork)),
            "webCategories": lambda n : setattr(self, 'web_categories', n.get_collection_of_object_values(WebCategory)),
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
        writer.write_collection_of_object_values("branches", self.branches)
        writer.write_collection_of_object_values("remoteNetworks", self.remote_networks)
        writer.write_collection_of_object_values("webCategories", self.web_categories)
    

