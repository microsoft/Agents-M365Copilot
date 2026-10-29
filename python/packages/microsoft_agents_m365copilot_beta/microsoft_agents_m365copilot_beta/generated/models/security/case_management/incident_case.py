from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_counts import AlertCounts
    from .case import Case
    from .impacted_assets_counts import ImpactedAssetsCounts
    from .incident_classification import IncidentClassification
    from .incident_determination import IncidentDetermination
    from .incident_severity import IncidentSeverity
    from .investigation import Investigation

from .case import Case

@dataclass
class IncidentCase(Case, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.incidentCase"
    # The list of AI agent identifiers associated with the incident. Supports $filter.
    ai_agent_ids: Optional[list[str]] = None
    # A summary of alert counts grouped by severity and status. Supports $filter.
    alert_counts: Optional[AlertCounts] = None
    # The list of alert policy identifiers associated with the incident. Supports $filter.
    alert_policy_ids: Optional[list[str]] = None
    # The user assigned to investigate the incident case. Supports $filter and $orderby.
    assigned_to: Optional[str] = None
    # The list of threat identifiers associated with the incident. Supports $filter.
    associated_threat_ids: Optional[list[str]] = None
    # The incident categories. Supports $filter.
    categories: Optional[list[str]] = None
    # The classification property
    classification: Optional[IncidentClassification] = None
    # The cloud scopes associated with the incident. Supports $filter.
    cloud_scopes: Optional[list[str]] = None
    # The data sensitivity labels associated with the incident. Supports $filter.
    data_sensitivity_labels: Optional[list[str]] = None
    # The data streams associated with the incident. Supports $filter.
    data_streams: Optional[list[str]] = None
    # The detection sources that identified the incident. Supports $filter.
    detection_sources: Optional[list[str]] = None
    # The determination property
    determination: Optional[IncidentDetermination] = None
    # The target completion date and time for the incident case. Supports $filter.
    due_date_time: Optional[datetime.datetime] = None
    # The email notification recipients for the incident case. Supports $filter.
    email_notification_recipients: Optional[list[str]] = None
    # The date and time of the first event in the incident. Supports $filter.
    first_event_time: Optional[datetime.datetime] = None
    # A summary of impacted asset counts for the incident. Supports $filter.
    impacted_assets: Optional[ImpactedAssetsCounts] = None
    # The Microsoft Security incident identifier. Supports $filter.
    incident_id: Optional[int] = None
    # The URL for the incident in the Microsoft Defender portal. Supports $filter.
    incident_web_url: Optional[str] = None
    # A summary of investigation details associated with the incident. Supports $filter.
    investigation: Optional[Investigation] = None
    # The list of investigation identifiers associated with the incident. Supports $filter.
    investigation_ids: Optional[list[str]] = None
    # The list of investigation states associated with the incident. Supports $filter.
    investigation_states: Optional[list[str]] = None
    # The date and time of the most recent event in the incident. Supports $filter.
    last_event_time: Optional[datetime.datetime] = None
    # The list of machine group identifiers associated with the incident. Supports $filter.
    machine_group_ids: Optional[list[str]] = None
    # The operating system platforms associated with the incident. Supports $filter.
    os_platforms: Optional[list[str]] = None
    # The policy names associated with the incident. Supports $filter.
    policy_names: Optional[list[str]] = None
    # The priority score assigned to the incident. Supports $filter.
    priority_score: Optional[int] = None
    # The product names associated with the incident. Supports $filter.
    product_names: Optional[list[str]] = None
    # The redirectCaseId property
    redirect_case_id: Optional[int] = None
    # The redirectIncidentId property
    redirect_incident_id: Optional[int] = None
    # The service sources associated with the incident. Supports $filter.
    service_sources: Optional[list[str]] = None
    # The severity property
    severity: Optional[IncidentSeverity] = None
    # A summary of the incident. Supports $filter.
    summary: Optional[str] = None
    # The system tags associated with the incident. Supports $filter.
    system_tags: Optional[list[str]] = None
    # The top risk score associated with the incident. Supports $filter.
    top_risk_score: Optional[int] = None
    # The list of workspace identifiers associated with the incident. Supports $filter.
    workspace_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IncidentCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IncidentCase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IncidentCase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_counts import AlertCounts
        from .case import Case
        from .impacted_assets_counts import ImpactedAssetsCounts
        from .incident_classification import IncidentClassification
        from .incident_determination import IncidentDetermination
        from .incident_severity import IncidentSeverity
        from .investigation import Investigation

        from .alert_counts import AlertCounts
        from .case import Case
        from .impacted_assets_counts import ImpactedAssetsCounts
        from .incident_classification import IncidentClassification
        from .incident_determination import IncidentDetermination
        from .incident_severity import IncidentSeverity
        from .investigation import Investigation

        fields: dict[str, Callable[[Any], None]] = {
            "aiAgentIds": lambda n : setattr(self, 'ai_agent_ids', n.get_collection_of_primitive_values(str)),
            "alertCounts": lambda n : setattr(self, 'alert_counts', n.get_object_value(AlertCounts)),
            "alertPolicyIds": lambda n : setattr(self, 'alert_policy_ids', n.get_collection_of_primitive_values(str)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "associatedThreatIds": lambda n : setattr(self, 'associated_threat_ids', n.get_collection_of_primitive_values(str)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(IncidentClassification)),
            "cloudScopes": lambda n : setattr(self, 'cloud_scopes', n.get_collection_of_primitive_values(str)),
            "dataSensitivityLabels": lambda n : setattr(self, 'data_sensitivity_labels', n.get_collection_of_primitive_values(str)),
            "dataStreams": lambda n : setattr(self, 'data_streams', n.get_collection_of_primitive_values(str)),
            "detectionSources": lambda n : setattr(self, 'detection_sources', n.get_collection_of_primitive_values(str)),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(IncidentDetermination)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "emailNotificationRecipients": lambda n : setattr(self, 'email_notification_recipients', n.get_collection_of_primitive_values(str)),
            "firstEventTime": lambda n : setattr(self, 'first_event_time', n.get_datetime_value()),
            "impactedAssets": lambda n : setattr(self, 'impacted_assets', n.get_object_value(ImpactedAssetsCounts)),
            "incidentId": lambda n : setattr(self, 'incident_id', n.get_int_value()),
            "incidentWebUrl": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "investigation": lambda n : setattr(self, 'investigation', n.get_object_value(Investigation)),
            "investigationIds": lambda n : setattr(self, 'investigation_ids', n.get_collection_of_primitive_values(str)),
            "investigationStates": lambda n : setattr(self, 'investigation_states', n.get_collection_of_primitive_values(str)),
            "lastEventTime": lambda n : setattr(self, 'last_event_time', n.get_datetime_value()),
            "machineGroupIds": lambda n : setattr(self, 'machine_group_ids', n.get_collection_of_primitive_values(str)),
            "osPlatforms": lambda n : setattr(self, 'os_platforms', n.get_collection_of_primitive_values(str)),
            "policyNames": lambda n : setattr(self, 'policy_names', n.get_collection_of_primitive_values(str)),
            "priorityScore": lambda n : setattr(self, 'priority_score', n.get_int_value()),
            "productNames": lambda n : setattr(self, 'product_names', n.get_collection_of_primitive_values(str)),
            "redirectCaseId": lambda n : setattr(self, 'redirect_case_id', n.get_int_value()),
            "redirectIncidentId": lambda n : setattr(self, 'redirect_incident_id', n.get_int_value()),
            "serviceSources": lambda n : setattr(self, 'service_sources', n.get_collection_of_primitive_values(str)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(IncidentSeverity)),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "systemTags": lambda n : setattr(self, 'system_tags', n.get_collection_of_primitive_values(str)),
            "topRiskScore": lambda n : setattr(self, 'top_risk_score', n.get_int_value()),
            "workspaceIds": lambda n : setattr(self, 'workspace_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("aiAgentIds", self.ai_agent_ids)
        writer.write_object_value("alertCounts", self.alert_counts)
        writer.write_collection_of_primitive_values("alertPolicyIds", self.alert_policy_ids)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_collection_of_primitive_values("associatedThreatIds", self.associated_threat_ids)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_primitive_values("cloudScopes", self.cloud_scopes)
        writer.write_collection_of_primitive_values("dataSensitivityLabels", self.data_sensitivity_labels)
        writer.write_collection_of_primitive_values("dataStreams", self.data_streams)
        writer.write_collection_of_primitive_values("detectionSources", self.detection_sources)
        writer.write_enum_value("determination", self.determination)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_collection_of_primitive_values("emailNotificationRecipients", self.email_notification_recipients)
        writer.write_datetime_value("firstEventTime", self.first_event_time)
        writer.write_object_value("impactedAssets", self.impacted_assets)
        writer.write_int_value("incidentId", self.incident_id)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_object_value("investigation", self.investigation)
        writer.write_collection_of_primitive_values("investigationIds", self.investigation_ids)
        writer.write_collection_of_primitive_values("investigationStates", self.investigation_states)
        writer.write_datetime_value("lastEventTime", self.last_event_time)
        writer.write_collection_of_primitive_values("machineGroupIds", self.machine_group_ids)
        writer.write_collection_of_primitive_values("osPlatforms", self.os_platforms)
        writer.write_collection_of_primitive_values("policyNames", self.policy_names)
        writer.write_int_value("priorityScore", self.priority_score)
        writer.write_collection_of_primitive_values("productNames", self.product_names)
        writer.write_int_value("redirectCaseId", self.redirect_case_id)
        writer.write_int_value("redirectIncidentId", self.redirect_incident_id)
        writer.write_collection_of_primitive_values("serviceSources", self.service_sources)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("summary", self.summary)
        writer.write_collection_of_primitive_values("systemTags", self.system_tags)
        writer.write_int_value("topRiskScore", self.top_risk_score)
        writer.write_collection_of_primitive_values("workspaceIds", self.workspace_ids)
    

