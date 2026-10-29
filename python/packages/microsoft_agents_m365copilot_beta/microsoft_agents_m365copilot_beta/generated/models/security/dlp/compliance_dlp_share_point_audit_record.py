from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
    from .share_point_meta_data_info import SharePointMetaDataInfo

from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord

@dataclass
class ComplianceDlpSharePointAuditRecord(ComplianceDLPBaseAuditRecord, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dlp.complianceDlpSharePointAuditRecord"
    # The sharePointMetaData property
    share_point_meta_data: Optional[SharePointMetaDataInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceDlpSharePointAuditRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceDlpSharePointAuditRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComplianceDlpSharePointAuditRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .share_point_meta_data_info import SharePointMetaDataInfo

        from .compliance_d_l_p_base_audit_record import ComplianceDLPBaseAuditRecord
        from .share_point_meta_data_info import SharePointMetaDataInfo

        fields: dict[str, Callable[[Any], None]] = {
            "sharePointMetaData": lambda n : setattr(self, 'share_point_meta_data', n.get_object_value(SharePointMetaDataInfo)),
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
        writer.write_object_value("sharePointMetaData", self.share_point_meta_data)
    

