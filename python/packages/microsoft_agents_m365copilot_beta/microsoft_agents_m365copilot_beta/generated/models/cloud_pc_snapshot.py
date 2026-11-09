from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_snapshot_health_check_status import CloudPcSnapshotHealthCheckStatus
    from .cloud_pc_snapshot_status import CloudPcSnapshotStatus
    from .cloud_pc_snapshot_type import CloudPcSnapshotType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcSnapshot(Entity, Parsable):
    # The unique identifier for the Cloud PC.
    cloud_pc_id: Optional[str] = None
    # The date and time at which the snapshot was taken. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the snapshot expires. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration_date_time: Optional[datetime.datetime] = None
    # Indicates the health check status of the Cloud PC snapshot. The possible values are: unknown, healthy, unhealthy, unknownFutureValue. The default value is unknown. Read-only. Nullable.
    health_check_status: Optional[CloudPcSnapshotHealthCheckStatus] = None
    # The date and time at which the snapshot was last used to restore the Cloud PC device. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_restored_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of snapshot that indicates how to create the snapshot. Possible values are automatic, manual, unknownFutureValue, retention. Use the Prefer: include-unknown-enum-members request header to get the following members from this evolvable enum: retention. The default value is automatic.
    snapshot_type: Optional[CloudPcSnapshotType] = None
    # The status of the Cloud PC snapshot. The possible values are: ready, unknownFutureValue.
    status: Optional[CloudPcSnapshotStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSnapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcSnapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_snapshot_health_check_status import CloudPcSnapshotHealthCheckStatus
        from .cloud_pc_snapshot_status import CloudPcSnapshotStatus
        from .cloud_pc_snapshot_type import CloudPcSnapshotType
        from .entity import Entity

        from .cloud_pc_snapshot_health_check_status import CloudPcSnapshotHealthCheckStatus
        from .cloud_pc_snapshot_status import CloudPcSnapshotStatus
        from .cloud_pc_snapshot_type import CloudPcSnapshotType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "healthCheckStatus": lambda n : setattr(self, 'health_check_status', n.get_enum_value(CloudPcSnapshotHealthCheckStatus)),
            "lastRestoredDateTime": lambda n : setattr(self, 'last_restored_date_time', n.get_datetime_value()),
            "snapshotType": lambda n : setattr(self, 'snapshot_type', n.get_enum_value(CloudPcSnapshotType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcSnapshotStatus)),
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
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_enum_value("healthCheckStatus", self.health_check_status)
        writer.write_datetime_value("lastRestoredDateTime", self.last_restored_date_time)
        writer.write_enum_value("snapshotType", self.snapshot_type)
        writer.write_enum_value("status", self.status)
    

