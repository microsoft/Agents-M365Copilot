from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_detection import Win32LobAppDetection

from .win32_lob_app_detection import Win32LobAppDetection

@dataclass
class Win32LobAppPowerShellScriptDetection(Win32LobAppDetection, Parsable):
    """
    Contains PowerShell script properties to detect a Win32 App
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppPowerShellScriptDetection"
    # A value indicating whether signature check is enforced
    enforce_signature_check: Optional[bool] = None
    # A value indicating whether this script should run as 32-bit
    run_as32_bit: Optional[bool] = None
    # The base64 encoded script content to detect Win32 Line of Business (LoB) app
    script_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppPowerShellScriptDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppPowerShellScriptDetection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppPowerShellScriptDetection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_detection import Win32LobAppDetection

        from .win32_lob_app_detection import Win32LobAppDetection

        fields: dict[str, Callable[[Any], None]] = {
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "scriptContent": lambda n : setattr(self, 'script_content', n.get_str_value()),
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
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_str_value("scriptContent", self.script_content)
    

