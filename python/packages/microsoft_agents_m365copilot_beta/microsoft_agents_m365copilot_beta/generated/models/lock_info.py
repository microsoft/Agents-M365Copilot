from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lock_type import LockType
    from .user_identity import UserIdentity

@dataclass
class LockInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time when the lock was created, in UTC. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the lock expires, in UTC. Read-only.
    expiration_date_time: Optional[datetime.datetime] = None
    # The lockType property
    lock_type: Optional[LockType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of users that currently hold the lock on the file. Read-only.
    owners: Optional[list[UserIdentity]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LockInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LockInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LockInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lock_type import LockType
        from .user_identity import UserIdentity

        from .lock_type import LockType
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lockType": lambda n : setattr(self, 'lock_type', n.get_enum_value(LockType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(UserIdentity)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_enum_value("lockType", self.lock_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_additional_data_value(self.additional_data)
    

