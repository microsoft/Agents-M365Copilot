from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .educational_activity_detail import EducationalActivityDetail
    from .institution_data import InstitutionData
    from .item_facet import ItemFacet

from .item_facet import ItemFacet

@dataclass
class EducationalActivity(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationalActivity"
    # The month and year the user graduated or completed the activity.
    completion_month_year: Optional[datetime.date] = None
    # The month and year the user completed the educational activity referenced.
    end_month_year: Optional[datetime.date] = None
    # Contains details of the institution studied at.
    institution: Optional[InstitutionData] = None
    # Contains extended information about the program or course.
    program: Optional[EducationalActivityDetail] = None
    # The month and year the user commenced the activity referenced.
    start_month_year: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationalActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationalActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .educational_activity_detail import EducationalActivityDetail
        from .institution_data import InstitutionData
        from .item_facet import ItemFacet

        from .educational_activity_detail import EducationalActivityDetail
        from .institution_data import InstitutionData
        from .item_facet import ItemFacet

        fields: dict[str, Callable[[Any], None]] = {
            "completionMonthYear": lambda n : setattr(self, 'completion_month_year', n.get_date_value()),
            "endMonthYear": lambda n : setattr(self, 'end_month_year', n.get_date_value()),
            "institution": lambda n : setattr(self, 'institution', n.get_object_value(InstitutionData)),
            "program": lambda n : setattr(self, 'program', n.get_object_value(EducationalActivityDetail)),
            "startMonthYear": lambda n : setattr(self, 'start_month_year', n.get_date_value()),
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
        writer.write_date_value("completionMonthYear", self.completion_month_year)
        writer.write_date_value("endMonthYear", self.end_month_year)
        writer.write_object_value("institution", self.institution)
        writer.write_object_value("program", self.program)
        writer.write_date_value("startMonthYear", self.start_month_year)
    

