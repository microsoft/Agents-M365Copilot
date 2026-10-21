from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
    from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense

from .entity import Entity

@dataclass
class IosVppAppAssignedLicense(Entity, Parsable):
    """
    iOS Volume Purchase Program license assignment. This class does not support Create, Delete, or Update.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The user email address.
    user_email_address: Optional[str] = None
    # The user ID.
    user_id: Optional[str] = None
    # The user name.
    user_name: Optional[str] = None
    # The user principal name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosVppAppAssignedLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignedLicense
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppAppAssignedDeviceLicense".casefold():
            from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense

            return IosVppAppAssignedDeviceLicense()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppAppAssignedUserLicense".casefold():
            from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense

            return IosVppAppAssignedUserLicense()
        return IosVppAppAssignedLicense()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
        from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense

        from .entity import Entity
        from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
        from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense

        fields: dict[str, Callable[[Any], None]] = {
            "userEmailAddress": lambda n : setattr(self, 'user_email_address', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("userEmailAddress", self.user_email_address)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

