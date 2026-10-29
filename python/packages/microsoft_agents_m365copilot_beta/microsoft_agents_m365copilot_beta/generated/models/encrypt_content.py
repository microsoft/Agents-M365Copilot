from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .encrypt_with import EncryptWith
    from .encrypt_with_template import EncryptWithTemplate
    from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
    from .label_action_base import LabelActionBase

from .label_action_base import LabelActionBase

@dataclass
class EncryptContent(LabelActionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.encryptContent"
    # The encryptWith property
    encrypt_with: Optional[EncryptWith] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EncryptContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptWithTemplate".casefold():
            from .encrypt_with_template import EncryptWithTemplate

            return EncryptWithTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptWithUserDefinedRights".casefold():
            from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights

            return EncryptWithUserDefinedRights()
        return EncryptContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .encrypt_with import EncryptWith
        from .encrypt_with_template import EncryptWithTemplate
        from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
        from .label_action_base import LabelActionBase

        from .encrypt_with import EncryptWith
        from .encrypt_with_template import EncryptWithTemplate
        from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
        from .label_action_base import LabelActionBase

        fields: dict[str, Callable[[Any], None]] = {
            "encryptWith": lambda n : setattr(self, 'encrypt_with', n.get_enum_value(EncryptWith)),
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
        writer.write_enum_value("encryptWith", self.encrypt_with)
    

