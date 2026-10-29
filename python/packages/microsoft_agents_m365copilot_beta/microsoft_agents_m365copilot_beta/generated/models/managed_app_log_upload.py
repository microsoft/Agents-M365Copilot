from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_app_log_upload_state import ManagedAppLogUploadState

@dataclass
class ManagedAppLogUpload(AdditionalDataHolder, Parsable):
    """
    A `managedAppLogUpload` represents the log upload result for a given Mobile Application Management (MAM) Logs Uploading Component. Such components can be the application itself, the MAM SDK, and other on-device components that are capable of uploading diagnostic logs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Mobile Application Management (MAM) Logs Uploading Component. Such components can be the application itself, the MAM SDK, and other on-device components that are capable of uploading diagnostic logs. Read-only.
    managed_app_component_description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A provider-specific reference id for the uploaded logs. Read-only.
    reference_id: Optional[str] = None
    # Represents the current status of the associated `managedAppLogCollectionRequest`.
    status: Optional[ManagedAppLogUploadState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppLogUpload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppLogUpload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppLogUpload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_log_upload_state import ManagedAppLogUploadState

        from .managed_app_log_upload_state import ManagedAppLogUploadState

        fields: dict[str, Callable[[Any], None]] = {
            "managedAppComponentDescription": lambda n : setattr(self, 'managed_app_component_description', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referenceId": lambda n : setattr(self, 'reference_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ManagedAppLogUploadState)),
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
        writer.write_str_value("managedAppComponentDescription", self.managed_app_component_description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("referenceId", self.reference_id)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

