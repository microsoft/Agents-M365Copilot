from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .mdm_app_setting import MdmAppSetting

from ..entity import Entity

@dataclass
class TenantSetting(Entity, Parsable):
    """
    Tenant-level settings singleton for Windows Autopatch updates. Each tenant has at most one resource; a missing resource means all defaults apply.
    """
    # Whether Data Processor Service for Windows (DPSW) features are enabled for this tenant. The default is false.
    are_data_processor_service_for_windows_features_enabled: Optional[bool] = None
    # The per-MDM-application settings for the current tenant.
    mdm_app_settings: Optional[list[MdmAppSetting]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .mdm_app_setting import MdmAppSetting

        from ..entity import Entity
        from .mdm_app_setting import MdmAppSetting

        fields: dict[str, Callable[[Any], None]] = {
            "areDataProcessorServiceForWindowsFeaturesEnabled": lambda n : setattr(self, 'are_data_processor_service_for_windows_features_enabled', n.get_bool_value()),
            "mdmAppSettings": lambda n : setattr(self, 'mdm_app_settings', n.get_collection_of_object_values(MdmAppSetting)),
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
        writer.write_bool_value("areDataProcessorServiceForWindowsFeaturesEnabled", self.are_data_processor_service_for_windows_features_enabled)
        writer.write_collection_of_object_values("mdmAppSettings", self.mdm_app_settings)
    

