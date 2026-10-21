from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comanagement_eligible_type import ComanagementEligibleType
    from .device_registration_state import DeviceRegistrationState
    from .device_type import DeviceType
    from .entity import Entity
    from .management_agent_type import ManagementAgentType
    from .management_state import ManagementState
    from .owner_type import OwnerType

from .entity import Entity

@dataclass
class ComanagementEligibleDevice(Entity, Parsable):
    """
    Device Co-Management eligibility state
    """
    # Device registration status.
    client_registration_status: Optional[DeviceRegistrationState] = None
    # DeviceName
    device_name: Optional[str] = None
    # Device type.
    device_type: Optional[DeviceType] = None
    # EntitySource
    entity_source: Optional[int] = None
    # Management agent type.
    management_agents: Optional[ManagementAgentType] = None
    # Management state of device in Microsoft Intune.
    management_state: Optional[ManagementState] = None
    # Manufacturer
    manufacturer: Optional[str] = None
    # MDMStatus
    mdm_status: Optional[str] = None
    # Model
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # OSDescription
    os_description: Optional[str] = None
    # OSVersion
    os_version: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[OwnerType] = None
    # ReferenceId
    reference_id: Optional[str] = None
    # SerialNumber
    serial_number: Optional[str] = None
    # The status property
    status: Optional[ComanagementEligibleType] = None
    # UPN
    upn: Optional[str] = None
    # UserEmail
    user_email: Optional[str] = None
    # UserId
    user_id: Optional[str] = None
    # UserName
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComanagementEligibleDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComanagementEligibleDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComanagementEligibleDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .comanagement_eligible_type import ComanagementEligibleType
        from .device_registration_state import DeviceRegistrationState
        from .device_type import DeviceType
        from .entity import Entity
        from .management_agent_type import ManagementAgentType
        from .management_state import ManagementState
        from .owner_type import OwnerType

        from .comanagement_eligible_type import ComanagementEligibleType
        from .device_registration_state import DeviceRegistrationState
        from .device_type import DeviceType
        from .entity import Entity
        from .management_agent_type import ManagementAgentType
        from .management_state import ManagementState
        from .owner_type import OwnerType

        fields: dict[str, Callable[[Any], None]] = {
            "clientRegistrationStatus": lambda n : setattr(self, 'client_registration_status', n.get_enum_value(DeviceRegistrationState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(DeviceType)),
            "entitySource": lambda n : setattr(self, 'entity_source', n.get_int_value()),
            "managementAgents": lambda n : setattr(self, 'management_agents', n.get_enum_value(ManagementAgentType)),
            "managementState": lambda n : setattr(self, 'management_state', n.get_enum_value(ManagementState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "mdmStatus": lambda n : setattr(self, 'mdm_status', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(OwnerType)),
            "referenceId": lambda n : setattr(self, 'reference_id', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ComanagementEligibleType)),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_enum_value("clientRegistrationStatus", self.client_registration_status)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_int_value("entitySource", self.entity_source)
        writer.write_enum_value("managementAgents", self.management_agents)
        writer.write_enum_value("managementState", self.management_state)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("mdmStatus", self.mdm_status)
        writer.write_str_value("model", self.model)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_str_value("referenceId", self.reference_id)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("upn", self.upn)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
    

