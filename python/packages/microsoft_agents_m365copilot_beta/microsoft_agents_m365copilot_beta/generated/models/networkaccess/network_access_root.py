from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert import Alert
    from .cloud_firewall_policy import CloudFirewallPolicy
    from .connectivity import Connectivity
    from .filtering_policy import FilteringPolicy
    from .filtering_profile import FilteringProfile
    from .forwarding_policy import ForwardingPolicy
    from .forwarding_profile import ForwardingProfile
    from .logs import Logs
    from .reports import Reports
    from .settings import Settings
    from .tenant_status import TenantStatus
    from .threat_intelligence_policy import ThreatIntelligencePolicy
    from .tls_inspection_policy import TlsInspectionPolicy
    from .tls_termination import TlsTermination

from ..entity import Entity

@dataclass
class NetworkAccessRoot(Entity, Parsable):
    # The alerts property
    alerts: Optional[list[Alert]] = None
    # A collection of cloud firewall policies that define rules for managing network traffic through the Global Secure Access services.
    cloud_firewall_policies: Optional[list[CloudFirewallPolicy]] = None
    # Connectivity represents all the connectivity components in Global Secure Access.
    connectivity: Optional[Connectivity] = None
    # A filtering policy defines the specific traffic that is allowed or blocked through the Global Secure Access services for a filtering profile.
    filtering_policies: Optional[list[FilteringPolicy]] = None
    # A filtering profile associates network access policies with Microsoft Entra ID Conditional Access policies, so that access policies can be applied to users and groups.
    filtering_profiles: Optional[list[FilteringProfile]] = None
    # The forwardingPolicies property
    forwarding_policies: Optional[list[ForwardingPolicy]] = None
    # The forwardingProfiles property
    forwarding_profiles: Optional[list[ForwardingProfile]] = None
    # Represents network connections that are routed through Global Secure Access.
    logs: Optional[Logs] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the status of the Global Secure Access services for the tenant.
    reports: Optional[Reports] = None
    # Global Secure Access settings.
    settings: Optional[Settings] = None
    # Represents the status of the Global Secure Access services for the tenant.
    tenant_status: Optional[TenantStatus] = None
    # The threatIntelligencePolicies property
    threat_intelligence_policies: Optional[list[ThreatIntelligencePolicy]] = None
    # A container for tenant-level TLS inspection settings for Global Secure Access.
    tls: Optional[TlsTermination] = None
    # Allows you to configure TLS termination for your organization's network traffic through Global Secure Access.
    tls_inspection_policies: Optional[list[TlsInspectionPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkAccessRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkAccessRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert import Alert
        from .cloud_firewall_policy import CloudFirewallPolicy
        from .connectivity import Connectivity
        from .filtering_policy import FilteringPolicy
        from .filtering_profile import FilteringProfile
        from .forwarding_policy import ForwardingPolicy
        from .forwarding_profile import ForwardingProfile
        from .logs import Logs
        from .reports import Reports
        from .settings import Settings
        from .tenant_status import TenantStatus
        from .threat_intelligence_policy import ThreatIntelligencePolicy
        from .tls_inspection_policy import TlsInspectionPolicy
        from .tls_termination import TlsTermination

        from ..entity import Entity
        from .alert import Alert
        from .cloud_firewall_policy import CloudFirewallPolicy
        from .connectivity import Connectivity
        from .filtering_policy import FilteringPolicy
        from .filtering_profile import FilteringProfile
        from .forwarding_policy import ForwardingPolicy
        from .forwarding_profile import ForwardingProfile
        from .logs import Logs
        from .reports import Reports
        from .settings import Settings
        from .tenant_status import TenantStatus
        from .threat_intelligence_policy import ThreatIntelligencePolicy
        from .tls_inspection_policy import TlsInspectionPolicy
        from .tls_termination import TlsTermination

        fields: dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(Alert)),
            "cloudFirewallPolicies": lambda n : setattr(self, 'cloud_firewall_policies', n.get_collection_of_object_values(CloudFirewallPolicy)),
            "connectivity": lambda n : setattr(self, 'connectivity', n.get_object_value(Connectivity)),
            "filteringPolicies": lambda n : setattr(self, 'filtering_policies', n.get_collection_of_object_values(FilteringPolicy)),
            "filteringProfiles": lambda n : setattr(self, 'filtering_profiles', n.get_collection_of_object_values(FilteringProfile)),
            "forwardingPolicies": lambda n : setattr(self, 'forwarding_policies', n.get_collection_of_object_values(ForwardingPolicy)),
            "forwardingProfiles": lambda n : setattr(self, 'forwarding_profiles', n.get_collection_of_object_values(ForwardingProfile)),
            "logs": lambda n : setattr(self, 'logs', n.get_object_value(Logs)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(Reports)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(Settings)),
            "tenantStatus": lambda n : setattr(self, 'tenant_status', n.get_object_value(TenantStatus)),
            "threatIntelligencePolicies": lambda n : setattr(self, 'threat_intelligence_policies', n.get_collection_of_object_values(ThreatIntelligencePolicy)),
            "tls": lambda n : setattr(self, 'tls', n.get_object_value(TlsTermination)),
            "tlsInspectionPolicies": lambda n : setattr(self, 'tls_inspection_policies', n.get_collection_of_object_values(TlsInspectionPolicy)),
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
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_collection_of_object_values("cloudFirewallPolicies", self.cloud_firewall_policies)
        writer.write_object_value("connectivity", self.connectivity)
        writer.write_collection_of_object_values("filteringPolicies", self.filtering_policies)
        writer.write_collection_of_object_values("filteringProfiles", self.filtering_profiles)
        writer.write_collection_of_object_values("forwardingPolicies", self.forwarding_policies)
        writer.write_collection_of_object_values("forwardingProfiles", self.forwarding_profiles)
        writer.write_object_value("logs", self.logs)
        writer.write_object_value("reports", self.reports)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("tenantStatus", self.tenant_status)
        writer.write_collection_of_object_values("threatIntelligencePolicies", self.threat_intelligence_policies)
        writer.write_object_value("tls", self.tls)
        writer.write_collection_of_object_values("tlsInspectionPolicies", self.tls_inspection_policies)
    

