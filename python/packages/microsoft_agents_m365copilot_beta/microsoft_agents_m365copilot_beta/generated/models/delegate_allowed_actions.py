from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DelegateAllowedActions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the delegator or delegate allows participation in active calls.
    join_active_calls: Optional[bool] = None
    # Indicates whether the delegator or delegate allows calls to be made on their behalf.
    make_calls: Optional[bool] = None
    # Indicates whether the delegator or delegate allows the management of call and delegation settings.
    manage_call_and_delegate_settings: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the delegator or delegate allows held calls to be picked up.
    pick_up_held_calls: Optional[bool] = None
    # Indicates whether the delegator or delegate allows calls to be received on their behalf.
    receive_calls: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegateAllowedActions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegateAllowedActions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegateAllowedActions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "joinActiveCalls": lambda n : setattr(self, 'join_active_calls', n.get_bool_value()),
            "makeCalls": lambda n : setattr(self, 'make_calls', n.get_bool_value()),
            "manageCallAndDelegateSettings": lambda n : setattr(self, 'manage_call_and_delegate_settings', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pickUpHeldCalls": lambda n : setattr(self, 'pick_up_held_calls', n.get_bool_value()),
            "receiveCalls": lambda n : setattr(self, 'receive_calls', n.get_bool_value()),
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
        writer.write_bool_value("joinActiveCalls", self.join_active_calls)
        writer.write_bool_value("makeCalls", self.make_calls)
        writer.write_bool_value("manageCallAndDelegateSettings", self.manage_call_and_delegate_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("pickUpHeldCalls", self.pick_up_held_calls)
        writer.write_bool_value("receiveCalls", self.receive_calls)
        writer.write_additional_data_value(self.additional_data)
    

