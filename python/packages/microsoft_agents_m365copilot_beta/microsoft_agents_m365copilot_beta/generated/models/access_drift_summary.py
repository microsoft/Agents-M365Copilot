from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_drift_detail import AccessDriftDetail
    from .access_drift_source import AccessDriftSource
    from .drift_counts import DriftCounts
    from .drift_resource_info import DriftResourceInfo
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessDriftSummary(Entity, Parsable):
    # The date and time when the drift snapshot was created.
    created_date_time: Optional[datetime.datetime] = None
    # The collection of access drift details for this summary.
    details: Optional[list[AccessDriftDetail]] = None
    # The driftCounts property
    drift_counts: Optional[DriftCounts] = None
    # The driftSource property
    drift_source: Optional[AccessDriftSource] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resource property
    resource: Optional[DriftResourceInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessDriftSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessDriftSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessDriftSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_drift_detail import AccessDriftDetail
        from .access_drift_source import AccessDriftSource
        from .drift_counts import DriftCounts
        from .drift_resource_info import DriftResourceInfo
        from .entity import Entity

        from .access_drift_detail import AccessDriftDetail
        from .access_drift_source import AccessDriftSource
        from .drift_counts import DriftCounts
        from .drift_resource_info import DriftResourceInfo
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(AccessDriftDetail)),
            "driftCounts": lambda n : setattr(self, 'drift_counts', n.get_object_value(DriftCounts)),
            "driftSource": lambda n : setattr(self, 'drift_source', n.get_enum_value(AccessDriftSource)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(DriftResourceInfo)),
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
        writer.write_collection_of_object_values("details", self.details)
        writer.write_object_value("driftCounts", self.drift_counts)
        writer.write_enum_value("driftSource", self.drift_source)
        writer.write_object_value("resource", self.resource)
    

