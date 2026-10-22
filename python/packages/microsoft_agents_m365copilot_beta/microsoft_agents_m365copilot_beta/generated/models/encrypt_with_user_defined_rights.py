from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .encrypt_content import EncryptContent

from .encrypt_content import EncryptContent

@dataclass
class EncryptWithUserDefinedRights(EncryptContent, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.encryptWithUserDefinedRights"
    # The allowAdHocPermissions property
    allow_ad_hoc_permissions: Optional[bool] = None
    # The allowMailForwarding property
    allow_mail_forwarding: Optional[bool] = None
    # The decryptionRightsManagementTemplateId property
    decryption_rights_management_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EncryptWithUserDefinedRights:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptWithUserDefinedRights
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EncryptWithUserDefinedRights()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .encrypt_content import EncryptContent

        from .encrypt_content import EncryptContent

        fields: dict[str, Callable[[Any], None]] = {
            "allowAdHocPermissions": lambda n : setattr(self, 'allow_ad_hoc_permissions', n.get_bool_value()),
            "allowMailForwarding": lambda n : setattr(self, 'allow_mail_forwarding', n.get_bool_value()),
            "decryptionRightsManagementTemplateId": lambda n : setattr(self, 'decryption_rights_management_template_id', n.get_str_value()),
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
        writer.write_bool_value("allowAdHocPermissions", self.allow_ad_hoc_permissions)
        writer.write_bool_value("allowMailForwarding", self.allow_mail_forwarding)
        writer.write_str_value("decryptionRightsManagementTemplateId", self.decryption_rights_management_template_id)
    

