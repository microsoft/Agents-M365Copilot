from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_audit_record import BaseAuditRecord
    from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
    from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
    from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
    from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

from .base_audit_record import BaseAuditRecord

@dataclass
class ComplianceBaseAuditRecord(BaseAuditRecord, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dlp.complianceBaseAuditRecord"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceBaseAuditRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceBaseAuditRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
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
        return ComplianceBaseAuditRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_audit_record import BaseAuditRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

        from .base_audit_record import BaseAuditRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

        fields: dict[str, Callable[[Any], None]] = {
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
    

