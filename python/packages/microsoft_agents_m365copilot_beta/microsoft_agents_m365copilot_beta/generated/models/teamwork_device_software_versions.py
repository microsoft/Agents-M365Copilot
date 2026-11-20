from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkDeviceSoftwareVersions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The software version for the admin agent running on the device.
    admin_agent_software_version: Optional[str] = None
    # The software version for the firmware running on the device.
    firmware_software_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The software version for the operating system on the device.
    operating_system_software_version: Optional[str] = None
    # The software version for the partner agent running on the device.
    partner_agent_software_version: Optional[str] = None
    # The software version for the Teams client running on the device.
    teams_client_software_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDeviceSoftwareVersions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceSoftwareVersions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDeviceSoftwareVersions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "adminAgentSoftwareVersion": lambda n : setattr(self, 'admin_agent_software_version', n.get_str_value()),
            "firmwareSoftwareVersion": lambda n : setattr(self, 'firmware_software_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystemSoftwareVersion": lambda n : setattr(self, 'operating_system_software_version', n.get_str_value()),
            "partnerAgentSoftwareVersion": lambda n : setattr(self, 'partner_agent_software_version', n.get_str_value()),
            "teamsClientSoftwareVersion": lambda n : setattr(self, 'teams_client_software_version', n.get_str_value()),
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
        writer.write_str_value("adminAgentSoftwareVersion", self.admin_agent_software_version)
        writer.write_str_value("firmwareSoftwareVersion", self.firmware_software_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystemSoftwareVersion", self.operating_system_software_version)
        writer.write_str_value("partnerAgentSoftwareVersion", self.partner_agent_software_version)
        writer.write_str_value("teamsClientSoftwareVersion", self.teams_client_software_version)
        writer.write_additional_data_value(self.additional_data)
    

