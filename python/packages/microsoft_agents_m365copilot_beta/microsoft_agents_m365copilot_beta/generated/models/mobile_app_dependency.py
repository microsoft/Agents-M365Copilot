from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_dependency_type import MobileAppDependencyType
    from .mobile_app_relationship import MobileAppRelationship

from .mobile_app_relationship import MobileAppRelationship

@dataclass
class MobileAppDependency(MobileAppRelationship, Parsable):
    """
    Describes a dependency type between two mobile apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mobileAppDependency"
    # Indicates the dependency type associated with a relationship between two mobile apps.
    dependency_type: Optional[MobileAppDependencyType] = None
    # The total number of apps that directly or indirectly depend on the parent app. Read-Only. This property is read-only.
    dependent_app_count: Optional[int] = None
    # The total number of apps the child app directly or indirectly depends on. Read-Only. This property is read-only.
    depends_on_app_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppDependency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppDependency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppDependency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_dependency_type import MobileAppDependencyType
        from .mobile_app_relationship import MobileAppRelationship

        from .mobile_app_dependency_type import MobileAppDependencyType
        from .mobile_app_relationship import MobileAppRelationship

        fields: dict[str, Callable[[Any], None]] = {
            "dependencyType": lambda n : setattr(self, 'dependency_type', n.get_enum_value(MobileAppDependencyType)),
            "dependentAppCount": lambda n : setattr(self, 'dependent_app_count', n.get_int_value()),
            "dependsOnAppCount": lambda n : setattr(self, 'depends_on_app_count', n.get_int_value()),
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
        writer.write_enum_value("dependencyType", self.dependency_type)
    

