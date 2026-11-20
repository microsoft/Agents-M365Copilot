from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .service_now_authentication_method import ServiceNowAuthenticationMethod
    from .service_now_connection_status import ServiceNowConnectionStatus

from .entity import Entity

@dataclass
class ServiceNowConnection(Entity, Parsable):
    """
    ServiceNow properties including the ServiceNow instanceUrl, connection credentials and other metadata.
    """
    # Indicates the method used by Intune to authenticate with ServiceNow. Currently supports only web authentication with ServiceNow using the specified app id.
    authentication_method: Optional[ServiceNowAuthenticationMethod] = None
    # Date Time when connection properties were created. The value cannot be modified and is automatically populated when the connection properties were entered.
    created_date_time: Optional[datetime.datetime] = None
    # Indicates the ServiceNow incident API URL that Intune will use the fetch incidents. Saved in the format of /api/now/table/incident
    incident_api_url: Optional[str] = None
    # Indicates the ServiceNow instance URL that Intune will connect to. Saved in the format of https://<instance>.service-now.com
    instance_url: Optional[str] = None
    # Date Time when connection properties were last updated. The value cannot be modified and is automatically populated when the connection properties were updated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Date Time when incidents from ServiceNow were last queried
    last_queried_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Status of ServiceNow Connection
    service_now_connection_status: Optional[ServiceNowConnectionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceNowConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceNowConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceNowConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .service_now_authentication_method import ServiceNowAuthenticationMethod
        from .service_now_connection_status import ServiceNowConnectionStatus

        from .entity import Entity
        from .service_now_authentication_method import ServiceNowAuthenticationMethod
        from .service_now_connection_status import ServiceNowConnectionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_object_value(ServiceNowAuthenticationMethod)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "incidentApiUrl": lambda n : setattr(self, 'incident_api_url', n.get_str_value()),
            "instanceUrl": lambda n : setattr(self, 'instance_url', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastQueriedDateTime": lambda n : setattr(self, 'last_queried_date_time', n.get_datetime_value()),
            "serviceNowConnectionStatus": lambda n : setattr(self, 'service_now_connection_status', n.get_enum_value(ServiceNowConnectionStatus)),
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
        writer.write_object_value("authenticationMethod", self.authentication_method)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("incidentApiUrl", self.incident_api_url)
        writer.write_str_value("instanceUrl", self.instance_url)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastQueriedDateTime", self.last_queried_date_time)
        writer.write_enum_value("serviceNowConnectionStatus", self.service_now_connection_status)
    

