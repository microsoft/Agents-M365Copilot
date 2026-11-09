from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_permissions_required import ApplicationPermissionsRequired
    from .entity import Entity
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class CloudAppSecurityProfile(Entity, Parsable):
    # The azureSubscriptionId property
    azure_subscription_id: Optional[str] = None
    # The azureTenantId property
    azure_tenant_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The deploymentPackageUrl property
    deployment_package_url: Optional[str] = None
    # The destinationServiceName property
    destination_service_name: Optional[str] = None
    # The isSigned property
    is_signed: Optional[bool] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The manifest property
    manifest: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsRequired property
    permissions_required: Optional[ApplicationPermissionsRequired] = None
    # The platform property
    platform: Optional[str] = None
    # The policyName property
    policy_name: Optional[str] = None
    # The publisher property
    publisher: Optional[str] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The type property
    type: Optional[str] = None
    # The vendorInformation property
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudAppSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppSecurityProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudAppSecurityProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_permissions_required import ApplicationPermissionsRequired
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation

        from .application_permissions_required import ApplicationPermissionsRequired
        from .entity import Entity
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deploymentPackageUrl": lambda n : setattr(self, 'deployment_package_url', n.get_str_value()),
            "destinationServiceName": lambda n : setattr(self, 'destination_service_name', n.get_str_value()),
            "isSigned": lambda n : setattr(self, 'is_signed', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "manifest": lambda n : setattr(self, 'manifest', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "permissionsRequired": lambda n : setattr(self, 'permissions_required', n.get_enum_value(ApplicationPermissionsRequired)),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deploymentPackageUrl", self.deployment_package_url)
        writer.write_str_value("destinationServiceName", self.destination_service_name)
        writer.write_bool_value("isSigned", self.is_signed)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("manifest", self.manifest)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("permissionsRequired", self.permissions_required)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("type", self.type)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

