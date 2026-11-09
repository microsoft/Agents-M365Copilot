from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connectivity_configuration_link import ConnectivityConfigurationLink

@dataclass
class BranchConnectivityConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier or a specific reference assigned to a branchSite. Key.
    branch_id: Optional[str] = None
    # Display name assigned to a branchSite.
    branch_name: Optional[str] = None
    # List of connectivity configurations for deviceLink objects.
    links: Optional[list[ConnectivityConfigurationLink]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BranchConnectivityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BranchConnectivityConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BranchConnectivityConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connectivity_configuration_link import ConnectivityConfigurationLink

        from .connectivity_configuration_link import ConnectivityConfigurationLink

        fields: dict[str, Callable[[Any], None]] = {
            "branchId": lambda n : setattr(self, 'branch_id', n.get_str_value()),
            "branchName": lambda n : setattr(self, 'branch_name', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(ConnectivityConfigurationLink)),
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
        writer.write_str_value("branchId", self.branch_id)
        writer.write_str_value("branchName", self.branch_name)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

