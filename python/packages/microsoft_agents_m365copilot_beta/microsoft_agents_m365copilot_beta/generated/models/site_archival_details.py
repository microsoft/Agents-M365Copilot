from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .site_archive_status import SiteArchiveStatus

@dataclass
class SiteArchivalDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents the current archive status of the site collection. Requires $select to retrieve.
    archive_status: Optional[SiteArchiveStatus] = None
    # The user or application that archived the container.
    archived_by: Optional[IdentitySet] = None
    # Time when the container was archived. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    archived_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SiteArchivalDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SiteArchivalDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SiteArchivalDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .site_archive_status import SiteArchiveStatus

        from .identity_set import IdentitySet
        from .site_archive_status import SiteArchiveStatus

        fields: dict[str, Callable[[Any], None]] = {
            "archiveStatus": lambda n : setattr(self, 'archive_status', n.get_enum_value(SiteArchiveStatus)),
            "archivedBy": lambda n : setattr(self, 'archived_by', n.get_object_value(IdentitySet)),
            "archivedDateTime": lambda n : setattr(self, 'archived_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("archiveStatus", self.archive_status)
        writer.write_object_value("archivedBy", self.archived_by)
        writer.write_datetime_value("archivedDateTime", self.archived_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

