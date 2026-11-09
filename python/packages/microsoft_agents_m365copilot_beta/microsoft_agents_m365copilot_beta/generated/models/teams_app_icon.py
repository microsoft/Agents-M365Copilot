from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teamwork_hosted_content import TeamworkHostedContent

from .entity import Entity

@dataclass
class TeamsAppIcon(Entity, Parsable):
    # The contents of the app icon if the icon is hosted within the Teams infrastructure.
    hosted_content: Optional[TeamworkHostedContent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The web URL that can be used for downloading the image.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppIcon:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppIcon
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppIcon()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teamwork_hosted_content import TeamworkHostedContent

        from .entity import Entity
        from .teamwork_hosted_content import TeamworkHostedContent

        fields: dict[str, Callable[[Any], None]] = {
            "hostedContent": lambda n : setattr(self, 'hosted_content', n.get_object_value(TeamworkHostedContent)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_object_value("hostedContent", self.hosted_content)
        writer.write_str_value("webUrl", self.web_url)
    

