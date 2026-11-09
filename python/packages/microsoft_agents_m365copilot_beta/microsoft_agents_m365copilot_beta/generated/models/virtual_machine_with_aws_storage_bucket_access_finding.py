from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .aws_role import AwsRole
    from .finding import Finding
    from .permissions_creep_index import PermissionsCreepIndex

from .finding import Finding

@dataclass
class VirtualMachineWithAwsStorageBucketAccessFinding(Finding, Parsable):
    # The total number of storage buckets that the EC2 instance can access using the role.
    accessible_count: Optional[int] = None
    # The total number of storage buckets in the authorization system that hosts the EC2 instance.
    bucket_count: Optional[int] = None
    # The ec2Instance property
    ec2_instance: Optional[AuthorizationSystemResource] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    # The role property
    role: Optional[AwsRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualMachineWithAwsStorageBucketAccessFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualMachineWithAwsStorageBucketAccessFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualMachineWithAwsStorageBucketAccessFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .aws_role import AwsRole
        from .finding import Finding
        from .permissions_creep_index import PermissionsCreepIndex

        from .authorization_system_resource import AuthorizationSystemResource
        from .aws_role import AwsRole
        from .finding import Finding
        from .permissions_creep_index import PermissionsCreepIndex

        fields: dict[str, Callable[[Any], None]] = {
            "accessibleCount": lambda n : setattr(self, 'accessible_count', n.get_int_value()),
            "bucketCount": lambda n : setattr(self, 'bucket_count', n.get_int_value()),
            "ec2Instance": lambda n : setattr(self, 'ec2_instance', n.get_object_value(AuthorizationSystemResource)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
            "role": lambda n : setattr(self, 'role', n.get_object_value(AwsRole)),
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
        writer.write_int_value("accessibleCount", self.accessible_count)
        writer.write_int_value("bucketCount", self.bucket_count)
        writer.write_object_value("ec2Instance", self.ec2_instance)
        writer.write_object_value("permissionsCreepIndex", self.permissions_creep_index)
        writer.write_object_value("role", self.role)
    

