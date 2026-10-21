from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .app_access_context import AppAccessContext
    from .audit_record_type import AuditRecordType
    from .compliance_base_audit_record import ComplianceBaseAuditRecord
    from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
    from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
    from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
    from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
    from .purpose_type import PurposeType
    from .subscription_info import SubscriptionInfo
    from .user_type import UserType

from ...entity import Entity

@dataclass
class BaseAuditRecord(Entity, Parsable):
    # The agentBlueprintId property
    agent_blueprint_id: Optional[str] = None
    # The agentBlueprintName property
    agent_blueprint_name: Optional[str] = None
    # The agentId property
    agent_id: Optional[str] = None
    # The agentName property
    agent_name: Optional[str] = None
    # The agentPlatform property
    agent_platform: Optional[str] = None
    # The agentVersion property
    agent_version: Optional[str] = None
    # The appAccessContext property
    app_access_context: Optional[AppAccessContext] = None
    # The appIdentity property
    app_identity: Optional[str] = None
    # The applicationName property
    application_name: Optional[str] = None
    # The associatedAdminUnitIds property
    associated_admin_unit_ids: Optional[list[str]] = None
    # The correlationIdentity property
    correlation_identity: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.date] = None
    # The isRequiresCustomerKeyEncryption property
    is_requires_customer_key_encryption: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The opId property
    op_id: Optional[str] = None
    # The operation property
    operation: Optional[str] = None
    # The organizationId property
    organization_id: Optional[str] = None
    # The parentId property
    parent_id: Optional[str] = None
    # The purpose property
    purpose: Optional[PurposeType] = None
    # The recordType property
    record_type: Optional[AuditRecordType] = None
    # The resultStatus property
    result_status: Optional[str] = None
    # The scopingEntityIds property
    scoping_entity_ids: Optional[list[str]] = None
    # The scopingEntityType property
    scoping_entity_type: Optional[int] = None
    # The sessionIdentity property
    session_identity: Optional[str] = None
    # The subjectType property
    subject_type: Optional[str] = None
    # The subscription property
    subscription: Optional[SubscriptionInfo] = None
    # The userKey property
    user_key: Optional[str] = None
    # The userType property
    user_type: Optional[UserType] = None
    # The version property
    version: Optional[int] = None
    # The workload property
    workload: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BaseAuditRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseAuditRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceBaseAuditRecord".casefold():
            from .compliance_base_audit_record import ComplianceBaseAuditRecord

            return ComplianceBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDLPBaseAuditRecord".casefold():
            from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

            return ComplianceDLPBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDlpEndpointAuditRecord".casefold():
            from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord

            return ComplianceDlpEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDlpExchangeAuditRecord".casefold():
            from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord

            return ComplianceDlpExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDlpSharePointAuditRecord".casefold():
            from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord

            return ComplianceDlpSharePointAuditRecord()
        return BaseAuditRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .app_access_context import AppAccessContext
        from .audit_record_type import AuditRecordType
        from .compliance_base_audit_record import ComplianceBaseAuditRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .purpose_type import PurposeType
        from .subscription_info import SubscriptionInfo
        from .user_type import UserType

        from ...entity import Entity
        from .app_access_context import AppAccessContext
        from .audit_record_type import AuditRecordType
        from .compliance_base_audit_record import ComplianceBaseAuditRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .purpose_type import PurposeType
        from .subscription_info import SubscriptionInfo
        from .user_type import UserType

        fields: dict[str, Callable[[Any], None]] = {
            "agentBlueprintId": lambda n : setattr(self, 'agent_blueprint_id', n.get_str_value()),
            "agentBlueprintName": lambda n : setattr(self, 'agent_blueprint_name', n.get_str_value()),
            "agentId": lambda n : setattr(self, 'agent_id', n.get_str_value()),
            "agentName": lambda n : setattr(self, 'agent_name', n.get_str_value()),
            "agentPlatform": lambda n : setattr(self, 'agent_platform', n.get_str_value()),
            "agentVersion": lambda n : setattr(self, 'agent_version', n.get_str_value()),
            "appAccessContext": lambda n : setattr(self, 'app_access_context', n.get_object_value(AppAccessContext)),
            "appIdentity": lambda n : setattr(self, 'app_identity', n.get_str_value()),
            "applicationName": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "associatedAdminUnitIds": lambda n : setattr(self, 'associated_admin_unit_ids', n.get_collection_of_primitive_values(str)),
            "correlationIdentity": lambda n : setattr(self, 'correlation_identity', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_date_value()),
            "isRequiresCustomerKeyEncryption": lambda n : setattr(self, 'is_requires_customer_key_encryption', n.get_bool_value()),
            "opId": lambda n : setattr(self, 'op_id', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "purpose": lambda n : setattr(self, 'purpose', n.get_enum_value(PurposeType)),
            "recordType": lambda n : setattr(self, 'record_type', n.get_enum_value(AuditRecordType)),
            "resultStatus": lambda n : setattr(self, 'result_status', n.get_str_value()),
            "scopingEntityIds": lambda n : setattr(self, 'scoping_entity_ids', n.get_collection_of_primitive_values(str)),
            "scopingEntityType": lambda n : setattr(self, 'scoping_entity_type', n.get_int_value()),
            "sessionIdentity": lambda n : setattr(self, 'session_identity', n.get_str_value()),
            "subjectType": lambda n : setattr(self, 'subject_type', n.get_str_value()),
            "subscription": lambda n : setattr(self, 'subscription', n.get_object_value(SubscriptionInfo)),
            "userKey": lambda n : setattr(self, 'user_key', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(UserType)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "workload": lambda n : setattr(self, 'workload', n.get_str_value()),
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
        writer.write_str_value("agentBlueprintId", self.agent_blueprint_id)
        writer.write_str_value("agentBlueprintName", self.agent_blueprint_name)
        writer.write_str_value("agentId", self.agent_id)
        writer.write_str_value("agentName", self.agent_name)
        writer.write_str_value("agentPlatform", self.agent_platform)
        writer.write_str_value("agentVersion", self.agent_version)
        writer.write_object_value("appAccessContext", self.app_access_context)
        writer.write_str_value("appIdentity", self.app_identity)
        writer.write_str_value("applicationName", self.application_name)
        writer.write_collection_of_primitive_values("associatedAdminUnitIds", self.associated_admin_unit_ids)
        writer.write_str_value("correlationIdentity", self.correlation_identity)
        writer.write_date_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isRequiresCustomerKeyEncryption", self.is_requires_customer_key_encryption)
        writer.write_str_value("opId", self.op_id)
        writer.write_str_value("operation", self.operation)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_enum_value("purpose", self.purpose)
        writer.write_enum_value("recordType", self.record_type)
        writer.write_str_value("resultStatus", self.result_status)
        writer.write_collection_of_primitive_values("scopingEntityIds", self.scoping_entity_ids)
        writer.write_int_value("scopingEntityType", self.scoping_entity_type)
        writer.write_str_value("sessionIdentity", self.session_identity)
        writer.write_str_value("subjectType", self.subject_type)
        writer.write_object_value("subscription", self.subscription)
        writer.write_str_value("userKey", self.user_key)
        writer.write_enum_value("userType", self.user_type)
        writer.write_int_value("version", self.version)
        writer.write_str_value("workload", self.workload)
    

