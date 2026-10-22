from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_entity import BaseEntity
    from .filtering_profile import FilteringProfile
    from .forwarding_profile import ForwardingProfile
    from .forwarding_profile_base import ForwardingProfileBase
    from .policy_link import PolicyLink
    from .status import Status

from .base_entity import BaseEntity

@dataclass
class Profile(BaseEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.profile"
    # Description.
    description: Optional[str] = None
    # The date and time when the profile was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The traffic forwarding policies associated with this profile.
    policies: Optional[list[PolicyLink]] = None
    # The state property
    state: Optional[Status] = None
    # Profile version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Profile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Profile
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
        return Profile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_entity import BaseEntity
        from .filtering_profile import FilteringProfile
        from .forwarding_profile import ForwardingProfile
        from .forwarding_profile_base import ForwardingProfileBase
        from .policy_link import PolicyLink
        from .status import Status

        from .base_entity import BaseEntity
        from .filtering_profile import FilteringProfile
        from .forwarding_profile import ForwardingProfile
        from .forwarding_profile_base import ForwardingProfileBase
        from .policy_link import PolicyLink
        from .status import Status

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(PolicyLink)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(Status)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    

