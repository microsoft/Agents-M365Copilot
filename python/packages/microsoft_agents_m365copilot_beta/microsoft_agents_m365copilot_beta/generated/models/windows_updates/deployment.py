from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .deployable_content import DeployableContent
    from .deployment_audience import DeploymentAudience
    from .deployment_settings import DeploymentSettings
    from .deployment_state import DeploymentState

from ..entity import Entity

@dataclass
class Deployment(Entity, Parsable):
    # Specifies the audience to which content is deployed.
    audience: Optional[DeploymentAudience] = None
    # Specifies what content to deploy. Cannot be changed. Returned by default.
    content: Optional[DeployableContent] = None
    # The date and time the deployment was created. Returned by default. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time the deployment was last modified. Returned by default. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Settings specified on the specific deployment governing how to deploy content. Returned by default.
    settings: Optional[DeploymentSettings] = None
    # Execution status of the deployment. Returned by default.
    state: Optional[DeploymentState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Deployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Deployment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Deployment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .deployable_content import DeployableContent
        from .deployment_audience import DeploymentAudience
        from .deployment_settings import DeploymentSettings
        from .deployment_state import DeploymentState

        from ..entity import Entity
        from .deployable_content import DeployableContent
        from .deployment_audience import DeploymentAudience
        from .deployment_settings import DeploymentSettings
        from .deployment_state import DeploymentState

        fields: dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_object_value(DeploymentAudience)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(DeployableContent)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(DeploymentSettings)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(DeploymentState)),
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
        writer.write_object_value("audience", self.audience)
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("state", self.state)
    

