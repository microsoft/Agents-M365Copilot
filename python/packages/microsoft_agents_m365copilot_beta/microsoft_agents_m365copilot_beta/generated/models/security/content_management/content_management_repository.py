from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .deployment_identity import DeploymentIdentity
    from .deployment_scope import DeploymentScope
    from .repository_content_type import RepositoryContentType
    from .repository_deployment_info import RepositoryDeploymentInfo
    from .repository_pull_request import RepositoryPullRequest
    from .repository_service_principal import RepositoryServicePrincipal
    from .repository_settings import RepositorySettings
    from .repository_type import RepositoryType
    from .repository_workload_identity_federation import RepositoryWorkloadIdentityFederation
    from .system_data import SystemData

from ...entity import Entity

@dataclass
class ContentManagementRepository(Entity, Parsable):
    """
    A connected source-control repository that delivers security content as code(the customer-facing shape of the internal Source Control resource). Tenant is resolvedfrom the caller token; there is no subscription, resource group, or workspace in the path.
    """
    # Content kinds this repository is configured to deploy. The possible values are: customDetection, unknownFutureValue, defenderWorkbook. Use the Prefer: include-unknown-enum-members request header to get defenderWorkbook.
    content_types: Optional[list[RepositoryContentType]] = None
    # Bring-your-own deployment identity used for deployment. Optional; when omitted the platform-managed identity path is used. Provide a service principal or a managed identity. Immutable after connecting.
    deployment_identity: Optional[DeploymentIdentity] = None
    # Optional Azure deployment scope, immutable after connecting the repository.
    deployment_scope: Optional[DeploymentScope] = None
    # Optional description of the connection.
    description: Optional[str] = None
    # Human-readable name of the connection. Supports $filter (eq, ne) and $orderby.
    display_name: Optional[str] = None
    # Status of the most recent deployment from this repository. Read-only.
    last_deployment_info: Optional[RepositoryDeploymentInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The setup pull request opened for this connection, when applicable. Read-only.
    pull_request: Optional[RepositoryPullRequest] = None
    # Source-control provider.
    repo_type: Optional[RepositoryType] = None
    # Service principal / managed identity used by the connection. Read-only.
    service_principal: Optional[RepositoryServicePrincipal] = None
    # Repository location settings.
    source_location: Optional[RepositorySettings] = None
    # Creation and last modification provenance. Read-only.
    system_data: Optional[SystemData] = None
    # Workload identity federation details for the connection, when configured. Read-only.
    workload_identity_federation: Optional[RepositoryWorkloadIdentityFederation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentManagementRepository:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentManagementRepository
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentManagementRepository()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .deployment_identity import DeploymentIdentity
        from .deployment_scope import DeploymentScope
        from .repository_content_type import RepositoryContentType
        from .repository_deployment_info import RepositoryDeploymentInfo
        from .repository_pull_request import RepositoryPullRequest
        from .repository_service_principal import RepositoryServicePrincipal
        from .repository_settings import RepositorySettings
        from .repository_type import RepositoryType
        from .repository_workload_identity_federation import RepositoryWorkloadIdentityFederation
        from .system_data import SystemData

        from ...entity import Entity
        from .deployment_identity import DeploymentIdentity
        from .deployment_scope import DeploymentScope
        from .repository_content_type import RepositoryContentType
        from .repository_deployment_info import RepositoryDeploymentInfo
        from .repository_pull_request import RepositoryPullRequest
        from .repository_service_principal import RepositoryServicePrincipal
        from .repository_settings import RepositorySettings
        from .repository_type import RepositoryType
        from .repository_workload_identity_federation import RepositoryWorkloadIdentityFederation
        from .system_data import SystemData

        fields: dict[str, Callable[[Any], None]] = {
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_enum_values(RepositoryContentType)),
            "deploymentIdentity": lambda n : setattr(self, 'deployment_identity', n.get_object_value(DeploymentIdentity)),
            "deploymentScope": lambda n : setattr(self, 'deployment_scope', n.get_object_value(DeploymentScope)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastDeploymentInfo": lambda n : setattr(self, 'last_deployment_info', n.get_object_value(RepositoryDeploymentInfo)),
            "pullRequest": lambda n : setattr(self, 'pull_request', n.get_object_value(RepositoryPullRequest)),
            "repoType": lambda n : setattr(self, 'repo_type', n.get_enum_value(RepositoryType)),
            "servicePrincipal": lambda n : setattr(self, 'service_principal', n.get_object_value(RepositoryServicePrincipal)),
            "sourceLocation": lambda n : setattr(self, 'source_location', n.get_object_value(RepositorySettings)),
            "systemData": lambda n : setattr(self, 'system_data', n.get_object_value(SystemData)),
            "workloadIdentityFederation": lambda n : setattr(self, 'workload_identity_federation', n.get_object_value(RepositoryWorkloadIdentityFederation)),
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
        writer.write_collection_of_enum_values("contentTypes", self.content_types)
        writer.write_object_value("deploymentIdentity", self.deployment_identity)
        writer.write_object_value("deploymentScope", self.deployment_scope)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("repoType", self.repo_type)
        writer.write_object_value("sourceLocation", self.source_location)
    

