from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_state import AlertState
    from .alert_type import AlertType
    from .category import Category
    from .documentation import Documentation
    from .enrichment import Enrichment
    from .scenario import Scenario
    from .signals import Signals

from ..entity import Entity

@dataclass
class Alert(Entity, Parsable):
    # The alertType property
    alert_type: Optional[AlertType] = None
    # The category property
    category: Optional[Category] = None
    # The time when Microsoft Entra Health monitoring generated the alert. Supports $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # A key-value pair that contains the name of and link to the documentation to aid in investigation of the alert.
    documentation: Optional[Documentation] = None
    # Investigative information on the alert. This information typically includes counts of impacted objects, which include directory objects such as users, groups, and devices, and a pointer to supporting data.
    enrichment: Optional[Enrichment] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scenario property
    scenario: Optional[Scenario] = None
    # The collection of signals that were used in the generation of the alert. These signals are sourced from serviceActivity APIs and are added to the alert as key-value pairs.
    signals: Optional[Signals] = None
    # The state property
    state: Optional[AlertState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Alert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_state import AlertState
        from .alert_type import AlertType
        from .category import Category
        from .documentation import Documentation
        from .enrichment import Enrichment
        from .scenario import Scenario
        from .signals import Signals

        from ..entity import Entity
        from .alert_state import AlertState
        from .alert_type import AlertType
        from .category import Category
        from .documentation import Documentation
        from .enrichment import Enrichment
        from .scenario import Scenario
        from .signals import Signals

        fields: dict[str, Callable[[Any], None]] = {
            "alertType": lambda n : setattr(self, 'alert_type', n.get_enum_value(AlertType)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(Category)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "documentation": lambda n : setattr(self, 'documentation', n.get_object_value(Documentation)),
            "enrichment": lambda n : setattr(self, 'enrichment', n.get_object_value(Enrichment)),
            "scenario": lambda n : setattr(self, 'scenario', n.get_enum_value(Scenario)),
            "signals": lambda n : setattr(self, 'signals', n.get_object_value(Signals)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AlertState)),
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
        writer.write_enum_value("alertType", self.alert_type)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("documentation", self.documentation)
        writer.write_object_value("enrichment", self.enrichment)
        writer.write_enum_value("scenario", self.scenario)
        writer.write_object_value("signals", self.signals)
        writer.write_enum_value("state", self.state)
    

