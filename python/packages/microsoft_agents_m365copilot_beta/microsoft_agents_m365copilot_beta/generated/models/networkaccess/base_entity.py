from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .filtering_profile import FilteringProfile
    from .forwarding_profile import ForwardingProfile
    from .forwarding_profile_base import ForwardingProfileBase
    from .profile import Profile
    from .remote_network import RemoteNetwork

from ..entity import Entity

@dataclass
class BaseEntity(Entity, Parsable):
    # Name of the entity
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BaseEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringProfile".casefold():
            from .filtering_profile import FilteringProfile

            return FilteringProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingProfile".casefold():
            from .forwarding_profile import ForwardingProfile

            return ForwardingProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingProfileBase".casefold():
            from .forwarding_profile_base import ForwardingProfileBase

            return ForwardingProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.profile".casefold():
            from .profile import Profile

            return Profile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.remoteNetwork".casefold():
            from .remote_network import RemoteNetwork

            return RemoteNetwork()
        return BaseEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .filtering_profile import FilteringProfile
        from .forwarding_profile import ForwardingProfile
        from .forwarding_profile_base import ForwardingProfileBase
        from .profile import Profile
        from .remote_network import RemoteNetwork

        from ..entity import Entity
        from .filtering_profile import FilteringProfile
        from .forwarding_profile import ForwardingProfile
        from .forwarding_profile_base import ForwardingProfileBase
        from .profile import Profile
        from .remote_network import RemoteNetwork

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
    

