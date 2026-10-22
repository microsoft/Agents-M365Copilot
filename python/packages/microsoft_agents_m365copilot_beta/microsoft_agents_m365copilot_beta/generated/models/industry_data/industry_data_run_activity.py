from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..public_error import PublicError
    from .inbound_flow_activity import InboundFlowActivity
    from .industry_data_activity import IndustryDataActivity
    from .industry_data_activity_status import IndustryDataActivityStatus
    from .outbound_flow_activity import OutboundFlowActivity

from ..entity import Entity

@dataclass
class IndustryDataRunActivity(Entity, Parsable):
    # The flow that was run by this activity.
    activity: Optional[IndustryDataActivity] = None
    # An error object to diagnose critical failures in an activity.
    blocking_error: Optional[PublicError] = None
    # The name of the running flow.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[IndustryDataActivityStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IndustryDataRunActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRunActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.inboundFlowActivity".casefold():
            from .inbound_flow_activity import InboundFlowActivity

            return InboundFlowActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.outboundFlowActivity".casefold():
            from .outbound_flow_activity import OutboundFlowActivity

            return OutboundFlowActivity()
        return IndustryDataRunActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..public_error import PublicError
        from .inbound_flow_activity import InboundFlowActivity
        from .industry_data_activity import IndustryDataActivity
        from .industry_data_activity_status import IndustryDataActivityStatus
        from .outbound_flow_activity import OutboundFlowActivity

        from ..entity import Entity
        from ..public_error import PublicError
        from .inbound_flow_activity import InboundFlowActivity
        from .industry_data_activity import IndustryDataActivity
        from .industry_data_activity_status import IndustryDataActivityStatus
        from .outbound_flow_activity import OutboundFlowActivity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(IndustryDataActivity)),
            "blockingError": lambda n : setattr(self, 'blocking_error', n.get_object_value(PublicError)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(IndustryDataActivityStatus)),
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
        writer.write_object_value("activity", self.activity)
        writer.write_enum_value("status", self.status)
    

