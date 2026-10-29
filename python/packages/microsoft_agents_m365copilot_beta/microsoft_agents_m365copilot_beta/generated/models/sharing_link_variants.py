from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sharing_operation_status import SharingOperationStatus
    from .sharing_role import SharingRole

@dataclass
class SharingLinkVariants(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the most permissive role with which an address bar link can be created. The possible values are: none, view, edit, manageList, review, restrictedView, submitOnly, unknownFutureValue.
    address_bar_link_permission: Optional[SharingRole] = None
    # Indicates whether a link can be embedded.
    allow_embed: Optional[SharingOperationStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether a link can be password protected, meaning that link users would need to enter a password to access the item for which the sharing link is produced. Creating a passwordProtected link for the first time requires providing a password.
    password_protected: Optional[SharingOperationStatus] = None
    # Indicates whether a link requires identity authentication for recipients. Users can be verified through either an email address or identity.
    requires_authentication: Optional[SharingOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharingLinkVariants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharingLinkVariants
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharingLinkVariants()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sharing_operation_status import SharingOperationStatus
        from .sharing_role import SharingRole

        from .sharing_operation_status import SharingOperationStatus
        from .sharing_role import SharingRole

        fields: dict[str, Callable[[Any], None]] = {
            "addressBarLinkPermission": lambda n : setattr(self, 'address_bar_link_permission', n.get_enum_value(SharingRole)),
            "allowEmbed": lambda n : setattr(self, 'allow_embed', n.get_object_value(SharingOperationStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordProtected": lambda n : setattr(self, 'password_protected', n.get_object_value(SharingOperationStatus)),
            "requiresAuthentication": lambda n : setattr(self, 'requires_authentication', n.get_object_value(SharingOperationStatus)),
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
        writer.write_enum_value("addressBarLinkPermission", self.address_bar_link_permission)
        writer.write_object_value("allowEmbed", self.allow_embed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("passwordProtected", self.password_protected)
        writer.write_object_value("requiresAuthentication", self.requires_authentication)
        writer.write_additional_data_value(self.additional_data)
    

