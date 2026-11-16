from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .plugin_auth import PluginAuth
    from .plugin_auth_types import PluginAuthTypes
    from .plugin_catalog_scope import PluginCatalogScope
    from .plugin_category import PluginCategory
    from .plugin_preview_states import PluginPreviewStates
    from .plugin_setting import PluginSetting

@dataclass
class Plugin(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Authorization for the plugin.
    authorization: Optional[PluginAuth] = None
    # The catalogScope property
    catalog_scope: Optional[PluginCatalogScope] = None
    # The category property
    category: Optional[PluginCategory] = None
    # Brief description of the plugin.
    description: Optional[str] = None
    # Display name of the plugin.   Supports $filter (eq).
    display_name: Optional[str] = None
    # Displays whether the plugin is enabled for use within the catalogScope.   Supports $filter (eq).
    is_enabled: Optional[bool] = None
    # Represents the name of the plugin. Primary key.   Supports $filter (eq, contains).
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The previewState property
    preview_state: Optional[PluginPreviewStates] = None
    # Settings for the plugin.
    settings: Optional[list[PluginSetting]] = None
    # The supportedAuthTypes property
    supported_auth_types: Optional[PluginAuthTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Plugin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Plugin
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Plugin()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .plugin_auth import PluginAuth
        from .plugin_auth_types import PluginAuthTypes
        from .plugin_catalog_scope import PluginCatalogScope
        from .plugin_category import PluginCategory
        from .plugin_preview_states import PluginPreviewStates
        from .plugin_setting import PluginSetting

        from .plugin_auth import PluginAuth
        from .plugin_auth_types import PluginAuthTypes
        from .plugin_catalog_scope import PluginCatalogScope
        from .plugin_category import PluginCategory
        from .plugin_preview_states import PluginPreviewStates
        from .plugin_setting import PluginSetting

        fields: dict[str, Callable[[Any], None]] = {
            "authorization": lambda n : setattr(self, 'authorization', n.get_object_value(PluginAuth)),
            "catalogScope": lambda n : setattr(self, 'catalog_scope', n.get_enum_value(PluginCatalogScope)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(PluginCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previewState": lambda n : setattr(self, 'preview_state', n.get_enum_value(PluginPreviewStates)),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(PluginSetting)),
            "supportedAuthTypes": lambda n : setattr(self, 'supported_auth_types', n.get_enum_value(PluginAuthTypes)),
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
        writer.write_object_value("authorization", self.authorization)
        writer.write_enum_value("catalogScope", self.catalog_scope)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("previewState", self.preview_state)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_enum_value("supportedAuthTypes", self.supported_auth_types)
        writer.write_additional_data_value(self.additional_data)
    

