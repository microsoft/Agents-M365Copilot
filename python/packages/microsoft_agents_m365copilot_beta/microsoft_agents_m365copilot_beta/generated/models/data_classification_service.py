from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exact_match_data_store import ExactMatchDataStore
    from .exact_match_upload_agent import ExactMatchUploadAgent
    from .job_response_base import JobResponseBase
    from .sensitive_type import SensitiveType
    from .sensitivity_label import SensitivityLabel

from .entity import Entity

@dataclass
class DataClassificationService(Entity, Parsable):
    # The classifyFileJobs property
    classify_file_jobs: Optional[list[JobResponseBase]] = None
    # The classifyTextJobs property
    classify_text_jobs: Optional[list[JobResponseBase]] = None
    # The evaluateDlpPoliciesJobs property
    evaluate_dlp_policies_jobs: Optional[list[JobResponseBase]] = None
    # The evaluateLabelJobs property
    evaluate_label_jobs: Optional[list[JobResponseBase]] = None
    # The exactMatchDataStores property
    exact_match_data_stores: Optional[list[ExactMatchDataStore]] = None
    # The exactMatchUploadAgents property
    exact_match_upload_agents: Optional[list[ExactMatchUploadAgent]] = None
    # The jobs property
    jobs: Optional[list[JobResponseBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sensitiveTypes property
    sensitive_types: Optional[list[SensitiveType]] = None
    # The sensitivityLabels property
    sensitivity_labels: Optional[list[SensitivityLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataClassificationService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataClassificationService
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DataClassificationService()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exact_match_data_store import ExactMatchDataStore
        from .exact_match_upload_agent import ExactMatchUploadAgent
        from .job_response_base import JobResponseBase
        from .sensitive_type import SensitiveType
        from .sensitivity_label import SensitivityLabel

        from .entity import Entity
        from .exact_match_data_store import ExactMatchDataStore
        from .exact_match_upload_agent import ExactMatchUploadAgent
        from .job_response_base import JobResponseBase
        from .sensitive_type import SensitiveType
        from .sensitivity_label import SensitivityLabel

        fields: dict[str, Callable[[Any], None]] = {
            "classifyFileJobs": lambda n : setattr(self, 'classify_file_jobs', n.get_collection_of_object_values(JobResponseBase)),
            "classifyTextJobs": lambda n : setattr(self, 'classify_text_jobs', n.get_collection_of_object_values(JobResponseBase)),
            "evaluateDlpPoliciesJobs": lambda n : setattr(self, 'evaluate_dlp_policies_jobs', n.get_collection_of_object_values(JobResponseBase)),
            "evaluateLabelJobs": lambda n : setattr(self, 'evaluate_label_jobs', n.get_collection_of_object_values(JobResponseBase)),
            "exactMatchDataStores": lambda n : setattr(self, 'exact_match_data_stores', n.get_collection_of_object_values(ExactMatchDataStore)),
            "exactMatchUploadAgents": lambda n : setattr(self, 'exact_match_upload_agents', n.get_collection_of_object_values(ExactMatchUploadAgent)),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(JobResponseBase)),
            "sensitiveTypes": lambda n : setattr(self, 'sensitive_types', n.get_collection_of_object_values(SensitiveType)),
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(SensitivityLabel)),
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
        writer.write_collection_of_object_values("classifyFileJobs", self.classify_file_jobs)
        writer.write_collection_of_object_values("classifyTextJobs", self.classify_text_jobs)
        writer.write_collection_of_object_values("evaluateDlpPoliciesJobs", self.evaluate_dlp_policies_jobs)
        writer.write_collection_of_object_values("evaluateLabelJobs", self.evaluate_label_jobs)
        writer.write_collection_of_object_values("exactMatchDataStores", self.exact_match_data_stores)
        writer.write_collection_of_object_values("exactMatchUploadAgents", self.exact_match_upload_agents)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_collection_of_object_values("sensitiveTypes", self.sensitive_types)
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
    

