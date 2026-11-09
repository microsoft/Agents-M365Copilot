from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_intent_and_state_detail import MobileAppIntentAndStateDetail

from .entity import Entity

@dataclass
class MobileAppIntentAndState(Entity, Parsable):
    """
    MobileApp Intent and Install State for a given device.
    """
    # Device identifier created or collected by Intune.
    managed_device_identifier: Optional[str] = None
    # The list of payload intents and states for the tenant.
    mobile_app_list: Optional[list[MobileAppIntentAndStateDetail]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier for the user that tried to enroll the device.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppIntentAndState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppIntentAndState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppIntentAndState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_intent_and_state_detail import MobileAppIntentAndStateDetail

        from .entity import Entity
        from .mobile_app_intent_and_state_detail import MobileAppIntentAndStateDetail

        fields: dict[str, Callable[[Any], None]] = {
            "managedDeviceIdentifier": lambda n : setattr(self, 'managed_device_identifier', n.get_str_value()),
            "mobileAppList": lambda n : setattr(self, 'mobile_app_list', n.get_collection_of_object_values(MobileAppIntentAndStateDetail)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("managedDeviceIdentifier", self.managed_device_identifier)
        writer.write_collection_of_object_values("mobileAppList", self.mobile_app_list)
        writer.write_str_value("userId", self.user_id)
    

