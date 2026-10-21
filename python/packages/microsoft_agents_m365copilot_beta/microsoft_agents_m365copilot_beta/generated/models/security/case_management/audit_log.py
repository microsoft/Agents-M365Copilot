from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity import Activity
    from .activity_resource_details import ActivityResourceDetails
    from .audit_action import AuditAction
    from .modified_property import ModifiedProperty

from .activity import Activity

@dataclass
class AuditLog(Activity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.auditLog"
    # The action property
    action: Optional[AuditAction] = None
    # The target resource details for the audit activity.
    details: Optional[ActivityResourceDetails] = None
    # The collection of property changes recorded in the audit log. Supports $filter.
    modified_properties: Optional[list[ModifiedProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditLog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity import Activity
        from .activity_resource_details import ActivityResourceDetails
        from .audit_action import AuditAction
        from .modified_property import ModifiedProperty

        from .activity import Activity
        from .activity_resource_details import ActivityResourceDetails
        from .audit_action import AuditAction
        from .modified_property import ModifiedProperty

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(AuditAction)),
            "details": lambda n : setattr(self, 'details', n.get_object_value(ActivityResourceDetails)),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(ModifiedProperty)),
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
        writer.write_enum_value("action", self.action)
        writer.write_object_value("details", self.details)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
    

