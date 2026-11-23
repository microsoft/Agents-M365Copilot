from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .repository_deployment import RepositoryDeployment
    from .repository_deployment_fetch_status import RepositoryDeploymentFetchStatus

@dataclass
class RepositoryDeploymentInfo(AdditionalDataHolder, Parsable):
    """
    Status fetch result and the most recent deployment, when available.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether deployment status could be fetched.
    deployment_fetch_status: Optional[RepositoryDeploymentFetchStatus] = None
    # Human-readable status or error message.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Deployment details; null when no run was fetched.
    run: Optional[RepositoryDeployment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RepositoryDeploymentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RepositoryDeploymentInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RepositoryDeploymentInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .repository_deployment import RepositoryDeployment
        from .repository_deployment_fetch_status import RepositoryDeploymentFetchStatus

        from .repository_deployment import RepositoryDeployment
        from .repository_deployment_fetch_status import RepositoryDeploymentFetchStatus

        fields: dict[str, Callable[[Any], None]] = {
            "deploymentFetchStatus": lambda n : setattr(self, 'deployment_fetch_status', n.get_enum_value(RepositoryDeploymentFetchStatus)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "run": lambda n : setattr(self, 'run', n.get_object_value(RepositoryDeployment)),
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
        writer.write_enum_value("deploymentFetchStatus", self.deployment_fetch_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

