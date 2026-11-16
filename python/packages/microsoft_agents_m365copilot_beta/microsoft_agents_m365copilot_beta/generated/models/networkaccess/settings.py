from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .conditional_access_settings import ConditionalAccessSettings
    from .cross_tenant_access_settings import CrossTenantAccessSettings
    from .custom_block_page import CustomBlockPage
    from .forwarding_options import ForwardingOptions

from ..entity import Entity

@dataclass
class Settings(Entity, Parsable):
    # The conditionalAccess property
    conditional_access: Optional[ConditionalAccessSettings] = None
    # The crossTenantAccess property
    cross_tenant_access: Optional[CrossTenantAccessSettings] = None
    # The customBlockPage property
    custom_block_page: Optional[CustomBlockPage] = None
    # The forwardingOptions property
    forwarding_options: Optional[ForwardingOptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Settings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Settings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Settings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .conditional_access_settings import ConditionalAccessSettings
        from .cross_tenant_access_settings import CrossTenantAccessSettings
        from .custom_block_page import CustomBlockPage
        from .forwarding_options import ForwardingOptions

        from ..entity import Entity
        from .conditional_access_settings import ConditionalAccessSettings
        from .cross_tenant_access_settings import CrossTenantAccessSettings
        from .custom_block_page import CustomBlockPage
        from .forwarding_options import ForwardingOptions

        fields: dict[str, Callable[[Any], None]] = {
            "conditionalAccess": lambda n : setattr(self, 'conditional_access', n.get_object_value(ConditionalAccessSettings)),
            "crossTenantAccess": lambda n : setattr(self, 'cross_tenant_access', n.get_object_value(CrossTenantAccessSettings)),
            "customBlockPage": lambda n : setattr(self, 'custom_block_page', n.get_object_value(CustomBlockPage)),
            "forwardingOptions": lambda n : setattr(self, 'forwarding_options', n.get_object_value(ForwardingOptions)),
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
        writer.write_object_value("conditionalAccess", self.conditional_access)
        writer.write_object_value("crossTenantAccess", self.cross_tenant_access)
        writer.write_object_value("customBlockPage", self.custom_block_page)
        writer.write_object_value("forwardingOptions", self.forwarding_options)
    

