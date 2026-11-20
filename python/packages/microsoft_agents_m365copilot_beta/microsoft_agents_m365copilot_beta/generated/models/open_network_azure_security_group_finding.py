from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .finding import Finding
    from .inbound_ports import InboundPorts
    from .virtual_machine_details import VirtualMachineDetails

from .finding import Finding

@dataclass
class OpenNetworkAzureSecurityGroupFinding(Finding, Parsable):
    # The inboundPorts property
    inbound_ports: Optional[InboundPorts] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The securityGroup property
    security_group: Optional[AuthorizationSystemResource] = None
    # Represents a virtual machine in an authorization system.
    virtual_machines: Optional[list[VirtualMachineDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenNetworkAzureSecurityGroupFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenNetworkAzureSecurityGroupFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenNetworkAzureSecurityGroupFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .finding import Finding
        from .inbound_ports import InboundPorts
        from .virtual_machine_details import VirtualMachineDetails

        from .authorization_system_resource import AuthorizationSystemResource
        from .finding import Finding
        from .inbound_ports import InboundPorts
        from .virtual_machine_details import VirtualMachineDetails

        fields: dict[str, Callable[[Any], None]] = {
            "inboundPorts": lambda n : setattr(self, 'inbound_ports', n.get_object_value(InboundPorts)),
            "securityGroup": lambda n : setattr(self, 'security_group', n.get_object_value(AuthorizationSystemResource)),
            "virtualMachines": lambda n : setattr(self, 'virtual_machines', n.get_collection_of_object_values(VirtualMachineDetails)),
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
        writer.write_object_value("inboundPorts", self.inbound_ports)
        writer.write_object_value("securityGroup", self.security_group)
        writer.write_collection_of_object_values("virtualMachines", self.virtual_machines)
    

