from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType
    from .app_list_item import AppListItem

@dataclass
class AndroidDeviceOwnerDelegatedScopeAppSetting(AdditionalDataHolder, Parsable):
    """
    Represents one item in the list of managed apps with app details and its associated delegated scope(s).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents an app in the list of managed applications
    app_detail: Optional[AppListItem] = None
    # List of scopes an app has been assigned.
    app_scopes: Optional[list[AndroidDeviceOwnerDelegatedAppScopeType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerDelegatedScopeAppSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerDelegatedScopeAppSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerDelegatedScopeAppSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType
        from .app_list_item import AppListItem

        from .android_device_owner_delegated_app_scope_type import AndroidDeviceOwnerDelegatedAppScopeType
        from .app_list_item import AppListItem

        fields: dict[str, Callable[[Any], None]] = {
            "appDetail": lambda n : setattr(self, 'app_detail', n.get_object_value(AppListItem)),
            "appScopes": lambda n : setattr(self, 'app_scopes', n.get_collection_of_enum_values(AndroidDeviceOwnerDelegatedAppScopeType)),
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
        writer.write_object_value("appDetail", self.app_detail)
        writer.write_collection_of_enum_values("appScopes", self.app_scopes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

