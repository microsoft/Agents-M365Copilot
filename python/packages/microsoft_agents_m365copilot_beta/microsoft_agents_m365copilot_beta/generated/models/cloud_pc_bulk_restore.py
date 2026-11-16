from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_bulk_action import CloudPcBulkAction
    from .restore_time_range import RestoreTimeRange

from .cloud_pc_bulk_action import CloudPcBulkAction

@dataclass
class CloudPcBulkRestore(CloudPcBulkAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcBulkRestore"
    # True indicates that snapshots of unhealthy Cloud PCs are ignored. If no healthy snapshot exists within the selected timeRange, the healthy snapshot closest to the restorePointDateTime is used. False indicates that the snapshot within the selected timeRange and closest to the restorePointDateTime is used. The default value is false.
    ignore_unhealthy_snapshots: Optional[bool] = None
    # The date and time point for the selected Cloud PCs to restore. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    restore_point_date_time: Optional[datetime.datetime] = None
    # The timeRange property
    time_range: Optional[RestoreTimeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcBulkRestore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkRestore
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkRestore()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .restore_time_range import RestoreTimeRange

        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .restore_time_range import RestoreTimeRange

        fields: dict[str, Callable[[Any], None]] = {
            "ignoreUnhealthySnapshots": lambda n : setattr(self, 'ignore_unhealthy_snapshots', n.get_bool_value()),
            "restorePointDateTime": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "timeRange": lambda n : setattr(self, 'time_range', n.get_enum_value(RestoreTimeRange)),
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
        writer.write_bool_value("ignoreUnhealthySnapshots", self.ignore_unhealthy_snapshots)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_enum_value("timeRange", self.time_range)
    

