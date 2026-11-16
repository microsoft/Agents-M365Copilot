from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UserExperienceSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies the number of days after an update is installed, during which the user of the device can control when the device restarts.
    days_until_forced_reboot: Optional[int] = None
    # Specifies whether the update is offered as a hotpatch. It can only be set to true on automatic policies that target monthly security updates.
    is_hotpatch_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether the update is offered as Optional rather than Required.
    offer_as_optional: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "daysUntilForcedReboot": lambda n : setattr(self, 'days_until_forced_reboot', n.get_int_value()),
            "isHotpatchEnabled": lambda n : setattr(self, 'is_hotpatch_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offerAsOptional": lambda n : setattr(self, 'offer_as_optional', n.get_bool_value()),
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
        writer.write_int_value("daysUntilForcedReboot", self.days_until_forced_reboot)
        writer.write_bool_value("isHotpatchEnabled", self.is_hotpatch_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("offerAsOptional", self.offer_as_optional)
        writer.write_additional_data_value(self.additional_data)
    

