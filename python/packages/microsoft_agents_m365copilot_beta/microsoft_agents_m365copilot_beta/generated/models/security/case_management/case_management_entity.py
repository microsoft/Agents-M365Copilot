from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .activity import Activity
    from .attachment import Attachment
    from .audit_log import AuditLog
    from .case import Case
    from .comment import Comment
    from .exposure_case import ExposureCase
    from .generic_case import GenericCase
    from .incident_case import IncidentCase
    from .incident_relation import IncidentRelation
    from .recommendation_relation import RecommendationRelation
    from .relation import Relation
    from .task import Task
    from .workspace_indicator_relation import WorkspaceIndicatorRelation

from ...entity import Entity

@dataclass
class CaseManagementEntity(Entity, Parsable):
    # The user or service that created the resource.
    created_by: Optional[str] = None
    # The date and time when the resource was created.
    created_date_time: Optional[datetime.datetime] = None
    # The user or service that last modified the resource.
    last_modified_by: Optional[str] = None
    # The date and time when the resource was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CaseManagementEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaseManagementEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.activity".casefold():
            from .activity import Activity

            return Activity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.attachment".casefold():
            from .attachment import Attachment

            return Attachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.auditLog".casefold():
            from .audit_log import AuditLog

            return AuditLog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.case".casefold():
            from .case import Case

            return Case()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.comment".casefold():
            from .comment import Comment

            return Comment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.exposureCase".casefold():
            from .exposure_case import ExposureCase

            return ExposureCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.genericCase".casefold():
            from .generic_case import GenericCase

            return GenericCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.incidentCase".casefold():
            from .incident_case import IncidentCase

            return IncidentCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.incidentRelation".casefold():
            from .incident_relation import IncidentRelation

            return IncidentRelation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.recommendationRelation".casefold():
            from .recommendation_relation import RecommendationRelation

            return RecommendationRelation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.relation".casefold():
            from .relation import Relation

            return Relation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.task".casefold():
            from .task import Task

            return Task()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.workspaceIndicatorRelation".casefold():
            from .workspace_indicator_relation import WorkspaceIndicatorRelation

            return WorkspaceIndicatorRelation()
        return CaseManagementEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .activity import Activity
        from .attachment import Attachment
        from .audit_log import AuditLog
        from .case import Case
        from .comment import Comment
        from .exposure_case import ExposureCase
        from .generic_case import GenericCase
        from .incident_case import IncidentCase
        from .incident_relation import IncidentRelation
        from .recommendation_relation import RecommendationRelation
        from .relation import Relation
        from .task import Task
        from .workspace_indicator_relation import WorkspaceIndicatorRelation

        from ...entity import Entity
        from .activity import Activity
        from .attachment import Attachment
        from .audit_log import AuditLog
        from .case import Case
        from .comment import Comment
        from .exposure_case import ExposureCase
        from .generic_case import GenericCase
        from .incident_case import IncidentCase
        from .incident_relation import IncidentRelation
        from .recommendation_relation import RecommendationRelation
        from .relation import Relation
        from .task import Task
        from .workspace_indicator_relation import WorkspaceIndicatorRelation

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

