from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_relationship import MobileAppRelationship
    from .mobile_app_supersedence_type import MobileAppSupersedenceType

from .mobile_app_relationship import MobileAppRelationship

@dataclass
class MobileAppSupersedence(MobileAppRelationship, Parsable):
    """
    Describes a supersedence relationship between two mobile apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mobileAppSupersedence"
    # The total number of apps directly or indirectly superseded by the child app. Read-Only. This property is read-only.
    superseded_app_count: Optional[int] = None
    # Indicates the supersedence type associated with a relationship between two mobile apps.
    supersedence_type: Optional[MobileAppSupersedenceType] = None
    # The total number of apps directly or indirectly superseding the parent app. Read-Only. This property is read-only.
    superseding_app_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppSupersedence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppSupersedence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppSupersedence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_app_supersedence_type import MobileAppSupersedenceType

        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_app_supersedence_type import MobileAppSupersedenceType

        fields: dict[str, Callable[[Any], None]] = {
            "supersededAppCount": lambda n : setattr(self, 'superseded_app_count', n.get_int_value()),
            "supersedenceType": lambda n : setattr(self, 'supersedence_type', n.get_enum_value(MobileAppSupersedenceType)),
            "supersedingAppCount": lambda n : setattr(self, 'superseding_app_count', n.get_int_value()),
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
        writer.write_enum_value("supersedenceType", self.supersedence_type)
    

