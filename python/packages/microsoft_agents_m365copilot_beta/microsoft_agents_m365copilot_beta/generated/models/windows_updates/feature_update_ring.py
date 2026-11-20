from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ring import Ring

from .ring import Ring

@dataclass
class FeatureUpdateRing(Ring, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.featureUpdateRing"
    # Indicates whether the feature update is offered to end users as optional rather than required. Default is false.
    is_offer_optional: Optional[bool] = None
    # The total length of the gradual-rollout window, in days, from when the update is first offered to when the rollout completes. The minimum is 1. Only used when offerIntervalInDays is 1 or greater; ignored when offerIntervalInDays is 0. Default is 1.
    offer_duration_in_days: Optional[int] = None
    # How often, in days, a new subset of devices is offered the update. Accepted range is 0 to 30. Set to 0 to offer the update to all devices at once. When the value is 1 or greater, the rollout advances one subset at each interval until every device has been offered the update. Must be less than or equal to offerDurationInDays. Default is 0.
    offer_interval_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeatureUpdateRing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeatureUpdateRing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeatureUpdateRing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ring import Ring

        from .ring import Ring

        fields: dict[str, Callable[[Any], None]] = {
            "isOfferOptional": lambda n : setattr(self, 'is_offer_optional', n.get_bool_value()),
            "offerDurationInDays": lambda n : setattr(self, 'offer_duration_in_days', n.get_int_value()),
            "offerIntervalInDays": lambda n : setattr(self, 'offer_interval_in_days', n.get_int_value()),
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
        writer.write_bool_value("isOfferOptional", self.is_offer_optional)
        writer.write_int_value("offerDurationInDays", self.offer_duration_in_days)
        writer.write_int_value("offerIntervalInDays", self.offer_interval_in_days)
    

