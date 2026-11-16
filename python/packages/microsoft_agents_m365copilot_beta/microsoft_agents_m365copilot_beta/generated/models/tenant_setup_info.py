from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privileged_role_settings import PrivilegedRoleSettings
    from .setup_status import SetupStatus

from .entity import Entity

@dataclass
class TenantSetupInfo(Entity, Parsable):
    # The defaultRolesSettings property
    default_roles_settings: Optional[PrivilegedRoleSettings] = None
    # The firstTimeSetup property
    first_time_setup: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relevantRolesSettings property
    relevant_roles_settings: Optional[list[str]] = None
    # The setupStatus property
    setup_status: Optional[SetupStatus] = None
    # The skipSetup property
    skip_setup: Optional[bool] = None
    # The userRolesActions property
    user_roles_actions: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantSetupInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantSetupInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantSetupInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privileged_role_settings import PrivilegedRoleSettings
        from .setup_status import SetupStatus

        from .entity import Entity
        from .privileged_role_settings import PrivilegedRoleSettings
        from .setup_status import SetupStatus

        fields: dict[str, Callable[[Any], None]] = {
            "defaultRolesSettings": lambda n : setattr(self, 'default_roles_settings', n.get_object_value(PrivilegedRoleSettings)),
            "firstTimeSetup": lambda n : setattr(self, 'first_time_setup', n.get_bool_value()),
            "relevantRolesSettings": lambda n : setattr(self, 'relevant_roles_settings', n.get_collection_of_primitive_values(str)),
            "setupStatus": lambda n : setattr(self, 'setup_status', n.get_enum_value(SetupStatus)),
            "skipSetup": lambda n : setattr(self, 'skip_setup', n.get_bool_value()),
            "userRolesActions": lambda n : setattr(self, 'user_roles_actions', n.get_str_value()),
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
        writer.write_object_value("defaultRolesSettings", self.default_roles_settings)
        writer.write_bool_value("firstTimeSetup", self.first_time_setup)
        writer.write_collection_of_primitive_values("relevantRolesSettings", self.relevant_roles_settings)
        writer.write_enum_value("setupStatus", self.setup_status)
        writer.write_bool_value("skipSetup", self.skip_setup)
        writer.write_str_value("userRolesActions", self.user_roles_actions)
    

