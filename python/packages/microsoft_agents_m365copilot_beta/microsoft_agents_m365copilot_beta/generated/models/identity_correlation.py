from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .correlated_identity import CorrelatedIdentity
    from .correlation_error import CorrelationError
    from .entity import Entity
    from .service_principal import ServicePrincipal

from .entity import Entity

@dataclass
class IdentityCorrelation(Entity, Parsable):
    # The date and time when the correlation process completed.
    end_date_time: Optional[datetime.datetime] = None
    # Error information if the correlation process failed. null if successful.  Supports $filter (eq).
    error: Optional[CorrelationError] = None
    # The collection of correlated identity results for this correlation report.
    identities: Optional[list[CorrelatedIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The servicePrincipal property
    service_principal: Optional[ServicePrincipal] = None
    # The date and time when the correlation process started.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityCorrelation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityCorrelation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityCorrelation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .correlated_identity import CorrelatedIdentity
        from .correlation_error import CorrelationError
        from .entity import Entity
        from .service_principal import ServicePrincipal

        from .correlated_identity import CorrelatedIdentity
        from .correlation_error import CorrelationError
        from .entity import Entity
        from .service_principal import ServicePrincipal

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(CorrelationError)),
            "identities": lambda n : setattr(self, 'identities', n.get_collection_of_object_values(CorrelatedIdentity)),
            "servicePrincipal": lambda n : setattr(self, 'service_principal', n.get_object_value(ServicePrincipal)),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("error", self.error)
        writer.write_collection_of_object_values("identities", self.identities)
        writer.write_object_value("servicePrincipal", self.service_principal)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

