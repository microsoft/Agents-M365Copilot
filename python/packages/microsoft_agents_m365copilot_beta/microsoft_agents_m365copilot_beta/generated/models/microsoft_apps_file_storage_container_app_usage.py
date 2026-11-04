from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MicrosoftAppsFileStorageContainerAppUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of active file storage containers for this application.
    active_container_count: Optional[int] = None
    # The storage used in bytes for active file storage containers for this application.
    active_storage_used_in_bytes: Optional[int] = None
    # The unique identifier (GUID) of the Microsoft application.
    app_id: Optional[str] = None
    # The display name of the Microsoft application (for example, Loop, Designer).
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftAppsFileStorageContainerAppUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAppsFileStorageContainerAppUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAppsFileStorageContainerAppUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activeContainerCount": lambda n : setattr(self, 'active_container_count', n.get_int_value()),
            "activeStorageUsedInBytes": lambda n : setattr(self, 'active_storage_used_in_bytes', n.get_int_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

