from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

@dataclass
class CopilotPolicySettingAllowedAgentTypesValueObject(CopilotPolicySettingValueObject, Parsable):
    """
    The value of the microsoft.agent.allowedagenttypes policy setting.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.copilotPolicySettingAllowedAgentTypesValueObject"
    # Indicates whether independent software vendor (ISV) apps are allowed.
    are_i_s_v_apps_allowed: Optional[bool] = None
    # Indicates whether Microsoft apps are allowed.
    are_microsoft_apps_allowed: Optional[bool] = None
    # Indicates whether Microsoft-certified third-party apps are allowed.
    are_microsoft_certified_third_party_apps_allowed: Optional[bool] = None
    # Indicates whether tenant-scoped apps are allowed.
    are_tenant_scoped_apps_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPolicySettingAllowedAgentTypesValueObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPolicySettingAllowedAgentTypesValueObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPolicySettingAllowedAgentTypesValueObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

        from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

        fields: dict[str, Callable[[Any], None]] = {
            "areISVAppsAllowed": lambda n : setattr(self, 'are_i_s_v_apps_allowed', n.get_bool_value()),
            "areMicrosoftAppsAllowed": lambda n : setattr(self, 'are_microsoft_apps_allowed', n.get_bool_value()),
            "areMicrosoftCertifiedThirdPartyAppsAllowed": lambda n : setattr(self, 'are_microsoft_certified_third_party_apps_allowed', n.get_bool_value()),
            "areTenantScopedAppsAllowed": lambda n : setattr(self, 'are_tenant_scoped_apps_allowed', n.get_bool_value()),
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
        writer.write_bool_value("areISVAppsAllowed", self.are_i_s_v_apps_allowed)
        writer.write_bool_value("areMicrosoftAppsAllowed", self.are_microsoft_apps_allowed)
        writer.write_bool_value("areMicrosoftCertifiedThirdPartyAppsAllowed", self.are_microsoft_certified_third_party_apps_allowed)
        writer.write_bool_value("areTenantScopedAppsAllowed", self.are_tenant_scoped_apps_allowed)
    

