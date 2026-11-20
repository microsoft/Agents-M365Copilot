from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .tenant_contract import TenantContract
    from .tenant_status_information import TenantStatusInformation

from ..entity import Entity

@dataclass
class Tenant(Entity, Parsable):
    # The relationship details for the tenant with the managing entity.
    contract: Optional[TenantContract] = None
    # The date and time the tenant was created in the multi-tenant management platform. Optional. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The display name for the tenant. Required. Read-only.
    display_name: Optional[str] = None
    # The date and time the tenant was last updated within the multi-tenant management platform. Optional. Read-only.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    # The onboarding status information for the tenant. Optional. Read-only.
    tenant_status_information: Optional[TenantStatusInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tenant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tenant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .tenant_contract import TenantContract
        from .tenant_status_information import TenantStatusInformation

        from ..entity import Entity
        from .tenant_contract import TenantContract
        from .tenant_status_information import TenantStatusInformation

        fields: dict[str, Callable[[Any], None]] = {
            "contract": lambda n : setattr(self, 'contract', n.get_object_value(TenantContract)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "tenantStatusInformation": lambda n : setattr(self, 'tenant_status_information', n.get_object_value(TenantStatusInformation)),
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
        writer.write_object_value("contract", self.contract)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("tenantStatusInformation", self.tenant_status_information)
    

