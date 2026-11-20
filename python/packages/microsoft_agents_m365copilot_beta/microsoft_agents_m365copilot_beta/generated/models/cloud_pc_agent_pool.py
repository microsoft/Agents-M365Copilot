from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_agent_pool_billing_configuration import CloudPcAgentPoolBillingConfiguration
    from .cloud_pc_agent_pool_capability_configuration import CloudPcAgentPoolCapabilityConfiguration
    from .cloud_pc_agent_pool_scaling_policy import CloudPcAgentPoolScalingPolicy
    from .cloud_pc_agent_pool_session_usage import CloudPcAgentPoolSessionUsage
    from .cloud_pc_pool import CloudPcPool

from .cloud_pc_pool import CloudPcPool

@dataclass
class CloudPcAgentPool(CloudPcPool, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcAgentPool"
    # The billingConfiguration property
    billing_configuration: Optional[CloudPcAgentPoolBillingConfiguration] = None
    # The capabilities property
    capabilities: Optional[CloudPcAgentPoolCapabilityConfiguration] = None
    # The endpoint URL used to check out and check in agent sessions. This value becomes available after the pool reaches the active status. Read-only.
    pool_url: Optional[str] = None
    # The scalingPolicy property
    scaling_policy: Optional[CloudPcAgentPoolScalingPolicy] = None
    # The sessionUsage property
    session_usage: Optional[CloudPcAgentPoolSessionUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAgentPool:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAgentPool
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAgentPool()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_agent_pool_billing_configuration import CloudPcAgentPoolBillingConfiguration
        from .cloud_pc_agent_pool_capability_configuration import CloudPcAgentPoolCapabilityConfiguration
        from .cloud_pc_agent_pool_scaling_policy import CloudPcAgentPoolScalingPolicy
        from .cloud_pc_agent_pool_session_usage import CloudPcAgentPoolSessionUsage
        from .cloud_pc_pool import CloudPcPool

        from .cloud_pc_agent_pool_billing_configuration import CloudPcAgentPoolBillingConfiguration
        from .cloud_pc_agent_pool_capability_configuration import CloudPcAgentPoolCapabilityConfiguration
        from .cloud_pc_agent_pool_scaling_policy import CloudPcAgentPoolScalingPolicy
        from .cloud_pc_agent_pool_session_usage import CloudPcAgentPoolSessionUsage
        from .cloud_pc_pool import CloudPcPool

        fields: dict[str, Callable[[Any], None]] = {
            "billingConfiguration": lambda n : setattr(self, 'billing_configuration', n.get_object_value(CloudPcAgentPoolBillingConfiguration)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(CloudPcAgentPoolCapabilityConfiguration)),
            "poolUrl": lambda n : setattr(self, 'pool_url', n.get_str_value()),
            "scalingPolicy": lambda n : setattr(self, 'scaling_policy', n.get_object_value(CloudPcAgentPoolScalingPolicy)),
            "sessionUsage": lambda n : setattr(self, 'session_usage', n.get_object_value(CloudPcAgentPoolSessionUsage)),
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
        writer.write_object_value("billingConfiguration", self.billing_configuration)
        writer.write_object_value("capabilities", self.capabilities)
        writer.write_str_value("poolUrl", self.pool_url)
        writer.write_object_value("scalingPolicy", self.scaling_policy)
        writer.write_object_value("sessionUsage", self.session_usage)
    

