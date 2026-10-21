from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .allotment import Allotment
    from .assignment import Assignment
    from .assignment_error import AssignmentError

from ..entity import Entity

@dataclass
class AdminCloudLicensing(Entity, Parsable):
    # The set of all allotments within the organization. Read-only.
    allotments: Optional[list[Allotment]] = None
    # The set of all asynchronous allotment assignment errors that affect the organization. Read-only.
    assignment_errors: Optional[list[AssignmentError]] = None
    # The set of all license assignments within the organization. Not nullable.
    assignments: Optional[list[Assignment]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminCloudLicensing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminCloudLicensing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminCloudLicensing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .allotment import Allotment
        from .assignment import Assignment
        from .assignment_error import AssignmentError

        from ..entity import Entity
        from .allotment import Allotment
        from .assignment import Assignment
        from .assignment_error import AssignmentError

        fields: dict[str, Callable[[Any], None]] = {
            "allotments": lambda n : setattr(self, 'allotments', n.get_collection_of_object_values(Allotment)),
            "assignmentErrors": lambda n : setattr(self, 'assignment_errors', n.get_collection_of_object_values(AssignmentError)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(Assignment)),
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
        writer.write_collection_of_object_values("allotments", self.allotments)
        writer.write_collection_of_object_values("assignmentErrors", self.assignment_errors)
        writer.write_collection_of_object_values("assignments", self.assignments)
    

