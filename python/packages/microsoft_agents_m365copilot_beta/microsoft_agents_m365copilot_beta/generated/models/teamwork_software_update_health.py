from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus

@dataclass
class TeamworkSoftwareUpdateHealth(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The software update available for the admin agent.
    admin_agent_software_update_status: Optional[TeamworkSoftwareUpdateStatus] = None
    # The software update available for the company portal.
    company_portal_software_update_status: Optional[TeamworkSoftwareUpdateStatus] = None
    # The software update available for the firmware.
    firmware_software_update_status: Optional[TeamworkSoftwareUpdateStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The software update available for the operating system.
    operating_system_software_update_status: Optional[TeamworkSoftwareUpdateStatus] = None
    # The software update available for the partner agent.
    partner_agent_software_update_status: Optional[TeamworkSoftwareUpdateStatus] = None
    # The software update available for the Teams client.
    teams_client_software_update_status: Optional[TeamworkSoftwareUpdateStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkSoftwareUpdateHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSoftwareUpdateHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkSoftwareUpdateHealth()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus

        from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus

        fields: dict[str, Callable[[Any], None]] = {
            "adminAgentSoftwareUpdateStatus": lambda n : setattr(self, 'admin_agent_software_update_status', n.get_object_value(TeamworkSoftwareUpdateStatus)),
            "companyPortalSoftwareUpdateStatus": lambda n : setattr(self, 'company_portal_software_update_status', n.get_object_value(TeamworkSoftwareUpdateStatus)),
            "firmwareSoftwareUpdateStatus": lambda n : setattr(self, 'firmware_software_update_status', n.get_object_value(TeamworkSoftwareUpdateStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystemSoftwareUpdateStatus": lambda n : setattr(self, 'operating_system_software_update_status', n.get_object_value(TeamworkSoftwareUpdateStatus)),
            "partnerAgentSoftwareUpdateStatus": lambda n : setattr(self, 'partner_agent_software_update_status', n.get_object_value(TeamworkSoftwareUpdateStatus)),
            "teamsClientSoftwareUpdateStatus": lambda n : setattr(self, 'teams_client_software_update_status', n.get_object_value(TeamworkSoftwareUpdateStatus)),
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
        writer.write_object_value("adminAgentSoftwareUpdateStatus", self.admin_agent_software_update_status)
        writer.write_object_value("companyPortalSoftwareUpdateStatus", self.company_portal_software_update_status)
        writer.write_object_value("firmwareSoftwareUpdateStatus", self.firmware_software_update_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("operatingSystemSoftwareUpdateStatus", self.operating_system_software_update_status)
        writer.write_object_value("partnerAgentSoftwareUpdateStatus", self.partner_agent_software_update_status)
        writer.write_object_value("teamsClientSoftwareUpdateStatus", self.teams_client_software_update_status)
        writer.write_additional_data_value(self.additional_data)
    

