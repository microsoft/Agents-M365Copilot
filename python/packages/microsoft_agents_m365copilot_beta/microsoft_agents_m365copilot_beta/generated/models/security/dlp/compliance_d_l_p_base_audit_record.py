from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .compliance_base_audit_record import ComplianceBaseAuditRecord
    from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
    from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
    from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
    from .enforcement_type import EnforcementType
    from .exception_info import ExceptionInfo
    from .remediation_info import RemediationInfo
    from .session_metadata_info import SessionMetadataInfo

from .compliance_base_audit_record import ComplianceBaseAuditRecord

@dataclass
class ComplianceDLPBaseAuditRecord(ComplianceBaseAuditRecord, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dlp.complianceDLPBaseAuditRecord"
    # The enforcementType property
    enforcement_type: Optional[EnforcementType] = None
    # The evaluationSource property
    evaluation_source: Optional[str] = None
    # The exceptionInfo property
    exception_info: Optional[ExceptionInfo] = None
    # The incidentId property
    incident_id: Optional[UUID] = None
    # The isSensitiveInfoDetectionIsIncluded property
    is_sensitive_info_detection_is_included: Optional[bool] = None
    # The location property
    location: Optional[str] = None
    # The policyDetails property
    policy_details: Optional[list[str]] = None
    # The remediationDetails property
    remediation_details: Optional[RemediationInfo] = None
    # The sessionMetadata property
    session_metadata: Optional[SessionMetadataInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceDLPBaseAuditRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceDLPBaseAuditRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDlpEndpointAuditRecord".casefold():
            from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord

            return ComplianceDlpEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDlpExchangeAuditRecord".casefold():
            from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord

            return ComplianceDlpExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlp.complianceDlpSharePointAuditRecord".casefold():
            from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord

            return ComplianceDlpSharePointAuditRecord()
        return ComplianceDLPBaseAuditRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_base_audit_record import ComplianceBaseAuditRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .enforcement_type import EnforcementType
        from .exception_info import ExceptionInfo
        from .remediation_info import RemediationInfo
        from .session_metadata_info import SessionMetadataInfo

        from .compliance_base_audit_record import ComplianceBaseAuditRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .enforcement_type import EnforcementType
        from .exception_info import ExceptionInfo
        from .remediation_info import RemediationInfo
        from .session_metadata_info import SessionMetadataInfo

        fields: dict[str, Callable[[Any], None]] = {
            "enforcementType": lambda n : setattr(self, 'enforcement_type', n.get_enum_value(EnforcementType)),
            "evaluationSource": lambda n : setattr(self, 'evaluation_source', n.get_str_value()),
            "exceptionInfo": lambda n : setattr(self, 'exception_info', n.get_object_value(ExceptionInfo)),
            "incidentId": lambda n : setattr(self, 'incident_id', n.get_uuid_value()),
            "isSensitiveInfoDetectionIsIncluded": lambda n : setattr(self, 'is_sensitive_info_detection_is_included', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "policyDetails": lambda n : setattr(self, 'policy_details', n.get_collection_of_primitive_values(str)),
            "remediationDetails": lambda n : setattr(self, 'remediation_details', n.get_object_value(RemediationInfo)),
            "sessionMetadata": lambda n : setattr(self, 'session_metadata', n.get_object_value(SessionMetadataInfo)),
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
        writer.write_enum_value("enforcementType", self.enforcement_type)
        writer.write_str_value("evaluationSource", self.evaluation_source)
        writer.write_object_value("exceptionInfo", self.exception_info)
        writer.write_uuid_value("incidentId", self.incident_id)
        writer.write_bool_value("isSensitiveInfoDetectionIsIncluded", self.is_sensitive_info_detection_is_included)
        writer.write_str_value("location", self.location)
        writer.write_collection_of_primitive_values("policyDetails", self.policy_details)
        writer.write_object_value("remediationDetails", self.remediation_details)
        writer.write_object_value("sessionMetadata", self.session_metadata)
    

