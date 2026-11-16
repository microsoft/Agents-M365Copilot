from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .graph_a_p_i_error_details import GraphAPIErrorDetails
    from .management_template_deployment_status import ManagementTemplateDeploymentStatus
    from .management_template_step_version import ManagementTemplateStepVersion

from ..entity import Entity

@dataclass
class ManagementTemplateStepDeployment(Entity, Parsable):
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The error property
    error: Optional[GraphAPIErrorDetails] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ManagementTemplateDeploymentStatus] = None
    # The templateStepVersion property
    template_step_version: Optional[ManagementTemplateStepVersion] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementTemplateStepDeployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStepDeployment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateStepDeployment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .graph_a_p_i_error_details import GraphAPIErrorDetails
        from .management_template_deployment_status import ManagementTemplateDeploymentStatus
        from .management_template_step_version import ManagementTemplateStepVersion

        from ..entity import Entity
        from .graph_a_p_i_error_details import GraphAPIErrorDetails
        from .management_template_deployment_status import ManagementTemplateDeploymentStatus
        from .management_template_step_version import ManagementTemplateStepVersion

        fields: dict[str, Callable[[Any], None]] = {
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(GraphAPIErrorDetails)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ManagementTemplateDeploymentStatus)),
            "templateStepVersion": lambda n : setattr(self, 'template_step_version', n.get_object_value(ManagementTemplateStepVersion)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("templateStepVersion", self.template_step_version)
        writer.write_str_value("tenantId", self.tenant_id)
    

