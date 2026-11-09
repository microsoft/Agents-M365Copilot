from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .storyline_follower import StorylineFollower
    from .storyline_following import StorylineFollowing

from .entity import Entity

@dataclass
class Storyline(Entity, Parsable):
    """
    User's storyline singleton container.
    """
    # The users who are following this user.
    followers: Optional[list[StorylineFollower]] = None
    # The users that this user is following.
    followings: Optional[list[StorylineFollowing]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Storyline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Storyline
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Storyline()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .storyline_follower import StorylineFollower
        from .storyline_following import StorylineFollowing

        from .entity import Entity
        from .storyline_follower import StorylineFollower
        from .storyline_following import StorylineFollowing

        fields: dict[str, Callable[[Any], None]] = {
            "followers": lambda n : setattr(self, 'followers', n.get_collection_of_object_values(StorylineFollower)),
            "followings": lambda n : setattr(self, 'followings', n.get_collection_of_object_values(StorylineFollowing)),
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
        writer.write_collection_of_object_values("followers", self.followers)
        writer.write_collection_of_object_values("followings", self.followings)
    

