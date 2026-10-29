from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_rule_definition_template import AlertRuleDefinitionTemplate
    from .managed_tenant_alert_rule import ManagedTenantAlertRule

from ..entity import Entity

@dataclass
class ManagedTenantAlertRuleDefinition(Entity, Parsable):
    # The alertRules property
    alert_rules: Optional[list[ManagedTenantAlertRule]] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The definitionTemplate property
    definition_template: Optional[AlertRuleDefinitionTemplate] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedTenantAlertRuleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantAlertRuleDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedTenantAlertRuleDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_rule_definition_template import AlertRuleDefinitionTemplate
        from .managed_tenant_alert_rule import ManagedTenantAlertRule

        from ..entity import Entity
        from .alert_rule_definition_template import AlertRuleDefinitionTemplate
        from .managed_tenant_alert_rule import ManagedTenantAlertRule

        fields: dict[str, Callable[[Any], None]] = {
            "alertRules": lambda n : setattr(self, 'alert_rules', n.get_collection_of_object_values(ManagedTenantAlertRule)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definitionTemplate": lambda n : setattr(self, 'definition_template', n.get_object_value(AlertRuleDefinitionTemplate)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("alertRules", self.alert_rules)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definitionTemplate", self.definition_template)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
    

