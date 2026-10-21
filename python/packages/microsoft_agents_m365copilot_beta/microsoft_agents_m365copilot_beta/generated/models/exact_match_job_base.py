from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_error import ClassificationError
    from .entity import Entity
    from .exact_match_lookup_job import ExactMatchLookupJob
    from .exact_match_session import ExactMatchSession
    from .exact_match_session_base import ExactMatchSessionBase

from .entity import Entity

@dataclass
class ExactMatchJobBase(Entity, Parsable):
    # The completionDateTime property
    completion_date_time: Optional[datetime.datetime] = None
    # The creationDateTime property
    creation_date_time: Optional[datetime.datetime] = None
    # The error property
    error: Optional[ClassificationError] = None
    # The lastUpdatedDateTime property
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExactMatchJobBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchJobBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchLookupJob".casefold():
            from .exact_match_lookup_job import ExactMatchLookupJob

            return ExactMatchLookupJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchSession".casefold():
            from .exact_match_session import ExactMatchSession

            return ExactMatchSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchSessionBase".casefold():
            from .exact_match_session_base import ExactMatchSessionBase

            return ExactMatchSessionBase()
        return ExactMatchJobBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classification_error import ClassificationError
        from .entity import Entity
        from .exact_match_lookup_job import ExactMatchLookupJob
        from .exact_match_session import ExactMatchSession
        from .exact_match_session_base import ExactMatchSessionBase

        from .classification_error import ClassificationError
        from .entity import Entity
        from .exact_match_lookup_job import ExactMatchLookupJob
        from .exact_match_session import ExactMatchSession
        from .exact_match_session_base import ExactMatchSessionBase

        fields: dict[str, Callable[[Any], None]] = {
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(ClassificationError)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

