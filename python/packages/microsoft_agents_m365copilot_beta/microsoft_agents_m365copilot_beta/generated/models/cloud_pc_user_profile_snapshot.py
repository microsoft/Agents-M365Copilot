from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_user_settings_persistence_snapshot_type import CloudPcUserSettingsPersistenceSnapshotType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcUserProfileSnapshot(Entity, Parsable):
    # The cloudProfileId property
    cloud_profile_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The lastRestoredDateTime property
    last_restored_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The snapshotSizeInGB property
    snapshot_size_in_g_b: Optional[int] = None
    # The snapshotType property
    snapshot_type: Optional[CloudPcUserSettingsPersistenceSnapshotType] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcUserProfileSnapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserProfileSnapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserProfileSnapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_user_settings_persistence_snapshot_type import CloudPcUserSettingsPersistenceSnapshotType
        from .entity import Entity

        from .cloud_pc_user_settings_persistence_snapshot_type import CloudPcUserSettingsPersistenceSnapshotType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "cloudProfileId": lambda n : setattr(self, 'cloud_profile_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastRestoredDateTime": lambda n : setattr(self, 'last_restored_date_time', n.get_datetime_value()),
            "snapshotSizeInGB": lambda n : setattr(self, 'snapshot_size_in_g_b', n.get_int_value()),
            "snapshotType": lambda n : setattr(self, 'snapshot_type', n.get_enum_value(CloudPcUserSettingsPersistenceSnapshotType)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("cloudProfileId", self.cloud_profile_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastRestoredDateTime", self.last_restored_date_time)
        writer.write_int_value("snapshotSizeInGB", self.snapshot_size_in_g_b)
        writer.write_enum_value("snapshotType", self.snapshot_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

