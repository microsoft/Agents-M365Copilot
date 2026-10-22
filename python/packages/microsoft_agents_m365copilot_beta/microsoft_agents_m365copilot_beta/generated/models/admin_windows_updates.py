from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_updates.catalog import Catalog
    from .windows_updates.deployment import Deployment
    from .windows_updates.deployment_audience import DeploymentAudience
    from .windows_updates.policy import Policy
    from .windows_updates.product import Product
    from .windows_updates.resource_connection import ResourceConnection
    from .windows_updates.updatable_asset import UpdatableAsset
    from .windows_updates.update_policy import UpdatePolicy

from .entity import Entity

@dataclass
class AdminWindowsUpdates(Entity, Parsable):
    # Catalog of content that can be approved for deployment by Windows Autopatch. Read-only.
    catalog: Optional[Catalog] = None
    # The set of updatableAsset resources to which a deployment can apply.
    deployment_audiences: Optional[list[DeploymentAudience]] = None
    # Deployments created using Windows Autopatch.
    deployments: Optional[list[Deployment]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of policies for approving the deployment of different content to an audience over time.
    policies: Optional[list[Policy]] = None
    # A collection of Windows products.
    products: Optional[list[Product]] = None
    # Service connections to external resources such as analytics workspaces.
    resource_connections: Optional[list[ResourceConnection]] = None
    # Assets registered with Windows Autopatch that can receive updates.
    updatable_assets: Optional[list[UpdatableAsset]] = None
    # A collection of policies for approving the deployment of different content to an audience over time.
    update_policies: Optional[list[UpdatePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminWindowsUpdates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminWindowsUpdates
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminWindowsUpdates()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_updates.catalog import Catalog
        from .windows_updates.deployment import Deployment
        from .windows_updates.deployment_audience import DeploymentAudience
        from .windows_updates.policy import Policy
        from .windows_updates.product import Product
        from .windows_updates.resource_connection import ResourceConnection
        from .windows_updates.updatable_asset import UpdatableAsset
        from .windows_updates.update_policy import UpdatePolicy

        from .entity import Entity
        from .windows_updates.catalog import Catalog
        from .windows_updates.deployment import Deployment
        from .windows_updates.deployment_audience import DeploymentAudience
        from .windows_updates.policy import Policy
        from .windows_updates.product import Product
        from .windows_updates.resource_connection import ResourceConnection
        from .windows_updates.updatable_asset import UpdatableAsset
        from .windows_updates.update_policy import UpdatePolicy

        fields: dict[str, Callable[[Any], None]] = {
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(Catalog)),
            "deploymentAudiences": lambda n : setattr(self, 'deployment_audiences', n.get_collection_of_object_values(DeploymentAudience)),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(Deployment)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(Policy)),
            "products": lambda n : setattr(self, 'products', n.get_collection_of_object_values(Product)),
            "resourceConnections": lambda n : setattr(self, 'resource_connections', n.get_collection_of_object_values(ResourceConnection)),
            "updatableAssets": lambda n : setattr(self, 'updatable_assets', n.get_collection_of_object_values(UpdatableAsset)),
            "updatePolicies": lambda n : setattr(self, 'update_policies', n.get_collection_of_object_values(UpdatePolicy)),
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
        writer.write_object_value("catalog", self.catalog)
        writer.write_collection_of_object_values("deploymentAudiences", self.deployment_audiences)
        writer.write_collection_of_object_values("deployments", self.deployments)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_collection_of_object_values("products", self.products)
        writer.write_collection_of_object_values("resourceConnections", self.resource_connections)
        writer.write_collection_of_object_values("updatableAssets", self.updatable_assets)
        writer.write_collection_of_object_values("updatePolicies", self.update_policies)
    

