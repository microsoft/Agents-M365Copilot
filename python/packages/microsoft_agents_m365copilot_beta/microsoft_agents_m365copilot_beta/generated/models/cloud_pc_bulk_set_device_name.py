from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_bulk_action import CloudPcBulkAction

from .cloud_pc_bulk_action import CloudPcBulkAction

@dataclass
class CloudPcBulkSetDeviceName(CloudPcBulkAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcBulkSetDeviceName"
    # The template used to generate a unique device name for each Cloud PC. Required when creating the action. Use an optional prefix followed by one %RAND:x% macro, where x is the number of random alphanumeric characters and is at least 5. The generated name must be 5–15 characters long. The prefix can contain ASCII letters, digits, and hyphens, and must not start with a hyphen. The prefix length plus x must not exceed 15. For example, ACRA-%RAND:5% generates a ten-character name such as ACRA-A1B2C.
    device_naming_template: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcBulkSetDeviceName:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkSetDeviceName
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkSetDeviceName()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_bulk_action import CloudPcBulkAction

        from .cloud_pc_bulk_action import CloudPcBulkAction

        fields: dict[str, Callable[[Any], None]] = {
            "deviceNamingTemplate": lambda n : setattr(self, 'device_naming_template', n.get_str_value()),
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
        writer.write_str_value("deviceNamingTemplate", self.device_naming_template)
    

