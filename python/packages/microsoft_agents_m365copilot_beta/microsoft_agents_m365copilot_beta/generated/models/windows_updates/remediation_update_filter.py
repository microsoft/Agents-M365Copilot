from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .remediation_type import RemediationType
    from .windows_update_filter import WindowsUpdateFilter

from .windows_update_filter import WindowsUpdateFilter

@dataclass
class RemediationUpdateFilter(WindowsUpdateFilter, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.remediationUpdateFilter"
    # The remediationType property
    remediation_type: Optional[RemediationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemediationUpdateFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemediationUpdateFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemediationUpdateFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .remediation_type import RemediationType
        from .windows_update_filter import WindowsUpdateFilter

        from .remediation_type import RemediationType
        from .windows_update_filter import WindowsUpdateFilter

        fields: dict[str, Callable[[Any], None]] = {
            "remediationType": lambda n : setattr(self, 'remediation_type', n.get_enum_value(RemediationType)),
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
        writer.write_enum_value("remediationType", self.remediation_type)
    

