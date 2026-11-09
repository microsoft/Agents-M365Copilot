from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_process_operation_type import Win32LobAppProcessOperationType
    from .win32_lob_app_rule import Win32LobAppRule

from .win32_lob_app_rule import Win32LobAppRule

@dataclass
class Win32LobAppProcessRule(Win32LobAppRule, Parsable):
    """
    A complex type to store process rule data for a Win32 LOB app.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppProcessRule"
    # A list of possible operations for rules used to make determinations about whether an application is in-use based on process state.
    operation_type: Optional[Win32LobAppProcessOperationType] = None
    # Indicates the display name for the process in the Intune admin console. Example: `Microsoft Word`.
    process_display_name: Optional[str] = None
    # Indicates the process name to be searched for on a managed device when enforcing a managed app. Example: `TestApp.exe`.
    process_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppProcessRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppProcessRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppProcessRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_process_operation_type import Win32LobAppProcessOperationType
        from .win32_lob_app_rule import Win32LobAppRule

        from .win32_lob_app_process_operation_type import Win32LobAppProcessOperationType
        from .win32_lob_app_rule import Win32LobAppRule

        fields: dict[str, Callable[[Any], None]] = {
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(Win32LobAppProcessOperationType)),
            "processDisplayName": lambda n : setattr(self, 'process_display_name', n.get_str_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
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
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_str_value("processDisplayName", self.process_display_name)
        writer.write_str_value("processName", self.process_name)
    

