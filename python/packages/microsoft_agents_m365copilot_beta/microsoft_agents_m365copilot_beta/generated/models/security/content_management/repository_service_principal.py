from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RepositoryServicePrincipal(AdditionalDataHolder, Parsable):
    """
    Service principal / managed identity backing a repository connection.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Application (client) id of the identity.
    app_id: Optional[str] = None
    # When the identity's credentials expire.
    credentials_expire_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Object id of the service principal.
    service_principal_id: Optional[str] = None
    # Tenant id that owns the identity.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RepositoryServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RepositoryServicePrincipal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RepositoryServicePrincipal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "credentialsExpireDateTime": lambda n : setattr(self, 'credentials_expire_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_datetime_value("credentialsExpireDateTime", self.credentials_expire_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    

