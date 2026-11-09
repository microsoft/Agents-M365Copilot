from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enforcement_result_status import EnforcementResultStatus
    from .process_content_metadata_base import ProcessContentMetadataBase

from .process_content_metadata_base import ProcessContentMetadataBase

@dataclass
class ContentActivityMetadata(ProcessContentMetadataBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.contentActivityMetadata"
    # The enforcementResultStatus property
    enforcement_result_status: Optional[EnforcementResultStatus] = None
    # The recordType property
    record_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentActivityMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentActivityMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentActivityMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enforcement_result_status import EnforcementResultStatus
        from .process_content_metadata_base import ProcessContentMetadataBase

        from .enforcement_result_status import EnforcementResultStatus
        from .process_content_metadata_base import ProcessContentMetadataBase

        fields: dict[str, Callable[[Any], None]] = {
            "enforcementResultStatus": lambda n : setattr(self, 'enforcement_result_status', n.get_enum_value(EnforcementResultStatus)),
            "recordType": lambda n : setattr(self, 'record_type', n.get_str_value()),
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
        writer.write_enum_value("enforcementResultStatus", self.enforcement_result_status)
        writer.write_str_value("recordType", self.record_type)
    

