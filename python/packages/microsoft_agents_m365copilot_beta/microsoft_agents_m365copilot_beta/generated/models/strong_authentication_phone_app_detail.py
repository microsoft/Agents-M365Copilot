from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .oath_token_metadata import OathTokenMetadata

from .entity import Entity

@dataclass
class StrongAuthenticationPhoneAppDetail(Entity, Parsable):
    # The authenticationType property
    authentication_type: Optional[str] = None
    # The authenticatorFlavor property
    authenticator_flavor: Optional[str] = None
    # The deviceId property
    device_id: Optional[UUID] = None
    # The deviceName property
    device_name: Optional[str] = None
    # The deviceTag property
    device_tag: Optional[str] = None
    # The deviceToken property
    device_token: Optional[str] = None
    # The hashFunction property
    hash_function: Optional[str] = None
    # The lastAuthenticatedDateTime property
    last_authenticated_date_time: Optional[datetime.datetime] = None
    # The notificationType property
    notification_type: Optional[str] = None
    # The oathSecretKey property
    oath_secret_key: Optional[str] = None
    # The oathTokenMetadata property
    oath_token_metadata: Optional[OathTokenMetadata] = None
    # The oathTokenTimeDriftInSeconds property
    oath_token_time_drift_in_seconds: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phoneAppVersion property
    phone_app_version: Optional[str] = None
    # The tenantDeviceId property
    tenant_device_id: Optional[str] = None
    # The tokenGenerationIntervalInSeconds property
    token_generation_interval_in_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StrongAuthenticationPhoneAppDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StrongAuthenticationPhoneAppDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StrongAuthenticationPhoneAppDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .oath_token_metadata import OathTokenMetadata

        from .entity import Entity
        from .oath_token_metadata import OathTokenMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationType": lambda n : setattr(self, 'authentication_type', n.get_str_value()),
            "authenticatorFlavor": lambda n : setattr(self, 'authenticator_flavor', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_uuid_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceTag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
            "deviceToken": lambda n : setattr(self, 'device_token', n.get_str_value()),
            "hashFunction": lambda n : setattr(self, 'hash_function', n.get_str_value()),
            "lastAuthenticatedDateTime": lambda n : setattr(self, 'last_authenticated_date_time', n.get_datetime_value()),
            "notificationType": lambda n : setattr(self, 'notification_type', n.get_str_value()),
            "oathSecretKey": lambda n : setattr(self, 'oath_secret_key', n.get_str_value()),
            "oathTokenMetadata": lambda n : setattr(self, 'oath_token_metadata', n.get_object_value(OathTokenMetadata)),
            "oathTokenTimeDriftInSeconds": lambda n : setattr(self, 'oath_token_time_drift_in_seconds', n.get_int_value()),
            "phoneAppVersion": lambda n : setattr(self, 'phone_app_version', n.get_str_value()),
            "tenantDeviceId": lambda n : setattr(self, 'tenant_device_id', n.get_str_value()),
            "tokenGenerationIntervalInSeconds": lambda n : setattr(self, 'token_generation_interval_in_seconds', n.get_int_value()),
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
        writer.write_str_value("authenticationType", self.authentication_type)
        writer.write_str_value("authenticatorFlavor", self.authenticator_flavor)
        writer.write_uuid_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_str_value("deviceToken", self.device_token)
        writer.write_str_value("hashFunction", self.hash_function)
        writer.write_datetime_value("lastAuthenticatedDateTime", self.last_authenticated_date_time)
        writer.write_str_value("notificationType", self.notification_type)
        writer.write_str_value("oathSecretKey", self.oath_secret_key)
        writer.write_object_value("oathTokenMetadata", self.oath_token_metadata)
        writer.write_int_value("oathTokenTimeDriftInSeconds", self.oath_token_time_drift_in_seconds)
        writer.write_str_value("phoneAppVersion", self.phone_app_version)
        writer.write_str_value("tenantDeviceId", self.tenant_device_id)
        writer.write_int_value("tokenGenerationIntervalInSeconds", self.token_generation_interval_in_seconds)
    

