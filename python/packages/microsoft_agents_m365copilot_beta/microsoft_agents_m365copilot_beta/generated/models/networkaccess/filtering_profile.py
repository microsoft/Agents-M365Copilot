from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_policy import ConditionalAccessPolicy
    from .profile import Profile

from .profile import Profile

@dataclass
class FilteringProfile(Profile, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.filteringProfile"
    # A set of associated policies defined to regulate access to resources or systems based on specific conditions. Automatically expanded.
    conditional_access_policies: Optional[list[ConditionalAccessPolicy]] = None
    # The date and time when the filteringProfile was created.
    created_date_time: Optional[datetime.datetime] = None
    # The priority used to order the profile for processing within a list.
    priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilteringProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilteringProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilteringProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_policy import ConditionalAccessPolicy
        from .profile import Profile

        from .conditional_access_policy import ConditionalAccessPolicy
        from .profile import Profile

        fields: dict[str, Callable[[Any], None]] = {
            "conditionalAccessPolicies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        writer.write_collection_of_object_values("conditionalAccessPolicies", self.conditional_access_policies)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("priority", self.priority)
    

