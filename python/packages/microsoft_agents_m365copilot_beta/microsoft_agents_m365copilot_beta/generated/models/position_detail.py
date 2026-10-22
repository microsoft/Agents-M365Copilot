from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_detail import CompanyDetail

@dataclass
class PositionDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information about the company or employer.
    company: Optional[CompanyDetail] = None
    # A description for the position in question.
    description: Optional[str] = None
    # The identifier assigned to the employee.
    employee_id: Optional[str] = None
    # The type of employment for the position.
    employee_type: Optional[str] = None
    # The date when the position ended.
    end_month_year: Optional[datetime.date] = None
    # The title of the position.
    job_title: Optional[str] = None
    # The place where the employee is within the organizational hierarchy.
    layer: Optional[int] = None
    # The employee’s experience or management level.
    level: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role the position entailed.
    role: Optional[str] = None
    # An optional job title for the position.
    secondary_job_title: Optional[str] = None
    # An optional role for the position entailed.
    secondary_role: Optional[str] = None
    # The start date of the position.
    start_month_year: Optional[datetime.date] = None
    # The summary of the position.
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PositionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PositionDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PositionDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .company_detail import CompanyDetail

        from .company_detail import CompanyDetail

        fields: dict[str, Callable[[Any], None]] = {
            "company": lambda n : setattr(self, 'company', n.get_object_value(CompanyDetail)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_str_value()),
            "employeeType": lambda n : setattr(self, 'employee_type', n.get_str_value()),
            "endMonthYear": lambda n : setattr(self, 'end_month_year', n.get_date_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "layer": lambda n : setattr(self, 'layer', n.get_int_value()),
            "level": lambda n : setattr(self, 'level', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "secondaryJobTitle": lambda n : setattr(self, 'secondary_job_title', n.get_str_value()),
            "secondaryRole": lambda n : setattr(self, 'secondary_role', n.get_str_value()),
            "startMonthYear": lambda n : setattr(self, 'start_month_year', n.get_date_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_object_value("company", self.company)
        writer.write_str_value("description", self.description)
        writer.write_str_value("employeeId", self.employee_id)
        writer.write_str_value("employeeType", self.employee_type)
        writer.write_date_value("endMonthYear", self.end_month_year)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_int_value("layer", self.layer)
        writer.write_str_value("level", self.level)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("role", self.role)
        writer.write_str_value("secondaryJobTitle", self.secondary_job_title)
        writer.write_str_value("secondaryRole", self.secondary_role)
        writer.write_date_value("startMonthYear", self.start_month_year)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

