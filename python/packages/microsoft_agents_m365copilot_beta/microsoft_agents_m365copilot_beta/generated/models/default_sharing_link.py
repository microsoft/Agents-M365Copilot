from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sharing_role import SharingRole
    from .sharing_scope import SharingScope

@dataclass
class DefaultSharingLink(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the default link setting for this object is a direct URL rather than a sharing link.
    default_to_existing_access: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The default sharing link role. The possible values are: none, view, edit, manageList, review, restrictedView, submitOnly, unknownFutureValue.
    role: Optional[SharingRole] = None
    # The default sharing link scope. The possible values are: anyone, organization, specificPeople, anonymous, users, unknownFutureValue.
    scope: Optional[SharingScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DefaultSharingLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultSharingLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DefaultSharingLink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sharing_role import SharingRole
        from .sharing_scope import SharingScope

        from .sharing_role import SharingRole
        from .sharing_scope import SharingScope

        fields: dict[str, Callable[[Any], None]] = {
            "defaultToExistingAccess": lambda n : setattr(self, 'default_to_existing_access', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(SharingRole)),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(SharingScope)),
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
        writer.write_bool_value("defaultToExistingAccess", self.default_to_existing_access)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("scope", self.scope)
        writer.write_additional_data_value(self.additional_data)
    

