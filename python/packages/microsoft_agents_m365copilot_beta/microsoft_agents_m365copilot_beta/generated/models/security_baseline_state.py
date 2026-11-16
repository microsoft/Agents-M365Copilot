from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .security_baseline_compliance_state import SecurityBaselineComplianceState
    from .security_baseline_setting_state import SecurityBaselineSettingState

from .entity import Entity

@dataclass
class SecurityBaselineState(Entity, Parsable):
    """
    Security baseline state for a device.
    """
    # The display name of the security baseline
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The security baseline template id
    security_baseline_template_id: Optional[str] = None
    # The security baseline state for different settings for a device
    setting_states: Optional[list[SecurityBaselineSettingState]] = None
    # Security Baseline Compliance State
    state: Optional[SecurityBaselineComplianceState] = None
    # User Principal Name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityBaselineState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .security_baseline_compliance_state import SecurityBaselineComplianceState
        from .security_baseline_setting_state import SecurityBaselineSettingState

        from .entity import Entity
        from .security_baseline_compliance_state import SecurityBaselineComplianceState
        from .security_baseline_setting_state import SecurityBaselineSettingState

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "securityBaselineTemplateId": lambda n : setattr(self, 'security_baseline_template_id', n.get_str_value()),
            "settingStates": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(SecurityBaselineSettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SecurityBaselineComplianceState)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("securityBaselineTemplateId", self.security_baseline_template_id)
        writer.write_collection_of_object_values("settingStates", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

