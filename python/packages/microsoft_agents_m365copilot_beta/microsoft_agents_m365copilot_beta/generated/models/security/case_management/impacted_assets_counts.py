from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ImpactedAssetsCounts(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of impacted AI agents.
    ai_agents: Optional[int] = None
    # The number of impacted apps.
    apps: Optional[int] = None
    # The number of impacted cloud resources.
    cloud_resources: Optional[int] = None
    # The number of impacted files.
    files: Optional[int] = None
    # The number of impacted IP addresses.
    ips: Optional[int] = None
    # The number of impacted machines.
    machines: Optional[int] = None
    # The number of impacted mailboxes.
    mailboxes: Optional[int] = None
    # The number of impacted OAuth apps.
    oauth_apps: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of impacted processes.
    processes: Optional[int] = None
    # The number of impacted registry keys.
    registry_keys: Optional[int] = None
    # The number of impacted security groups.
    security_groups: Optional[int] = None
    # The total number of impacted assets.
    total: Optional[int] = None
    # The number of impacted URLs.
    urls: Optional[int] = None
    # The number of impacted users.
    users: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImpactedAssetsCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImpactedAssetsCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImpactedAssetsCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "aiAgents": lambda n : setattr(self, 'ai_agents', n.get_int_value()),
            "apps": lambda n : setattr(self, 'apps', n.get_int_value()),
            "cloudResources": lambda n : setattr(self, 'cloud_resources', n.get_int_value()),
            "files": lambda n : setattr(self, 'files', n.get_int_value()),
            "ips": lambda n : setattr(self, 'ips', n.get_int_value()),
            "machines": lambda n : setattr(self, 'machines', n.get_int_value()),
            "mailboxes": lambda n : setattr(self, 'mailboxes', n.get_int_value()),
            "oauthApps": lambda n : setattr(self, 'oauth_apps', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processes": lambda n : setattr(self, 'processes', n.get_int_value()),
            "registryKeys": lambda n : setattr(self, 'registry_keys', n.get_int_value()),
            "securityGroups": lambda n : setattr(self, 'security_groups', n.get_int_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
            "urls": lambda n : setattr(self, 'urls', n.get_int_value()),
            "users": lambda n : setattr(self, 'users', n.get_int_value()),
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
        writer.write_int_value("aiAgents", self.ai_agents)
        writer.write_int_value("apps", self.apps)
        writer.write_int_value("cloudResources", self.cloud_resources)
        writer.write_int_value("files", self.files)
        writer.write_int_value("ips", self.ips)
        writer.write_int_value("machines", self.machines)
        writer.write_int_value("mailboxes", self.mailboxes)
        writer.write_int_value("oauthApps", self.oauth_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("processes", self.processes)
        writer.write_int_value("registryKeys", self.registry_keys)
        writer.write_int_value("securityGroups", self.security_groups)
        writer.write_int_value("total", self.total)
        writer.write_int_value("urls", self.urls)
        writer.write_int_value("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

