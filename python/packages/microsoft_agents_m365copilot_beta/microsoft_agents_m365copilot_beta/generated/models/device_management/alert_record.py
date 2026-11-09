from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_impact import AlertImpact
    from .alert_rule_template import AlertRuleTemplate
    from .alert_status_type import AlertStatusType
    from .rule_severity_type import RuleSeverityType

from ..entity import Entity

@dataclass
class AlertRecord(Entity, Parsable):
    # The impact of the alert event. Consists of a list of key-value pair and a number followed by the aggregation type. For example, 6 affectedCloudPcCount means that 6 Cloud PCs are affected. 12 affectedCloudPcPercentage means 12% of Cloud PCs are affected. The list of key-value pair indicates the details of the alert impact.
    alert_impact: Optional[AlertImpact] = None
    # The corresponding ID of the alert rule.
    alert_rule_id: Optional[str] = None
    # The rule template of the alert event. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue, cloudPcInGracePeriodScenario, cloudPcFrontlineInsufficientLicensesScenario, cloudPcInaccessibleScenario, cloudPcFrontlineConcurrencyScenario, cloudPcUserSettingsPersistenceScenario, cloudPcDeprovisionFailedScenario. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: cloudPcInGracePeriodScenario, cloudPcFrontlineInsufficientLicensesScenario, cloudPcInaccessibleScenario, cloudPcFrontlineConcurrencyScenario, cloudPcUserSettingsPersistenceScenario, cloudPcDeprovisionFailedScenario.
    alert_rule_template: Optional[AlertRuleTemplate] = None
    # The date and time when the alert event was detected. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    detected_date_time: Optional[datetime.datetime] = None
    # The display name of the alert record.
    display_name: Optional[str] = None
    # The date and time when the alert record was last updated. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the alert event was resolved. The Timestamp type represents date and time information using ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    resolved_date_time: Optional[datetime.datetime] = None
    # The severity of the alert event. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
    severity: Optional[RuleSeverityType] = None
    # The status of the alert record. The possible values are: active, resolved, unknownFutureValue.
    status: Optional[AlertStatusType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlertRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_impact import AlertImpact
        from .alert_rule_template import AlertRuleTemplate
        from .alert_status_type import AlertStatusType
        from .rule_severity_type import RuleSeverityType

        from ..entity import Entity
        from .alert_impact import AlertImpact
        from .alert_rule_template import AlertRuleTemplate
        from .alert_status_type import AlertStatusType
        from .rule_severity_type import RuleSeverityType

        fields: dict[str, Callable[[Any], None]] = {
            "alertImpact": lambda n : setattr(self, 'alert_impact', n.get_object_value(AlertImpact)),
            "alertRuleId": lambda n : setattr(self, 'alert_rule_id', n.get_str_value()),
            "alertRuleTemplate": lambda n : setattr(self, 'alert_rule_template', n.get_enum_value(AlertRuleTemplate)),
            "detectedDateTime": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "resolvedDateTime": lambda n : setattr(self, 'resolved_date_time', n.get_datetime_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(RuleSeverityType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AlertStatusType)),
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
        writer.write_object_value("alertImpact", self.alert_impact)
        writer.write_str_value("alertRuleId", self.alert_rule_id)
        writer.write_enum_value("alertRuleTemplate", self.alert_rule_template)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_datetime_value("resolvedDateTime", self.resolved_date_time)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
    

