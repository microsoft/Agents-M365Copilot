from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource import AccessPackageResource
    from .access_package_subject import AccessPackageSubject
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceRequest(Entity, Parsable):
    # The accessPackageResource property
    access_package_resource: Optional[AccessPackageResource] = None
    # The unique ID of the access package catalog.
    catalog_id: Optional[str] = None
    # The executeImmediately property
    execute_immediately: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    expiration_date_time: Optional[datetime.datetime] = None
    # If set, doesn't add the resource.
    is_validation_only: Optional[bool] = None
    # The requestor's justification for adding or removing the resource.
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outcome of whether the service was able to add the resource to the catalog. The value is Delivered if the resource was added or removed. Read-only.
    request_state: Optional[str] = None
    # The requestStatus property
    request_status: Optional[str] = None
    # Use AdminAdd to add a resource, if the caller is an administrator or resource owner, AdminUpdate to update a resource, or AdminRemove to remove a resource.
    request_type: Optional[str] = None
    # Read-only. Nullable. Supports $expand.
    requestor: Optional[AccessPackageSubject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource import AccessPackageResource
        from .access_package_subject import AccessPackageSubject
        from .entity import Entity

        from .access_package_resource import AccessPackageResource
        from .access_package_subject import AccessPackageSubject
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageResource": lambda n : setattr(self, 'access_package_resource', n.get_object_value(AccessPackageResource)),
            "catalogId": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "executeImmediately": lambda n : setattr(self, 'execute_immediately', n.get_bool_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "isValidationOnly": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "requestState": lambda n : setattr(self, 'request_state', n.get_str_value()),
            "requestStatus": lambda n : setattr(self, 'request_status', n.get_str_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_str_value()),
            "requestor": lambda n : setattr(self, 'requestor', n.get_object_value(AccessPackageSubject)),
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
        writer.write_object_value("accessPackageResource", self.access_package_resource)
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_bool_value("executeImmediately", self.execute_immediately)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("isValidationOnly", self.is_validation_only)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("requestState", self.request_state)
        writer.write_str_value("requestStatus", self.request_status)
        writer.write_str_value("requestType", self.request_type)
        writer.write_object_value("requestor", self.requestor)
    

