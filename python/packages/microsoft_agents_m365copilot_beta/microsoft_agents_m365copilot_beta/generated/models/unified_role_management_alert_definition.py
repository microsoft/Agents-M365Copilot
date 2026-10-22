from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_severity import AlertSeverity
    from .entity import Entity

from .entity import Entity

@dataclass
class UnifiedRoleManagementAlertDefinition(Entity, Parsable):
    # The description of the alert.
    description: Optional[str] = None
    # The friendly display name that renders in Privileged Identity Management (PIM) alerts in the Microsoft Entra admin center.
    display_name: Optional[str] = None
    # Long-form text that indicates the ways to prevent the alert from being triggered in your tenant.
    how_to_prevent: Optional[str] = None
    # true if the alert configuration can be customized in the tenant, and false otherwise. For example, the number and percentage thresholds of the 'There are too many global administrators' alert can be configured by users, while the 'This organization doesn't have Microsoft Entra ID P2' can't be configured, because the criteria are restricted.
    is_configurable: Optional[bool] = None
    # true if the alert can be remediated, and false otherwise.
    is_remediatable: Optional[bool] = None
    # The methods to mitigate the alert when it's triggered in the tenant. For example, to mitigate the 'There are too many global administrators', you could remove redundant privileged role assignments.
    mitigation_steps: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the scope where the alert is related. / is the only supported one for the tenant. Supports $filter (eq, ne).
    scope_id: Optional[str] = None
    # The type of scope where the alert is created. DirectoryRole is the only currently supported scope type for Microsoft Entra roles.
    scope_type: Optional[str] = None
    # Security impact of the alert. For example, it could be information leaks or unauthorized access.
    security_impact: Optional[str] = None
    # Severity level of the alert. The possible values are: unknown, informational, low, medium, high, unknownFutureValue.
    severity_level: Optional[AlertSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementAlertDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementAlertDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_severity import AlertSeverity
        from .entity import Entity

        from .alert_severity import AlertSeverity
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "howToPrevent": lambda n : setattr(self, 'how_to_prevent', n.get_str_value()),
            "isConfigurable": lambda n : setattr(self, 'is_configurable', n.get_bool_value()),
            "isRemediatable": lambda n : setattr(self, 'is_remediatable', n.get_bool_value()),
            "mitigationSteps": lambda n : setattr(self, 'mitigation_steps', n.get_str_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
            "securityImpact": lambda n : setattr(self, 'security_impact', n.get_str_value()),
            "severityLevel": lambda n : setattr(self, 'severity_level', n.get_enum_value(AlertSeverity)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("howToPrevent", self.how_to_prevent)
        writer.write_bool_value("isConfigurable", self.is_configurable)
        writer.write_bool_value("isRemediatable", self.is_remediatable)
        writer.write_str_value("mitigationSteps", self.mitigation_steps)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
        writer.write_str_value("securityImpact", self.security_impact)
        writer.write_enum_value("severityLevel", self.severity_level)
    

