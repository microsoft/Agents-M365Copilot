from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
    from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
    from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

from .entity import Entity

@dataclass
class UnifiedRoleManagementAlert(Entity, Parsable):
    # The configuration of the alert in PIM for Microsoft Entra roles. Alert configurations are pre-defined and cannot be created or deleted, but some configurations can be modified. Supports $filter for the isEnabled property and $expand.
    alert_configuration: Optional[UnifiedRoleManagementAlertConfiguration] = None
    # Contains the description, impact, and measures to mitigate or prevent the security alert from being triggered in your tenant. Supports $expand.
    alert_definition: Optional[UnifiedRoleManagementAlertDefinition] = None
    # The identifier of an alert definition. Supports $filter (eq, ne).
    alert_definition_id: Optional[str] = None
    # Represents the incidents of this type of alert that have been triggered in Privileged Identity Management (PIM) for Microsoft Entra roles in the tenant. Supports $expand.
    alert_incidents: Optional[list[UnifiedRoleManagementAlertIncident]] = None
    # The number of incidents triggered in the tenant and relating to the alert. Can only be a positive integer.
    incident_count: Optional[int] = None
    # false by default. true if the alert is active.
    is_active: Optional[bool] = None
    # The date time when the alert configuration was updated or new incidents generated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The date time when the tenant was last scanned for incidents that trigger this alert.
    last_scanned_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the scope where the alert is related. / is the only supported one for the tenant. Supports $filter (eq, ne).
    scope_id: Optional[str] = None
    # The type of scope where the alert is created. DirectoryRole is the only currently supported scope type for Microsoft Entra roles.
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementAlert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

        from .entity import Entity
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition
        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

        fields: dict[str, Callable[[Any], None]] = {
            "alertConfiguration": lambda n : setattr(self, 'alert_configuration', n.get_object_value(UnifiedRoleManagementAlertConfiguration)),
            "alertDefinition": lambda n : setattr(self, 'alert_definition', n.get_object_value(UnifiedRoleManagementAlertDefinition)),
            "alertDefinitionId": lambda n : setattr(self, 'alert_definition_id', n.get_str_value()),
            "alertIncidents": lambda n : setattr(self, 'alert_incidents', n.get_collection_of_object_values(UnifiedRoleManagementAlertIncident)),
            "incidentCount": lambda n : setattr(self, 'incident_count', n.get_int_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastScannedDateTime": lambda n : setattr(self, 'last_scanned_date_time', n.get_datetime_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
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
        writer.write_object_value("alertConfiguration", self.alert_configuration)
        writer.write_object_value("alertDefinition", self.alert_definition)
        writer.write_str_value("alertDefinitionId", self.alert_definition_id)
        writer.write_collection_of_object_values("alertIncidents", self.alert_incidents)
        writer.write_int_value("incidentCount", self.incident_count)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastScannedDateTime", self.last_scanned_date_time)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

