from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .managed_app_log_upload import ManagedAppLogUpload
    from .managed_app_log_upload_consent import ManagedAppLogUploadConsent

from .entity import Entity

@dataclass
class ManagedAppLogCollectionRequest(Entity, Parsable):
    """
    The Managed App log collection response
    """
    # DateTime of when the log upload request was completed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.
    completed_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the app instance for which diagnostic logs were collected. Read-only.
    managed_app_registration_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user principal name associated with the request for the managed application log collection. Read-only.
    requested_by_user_principal_name: Optional[str] = None
    # DateTime of when the log upload request was received. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.
    requested_date_time: Optional[datetime.datetime] = None
    # The collection of log upload results as reported by each component on the device. Such components can be the application itself, the Mobile Application Management (MAM) SDK, and other on-device components that are requested to upload diagnostic logs. Read-only.
    uploaded_logs: Optional[list[ManagedAppLogUpload]] = None
    # Represents the current consent status of the associated `managedAppLogCollectionRequest`.
    user_log_upload_consent: Optional[ManagedAppLogUploadConsent] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppLogCollectionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppLogCollectionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppLogCollectionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .managed_app_log_upload import ManagedAppLogUpload
        from .managed_app_log_upload_consent import ManagedAppLogUploadConsent

        from .entity import Entity
        from .managed_app_log_upload import ManagedAppLogUpload
        from .managed_app_log_upload_consent import ManagedAppLogUploadConsent

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "managedAppRegistrationId": lambda n : setattr(self, 'managed_app_registration_id', n.get_str_value()),
            "requestedByUserPrincipalName": lambda n : setattr(self, 'requested_by_user_principal_name', n.get_str_value()),
            "requestedDateTime": lambda n : setattr(self, 'requested_date_time', n.get_datetime_value()),
            "uploadedLogs": lambda n : setattr(self, 'uploaded_logs', n.get_collection_of_object_values(ManagedAppLogUpload)),
            "userLogUploadConsent": lambda n : setattr(self, 'user_log_upload_consent', n.get_enum_value(ManagedAppLogUploadConsent)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_str_value("managedAppRegistrationId", self.managed_app_registration_id)
        writer.write_str_value("requestedByUserPrincipalName", self.requested_by_user_principal_name)
        writer.write_datetime_value("requestedDateTime", self.requested_date_time)
        writer.write_collection_of_object_values("uploadedLogs", self.uploaded_logs)
        writer.write_enum_value("userLogUploadConsent", self.user_log_upload_consent)
        writer.write_str_value("version", self.version)
    

