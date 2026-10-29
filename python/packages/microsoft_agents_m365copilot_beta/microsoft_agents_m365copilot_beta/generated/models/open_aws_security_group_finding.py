from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_compute_instance_details import AssignedComputeInstanceDetails
    from .aws_authorization_system_resource import AwsAuthorizationSystemResource
    from .finding import Finding
    from .inbound_ports import InboundPorts

from .finding import Finding

@dataclass
class OpenAwsSecurityGroupFinding(Finding, Parsable):
    # A set of AWS EC2 compute instances related to this open security group.
    assigned_compute_instances_details: Optional[list[AssignedComputeInstanceDetails]] = None
    # The inboundPorts property
    inbound_ports: Optional[InboundPorts] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The securityGroup property
    security_group: Optional[AwsAuthorizationSystemResource] = None
    # The number of storage buckets accessed by the assigned compute instances.
    total_storage_bucket_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenAwsSecurityGroupFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenAwsSecurityGroupFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenAwsSecurityGroupFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_compute_instance_details import AssignedComputeInstanceDetails
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .finding import Finding
        from .inbound_ports import InboundPorts

        from .assigned_compute_instance_details import AssignedComputeInstanceDetails
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .finding import Finding
        from .inbound_ports import InboundPorts

        fields: dict[str, Callable[[Any], None]] = {
            "assignedComputeInstancesDetails": lambda n : setattr(self, 'assigned_compute_instances_details', n.get_collection_of_object_values(AssignedComputeInstanceDetails)),
            "inboundPorts": lambda n : setattr(self, 'inbound_ports', n.get_object_value(InboundPorts)),
            "securityGroup": lambda n : setattr(self, 'security_group', n.get_object_value(AwsAuthorizationSystemResource)),
            "totalStorageBucketCount": lambda n : setattr(self, 'total_storage_bucket_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignedComputeInstancesDetails", self.assigned_compute_instances_details)
        writer.write_object_value("inboundPorts", self.inbound_ports)
        writer.write_object_value("securityGroup", self.security_group)
        writer.write_int_value("totalStorageBucketCount", self.total_storage_bucket_count)
    

