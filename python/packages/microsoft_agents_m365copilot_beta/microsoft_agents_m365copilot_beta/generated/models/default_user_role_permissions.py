from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DefaultUserRolePermissions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the default user role can create applications. This setting corresponds to the Users can register applications setting in the User settings menu in the Microsoft Entra admin center.
    allowed_to_create_apps: Optional[bool] = None
    # Indicates whether the default user role can create security groups. This setting corresponds to the following menus in the Microsoft Entra admin center:  The Users can create security groups in Microsoft Entra admin centers, API or PowerShell setting in the Group settings menu.  Users can create security groups setting in the User settings menu.
    allowed_to_create_security_groups: Optional[bool] = None
    # Indicates whether the default user role can create tenants. This setting corresponds to the Restrict non-admin users from creating tenants setting in the User settings menu in the Microsoft Entra admin center. When this setting is false, users assigned the Tenant Creator role can still create tenants.
    allowed_to_create_tenants: Optional[bool] = None
    # Indicates whether the registered owners of a device can read their own BitLocker recovery keys with default user role.
    allowed_to_read_bitlocker_keys_for_owned_device: Optional[bool] = None
    # Indicates whether the default user role can read other users. DO NOT SET THIS VALUE TO false.
    allowed_to_read_other_users: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DefaultUserRolePermissions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultUserRolePermissions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DefaultUserRolePermissions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowedToCreateApps": lambda n : setattr(self, 'allowed_to_create_apps', n.get_bool_value()),
            "allowedToCreateSecurityGroups": lambda n : setattr(self, 'allowed_to_create_security_groups', n.get_bool_value()),
            "allowedToCreateTenants": lambda n : setattr(self, 'allowed_to_create_tenants', n.get_bool_value()),
            "allowedToReadBitlockerKeysForOwnedDevice": lambda n : setattr(self, 'allowed_to_read_bitlocker_keys_for_owned_device', n.get_bool_value()),
            "allowedToReadOtherUsers": lambda n : setattr(self, 'allowed_to_read_other_users', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("allowedToCreateApps", self.allowed_to_create_apps)
        writer.write_bool_value("allowedToCreateSecurityGroups", self.allowed_to_create_security_groups)
        writer.write_bool_value("allowedToCreateTenants", self.allowed_to_create_tenants)
        writer.write_bool_value("allowedToReadBitlockerKeysForOwnedDevice", self.allowed_to_read_bitlocker_keys_for_owned_device)
        writer.write_bool_value("allowedToReadOtherUsers", self.allowed_to_read_other_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

