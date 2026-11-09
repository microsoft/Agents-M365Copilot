from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_agents import ConditionalAccessAgents
    from .conditional_access_agent_context import ConditionalAccessAgentContext
    from .conditional_access_agent_id_risk_levels import ConditionalAccessAgentIdRiskLevels
    from .conditional_access_applications import ConditionalAccessApplications
    from .conditional_access_authentication_flows import ConditionalAccessAuthenticationFlows
    from .conditional_access_client_app import ConditionalAccessClientApp
    from .conditional_access_client_applications import ConditionalAccessClientApplications
    from .conditional_access_devices import ConditionalAccessDevices
    from .conditional_access_device_states import ConditionalAccessDeviceStates
    from .conditional_access_insider_risk_levels import ConditionalAccessInsiderRiskLevels
    from .conditional_access_locations import ConditionalAccessLocations
    from .conditional_access_platforms import ConditionalAccessPlatforms
    from .conditional_access_users import ConditionalAccessUsers
    from .risk_level import RiskLevel

@dataclass
class ConditionalAccessConditionSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The agentContext property
    agent_context: Optional[ConditionalAccessAgentContext] = None
    # Agent identity risk levels included in the policy. The possible values are: low, medium, high, unknownFutureValue. This enumeration is multivalued.
    agent_id_risk_levels: Optional[ConditionalAccessAgentIdRiskLevels] = None
    # The agents property
    agents: Optional[ConditionalAccessAgents] = None
    # Applications and user actions included in and excluded from the policy. Required.
    applications: Optional[ConditionalAccessApplications] = None
    # Authentication flows included in the policy scope. For more information, see Conditional Access: Authentication flows.
    authentication_flows: Optional[ConditionalAccessAuthenticationFlows] = None
    # Client application types included in the policy. The possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other. Required.  The easUnsupported enumeration member is deprecated in favor of exchangeActiveSync, which includes EAS supported and unsupported platforms.
    client_app_types: Optional[list[ConditionalAccessClientApp]] = None
    # Client applications (service principals and workload identities) included in and excluded from the policy. Either users or clientApplications is required.
    client_applications: Optional[ConditionalAccessClientApplications] = None
    # Device states in the policy. To be deprecated and removed. Use the devices property instead.
    device_states: Optional[ConditionalAccessDeviceStates] = None
    # Devices in the policy.
    devices: Optional[ConditionalAccessDevices] = None
    # Insider risk levels included in the policy. The possible values are: minor, moderate, elevated, unknownFutureValue.
    insider_risk_levels: Optional[ConditionalAccessInsiderRiskLevels] = None
    # Locations included in and excluded from the policy.
    locations: Optional[ConditionalAccessLocations] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Platforms included in and excluded from the policy.
    platforms: Optional[ConditionalAccessPlatforms] = None
    # Service principal risk levels included in the policy. The possible values are: low, medium, high, none, unknownFutureValue.
    service_principal_risk_levels: Optional[list[RiskLevel]] = None
    # Sign-in risk levels included in the policy. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
    sign_in_risk_levels: Optional[list[RiskLevel]] = None
    # User risk levels included in the policy. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
    user_risk_levels: Optional[list[RiskLevel]] = None
    # Users, groups, and roles included in and excluded from the policy. Either users or clientApplications is required.
    users: Optional[ConditionalAccessUsers] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessConditionSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessConditionSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_agents import ConditionalAccessAgents
        from .conditional_access_agent_context import ConditionalAccessAgentContext
        from .conditional_access_agent_id_risk_levels import ConditionalAccessAgentIdRiskLevels
        from .conditional_access_applications import ConditionalAccessApplications
        from .conditional_access_authentication_flows import ConditionalAccessAuthenticationFlows
        from .conditional_access_client_app import ConditionalAccessClientApp
        from .conditional_access_client_applications import ConditionalAccessClientApplications
        from .conditional_access_devices import ConditionalAccessDevices
        from .conditional_access_device_states import ConditionalAccessDeviceStates
        from .conditional_access_insider_risk_levels import ConditionalAccessInsiderRiskLevels
        from .conditional_access_locations import ConditionalAccessLocations
        from .conditional_access_platforms import ConditionalAccessPlatforms
        from .conditional_access_users import ConditionalAccessUsers
        from .risk_level import RiskLevel

        from .conditional_access_agents import ConditionalAccessAgents
        from .conditional_access_agent_context import ConditionalAccessAgentContext
        from .conditional_access_agent_id_risk_levels import ConditionalAccessAgentIdRiskLevels
        from .conditional_access_applications import ConditionalAccessApplications
        from .conditional_access_authentication_flows import ConditionalAccessAuthenticationFlows
        from .conditional_access_client_app import ConditionalAccessClientApp
        from .conditional_access_client_applications import ConditionalAccessClientApplications
        from .conditional_access_devices import ConditionalAccessDevices
        from .conditional_access_device_states import ConditionalAccessDeviceStates
        from .conditional_access_insider_risk_levels import ConditionalAccessInsiderRiskLevels
        from .conditional_access_locations import ConditionalAccessLocations
        from .conditional_access_platforms import ConditionalAccessPlatforms
        from .conditional_access_users import ConditionalAccessUsers
        from .risk_level import RiskLevel

        fields: dict[str, Callable[[Any], None]] = {
            "agentContext": lambda n : setattr(self, 'agent_context', n.get_object_value(ConditionalAccessAgentContext)),
            "agentIdRiskLevels": lambda n : setattr(self, 'agent_id_risk_levels', n.get_collection_of_enum_values(ConditionalAccessAgentIdRiskLevels)),
            "agents": lambda n : setattr(self, 'agents', n.get_object_value(ConditionalAccessAgents)),
            "applications": lambda n : setattr(self, 'applications', n.get_object_value(ConditionalAccessApplications)),
            "authenticationFlows": lambda n : setattr(self, 'authentication_flows', n.get_object_value(ConditionalAccessAuthenticationFlows)),
            "clientAppTypes": lambda n : setattr(self, 'client_app_types', n.get_collection_of_enum_values(ConditionalAccessClientApp)),
            "clientApplications": lambda n : setattr(self, 'client_applications', n.get_object_value(ConditionalAccessClientApplications)),
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_object_value(ConditionalAccessDeviceStates)),
            "devices": lambda n : setattr(self, 'devices', n.get_object_value(ConditionalAccessDevices)),
            "insiderRiskLevels": lambda n : setattr(self, 'insider_risk_levels', n.get_collection_of_enum_values(ConditionalAccessInsiderRiskLevels)),
            "locations": lambda n : setattr(self, 'locations', n.get_object_value(ConditionalAccessLocations)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_object_value(ConditionalAccessPlatforms)),
            "servicePrincipalRiskLevels": lambda n : setattr(self, 'service_principal_risk_levels', n.get_collection_of_enum_values(RiskLevel)),
            "signInRiskLevels": lambda n : setattr(self, 'sign_in_risk_levels', n.get_collection_of_enum_values(RiskLevel)),
            "userRiskLevels": lambda n : setattr(self, 'user_risk_levels', n.get_collection_of_enum_values(RiskLevel)),
            "users": lambda n : setattr(self, 'users', n.get_object_value(ConditionalAccessUsers)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("agentContext", self.agent_context)
        writer.write_enum_value("agentIdRiskLevels", self.agent_id_risk_levels)
        writer.write_object_value("agents", self.agents)
        writer.write_object_value("applications", self.applications)
        writer.write_object_value("authenticationFlows", self.authentication_flows)
        writer.write_collection_of_enum_values("clientAppTypes", self.client_app_types)
        writer.write_object_value("clientApplications", self.client_applications)
        writer.write_object_value("deviceStates", self.device_states)
        writer.write_object_value("devices", self.devices)
        writer.write_enum_value("insiderRiskLevels", self.insider_risk_levels)
        writer.write_object_value("locations", self.locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("platforms", self.platforms)
        writer.write_collection_of_enum_values("servicePrincipalRiskLevels", self.service_principal_risk_levels)
        writer.write_collection_of_enum_values("signInRiskLevels", self.sign_in_risk_levels)
        writer.write_collection_of_enum_values("userRiskLevels", self.user_risk_levels)
        writer.write_object_value("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

