from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .security_vendor_information import SecurityVendorInformation
    from .user_account import UserAccount

from .entity import Entity

@dataclass
class UserSecurityProfile(Entity, Parsable):
    # The accounts property
    accounts: Optional[list[UserAccount]] = None
    # The azureSubscriptionId property
    azure_subscription_id: Optional[str] = None
    # The azureTenantId property
    azure_tenant_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    # The vendorInformation property
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSecurityProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSecurityProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation
        from .user_account import UserAccount

        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation
        from .user_account import UserAccount

        fields: dict[str, Callable[[Any], None]] = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(UserAccount)),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
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
        writer.write_collection_of_object_values("accounts", self.accounts)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

