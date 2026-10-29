from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sharing_operation_status import SharingOperationStatus

@dataclass
class DirectSharingAbilities(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the current user can add existing guest recipients to this item using direct sharing.
    add_existing_external_users: Optional[SharingOperationStatus] = None
    # Indicates whether the current user can add internal recipients to this item using direct sharing.
    add_internal_users: Optional[SharingOperationStatus] = None
    # Indicates whether the current user can add new guest recipients to this item using direct sharing.
    add_new_external_users: Optional[SharingOperationStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the user querying this endpoint can request access for the user or on behalf of other users, after which, site admins, can approve or deny the creation of a potential sharing link.
    request_grant_access: Optional[SharingOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectSharingAbilities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectSharingAbilities
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectSharingAbilities()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sharing_operation_status import SharingOperationStatus

        from .sharing_operation_status import SharingOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "addExistingExternalUsers": lambda n : setattr(self, 'add_existing_external_users', n.get_object_value(SharingOperationStatus)),
            "addInternalUsers": lambda n : setattr(self, 'add_internal_users', n.get_object_value(SharingOperationStatus)),
            "addNewExternalUsers": lambda n : setattr(self, 'add_new_external_users', n.get_object_value(SharingOperationStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requestGrantAccess": lambda n : setattr(self, 'request_grant_access', n.get_object_value(SharingOperationStatus)),
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
        writer.write_object_value("addExistingExternalUsers", self.add_existing_external_users)
        writer.write_object_value("addInternalUsers", self.add_internal_users)
        writer.write_object_value("addNewExternalUsers", self.add_new_external_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("requestGrantAccess", self.request_grant_access)
        writer.write_additional_data_value(self.additional_data)
    

