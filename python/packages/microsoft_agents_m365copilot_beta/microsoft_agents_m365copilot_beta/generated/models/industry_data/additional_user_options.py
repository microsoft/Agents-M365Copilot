from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .student_age_group import StudentAgeGroup

@dataclass
class AdditionalUserOptions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether student contact association should be allowed.
    allow_student_contact_association: Optional[bool] = None
    # Indicates whether all students should be marked as minors. The markAllStudentsAsMinors property is deprecated and will stop returning data on October 15, 2025. Going forward, use the studentAgeGroup property.
    mark_all_students_as_minors: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the age group classification for students. The possible values are: minor, notAdult, adult, unknownFutureValue. Use null to disable age group enforcement.
    student_age_group: Optional[StudentAgeGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdditionalUserOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdditionalUserOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdditionalUserOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .student_age_group import StudentAgeGroup

        from .student_age_group import StudentAgeGroup

        fields: dict[str, Callable[[Any], None]] = {
            "allowStudentContactAssociation": lambda n : setattr(self, 'allow_student_contact_association', n.get_bool_value()),
            "markAllStudentsAsMinors": lambda n : setattr(self, 'mark_all_students_as_minors', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "studentAgeGroup": lambda n : setattr(self, 'student_age_group', n.get_enum_value(StudentAgeGroup)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allowStudentContactAssociation", self.allow_student_contact_association)
        writer.write_bool_value("markAllStudentsAsMinors", self.mark_all_students_as_minors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("studentAgeGroup", self.student_age_group)
        writer.write_additional_data_value(self.additional_data)
    

