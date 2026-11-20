from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Win32LobAppInUseSettings(AdditionalDataHolder, Parsable):
    """
    Contains in-use deferral and prompt countdown settings for Required and Available Win32 app installation assignments. These settings apply only when the app's `installExperience.inUseBehavior` is `terminateWithUserInteraction`. They are not supported for Uninstall assignments.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the prompt countdown duration in minutes before installation is enforced. For Required assignments, the countdown starts after the final deferral and valid values are 1 to 240 (4 hours). Available assignments require a fixed value of 5.
    countdown_minutes: Optional[int] = None
    # Indicates the duration in minutes between deferral attempts. For Required assignments, valid values are 1 to 1440 (24 hours). Available assignments require 1 as a fixed placeholder because deferrals are not supported.
    minutes_between_deferrals: Optional[int] = None
    # Indicates the maximum number of times the user can defer installation. For Required assignments, valid values are 0 to 5. Available assignments require 0.
    number_of_deferrals: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppInUseSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppInUseSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppInUseSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "countdownMinutes": lambda n : setattr(self, 'countdown_minutes', n.get_int_value()),
            "minutesBetweenDeferrals": lambda n : setattr(self, 'minutes_between_deferrals', n.get_int_value()),
            "numberOfDeferrals": lambda n : setattr(self, 'number_of_deferrals', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("countdownMinutes", self.countdown_minutes)
        writer.write_int_value("minutesBetweenDeferrals", self.minutes_between_deferrals)
        writer.write_int_value("numberOfDeferrals", self.number_of_deferrals)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

