from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .long_running_operation import LongRunningOperation
    from .unified_role_management_alert import UnifiedRoleManagementAlert
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
    from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

from .entity import Entity

@dataclass
class RoleManagementAlert(Entity, Parsable):
    # The various configurations of an alert for Microsoft Entra roles. The configurations are predefined and can't be created or deleted, but some of the configurations can be modified.
    alert_configurations: Optional[list[UnifiedRoleManagementAlertConfiguration]] = None
    # Defines an alert, its impact, and measures to mitigate or prevent it.
    alert_definitions: Optional[list[UnifiedRoleManagementAlertDefinition]] = None
    # Represents the alert entity.
    alerts: Optional[list[UnifiedRoleManagementAlert]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents operations on resources that take a long time to complete and can run in the background until completion.
    operations: Optional[list[LongRunningOperation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleManagementAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagementAlert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoleManagementAlert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .long_running_operation import LongRunningOperation
        from .unified_role_management_alert import UnifiedRoleManagementAlert
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

        from .entity import Entity
        from .long_running_operation import LongRunningOperation
        from .unified_role_management_alert import UnifiedRoleManagementAlert
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "alertConfigurations": lambda n : setattr(self, 'alert_configurations', n.get_collection_of_object_values(UnifiedRoleManagementAlertConfiguration)),
            "alertDefinitions": lambda n : setattr(self, 'alert_definitions', n.get_collection_of_object_values(UnifiedRoleManagementAlertDefinition)),
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(UnifiedRoleManagementAlert)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(LongRunningOperation)),
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
        writer.write_collection_of_object_values("alertConfigurations", self.alert_configurations)
        writer.write_collection_of_object_values("alertDefinitions", self.alert_definitions)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_collection_of_object_values("operations", self.operations)
    

