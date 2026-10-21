from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class AuditEvent(Entity, Parsable):
    # A string that uniquely represents the operation that occurred. Required. Read-only.
    activity: Optional[str] = None
    # The time when the activity occurred. Required. Read-only.
    activity_date_time: Optional[datetime.datetime] = None
    # The identifier of the activity request that made the audit event. Required. Read-only.
    activity_id: Optional[str] = None
    # A category that represents a logical grouping of activities. Required. Read-only.
    category: Optional[str] = None
    # The HTTP verb that was used when making the API request. Required. Read-only.
    http_verb: Optional[str] = None
    # The identifier of the app that was used to make the request. Required. Read-only.
    initiated_by_app_id: Optional[str] = None
    # The UPN of the user who initiated the activity. Required. Read-only.
    initiated_by_upn: Optional[str] = None
    # The identifier of the user who initiated the activity. Required. Read-only.
    initiated_by_user_id: Optional[str] = None
    # The IP address of where the activity was initiated. This may be an IPv4 or IPv6 address. Required. Read-only.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The raw HTTP request body. Some sensitive information may be removed.
    request_body: Optional[str] = None
    # The raw HTTP request URL. Required. Read-only.
    request_url: Optional[str] = None
    # The collection of Microsoft Entra tenant identifiers for the managed tenants that were affected by a change, and is formatted as a list of comma-separated values. Required. Read-only.
    tenant_ids: Optional[str] = None
    # The collection of tenant names that were affected by a change, and is formatted as a list of comma-separated values. Required. Read-only.
    tenant_names: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activityId": lambda n : setattr(self, 'activity_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "httpVerb": lambda n : setattr(self, 'http_verb', n.get_str_value()),
            "initiatedByAppId": lambda n : setattr(self, 'initiated_by_app_id', n.get_str_value()),
            "initiatedByUpn": lambda n : setattr(self, 'initiated_by_upn', n.get_str_value()),
            "initiatedByUserId": lambda n : setattr(self, 'initiated_by_user_id', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "requestBody": lambda n : setattr(self, 'request_body', n.get_str_value()),
            "requestUrl": lambda n : setattr(self, 'request_url', n.get_str_value()),
            "tenantIds": lambda n : setattr(self, 'tenant_ids', n.get_str_value()),
            "tenantNames": lambda n : setattr(self, 'tenant_names', n.get_str_value()),
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
        writer.write_str_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityId", self.activity_id)
        writer.write_str_value("category", self.category)
        writer.write_str_value("httpVerb", self.http_verb)
        writer.write_str_value("initiatedByAppId", self.initiated_by_app_id)
        writer.write_str_value("initiatedByUpn", self.initiated_by_upn)
        writer.write_str_value("initiatedByUserId", self.initiated_by_user_id)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("requestBody", self.request_body)
        writer.write_str_value("requestUrl", self.request_url)
        writer.write_str_value("tenantIds", self.tenant_ids)
        writer.write_str_value("tenantNames", self.tenant_names)
    

