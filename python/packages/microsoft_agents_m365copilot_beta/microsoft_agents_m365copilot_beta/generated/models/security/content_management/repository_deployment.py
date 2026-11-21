from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .repository_deployment_result import RepositoryDeploymentResult
    from .repository_deployment_state import RepositoryDeploymentState

@dataclass
class RepositoryDeployment(AdditionalDataHolder, Parsable):
    """
    Details of a fetched deployment run. Read-only.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # When the deployment ran.
    deployment_date_time: Optional[datetime.datetime] = None
    # Deployment id.
    deployment_id: Optional[str] = None
    # URL where the deployment logs can be viewed.
    deployment_logs_url: Optional[str] = None
    # Result of a completed deployment.
    deployment_result: Optional[RepositoryDeploymentResult] = None
    # State of a deployment run.
    deployment_state: Optional[RepositoryDeploymentState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RepositoryDeployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RepositoryDeployment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RepositoryDeployment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .repository_deployment_result import RepositoryDeploymentResult
        from .repository_deployment_state import RepositoryDeploymentState

        from .repository_deployment_result import RepositoryDeploymentResult
        from .repository_deployment_state import RepositoryDeploymentState

        fields: dict[str, Callable[[Any], None]] = {
            "deploymentDateTime": lambda n : setattr(self, 'deployment_date_time', n.get_datetime_value()),
            "deploymentId": lambda n : setattr(self, 'deployment_id', n.get_str_value()),
            "deploymentLogsUrl": lambda n : setattr(self, 'deployment_logs_url', n.get_str_value()),
            "deploymentResult": lambda n : setattr(self, 'deployment_result', n.get_enum_value(RepositoryDeploymentResult)),
            "deploymentState": lambda n : setattr(self, 'deployment_state', n.get_enum_value(RepositoryDeploymentState)),
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
        writer.write_enum_value("deploymentResult", self.deployment_result)
        writer.write_enum_value("deploymentState", self.deployment_state)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

