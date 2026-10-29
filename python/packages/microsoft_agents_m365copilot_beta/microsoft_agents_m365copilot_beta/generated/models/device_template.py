from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device import Device
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class DeviceTemplate(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceTemplate"
    # A tenant-defined name for the party that's responsible for provisioning and managing devices on the Microsoft Entra tenant. For example, Tailwind Traders (the manufacturer) makes security cameras that are installed in customer buildings and managed by Lakeshore Retail (the device authority). This value is provided to the customer by the device authority (manufacturer or reseller).
    device_authority: Optional[str] = None
    # Collection of device objects created based on this template.
    device_instances: Optional[list[Device]] = None
    # Manufacturer name.
    manufacturer: Optional[str] = None
    # Model name.
    model: Optional[str] = None
    # Object ID of the mutualTlsOauthConfiguration. This value isn't required if self-signed certificates are used. This value is provided to the customer by the device authority (manufacturer or reseller).
    mutual_tls_oauth_configuration_id: Optional[str] = None
    # ID (tenant ID for device authority) of the tenant that contains the mutualTlsOauthConfiguration. This value isn't required if self-signed certificates are used. This value is provided to the customer by the device authority (manufacturer or reseller).
    mutual_tls_oauth_configuration_tenant_id: Optional[str] = None
    # Operating system type. Supports $filter (eq, in).
    operating_system: Optional[str] = None
    # Collection of directory objects that can manage the device template and the related deviceInstances. Owners can be represented as service principals, users, or applications. An owner has full privileges over the device template and doesn't require other administrator roles to create, update, or delete devices from this template, as well as to add or remove template owners. There can be a maximum of 100 owners on a device template.  Supports $expand.
    owners: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device import Device
        from .directory_object import DirectoryObject

        from .device import Device
        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "deviceAuthority": lambda n : setattr(self, 'device_authority', n.get_str_value()),
            "deviceInstances": lambda n : setattr(self, 'device_instances', n.get_collection_of_object_values(Device)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "mutualTlsOauthConfigurationId": lambda n : setattr(self, 'mutual_tls_oauth_configuration_id', n.get_str_value()),
            "mutualTlsOauthConfigurationTenantId": lambda n : setattr(self, 'mutual_tls_oauth_configuration_tenant_id', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_str_value("deviceAuthority", self.device_authority)
        writer.write_collection_of_object_values("deviceInstances", self.device_instances)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("mutualTlsOauthConfigurationId", self.mutual_tls_oauth_configuration_id)
        writer.write_str_value("mutualTlsOauthConfigurationTenantId", self.mutual_tls_oauth_configuration_tenant_id)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_collection_of_object_values("owners", self.owners)
    

