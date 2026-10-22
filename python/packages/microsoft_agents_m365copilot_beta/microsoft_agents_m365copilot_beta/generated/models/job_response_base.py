from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_error import ClassificationError
    from .classification_job_response import ClassificationJobResponse
    from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
    from .entity import Entity
    from .evaluate_label_job_response import EvaluateLabelJobResponse

from .entity import Entity

@dataclass
class JobResponseBase(Entity, Parsable):
    # The creationDateTime property
    creation_date_time: Optional[datetime.datetime] = None
    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The error property
    error: Optional[ClassificationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobResponseBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobResponseBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.classificationJobResponse".casefold():
            from .classification_job_response import ClassificationJobResponse

            return ClassificationJobResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dlpEvaluatePoliciesJobResponse".casefold():
            from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse

            return DlpEvaluatePoliciesJobResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.evaluateLabelJobResponse".casefold():
            from .evaluate_label_job_response import EvaluateLabelJobResponse

            return EvaluateLabelJobResponse()
        return JobResponseBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classification_error import ClassificationError
        from .classification_job_response import ClassificationJobResponse
        from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
        from .entity import Entity
        from .evaluate_label_job_response import EvaluateLabelJobResponse

        from .classification_error import ClassificationError
        from .classification_job_response import ClassificationJobResponse
        from .dlp_evaluate_policies_job_response import DlpEvaluatePoliciesJobResponse
        from .entity import Entity
        from .evaluate_label_job_response import EvaluateLabelJobResponse

        fields: dict[str, Callable[[Any], None]] = {
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(ClassificationError)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
    

