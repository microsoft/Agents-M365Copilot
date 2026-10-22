from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
    from .endpoint_meta_data_info import EndpointMetaDataInfo

from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

@dataclass
class ComplianceDlpEndpointAuditRecord(ComplianceDLPBaseAuditRecord, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dlp.complianceDlpEndpointAuditRecord"
    # The authorizedGroup property
    authorized_group: Optional[str] = None
    # The endpointMetaData property
    endpoint_meta_data: Optional[EndpointMetaDataInfo] = None
    # The evidenceFile property
    evidence_file: Optional[str] = None
    # The networkLocationContextInAction property
    network_location_context_in_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceDlpEndpointAuditRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceDlpEndpointAuditRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComplianceDlpEndpointAuditRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .endpoint_meta_data_info import EndpointMetaDataInfo

        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .endpoint_meta_data_info import EndpointMetaDataInfo

        fields: dict[str, Callable[[Any], None]] = {
            "authorizedGroup": lambda n : setattr(self, 'authorized_group', n.get_str_value()),
            "endpointMetaData": lambda n : setattr(self, 'endpoint_meta_data', n.get_object_value(EndpointMetaDataInfo)),
            "evidenceFile": lambda n : setattr(self, 'evidence_file', n.get_str_value()),
            "networkLocationContextInAction": lambda n : setattr(self, 'network_location_context_in_action', n.get_str_value()),
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
        writer.write_str_value("authorizedGroup", self.authorized_group)
        writer.write_object_value("endpointMetaData", self.endpoint_meta_data)
        writer.write_str_value("evidenceFile", self.evidence_file)
        writer.write_str_value("networkLocationContextInAction", self.network_location_context_in_action)
    

