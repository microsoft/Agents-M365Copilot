from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .knowledge_base_article import KnowledgeBaseArticle
    from .known_issue_history_item import KnownIssueHistoryItem
    from .windows_release_health_status import WindowsReleaseHealthStatus

from ..entity import Entity

@dataclass
class KnownIssue(Entity, Parsable):
    # The description of the particular known issue.
    description: Optional[str] = None
    # The knownIssueHistories property
    known_issue_histories: Optional[list[KnownIssueHistoryItem]] = None
    # The date and time when the known issue was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Knowledge base article associated with the release when the known issue was first reported.
    originating_knowledge_base_article: Optional[KnowledgeBaseArticle] = None
    # The date and time when the known issue was resolved or mitigated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    resolved_date_time: Optional[datetime.datetime] = None
    # Knowledge base article associated with the release when the known issue was resolved or mitigated.
    resolving_knowledge_base_article: Optional[KnowledgeBaseArticle] = None
    # The safeguardHoldIds property
    safeguard_hold_ids: Optional[list[int]] = None
    # The date and time when the known issue was first reported. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[WindowsReleaseHealthStatus] = None
    # The title of the known issue.
    title: Optional[str] = None
    # The URL to the known issue in the Windows Release Health dashboard on Microsoft 365 admin center.
    web_view_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KnownIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KnownIssue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KnownIssue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .knowledge_base_article import KnowledgeBaseArticle
        from .known_issue_history_item import KnownIssueHistoryItem
        from .windows_release_health_status import WindowsReleaseHealthStatus

        from ..entity import Entity
        from .knowledge_base_article import KnowledgeBaseArticle
        from .known_issue_history_item import KnownIssueHistoryItem
        from .windows_release_health_status import WindowsReleaseHealthStatus

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "knownIssueHistories": lambda n : setattr(self, 'known_issue_histories', n.get_collection_of_object_values(KnownIssueHistoryItem)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "originatingKnowledgeBaseArticle": lambda n : setattr(self, 'originating_knowledge_base_article', n.get_object_value(KnowledgeBaseArticle)),
            "resolvedDateTime": lambda n : setattr(self, 'resolved_date_time', n.get_datetime_value()),
            "resolvingKnowledgeBaseArticle": lambda n : setattr(self, 'resolving_knowledge_base_article', n.get_object_value(KnowledgeBaseArticle)),
            "safeguardHoldIds": lambda n : setattr(self, 'safeguard_hold_ids', n.get_collection_of_primitive_values(int)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(WindowsReleaseHealthStatus)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "webViewUrl": lambda n : setattr(self, 'web_view_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("knownIssueHistories", self.known_issue_histories)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("originatingKnowledgeBaseArticle", self.originating_knowledge_base_article)
        writer.write_datetime_value("resolvedDateTime", self.resolved_date_time)
        writer.write_object_value("resolvingKnowledgeBaseArticle", self.resolving_knowledge_base_article)
        writer.write_collection_of_primitive_values("safeguardHoldIds", self.safeguard_hold_ids)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_str_value("webViewUrl", self.web_view_url)
    

