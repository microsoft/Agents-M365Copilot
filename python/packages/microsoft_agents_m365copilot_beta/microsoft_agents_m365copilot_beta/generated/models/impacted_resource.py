from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .key_value import KeyValue
    from .recommendation_status import RecommendationStatus
    from .recommendation_tag import RecommendationTag

from .entity import Entity

@dataclass
class ImpactedResource(Entity, Parsable):
    # The date and time when the impactedResource object was initially associated with the recommendation.
    added_date_time: Optional[datetime.datetime] = None
    # Additional information unique to the impactedResource to help contextualize the recommendation.
    additional_details: Optional[list[KeyValue]] = None
    # The URL link to the corresponding Microsoft Entra resource.
    api_url: Optional[str] = None
    # Friendly name of the Microsoft Entra resource.
    display_name: Optional[str] = None
    # Name of the user or service that last updated the status.
    last_modified_by: Optional[str] = None
    # The date and time when the status was last updated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user responsible for maintaining the resource.
    owner: Optional[str] = None
    # The URL link to the corresponding Microsoft Entra admin center page of the resource.
    portal_url: Optional[str] = None
    # The future date and time when the status of a postponed impactedResource will be active again.
    postpone_until_date_time: Optional[datetime.datetime] = None
    # Indicates the importance of the resource. A resource with a rank equal to 1 is of the highest importance.
    rank: Optional[int] = None
    # The unique identifier of the recommendation that the resource is associated with.
    recommendation_id: Optional[str] = None
    # Indicates the type of Microsoft Entra resource. Examples include user, application.
    resource_type: Optional[str] = None
    # The status property
    status: Optional[RecommendationStatus] = None
    # The related unique identifier, depending on the resourceType. For example, this property is set to the applicationId if the resourceType is an application.
    subject_id: Optional[str] = None
    # The user-defined free-form labels applied to the impactedResource. The collection isn't directly writable; tags are created and removed through the addTag and removeTag actions.
    tags: Optional[list[RecommendationTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImpactedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImpactedResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImpactedResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .key_value import KeyValue
        from .recommendation_status import RecommendationStatus
        from .recommendation_tag import RecommendationTag

        from .entity import Entity
        from .key_value import KeyValue
        from .recommendation_status import RecommendationStatus
        from .recommendation_tag import RecommendationTag

        fields: dict[str, Callable[[Any], None]] = {
            "addedDateTime": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(KeyValue)),
            "apiUrl": lambda n : setattr(self, 'api_url', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "portalUrl": lambda n : setattr(self, 'portal_url', n.get_str_value()),
            "postponeUntilDateTime": lambda n : setattr(self, 'postpone_until_date_time', n.get_datetime_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "recommendationId": lambda n : setattr(self, 'recommendation_id', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RecommendationStatus)),
            "subjectId": lambda n : setattr(self, 'subject_id', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(RecommendationTag)),
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
        writer.write_datetime_value("addedDateTime", self.added_date_time)
        writer.write_collection_of_object_values("additionalDetails", self.additional_details)
        writer.write_str_value("apiUrl", self.api_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("portalUrl", self.portal_url)
        writer.write_datetime_value("postponeUntilDateTime", self.postpone_until_date_time)
        writer.write_int_value("rank", self.rank)
        writer.write_str_value("recommendationId", self.recommendation_id)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subjectId", self.subject_id)
        writer.write_collection_of_object_values("tags", self.tags)
    

