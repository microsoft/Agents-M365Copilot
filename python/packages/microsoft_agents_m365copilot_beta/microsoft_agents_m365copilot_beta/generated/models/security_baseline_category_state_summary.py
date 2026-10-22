from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_baseline_state_summary import SecurityBaselineStateSummary

from .security_baseline_state_summary import SecurityBaselineStateSummary

@dataclass
class SecurityBaselineCategoryStateSummary(SecurityBaselineStateSummary, Parsable):
    """
    The security baseline per category compliance state summary for the security baseline of the account.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.securityBaselineCategoryStateSummary"
    # The category name
    display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineCategoryStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineCategoryStateSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineCategoryStateSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .security_baseline_state_summary import SecurityBaselineStateSummary

        from .security_baseline_state_summary import SecurityBaselineStateSummary

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
    

