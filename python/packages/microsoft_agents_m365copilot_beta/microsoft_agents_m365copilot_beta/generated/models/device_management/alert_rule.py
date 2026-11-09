from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_rule_template import AlertRuleTemplate
    from .notification_channel import NotificationChannel
    from .rule_condition import RuleCondition
    from .rule_severity_type import RuleSeverityType
    from .rule_threshold import RuleThreshold

from ..entity import Entity

@dataclass
class AlertRule(Entity, Parsable):
    # The rule template of the alert event. The possible values are: cloudPcProvisionScenario, cloudPcImageUploadScenario, cloudPcOnPremiseNetworkConnectionCheckScenario, unknownFutureValue, cloudPcInGracePeriodScenario, cloudPcFrontlineInsufficientLicensesScenario, cloudPcInaccessibleScenario, cloudPcFrontlineConcurrencyScenario, cloudPcUserSettingsPersistenceScenario, cloudPcDeprovisionFailedScenario.  Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: cloudPcInGracePeriodScenario, cloudPcFrontlineInsufficientLicensesScenario, cloudPcInaccessibleScenario, cloudPcFrontlineConcurrencyScenario, cloudPcUserSettingsPersistenceScenario, cloudPcDeprovisionFailedScenario.
    alert_rule_template: Optional[AlertRuleTemplate] = None
    # The conditions that determine when to send alerts. For example, you can configure a condition to send an alert when provisioning fails for six or more Cloud PCs.
    conditions: Optional[list[RuleCondition]] = None
    # The rule description.
    description: Optional[str] = None
    # The display name of the rule.
    display_name: Optional[str] = None
    # The status of the rule that indicates whether the rule is enabled or disabled. If true, the rule is enabled; otherwise, the rule is disabled.
    enabled: Optional[bool] = None
    # Indicates whether the rule is a system rule. If true, the rule is a system rule; otherwise, the rule is a custom-defined rule and can be edited. System rules are built in and only a few properties can be edited.
    is_system_rule: Optional[bool] = None
    # The notification channels of the rule selected by the user.
    notification_channels: Optional[list[NotificationChannel]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The severity of the rule. The possible values are: unknown, informational, warning, critical, unknownFutureValue.
    severity: Optional[RuleSeverityType] = None
    # The conditions that determine when to send alerts. For example, you can configure a condition to send an alert when provisioning fails for six or more Cloud PCs. This property is deprecated. Use conditions instead.
    threshold: Optional[RuleThreshold] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlertRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_rule_template import AlertRuleTemplate
        from .notification_channel import NotificationChannel
        from .rule_condition import RuleCondition
        from .rule_severity_type import RuleSeverityType
        from .rule_threshold import RuleThreshold

        from ..entity import Entity
        from .alert_rule_template import AlertRuleTemplate
        from .notification_channel import NotificationChannel
        from .rule_condition import RuleCondition
        from .rule_severity_type import RuleSeverityType
        from .rule_threshold import RuleThreshold

        fields: dict[str, Callable[[Any], None]] = {
            "alertRuleTemplate": lambda n : setattr(self, 'alert_rule_template', n.get_enum_value(AlertRuleTemplate)),
            "conditions": lambda n : setattr(self, 'conditions', n.get_collection_of_object_values(RuleCondition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "isSystemRule": lambda n : setattr(self, 'is_system_rule', n.get_bool_value()),
            "notificationChannels": lambda n : setattr(self, 'notification_channels', n.get_collection_of_object_values(NotificationChannel)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(RuleSeverityType)),
            "threshold": lambda n : setattr(self, 'threshold', n.get_object_value(RuleThreshold)),
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
        writer.write_enum_value("alertRuleTemplate", self.alert_rule_template)
        writer.write_collection_of_object_values("conditions", self.conditions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("isSystemRule", self.is_system_rule)
        writer.write_collection_of_object_values("notificationChannels", self.notification_channels)
        writer.write_enum_value("severity", self.severity)
        writer.write_object_value("threshold", self.threshold)
    

