from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

@dataclass
class SequentialActivationRenewalsAlertConfiguration(UnifiedRoleManagementAlertConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration"
    # The minimum number of activations within the timeIntervalBetweenActivations period to trigger an alert.
    sequential_activation_counter_threshold: Optional[int] = None
    # Time interval between activations to trigger an alert.
    time_interval_between_activations: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SequentialActivationRenewalsAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SequentialActivationRenewalsAlertConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SequentialActivationRenewalsAlertConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "sequentialActivationCounterThreshold": lambda n : setattr(self, 'sequential_activation_counter_threshold', n.get_int_value()),
            "timeIntervalBetweenActivations": lambda n : setattr(self, 'time_interval_between_activations', n.get_timedelta_value()),
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
        writer.write_int_value("sequentialActivationCounterThreshold", self.sequential_activation_counter_threshold)
        writer.write_timedelta_value("timeIntervalBetweenActivations", self.time_interval_between_activations)
    

