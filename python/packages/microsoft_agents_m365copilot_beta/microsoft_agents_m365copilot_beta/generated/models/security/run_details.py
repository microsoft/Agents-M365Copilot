from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hunting_rule_error_code import HuntingRuleErrorCode
    from .hunting_rule_run_status import HuntingRuleRunStatus

@dataclass
class RunDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Error code of the most recent run that encountered an error. The possible values are: queryExecutionFailed, queryExecutionThrottling, queryExceededResultSize, queryLimitsExceeded, queryTimeout, alertCreationFailed, alertReportNotFound, partialRowsFailed, unknownFutureValue.
    error_code: Optional[HuntingRuleErrorCode] = None
    # Reason for failure when the custom detection last ran and failed. See the table below.
    failure_reason: Optional[str] = None
    # Timestamp when the custom detection was last run.
    last_run_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Status of custom detection when it was last run. The possible values are: running, completed, failed, partiallyFailed, unknownFutureValue.
    status: Optional[HuntingRuleRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RunDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RunDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RunDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hunting_rule_error_code import HuntingRuleErrorCode
        from .hunting_rule_run_status import HuntingRuleRunStatus

        from .hunting_rule_error_code import HuntingRuleErrorCode
        from .hunting_rule_run_status import HuntingRuleRunStatus

        fields: dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(HuntingRuleErrorCode)),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "lastRunDateTime": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(HuntingRuleRunStatus)),
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
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

