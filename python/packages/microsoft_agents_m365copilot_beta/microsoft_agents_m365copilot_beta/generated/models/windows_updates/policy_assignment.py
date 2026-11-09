from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .device_profile import DeviceProfile

from ..entity import Entity

@dataclass
class PolicyAssignment(Entity, Parsable):
    # The Microsoft Entra identifier of the assigned device. Read-only.
    azure_ad_device_id: Optional[str] = None
    # The deviceProfile property
    device_profile: Optional[DeviceProfile] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the assigned Windows Autopatch policy. Read-only.
    policy_id: Optional[str] = None
    # The display name of the assigned Windows Autopatch policy. Read-only.
    policy_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .device_profile import DeviceProfile

        from ..entity import Entity
        from .device_profile import DeviceProfile

        fields: dict[str, Callable[[Any], None]] = {
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "deviceProfile": lambda n : setattr(self, 'device_profile', n.get_object_value(DeviceProfile)),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
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
        writer.write_object_value("deviceProfile", self.device_profile)
    

