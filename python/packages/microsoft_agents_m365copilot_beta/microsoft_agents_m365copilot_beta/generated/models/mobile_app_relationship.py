from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_dependency import MobileAppDependency
    from .mobile_app_relationship_type import MobileAppRelationshipType
    from .mobile_app_supersedence import MobileAppSupersedence

from .entity import Entity

@dataclass
class MobileAppRelationship(Entity, Parsable):
    """
    The MobileAppRelationship describes the relationship between two mobile applications by providing information that tells if an application is dependent on or superseded by another application.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The display name of the app that is the source of the mobile app relationship entity. For example: Orca. Maximum length is 500 characters. Read-Only. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    source_display_name: Optional[str] = None
    # The display version of the app that is the source of the mobile app relationship entity. For example 1.0.12 or 1.2203.156 or 3. Read-Only. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    source_display_version: Optional[str] = None
    # The unique app identifier of the source of the mobile app relationship entity. For example: 2dbc75b9-e993-4e4d-a071-91ac5a218672. If null during relationship creation, then it will be populated with parent Id. Read-Only. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    source_id: Optional[str] = None
    # The publisher display name of the app that is the source of the mobile app relationship entity. For example: Fabrikam. Maximum length is 500 characters. Read-Only. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    source_publisher_display_name: Optional[str] = None
    # The display name of the app that is the target of the mobile app relationship entity. For example: Firefox Setup 52.0.2 32bit.intunewin. Maximum length is 500 characters. Read-Only. Returned by default. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    target_display_name: Optional[str] = None
    # The display version of the app that is the target of the mobile app relationship entity. For example 1.0 or 1.2203.156. Read-Only. Returned by default. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    target_display_version: Optional[str] = None
    # The unique app identifier of the target of the mobile app relationship entity. For example: 2dbc75b9-e993-4e4d-a071-91ac5a218672. Read-Only. Returned by default. Supports: $select. Does not support $search, $filter, $orderBy.
    target_id: Optional[str] = None
    # The publisher of the app that is the target of the mobile app relationship entity. For example: Fabrikam. Maximum length is 500 characters. Read-Only. Returned by default. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    target_publisher: Optional[str] = None
    # The publisher display name of the app that is the target of the mobile app relationship entity. For example: Fabrikam. Maximum length is 500 characters. Read-Only. Supports: $select. Does not support $search, $filter, $orderBy. This property is read-only.
    target_publisher_display_name: Optional[str] = None
    # Indicates whether the target of a relationship is the parent or the child in the relationship.
    target_type: Optional[MobileAppRelationshipType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppRelationship
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppDependency".casefold():
            from .mobile_app_dependency import MobileAppDependency

            return MobileAppDependency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppSupersedence".casefold():
            from .mobile_app_supersedence import MobileAppSupersedence

            return MobileAppSupersedence()
        return MobileAppRelationship()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_dependency import MobileAppDependency
        from .mobile_app_relationship_type import MobileAppRelationshipType
        from .mobile_app_supersedence import MobileAppSupersedence

        from .entity import Entity
        from .mobile_app_dependency import MobileAppDependency
        from .mobile_app_relationship_type import MobileAppRelationshipType
        from .mobile_app_supersedence import MobileAppSupersedence

        fields: dict[str, Callable[[Any], None]] = {
            "sourceDisplayName": lambda n : setattr(self, 'source_display_name', n.get_str_value()),
            "sourceDisplayVersion": lambda n : setattr(self, 'source_display_version', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "sourcePublisherDisplayName": lambda n : setattr(self, 'source_publisher_display_name', n.get_str_value()),
            "targetDisplayName": lambda n : setattr(self, 'target_display_name', n.get_str_value()),
            "targetDisplayVersion": lambda n : setattr(self, 'target_display_version', n.get_str_value()),
            "targetId": lambda n : setattr(self, 'target_id', n.get_str_value()),
            "targetPublisher": lambda n : setattr(self, 'target_publisher', n.get_str_value()),
            "targetPublisherDisplayName": lambda n : setattr(self, 'target_publisher_display_name', n.get_str_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(MobileAppRelationshipType)),
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
        writer.write_str_value("targetId", self.target_id)
        writer.write_enum_value("targetType", self.target_type)
    

