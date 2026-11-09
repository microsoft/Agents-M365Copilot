from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .security_baseline_compliance_state import SecurityBaselineComplianceState
    from .security_baseline_contributing_policy import SecurityBaselineContributingPolicy
    from .setting_source import SettingSource

from .entity import Entity

@dataclass
class SecurityBaselineSettingState(Entity, Parsable):
    """
    The security baseline compliance state of a setting for a device
    """
    # The policies that contribute to this setting instance
    contributing_policies: Optional[list[SecurityBaselineContributingPolicy]] = None
    # The error code if the setting is in error state
    error_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The setting category id which this setting belongs to
    setting_category_id: Optional[str] = None
    # The setting category name which this setting belongs to
    setting_category_name: Optional[str] = None
    # The setting id guid
    setting_id: Optional[str] = None
    # The setting name that is being reported
    setting_name: Optional[str] = None
    # The policies that contribute to this setting instance
    source_policies: Optional[list[SettingSource]] = None
    # Security Baseline Compliance State
    state: Optional[SecurityBaselineComplianceState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineSettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineSettingState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineSettingState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .security_baseline_compliance_state import SecurityBaselineComplianceState
        from .security_baseline_contributing_policy import SecurityBaselineContributingPolicy
        from .setting_source import SettingSource

        from .entity import Entity
        from .security_baseline_compliance_state import SecurityBaselineComplianceState
        from .security_baseline_contributing_policy import SecurityBaselineContributingPolicy
        from .setting_source import SettingSource

        fields: dict[str, Callable[[Any], None]] = {
            "contributingPolicies": lambda n : setattr(self, 'contributing_policies', n.get_collection_of_object_values(SecurityBaselineContributingPolicy)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "settingCategoryId": lambda n : setattr(self, 'setting_category_id', n.get_str_value()),
            "settingCategoryName": lambda n : setattr(self, 'setting_category_name', n.get_str_value()),
            "settingId": lambda n : setattr(self, 'setting_id', n.get_str_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "sourcePolicies": lambda n : setattr(self, 'source_policies', n.get_collection_of_object_values(SettingSource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SecurityBaselineComplianceState)),
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
        writer.write_collection_of_object_values("contributingPolicies", self.contributing_policies)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("settingCategoryId", self.setting_category_id)
        writer.write_str_value("settingCategoryName", self.setting_category_name)
        writer.write_str_value("settingId", self.setting_id)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_collection_of_object_values("sourcePolicies", self.source_policies)
        writer.write_enum_value("state", self.state)
    

