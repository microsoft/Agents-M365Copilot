from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsUpdateRolloutSettings(AdditionalDataHolder, Parsable):
    """
    A complex type to store the windows update rollout settings including offer start date time, offer end date time, and days between each set of offers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The feature update's ending  of release date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
    offer_end_date_time_in_u_t_c: Optional[datetime.datetime] = None
    # The number of day(s) between each set of offers to be set, updated, and displayed for a feature update profile, for example: if OfferStartDateTimeInUTC is 2020-06-09T10:00:00Z, and OfferIntervalInDays is 1, then the next two sets of offers will be made consecutively on 2020-06-10T10:00:00Z (next day at the same specified time) and 2020-06-11T10:00:00Z (next next day at the same specified time) with 1 day in between each set of offers.
    offer_interval_in_days: Optional[int] = None
    # The feature update's starting date and time to be set, update, and displayed for a feature Update profile for example: 2020-06-09T10:00:00Z.
    offer_start_date_time_in_u_t_c: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsUpdateRolloutSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateRolloutSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsUpdateRolloutSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offerEndDateTimeInUTC": lambda n : setattr(self, 'offer_end_date_time_in_u_t_c', n.get_datetime_value()),
            "offerIntervalInDays": lambda n : setattr(self, 'offer_interval_in_days', n.get_int_value()),
            "offerStartDateTimeInUTC": lambda n : setattr(self, 'offer_start_date_time_in_u_t_c', n.get_datetime_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("offerEndDateTimeInUTC", self.offer_end_date_time_in_u_t_c)
        writer.write_int_value("offerIntervalInDays", self.offer_interval_in_days)
        writer.write_datetime_value("offerStartDateTimeInUTC", self.offer_start_date_time_in_u_t_c)
        writer.write_additional_data_value(self.additional_data)
    

