from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary(Entity, Parsable):
    """
    Contains properties for the deployment summary of a WindowsDefenderApplicationControl supplemental policy.
    """
    # Number of Devices that have successfully deployed this WindowsDefenderApplicationControl supplemental policy.
    deployed_device_count: Optional[int] = None
    # Number of Devices that have failed to deploy this WindowsDefenderApplicationControl supplemental policy.
    failed_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deployedDeviceCount": lambda n : setattr(self, 'deployed_device_count', n.get_int_value()),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
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
        writer.write_int_value("deployedDeviceCount", self.deployed_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
    

