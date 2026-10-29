from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_external_partner_agent_setting import CloudPcExternalPartnerAgentSetting
    from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcExternalPartner(Entity, Parsable):
    # The agent settings associated with the external partner.
    agent_setting: Optional[CloudPcExternalPartnerAgentSetting] = None
    # The connectionStatus property
    connection_status: Optional[CloudPcExternalPartnerStatus] = None
    # Enable or disable the connection to an external partner. If true, an external partner API accepts incoming calls from external partners. Required. Supports $filter (eq).
    enable_connection: Optional[bool] = None
    # Last data sync time for this external partner. The timeStamp type represents date and time information in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The partner identifier used to identify the external partner. When the Cloud PC service is ready to integrate with a new external partner, it generates a GUID to represent this partner. The Cloud PC service provides this partner ID to the partner, which can then use it to call this Microsoft Graph API and external partner APIs. Read-only.
    partner_id: Optional[str] = None
    # Status details message. Read-only.
    status_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcExternalPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcExternalPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcExternalPartner()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_external_partner_agent_setting import CloudPcExternalPartnerAgentSetting
        from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
        from .entity import Entity

        from .cloud_pc_external_partner_agent_setting import CloudPcExternalPartnerAgentSetting
        from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "agentSetting": lambda n : setattr(self, 'agent_setting', n.get_object_value(CloudPcExternalPartnerAgentSetting)),
            "connectionStatus": lambda n : setattr(self, 'connection_status', n.get_enum_value(CloudPcExternalPartnerStatus)),
            "enableConnection": lambda n : setattr(self, 'enable_connection', n.get_bool_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "partnerId": lambda n : setattr(self, 'partner_id', n.get_str_value()),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_str_value()),
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
        writer.write_object_value("agentSetting", self.agent_setting)
        writer.write_enum_value("connectionStatus", self.connection_status)
        writer.write_bool_value("enableConnection", self.enable_connection)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("partnerId", self.partner_id)
        writer.write_str_value("statusDetails", self.status_details)
    

