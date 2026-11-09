from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .updatable_asset import UpdatableAsset
    from .updatable_asset_error import UpdatableAssetError
    from .update_management_enrollment import UpdateManagementEnrollment

from .updatable_asset import UpdatableAsset

@dataclass
class AzureADDevice(UpdatableAsset, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.azureADDevice"
    # Specifies the update management enrollment for the device. Read-only. Returned by default.
    enrollment: Optional[UpdateManagementEnrollment] = None
    # Specifies any errors that prevent the device from being enrolled in update management or receiving deployed content. Read-only. Returned by default.
    errors: Optional[list[UpdatableAssetError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureADDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureADDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureADDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .updatable_asset import UpdatableAsset
        from .updatable_asset_error import UpdatableAssetError
        from .update_management_enrollment import UpdateManagementEnrollment

        from .updatable_asset import UpdatableAsset
        from .updatable_asset_error import UpdatableAssetError
        from .update_management_enrollment import UpdateManagementEnrollment

        fields: dict[str, Callable[[Any], None]] = {
            "enrollment": lambda n : setattr(self, 'enrollment', n.get_object_value(UpdateManagementEnrollment)),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(UpdatableAssetError)),
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
        writer.write_object_value("enrollment", self.enrollment)
        writer.write_collection_of_object_values("errors", self.errors)
    

