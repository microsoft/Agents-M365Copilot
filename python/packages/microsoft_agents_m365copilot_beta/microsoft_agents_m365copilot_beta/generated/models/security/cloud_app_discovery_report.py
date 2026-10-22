from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .entity_type import EntityType
    from .log_data_provider import LogDataProvider
    from .receiver_protocol import ReceiverProtocol
    from .traffic_type import TrafficType

from ..entity import Entity

@dataclass
class CloudAppDiscoveryReport(Entity, Parsable):
    # Use 1 if the machine information is anonymized; otherwise use 0.
    anonymize_machine_data: Optional[bool] = None
    # Use 1 if the user information is anonymized; otherwise use 0.
    anonymize_user_data: Optional[bool] = None
    # The date in the format specified. The Timestamp represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # A comment or description for the report.
    description: Optional[str] = None
    # The display name of the continuous report.
    display_name: Optional[str] = None
    # Use 1 for a snapshot report; otherwise use 0.
    is_snapshot_report: Optional[bool] = None
    # The date when the data was last received. The Timestamp represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_data_received_date_time: Optional[datetime.datetime] = None
    # The date when the continuous report was last modified. The Timestamp represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The applicable log data provider. The possible values are: barracuda, bluecoat, checkpoint, ciscoAsa, ciscoIronportProxy, fortigate, paloAlto, squid, zscaler, mcafeeSwg, ciscoScanSafe, juniperSrx, sophosSg, websenseV75, websenseSiemCef, machineZoneMeraki, squidNative, ciscoFwsm, microsoftIsaW3C, sonicwall, sophosCyberoam, clavister, customParser, juniperSsg, zscalerQradar, juniperSrxSd, juniperSrxWelf, microsoftConditionalAppAccess, ciscoAsaFirepower, genericCef, genericLeef, genericW3C, iFilter, checkpointXml, checkpointSmartViewTracker, barracudaNextGenFw, barracudaNextGenFwWeblog, microsoftDefenderForEndpoint, zscalerCef, sophosXg, iboss, forcepoint, fortios, ciscoIronportWsaIi, paloAltoLeef, forcepointLeef, stormshield, contentkeeper, ciscoIronportWsaIii, checkpointCef, corrata, ciscoFirepowerV6, menloSecurityCef, watchguardXtm, openSystemsSecureWebGateway, wandera, unknownFutureValue.
    log_data_provider: Optional[LogDataProvider] = None
    # The count of log files history.
    log_file_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The applicable receiver protocol. The possible values are: ftp, ftps, syslogUdp, syslogTcp, syslogTls, unknownFutureValue.
    receiver_protocol: Optional[ReceiverProtocol] = None
    # The supported entity type. The possible values are: userName, ipAddress, machineName, other, unknown, unknownFutureValue.
    supported_entity_types: Optional[list[EntityType]] = None
    # The supported traffic type. The possible values are: downloadedBytes, uploadedBytes, unknown, unknownFutureValue.
    supported_traffic_types: Optional[list[TrafficType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudAppDiscoveryReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppDiscoveryReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudAppDiscoveryReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .entity_type import EntityType
        from .log_data_provider import LogDataProvider
        from .receiver_protocol import ReceiverProtocol
        from .traffic_type import TrafficType

        from ..entity import Entity
        from .entity_type import EntityType
        from .log_data_provider import LogDataProvider
        from .receiver_protocol import ReceiverProtocol
        from .traffic_type import TrafficType

        fields: dict[str, Callable[[Any], None]] = {
            "anonymizeMachineData": lambda n : setattr(self, 'anonymize_machine_data', n.get_bool_value()),
            "anonymizeUserData": lambda n : setattr(self, 'anonymize_user_data', n.get_bool_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isSnapshotReport": lambda n : setattr(self, 'is_snapshot_report', n.get_bool_value()),
            "lastDataReceivedDateTime": lambda n : setattr(self, 'last_data_received_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "logDataProvider": lambda n : setattr(self, 'log_data_provider', n.get_enum_value(LogDataProvider)),
            "logFileCount": lambda n : setattr(self, 'log_file_count', n.get_int_value()),
            "receiverProtocol": lambda n : setattr(self, 'receiver_protocol', n.get_enum_value(ReceiverProtocol)),
            "supportedEntityTypes": lambda n : setattr(self, 'supported_entity_types', n.get_collection_of_enum_values(EntityType)),
            "supportedTrafficTypes": lambda n : setattr(self, 'supported_traffic_types', n.get_collection_of_enum_values(TrafficType)),
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
        writer.write_bool_value("anonymizeMachineData", self.anonymize_machine_data)
        writer.write_bool_value("anonymizeUserData", self.anonymize_user_data)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isSnapshotReport", self.is_snapshot_report)
        writer.write_datetime_value("lastDataReceivedDateTime", self.last_data_received_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("logDataProvider", self.log_data_provider)
        writer.write_int_value("logFileCount", self.log_file_count)
        writer.write_enum_value("receiverProtocol", self.receiver_protocol)
        writer.write_collection_of_enum_values("supportedEntityTypes", self.supported_entity_types)
        writer.write_collection_of_enum_values("supportedTrafficTypes", self.supported_traffic_types)
    

