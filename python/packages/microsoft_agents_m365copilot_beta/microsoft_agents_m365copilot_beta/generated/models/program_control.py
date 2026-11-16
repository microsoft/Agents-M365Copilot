from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .program import Program
    from .program_resource import ProgramResource
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class ProgramControl(Entity, Parsable):
    # The controlId of the control, in particular the identifier of an access review. Required on create.
    control_id: Optional[str] = None
    # The programControlType identifies the type of program control - for example, a control linking to guest access reviews. Required on create.
    control_type_id: Optional[str] = None
    # The creation date and time of the program control.
    created_date_time: Optional[datetime.datetime] = None
    # The name of the control.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user who created the program control.
    owner: Optional[UserIdentity] = None
    # The program this control is part of.
    program: Optional[Program] = None
    # The programId of the program this control is a part of. Required on create.
    program_id: Optional[str] = None
    # The resource, a group or an app, targeted by this program control's access review.
    resource: Optional[ProgramResource] = None
    # The life cycle status of the control.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProgramControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProgramControl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProgramControl()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .program import Program
        from .program_resource import ProgramResource
        from .user_identity import UserIdentity

        from .entity import Entity
        from .program import Program
        from .program_resource import ProgramResource
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "controlId": lambda n : setattr(self, 'control_id', n.get_str_value()),
            "controlTypeId": lambda n : setattr(self, 'control_type_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(UserIdentity)),
            "program": lambda n : setattr(self, 'program', n.get_object_value(Program)),
            "programId": lambda n : setattr(self, 'program_id', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(ProgramResource)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("controlId", self.control_id)
        writer.write_str_value("controlTypeId", self.control_type_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("program", self.program)
        writer.write_str_value("programId", self.program_id)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("status", self.status)
    

