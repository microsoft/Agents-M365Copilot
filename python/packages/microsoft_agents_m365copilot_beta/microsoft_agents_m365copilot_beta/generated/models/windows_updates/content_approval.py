from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_change import ComplianceChange
    from .deployable_content import DeployableContent
    from .deployment import Deployment
    from .deployment_settings import DeploymentSettings

from .compliance_change import ComplianceChange

@dataclass
class ContentApproval(ComplianceChange, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.contentApproval"
    # The content property
    content: Optional[DeployableContent] = None
    # Settings for governing how to deploy content.
    deployment_settings: Optional[DeploymentSettings] = None
    # Deployments created as a result of applying the approval.
    deployments: Optional[list[Deployment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentApproval
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentApproval()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_change import ComplianceChange
        from .deployable_content import DeployableContent
        from .deployment import Deployment
        from .deployment_settings import DeploymentSettings

        from .compliance_change import ComplianceChange
        from .deployable_content import DeployableContent
        from .deployment import Deployment
        from .deployment_settings import DeploymentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(DeployableContent)),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(DeploymentSettings)),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(Deployment)),
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
        writer.write_object_value("content", self.content)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
        writer.write_collection_of_object_values("deployments", self.deployments)
    

