from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .excluded_group_assignment import ExcludedGroupAssignment
    from .included_group_assignment import IncludedGroupAssignment
    from .quality_update_ring import QualityUpdateRing

from ..entity import Entity

@dataclass
class Ring(Entity, Parsable):
    # The date and time when the ring is created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only
    created_date_time: Optional[datetime.datetime] = None
    # The quality update deferral period in days. The value must be between 0 and 30. Optional.
    deferral_in_days: Optional[int] = None
    # The ring description. The maximum length is 1,500 characters. Required
    description: Optional[str] = None
    # The ring display name. The maximum length is 200 characters. Required.
    display_name: Optional[str] = None
    # The excludedGroupAssignment property
    excluded_group_assignment: Optional[ExcludedGroupAssignment] = None
    # The includedGroupAssignment property
    included_group_assignment: Optional[IncludedGroupAssignment] = None
    # The pause action for the quality update ring policy. Required.
    is_paused: Optional[bool] = None
    # The date and time whenthe ring was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Ring:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Ring
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdateRing".casefold():
            from .quality_update_ring import QualityUpdateRing

            return QualityUpdateRing()
        return Ring()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .excluded_group_assignment import ExcludedGroupAssignment
        from .included_group_assignment import IncludedGroupAssignment
        from .quality_update_ring import QualityUpdateRing

        from ..entity import Entity
        from .excluded_group_assignment import ExcludedGroupAssignment
        from .included_group_assignment import IncludedGroupAssignment
        from .quality_update_ring import QualityUpdateRing

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deferralInDays": lambda n : setattr(self, 'deferral_in_days', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "excludedGroupAssignment": lambda n : setattr(self, 'excluded_group_assignment', n.get_object_value(ExcludedGroupAssignment)),
            "includedGroupAssignment": lambda n : setattr(self, 'included_group_assignment', n.get_object_value(IncludedGroupAssignment)),
            "isPaused": lambda n : setattr(self, 'is_paused', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("deferralInDays", self.deferral_in_days)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("excludedGroupAssignment", self.excluded_group_assignment)
        writer.write_object_value("includedGroupAssignment", self.included_group_assignment)
        writer.write_bool_value("isPaused", self.is_paused)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

