from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .correlation_error import CorrelationError
    from .entity import Entity
    from .identity_info import IdentityInfo

from .entity import Entity

@dataclass
class CorrelatedIdentity(Entity, Parsable):
    # The date and time when the identity was correlated.  Supports $orderby.
    correlated_date_time: Optional[datetime.datetime] = None
    # Error information if the correlation for this identity failed. null if successful.  Supports $filter (eq).
    error: Optional[CorrelationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source identity information from the on-premises directory.  Supports $filter (eq).
    source_identity: Optional[IdentityInfo] = None
    # The correlation and assignment status. Possible values include: uncorrelated, correlatedNotAssigned, correlatedAssigned and failToCorrelate.  Supports $filter (eq), $count.
    status: Optional[str] = None
    # The target identity information from Microsoft Entra ID.  Supports $filter (eq).
    target_identity: Optional[IdentityInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CorrelatedIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CorrelatedIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CorrelatedIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .correlation_error import CorrelationError
        from .entity import Entity
        from .identity_info import IdentityInfo

        from .correlation_error import CorrelationError
        from .entity import Entity
        from .identity_info import IdentityInfo

        fields: dict[str, Callable[[Any], None]] = {
            "correlatedDateTime": lambda n : setattr(self, 'correlated_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(CorrelationError)),
            "sourceIdentity": lambda n : setattr(self, 'source_identity', n.get_object_value(IdentityInfo)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "targetIdentity": lambda n : setattr(self, 'target_identity', n.get_object_value(IdentityInfo)),
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
        writer.write_datetime_value("correlatedDateTime", self.correlated_date_time)
        writer.write_object_value("error", self.error)
        writer.write_object_value("sourceIdentity", self.source_identity)
        writer.write_str_value("status", self.status)
        writer.write_object_value("targetIdentity", self.target_identity)
    

