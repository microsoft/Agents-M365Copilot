from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class PrivilegedOperationEvent(Entity, Parsable):
    # The additionalInformation property
    additional_information: Optional[str] = None
    # The creationDateTime property
    creation_date_time: Optional[datetime.datetime] = None
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The referenceKey property
    reference_key: Optional[str] = None
    # The referenceSystem property
    reference_system: Optional[str] = None
    # The requestType property
    request_type: Optional[str] = None
    # The requestorId property
    requestor_id: Optional[str] = None
    # The requestorName property
    requestor_name: Optional[str] = None
    # The roleId property
    role_id: Optional[str] = None
    # The roleName property
    role_name: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    # The userMail property
    user_mail: Optional[str] = None
    # The userName property
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedOperationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedOperationEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedOperationEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "referenceKey": lambda n : setattr(self, 'reference_key', n.get_str_value()),
            "referenceSystem": lambda n : setattr(self, 'reference_system', n.get_str_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_str_value()),
            "requestorId": lambda n : setattr(self, 'requestor_id', n.get_str_value()),
            "requestorName": lambda n : setattr(self, 'requestor_name', n.get_str_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleName": lambda n : setattr(self, 'role_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userMail": lambda n : setattr(self, 'user_mail', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("referenceKey", self.reference_key)
        writer.write_str_value("referenceSystem", self.reference_system)
        writer.write_str_value("requestType", self.request_type)
        writer.write_str_value("requestorId", self.requestor_id)
        writer.write_str_value("requestorName", self.requestor_name)
        writer.write_str_value("roleId", self.role_id)
        writer.write_str_value("roleName", self.role_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userMail", self.user_mail)
        writer.write_str_value("userName", self.user_name)
    

