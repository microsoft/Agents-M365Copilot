from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
    from .exchange_meta_data_info import ExchangeMetaDataInfo

from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

@dataclass
class ComplianceDlpExchangeAuditRecord(ComplianceDLPBaseAuditRecord, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dlp.complianceDlpExchangeAuditRecord"
    # The exchangeMetaData property
    exchange_meta_data: Optional[ExchangeMetaDataInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceDlpExchangeAuditRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceDlpExchangeAuditRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComplianceDlpExchangeAuditRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .exchange_meta_data_info import ExchangeMetaDataInfo

        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .exchange_meta_data_info import ExchangeMetaDataInfo

        fields: dict[str, Callable[[Any], None]] = {
            "exchangeMetaData": lambda n : setattr(self, 'exchange_meta_data', n.get_object_value(ExchangeMetaDataInfo)),
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
        writer.write_object_value("exchangeMetaData", self.exchange_meta_data)
    

