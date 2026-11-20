from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExposureCaseGitHub(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The environmentId property
    environment_id: Optional[str] = None
    # The issueNumber property
    issue_number: Optional[int] = None
    # The issueUrl property
    issue_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The primaryAssessmentId property
    primary_assessment_id: Optional[str] = None
    # The repoName property
    repo_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExposureCaseGitHub:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExposureCaseGitHub
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExposureCaseGitHub()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "environmentId": lambda n : setattr(self, 'environment_id', n.get_str_value()),
            "issueNumber": lambda n : setattr(self, 'issue_number', n.get_int_value()),
            "issueUrl": lambda n : setattr(self, 'issue_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryAssessmentId": lambda n : setattr(self, 'primary_assessment_id', n.get_str_value()),
            "repoName": lambda n : setattr(self, 'repo_name', n.get_str_value()),
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
        writer.write_str_value("environmentId", self.environment_id)
        writer.write_int_value("issueNumber", self.issue_number)
        writer.write_str_value("issueUrl", self.issue_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("primaryAssessmentId", self.primary_assessment_id)
        writer.write_str_value("repoName", self.repo_name)
        writer.write_additional_data_value(self.additional_data)
    

