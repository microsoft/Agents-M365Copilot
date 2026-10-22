from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .management_template_step import ManagementTemplateStep
    from .management_template_step_deployment import ManagementTemplateStepDeployment

from ..entity import Entity

@dataclass
class ManagementTemplateStepVersion(Entity, Parsable):
    # The acceptedFor property
    accepted_for: Optional[ManagementTemplateStep] = None
    # The contentMarkdown property
    content_markdown: Optional[str] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The deployments property
    deployments: Optional[list[ManagementTemplateStepDeployment]] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The templateStep property
    template_step: Optional[ManagementTemplateStep] = None
    # The version property
    version: Optional[int] = None
    # The versionInformation property
    version_information: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementTemplateStepVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStepVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateStepVersion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .management_template_step import ManagementTemplateStep
        from .management_template_step_deployment import ManagementTemplateStepDeployment

        from ..entity import Entity
        from .management_template_step import ManagementTemplateStep
        from .management_template_step_deployment import ManagementTemplateStepDeployment

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedFor": lambda n : setattr(self, 'accepted_for', n.get_object_value(ManagementTemplateStep)),
            "contentMarkdown": lambda n : setattr(self, 'content_markdown', n.get_str_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(ManagementTemplateStepDeployment)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "templateStep": lambda n : setattr(self, 'template_step', n.get_object_value(ManagementTemplateStep)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versionInformation": lambda n : setattr(self, 'version_information', n.get_str_value()),
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
        writer.write_object_value("acceptedFor", self.accepted_for)
        writer.write_str_value("contentMarkdown", self.content_markdown)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("deployments", self.deployments)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("templateStep", self.template_step)
        writer.write_int_value("version", self.version)
        writer.write_str_value("versionInformation", self.version_information)
    

