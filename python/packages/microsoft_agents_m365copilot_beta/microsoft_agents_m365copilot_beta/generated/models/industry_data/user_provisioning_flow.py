from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provisioning_flow import ProvisioningFlow
    from .user_creation_options import UserCreationOptions
    from .user_management_options import UserManagementOptions

from .provisioning_flow import ProvisioningFlow

@dataclass
class UserProvisioningFlow(ProvisioningFlow, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.userProvisioningFlow"
    # A Boolean choice indicating whether unmatched users should be created or ignored.
    create_unmatched_users: Optional[bool] = None
    # The different management choices for the new users to be provisioned.
    creation_options: Optional[UserCreationOptions] = None
    # The managementOptions property
    management_options: Optional[UserManagementOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserProvisioningFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserProvisioningFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserProvisioningFlow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .provisioning_flow import ProvisioningFlow
        from .user_creation_options import UserCreationOptions
        from .user_management_options import UserManagementOptions

        from .provisioning_flow import ProvisioningFlow
        from .user_creation_options import UserCreationOptions
        from .user_management_options import UserManagementOptions

        fields: dict[str, Callable[[Any], None]] = {
            "createUnmatchedUsers": lambda n : setattr(self, 'create_unmatched_users', n.get_bool_value()),
            "creationOptions": lambda n : setattr(self, 'creation_options', n.get_object_value(UserCreationOptions)),
            "managementOptions": lambda n : setattr(self, 'management_options', n.get_object_value(UserManagementOptions)),
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
        writer.write_bool_value("createUnmatchedUsers", self.create_unmatched_users)
        writer.write_object_value("creationOptions", self.creation_options)
        writer.write_object_value("managementOptions", self.management_options)
    

