from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_file import CopilotFile
    from .copilot_web_context import CopilotWebContext

@dataclass
class CopilotContextualResources(AdditionalDataHolder, Parsable):
    """
    Represents copilot contextual resources parameter.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The files by URI to be used for the request.
    files: Optional[list[CopilotFile]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The web context to be used for the request.
    web_context: Optional[CopilotWebContext] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotContextualResources:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotContextualResources
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotContextualResources()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_file import CopilotFile
        from .copilot_web_context import CopilotWebContext

        from .copilot_file import CopilotFile
        from .copilot_web_context import CopilotWebContext

        fields: dict[str, Callable[[Any], None]] = {
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(CopilotFile)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "webContext": lambda n : setattr(self, 'web_context', n.get_object_value(CopilotWebContext)),
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
        writer.write_collection_of_object_values("files", self.files)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("webContext", self.web_context)
        writer.write_additional_data_value(self.additional_data)
    

