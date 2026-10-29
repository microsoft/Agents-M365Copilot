from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
    from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName

@dataclass
class CloudPcPartnerAgentInstallResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains a detailed error message when the partner agent installation failed.
    error_message: Optional[str] = None
    # The status of a partner agent installation. The possible values are: installed, installFailed, installing, uninstalling, uninstallFailed and licensed. Read-Only.
    install_status: Optional[CloudPcPartnerAgentInstallStatus] = None
    # Indicates whether the partner agent is a third party. When true, the agent is a third-party (non-Microsoft) agent and when false, the agent is a Microsoft agent or isn't known.  The default value is false.
    is_third_party_partner: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the first-party or third-party partner agent. Possible values for third-party partners are Citrix, VMware and HP. Read-Only.
    partner_agent_name: Optional[CloudPcPartnerAgentName] = None
    # Indicates whether the partner agent installation should be retried. The default value is false.
    retriable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcPartnerAgentInstallResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcPartnerAgentInstallResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcPartnerAgentInstallResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
        from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName

        from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
        from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName

        fields: dict[str, Callable[[Any], None]] = {
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "installStatus": lambda n : setattr(self, 'install_status', n.get_enum_value(CloudPcPartnerAgentInstallStatus)),
            "isThirdPartyPartner": lambda n : setattr(self, 'is_third_party_partner', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partnerAgentName": lambda n : setattr(self, 'partner_agent_name', n.get_enum_value(CloudPcPartnerAgentName)),
            "retriable": lambda n : setattr(self, 'retriable', n.get_bool_value()),
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
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_enum_value("installStatus", self.install_status)
        writer.write_bool_value("isThirdPartyPartner", self.is_third_party_partner)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("partnerAgentName", self.partner_agent_name)
        writer.write_bool_value("retriable", self.retriable)
        writer.write_additional_data_value(self.additional_data)
    

