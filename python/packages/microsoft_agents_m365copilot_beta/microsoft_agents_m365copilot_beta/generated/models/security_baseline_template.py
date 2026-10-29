from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_template import DeviceManagementTemplate
    from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
    from .security_baseline_device_state import SecurityBaselineDeviceState
    from .security_baseline_state_summary import SecurityBaselineStateSummary

from .device_management_template import DeviceManagementTemplate

@dataclass
class SecurityBaselineTemplate(DeviceManagementTemplate, Parsable):
    """
    The security baseline template of the account
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.securityBaselineTemplate"
    # The security baseline per category device state summary
    category_device_state_summaries: Optional[list[SecurityBaselineCategoryStateSummary]] = None
    # The security baseline device state summary
    device_state_summary: Optional[SecurityBaselineStateSummary] = None
    # The security baseline device states
    device_states: Optional[list[SecurityBaselineDeviceState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_template import DeviceManagementTemplate
        from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
        from .security_baseline_device_state import SecurityBaselineDeviceState
        from .security_baseline_state_summary import SecurityBaselineStateSummary

        from .device_management_template import DeviceManagementTemplate
        from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
        from .security_baseline_device_state import SecurityBaselineDeviceState
        from .security_baseline_state_summary import SecurityBaselineStateSummary

        fields: dict[str, Callable[[Any], None]] = {
            "categoryDeviceStateSummaries": lambda n : setattr(self, 'category_device_state_summaries', n.get_collection_of_object_values(SecurityBaselineCategoryStateSummary)),
            "deviceStateSummary": lambda n : setattr(self, 'device_state_summary', n.get_object_value(SecurityBaselineStateSummary)),
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(SecurityBaselineDeviceState)),
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
        writer.write_collection_of_object_values("categoryDeviceStateSummaries", self.category_device_state_summaries)
        writer.write_object_value("deviceStateSummary", self.device_state_summary)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
    

