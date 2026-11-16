from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

@dataclass
class TooManyGlobalAdminsAssignedToTenantAlertConfiguration(UnifiedRoleManagementAlertConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration"
    # The threshold for the number of accounts assigned the Global Administrator role in the tenant. Triggers an alert if the number of global administrators in the tenant reaches or crosses this threshold value.
    global_admin_count_threshold: Optional[int] = None
    # Threshold of the percentage of global administrators out of all the role assignments in the tenant. Triggers an alert if the percentage in the tenant reaches or crosses this threshold value.
    percentage_of_global_admins_out_of_roles_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TooManyGlobalAdminsAssignedToTenantAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "globalAdminCountThreshold": lambda n : setattr(self, 'global_admin_count_threshold', n.get_int_value()),
            "percentageOfGlobalAdminsOutOfRolesThreshold": lambda n : setattr(self, 'percentage_of_global_admins_out_of_roles_threshold', n.get_int_value()),
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
        writer.write_int_value("globalAdminCountThreshold", self.global_admin_count_threshold)
        writer.write_int_value("percentageOfGlobalAdminsOutOfRolesThreshold", self.percentage_of_global_admins_out_of_roles_threshold)
    

