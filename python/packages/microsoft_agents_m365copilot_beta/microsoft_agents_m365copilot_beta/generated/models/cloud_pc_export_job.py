from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_export_job_status import CloudPcExportJobStatus
    from .cloud_pc_report_name import CloudPcReportName
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcExportJob(Entity, Parsable):
    # The date and time when the export job expires.
    expiration_date_time: Optional[datetime.datetime] = None
    # The status of the export job. The possible values are: notStarted, inProgress, completed, unknownFutureValue. Read-only.
    export_job_status: Optional[CloudPcExportJobStatus] = None
    # The storage account URL of the exported report. It can be used to download the file.
    export_url: Optional[str] = None
    # The filter applied on the report.
    filter: Optional[str] = None
    # The format of the exported report.
    format: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The report name.
    report_name: Optional[CloudPcReportName] = None
    # The date and time when the export job was requested.
    request_date_time: Optional[datetime.datetime] = None
    # The selected columns of the report.
    select: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcExportJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcExportJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcExportJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_export_job_status import CloudPcExportJobStatus
        from .cloud_pc_report_name import CloudPcReportName
        from .entity import Entity

        from .cloud_pc_export_job_status import CloudPcExportJobStatus
        from .cloud_pc_report_name import CloudPcReportName
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "exportJobStatus": lambda n : setattr(self, 'export_job_status', n.get_enum_value(CloudPcExportJobStatus)),
            "exportUrl": lambda n : setattr(self, 'export_url', n.get_str_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "reportName": lambda n : setattr(self, 'report_name', n.get_enum_value(CloudPcReportName)),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_enum_value("exportJobStatus", self.export_job_status)
        writer.write_str_value("exportUrl", self.export_url)
        writer.write_str_value("filter", self.filter)
        writer.write_str_value("format", self.format)
        writer.write_enum_value("reportName", self.report_name)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_collection_of_primitive_values("select", self.select)
    

