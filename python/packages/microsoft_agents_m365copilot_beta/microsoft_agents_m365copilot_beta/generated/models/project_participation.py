from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_detail import CompanyDetail
    from .item_facet import ItemFacet
    from .position_detail import PositionDetail
    from .related_person import RelatedPerson

from .item_facet import ItemFacet

@dataclass
class ProjectParticipation(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.projectParticipation"
    # Contains categories a user has associated with the project (for example, digital transformation, oil rig).
    categories: Optional[list[str]] = None
    # Contains detailed information about the client the project was for.
    client: Optional[CompanyDetail] = None
    # Contains experience scenario tags a user has associated with the interest. Allowed values in the collection are: askMeAbout, ableToMentor, wantsToLearn, wantsToImprove.
    collaboration_tags: Optional[list[str]] = None
    # Lists people that also worked on the project.
    colleagues: Optional[list[RelatedPerson]] = None
    # Contains detail about the user's role on the project.
    detail: Optional[PositionDetail] = None
    # Contains a friendly name for the project.
    display_name: Optional[str] = None
    # The Person or people who sponsored the project.
    sponsors: Optional[list[RelatedPerson]] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProjectParticipation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProjectParticipation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProjectParticipation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .company_detail import CompanyDetail
        from .item_facet import ItemFacet
        from .position_detail import PositionDetail
        from .related_person import RelatedPerson

        from .company_detail import CompanyDetail
        from .item_facet import ItemFacet
        from .position_detail import PositionDetail
        from .related_person import RelatedPerson

        fields: dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "client": lambda n : setattr(self, 'client', n.get_object_value(CompanyDetail)),
            "collaborationTags": lambda n : setattr(self, 'collaboration_tags', n.get_collection_of_primitive_values(str)),
            "colleagues": lambda n : setattr(self, 'colleagues', n.get_collection_of_object_values(RelatedPerson)),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(PositionDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "sponsors": lambda n : setattr(self, 'sponsors', n.get_collection_of_object_values(RelatedPerson)),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_object_value("client", self.client)
        writer.write_collection_of_primitive_values("collaborationTags", self.collaboration_tags)
        writer.write_collection_of_object_values("colleagues", self.colleagues)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
    

