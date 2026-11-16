from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .update_window import UpdateWindow

@dataclass
class HybridAgentUpdaterConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates if updater configuration will be skipped and the agent will receive an update when the next version of the agent is available.
    allow_update_configuration_override: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    defer_update_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time window during which the agent can receive updates.
    update_window: Optional[UpdateWindow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HybridAgentUpdaterConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HybridAgentUpdaterConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HybridAgentUpdaterConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .update_window import UpdateWindow

        from .update_window import UpdateWindow

        fields: dict[str, Callable[[Any], None]] = {
            "allowUpdateConfigurationOverride": lambda n : setattr(self, 'allow_update_configuration_override', n.get_bool_value()),
            "deferUpdateDateTime": lambda n : setattr(self, 'defer_update_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updateWindow": lambda n : setattr(self, 'update_window', n.get_object_value(UpdateWindow)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allowUpdateConfigurationOverride", self.allow_update_configuration_override)
        writer.write_datetime_value("deferUpdateDateTime", self.defer_update_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("updateWindow", self.update_window)
        writer.write_additional_data_value(self.additional_data)
    

