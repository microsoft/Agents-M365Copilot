from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_storage_configuration import CloudPcStorageConfiguration
    from .cloud_pc_user_profile_snapshot import CloudPcUserProfileSnapshot
    from .cloud_pc_user_settings_persistence_snapshot_configuration import CloudPcUserSettingsPersistenceSnapshotConfiguration
    from .cloud_p_c_user_settings_persistence_auto_cleanup_detail import CloudPCUserSettingsPersistenceAutoCleanupDetail
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPCUserSettingsPersistenceDetail(Entity, Parsable):
    # The autoCleanupDetail property
    auto_cleanup_detail: Optional[CloudPCUserSettingsPersistenceAutoCleanupDetail] = None
    # Indicates the grace period end time when user settings persistence exceeds the available quota. If usage exceeds the available quota when the grace period expires, the system automatically deletes the profile with the oldest last attached timestamp. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    grace_period_end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The snapshotConfiguration property
    snapshot_configuration: Optional[CloudPcUserSettingsPersistenceSnapshotConfiguration] = None
    # The storageConfiguration property
    storage_configuration: Optional[CloudPcStorageConfiguration] = None
    # The userProfileSnapshots property
    user_profile_snapshots: Optional[list[CloudPcUserProfileSnapshot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPCUserSettingsPersistenceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPCUserSettingsPersistenceDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPCUserSettingsPersistenceDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_storage_configuration import CloudPcStorageConfiguration
        from .cloud_pc_user_profile_snapshot import CloudPcUserProfileSnapshot
        from .cloud_pc_user_settings_persistence_snapshot_configuration import CloudPcUserSettingsPersistenceSnapshotConfiguration
        from .cloud_p_c_user_settings_persistence_auto_cleanup_detail import CloudPCUserSettingsPersistenceAutoCleanupDetail
        from .entity import Entity

        from .cloud_pc_storage_configuration import CloudPcStorageConfiguration
        from .cloud_pc_user_profile_snapshot import CloudPcUserProfileSnapshot
        from .cloud_pc_user_settings_persistence_snapshot_configuration import CloudPcUserSettingsPersistenceSnapshotConfiguration
        from .cloud_p_c_user_settings_persistence_auto_cleanup_detail import CloudPCUserSettingsPersistenceAutoCleanupDetail
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "autoCleanupDetail": lambda n : setattr(self, 'auto_cleanup_detail', n.get_object_value(CloudPCUserSettingsPersistenceAutoCleanupDetail)),
            "gracePeriodEndDateTime": lambda n : setattr(self, 'grace_period_end_date_time', n.get_datetime_value()),
            "snapshotConfiguration": lambda n : setattr(self, 'snapshot_configuration', n.get_object_value(CloudPcUserSettingsPersistenceSnapshotConfiguration)),
            "storageConfiguration": lambda n : setattr(self, 'storage_configuration', n.get_object_value(CloudPcStorageConfiguration)),
            "userProfileSnapshots": lambda n : setattr(self, 'user_profile_snapshots', n.get_collection_of_object_values(CloudPcUserProfileSnapshot)),
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
        writer.write_object_value("autoCleanupDetail", self.auto_cleanup_detail)
        writer.write_datetime_value("gracePeriodEndDateTime", self.grace_period_end_date_time)
        writer.write_object_value("snapshotConfiguration", self.snapshot_configuration)
        writer.write_object_value("storageConfiguration", self.storage_configuration)
        writer.write_collection_of_object_values("userProfileSnapshots", self.user_profile_snapshots)
    

