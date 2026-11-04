from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_drift_report_resource_type import AccessDriftReportResourceType
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessDriftReport(Entity, Parsable):
    # The time-limited SAS URI for downloading the report file. This property is populated only in the response of the generateDownloadUri action.
    download_uri: Optional[str] = None
    # The date and time when the download URI expires. This property is populated only in the response of the generateDownloadUri action.
    expires_at: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceType property
    resource_type: Optional[AccessDriftReportResourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessDriftReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessDriftReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessDriftReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_drift_report_resource_type import AccessDriftReportResourceType
        from .entity import Entity

        from .access_drift_report_resource_type import AccessDriftReportResourceType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "downloadUri": lambda n : setattr(self, 'download_uri', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_enum_value(AccessDriftReportResourceType)),
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
        writer.write_enum_value("resourceType", self.resource_type)
    

