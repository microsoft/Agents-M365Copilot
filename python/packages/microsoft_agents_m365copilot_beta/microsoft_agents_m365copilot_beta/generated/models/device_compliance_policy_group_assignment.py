from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_policy import DeviceCompliancePolicy
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceCompliancePolicyGroupAssignment(Entity, Parsable):
    """
    Device compliance policy group assignment.
    """
    # The navigation link to the  device compliance polic targeted.
    device_compliance_policy: Optional[DeviceCompliancePolicy] = None
    # Indicates if this group is should be excluded. Defaults that the group should be included
    exclude_group: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Id of the AAD group we are targeting the device compliance policy to.
    target_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceCompliancePolicyGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyGroupAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceCompliancePolicyGroupAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_policy import DeviceCompliancePolicy
        from .entity import Entity

        from .device_compliance_policy import DeviceCompliancePolicy
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceCompliancePolicy": lambda n : setattr(self, 'device_compliance_policy', n.get_object_value(DeviceCompliancePolicy)),
            "excludeGroup": lambda n : setattr(self, 'exclude_group', n.get_bool_value()),
            "targetGroupId": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
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
        writer.write_object_value("deviceCompliancePolicy", self.device_compliance_policy)
        writer.write_bool_value("excludeGroup", self.exclude_group)
        writer.write_str_value("targetGroupId", self.target_group_id)
    

