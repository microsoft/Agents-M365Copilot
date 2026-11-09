from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcExternalPartnerAgentSetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The hash value of agent file by sha256 algorithm.
    agent_sha256: Optional[str] = None
    # The download link url of the agent, when admin sets this url, then partner can call deploy agent API to deploy this agent to targeted Cloud PCs. The format is like this: https://www.external-partner.com/resources/agents/exampleAgentFile.exe
    agent_url: Optional[str] = None
    # Indicates whether partner agent auto deployment is enabled. When true, then the partner agent will be deployed after the Cloud PC is provisioned. When false, auto deployment isn't performed. Default value is false
    auto_deployment_enabled: Optional[bool] = None
    # The install command parameters to run the agent install command. The format is like this: ['/p paramValue', '/quiet']
    install_parameters: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcExternalPartnerAgentSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcExternalPartnerAgentSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcExternalPartnerAgentSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "agentSha256": lambda n : setattr(self, 'agent_sha256', n.get_str_value()),
            "agentUrl": lambda n : setattr(self, 'agent_url', n.get_str_value()),
            "autoDeploymentEnabled": lambda n : setattr(self, 'auto_deployment_enabled', n.get_bool_value()),
            "installParameters": lambda n : setattr(self, 'install_parameters', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("agentSha256", self.agent_sha256)
        writer.write_str_value("agentUrl", self.agent_url)
        writer.write_bool_value("autoDeploymentEnabled", self.auto_deployment_enabled)
        writer.write_collection_of_primitive_values("installParameters", self.install_parameters)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

