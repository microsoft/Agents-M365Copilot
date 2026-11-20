from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary

from .app_scope import AppScope

@dataclass
class CustomAppScope(AppScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customAppScope"
    # The customAttributes property
    custom_attributes: Optional[CustomAppScopeAttributesDictionary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAppScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAppScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomAppScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary

        from .app_scope import AppScope
        from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary

        fields: dict[str, Callable[[Any], None]] = {
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_object_value(CustomAppScopeAttributesDictionary)),
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
        writer.write_object_value("customAttributes", self.custom_attributes)
    

