from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label_action_base import LabelActionBase
    from .site_access_type import SiteAccessType

from .label_action_base import LabelActionBase

@dataclass
class ProtectSite(LabelActionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.protectSite"
    # The accessType property
    access_type: Optional[SiteAccessType] = None
    # The conditionalAccessProtectionLevelId property
    conditional_access_protection_level_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectSite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProtectSite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .label_action_base import LabelActionBase
        from .site_access_type import SiteAccessType

        from .label_action_base import LabelActionBase
        from .site_access_type import SiteAccessType

        fields: dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(SiteAccessType)),
            "conditionalAccessProtectionLevelId": lambda n : setattr(self, 'conditional_access_protection_level_id', n.get_str_value()),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("conditionalAccessProtectionLevelId", self.conditional_access_protection_level_id)
    

