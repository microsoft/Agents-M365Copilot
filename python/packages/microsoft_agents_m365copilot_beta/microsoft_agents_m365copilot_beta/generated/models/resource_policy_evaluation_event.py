from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .policy_evaluation_detail import PolicyEvaluationDetail
    from .resource_policy_decision import ResourcePolicyDecision

from .entity import Entity

@dataclass
class ResourcePolicyEvaluationEvent(Entity, Parsable):
    # The apiVersion property
    api_version: Optional[str] = None
    # The appDisplayName property
    app_display_name: Optional[str] = None
    # The appId property
    app_id: Optional[str] = None
    # The applicablePoliciesCount property
    applicable_policies_count: Optional[int] = None
    # The auditPoliciesCount property
    audit_policies_count: Optional[int] = None
    # The clientRequestId property
    client_request_id: Optional[str] = None
    # The denyPoliciesCount property
    deny_policies_count: Optional[int] = None
    # The durationMs property
    duration_ms: Optional[int] = None
    # The errorPoliciesCount property
    error_policies_count: Optional[int] = None
    # The evaluatedDateTime property
    evaluated_date_time: Optional[datetime.datetime] = None
    # The evaluatedPoliciesCount property
    evaluated_policies_count: Optional[int] = None
    # The location property
    location: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationId property
    operation_id: Optional[str] = None
    # The policyDecision property
    policy_decision: Optional[ResourcePolicyDecision] = None
    # The policyDetails property
    policy_details: Optional[list[PolicyEvaluationDetail]] = None
    # The requestId property
    request_id: Optional[str] = None
    # The requestMethod property
    request_method: Optional[str] = None
    # The requestUri property
    request_uri: Optional[str] = None
    # The servicePrincipalId property
    service_principal_id: Optional[str] = None
    # The targetResourceId property
    target_resource_id: Optional[str] = None
    # The targetResourceName property
    target_resource_name: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The totalFetchDurationMs property
    total_fetch_duration_ms: Optional[int] = None
    # The totalPolicyEvaluationDurationMs property
    total_policy_evaluation_duration_ms: Optional[int] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourcePolicyEvaluationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourcePolicyEvaluationEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourcePolicyEvaluationEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .policy_evaluation_detail import PolicyEvaluationDetail
        from .resource_policy_decision import ResourcePolicyDecision

        from .entity import Entity
        from .policy_evaluation_detail import PolicyEvaluationDetail
        from .resource_policy_decision import ResourcePolicyDecision

        fields: dict[str, Callable[[Any], None]] = {
            "apiVersion": lambda n : setattr(self, 'api_version', n.get_str_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "applicablePoliciesCount": lambda n : setattr(self, 'applicable_policies_count', n.get_int_value()),
            "auditPoliciesCount": lambda n : setattr(self, 'audit_policies_count', n.get_int_value()),
            "clientRequestId": lambda n : setattr(self, 'client_request_id', n.get_str_value()),
            "denyPoliciesCount": lambda n : setattr(self, 'deny_policies_count', n.get_int_value()),
            "durationMs": lambda n : setattr(self, 'duration_ms', n.get_int_value()),
            "errorPoliciesCount": lambda n : setattr(self, 'error_policies_count', n.get_int_value()),
            "evaluatedDateTime": lambda n : setattr(self, 'evaluated_date_time', n.get_datetime_value()),
            "evaluatedPoliciesCount": lambda n : setattr(self, 'evaluated_policies_count', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "operationId": lambda n : setattr(self, 'operation_id', n.get_str_value()),
            "policyDecision": lambda n : setattr(self, 'policy_decision', n.get_enum_value(ResourcePolicyDecision)),
            "policyDetails": lambda n : setattr(self, 'policy_details', n.get_collection_of_object_values(PolicyEvaluationDetail)),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "requestMethod": lambda n : setattr(self, 'request_method', n.get_str_value()),
            "requestUri": lambda n : setattr(self, 'request_uri', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "targetResourceId": lambda n : setattr(self, 'target_resource_id', n.get_str_value()),
            "targetResourceName": lambda n : setattr(self, 'target_resource_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "totalFetchDurationMs": lambda n : setattr(self, 'total_fetch_duration_ms', n.get_int_value()),
            "totalPolicyEvaluationDurationMs": lambda n : setattr(self, 'total_policy_evaluation_duration_ms', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("apiVersion", self.api_version)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_int_value("applicablePoliciesCount", self.applicable_policies_count)
        writer.write_int_value("auditPoliciesCount", self.audit_policies_count)
        writer.write_str_value("clientRequestId", self.client_request_id)
        writer.write_int_value("denyPoliciesCount", self.deny_policies_count)
        writer.write_int_value("durationMs", self.duration_ms)
        writer.write_int_value("errorPoliciesCount", self.error_policies_count)
        writer.write_datetime_value("evaluatedDateTime", self.evaluated_date_time)
        writer.write_int_value("evaluatedPoliciesCount", self.evaluated_policies_count)
        writer.write_str_value("location", self.location)
        writer.write_str_value("operationId", self.operation_id)
        writer.write_enum_value("policyDecision", self.policy_decision)
        writer.write_collection_of_object_values("policyDetails", self.policy_details)
        writer.write_str_value("requestId", self.request_id)
        writer.write_str_value("requestMethod", self.request_method)
        writer.write_str_value("requestUri", self.request_uri)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("targetResourceId", self.target_resource_id)
        writer.write_str_value("targetResourceName", self.target_resource_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("totalFetchDurationMs", self.total_fetch_duration_ms)
        writer.write_int_value("totalPolicyEvaluationDurationMs", self.total_policy_evaluation_duration_ms)
        writer.write_str_value("userId", self.user_id)
    

