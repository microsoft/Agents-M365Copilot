from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_permission_action_type import AndroidPermissionActionType

@dataclass
class AndroidPermissionAction(AdditionalDataHolder, Parsable):
    """
    Mapping between an Android app permission and the action Android should take when that permission is requested.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Android action taken when an app requests a dangerous permission.
    action: Optional[AndroidPermissionActionType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Android permission string, defined in the official Android documentation.  Example 'android.permission.READ_CONTACTS'.
    permission: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidPermissionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidPermissionAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidPermissionAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_permission_action_type import AndroidPermissionActionType

        from .android_permission_action_type import AndroidPermissionActionType

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(AndroidPermissionActionType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("permission", self.permission)
        writer.write_additional_data_value(self.additional_data)
    

