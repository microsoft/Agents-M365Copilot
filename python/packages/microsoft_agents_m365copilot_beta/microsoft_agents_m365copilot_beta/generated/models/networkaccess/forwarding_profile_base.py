from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..service_principal import ServicePrincipal
    from .association import Association
    from .forwarding_profile import ForwardingProfile
    from .profile import Profile
    from .traffic_forwarding_type import TrafficForwardingType

from .profile import Profile

@dataclass
class ForwardingProfileBase(Profile, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.forwardingProfileBase"
    # The associations property
    associations: Optional[list[Association]] = None
    # The isCustomProfile property
    is_custom_profile: Optional[bool] = None
    # The priority property
    priority: Optional[int] = None
    # The servicePrincipal property
    service_principal: Optional[ServicePrincipal] = None
    # The trafficForwardingType property
    traffic_forwarding_type: Optional[TrafficForwardingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ForwardingProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ForwardingProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingProfile".casefold():
            from .forwarding_profile import ForwardingProfile

            return ForwardingProfile()
        return ForwardingProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..service_principal import ServicePrincipal
        from .association import Association
        from .forwarding_profile import ForwardingProfile
        from .profile import Profile
        from .traffic_forwarding_type import TrafficForwardingType

        from ..service_principal import ServicePrincipal
        from .association import Association
        from .forwarding_profile import ForwardingProfile
        from .profile import Profile
        from .traffic_forwarding_type import TrafficForwardingType

        fields: dict[str, Callable[[Any], None]] = {
            "associations": lambda n : setattr(self, 'associations', n.get_collection_of_object_values(Association)),
            "isCustomProfile": lambda n : setattr(self, 'is_custom_profile', n.get_bool_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "servicePrincipal": lambda n : setattr(self, 'service_principal', n.get_object_value(ServicePrincipal)),
            "trafficForwardingType": lambda n : setattr(self, 'traffic_forwarding_type', n.get_enum_value(TrafficForwardingType)),
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
        writer.write_collection_of_object_values("associations", self.associations)
        writer.write_bool_value("isCustomProfile", self.is_custom_profile)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("servicePrincipal", self.service_principal)
        writer.write_enum_value("trafficForwardingType", self.traffic_forwarding_type)
    

