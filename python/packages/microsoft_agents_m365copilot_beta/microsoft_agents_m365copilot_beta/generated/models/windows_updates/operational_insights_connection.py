from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .resource_connection import ResourceConnection

from .resource_connection import ResourceConnection

@dataclass
class OperationalInsightsConnection(ResourceConnection, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.operationalInsightsConnection"
    # The name of the Azure resource group that contains the Log Analytics workspace.
    azure_resource_group_name: Optional[str] = None
    # The Azure subscription ID that contains the Log Analytics workspace.
    azure_subscription_id: Optional[str] = None
    # The name of the Log Analytics workspace.
    workspace_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationalInsightsConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationalInsightsConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationalInsightsConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .resource_connection import ResourceConnection

        from .resource_connection import ResourceConnection

        fields: dict[str, Callable[[Any], None]] = {
            "azureResourceGroupName": lambda n : setattr(self, 'azure_resource_group_name', n.get_str_value()),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "workspaceName": lambda n : setattr(self, 'workspace_name', n.get_str_value()),
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
        writer.write_str_value("azureResourceGroupName", self.azure_resource_group_name)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("workspaceName", self.workspace_name)
    

