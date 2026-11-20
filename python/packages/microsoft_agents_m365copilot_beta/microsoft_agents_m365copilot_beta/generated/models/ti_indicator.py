from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .diamond_model import DiamondModel
    from .entity import Entity
    from .file_hash_type import FileHashType
    from .ti_action import TiAction
    from .tlp_level import TlpLevel

from .entity import Entity

@dataclass
class TiIndicator(Entity, Parsable):
    # The action to apply if the indicator is matched from within the targetProduct security tool. The possible values are: unknown, allow, block, alert. Required.
    action: Optional[TiAction] = None
    # The cyber threat intelligence name(s) for the parties responsible for the malicious activity covered by the threat indicator.
    activity_group_names: Optional[list[str]] = None
    # A catchall area for extra data from the indicator that is not specifically covered by other tiIndicator properties. The security tool specified by targetProduct typically does not utilize this data.
    additional_information: Optional[str] = None
    # Stamped by the system when the indicator is ingested. The Microsoft Entra tenant id of submitting client. Required.
    azure_tenant_id: Optional[str] = None
    # An integer representing the confidence the data within the indicator accurately identifies malicious behavior. Acceptable values are 0 – 100 with 100 being the highest.
    confidence: Optional[int] = None
    # Brief description (100 characters or less) of the threat represented by the indicator. Required.
    description: Optional[str] = None
    # The area of the Diamond Model in which this indicator exists. The possible values are: unknown, adversary, capability, infrastructure, victim.
    diamond_model: Optional[DiamondModel] = None
    # The domainName property
    domain_name: Optional[str] = None
    # The emailEncoding property
    email_encoding: Optional[str] = None
    # The emailLanguage property
    email_language: Optional[str] = None
    # The emailRecipient property
    email_recipient: Optional[str] = None
    # The emailSenderAddress property
    email_sender_address: Optional[str] = None
    # The emailSenderName property
    email_sender_name: Optional[str] = None
    # The emailSourceDomain property
    email_source_domain: Optional[str] = None
    # The emailSourceIpAddress property
    email_source_ip_address: Optional[str] = None
    # The emailSubject property
    email_subject: Optional[str] = None
    # The emailXMailer property
    email_x_mailer: Optional[str] = None
    # DateTime string indicating when the Indicator expires. All indicators must have an expiration date to avoid stale indicators persisting in the system. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
    expiration_date_time: Optional[datetime.datetime] = None
    # An identification number that ties the indicator back to the indicator provider’s system (for example, a foreign key).
    external_id: Optional[str] = None
    # The fileCompileDateTime property
    file_compile_date_time: Optional[datetime.datetime] = None
    # The fileCreatedDateTime property
    file_created_date_time: Optional[datetime.datetime] = None
    # The fileHashType property
    file_hash_type: Optional[FileHashType] = None
    # The fileHashValue property
    file_hash_value: Optional[str] = None
    # The fileMutexName property
    file_mutex_name: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    # The filePacker property
    file_packer: Optional[str] = None
    # The filePath property
    file_path: Optional[str] = None
    # The fileSize property
    file_size: Optional[int] = None
    # The fileType property
    file_type: Optional[str] = None
    # Stamped by the system when the indicator is ingested. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    ingested_date_time: Optional[datetime.datetime] = None
    # Used to deactivate indicators within system. By default, any indicator submitted is set as active. However, providers may submit existing indicators with this set to ‘False’ to deactivate indicators in the system.
    is_active: Optional[bool] = None
    # A JSON array of strings that describes which point or points on the Kill Chain this indicator targets. See ‘killChain values’ below for exact values.
    kill_chain: Optional[list[str]] = None
    # Scenarios in which the indicator may cause false positives. This should be human-readable text.
    known_false_positives: Optional[str] = None
    # The last time the indicator was seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_reported_date_time: Optional[datetime.datetime] = None
    # The malware family name associated with an indicator if it exists. Microsoft prefers the Microsoft malware family name if at all possible that can be found via the Windows Defender Security Intelligence threat encyclopedia.
    malware_family_names: Optional[list[str]] = None
    # The networkCidrBlock property
    network_cidr_block: Optional[str] = None
    # The networkDestinationAsn property
    network_destination_asn: Optional[int] = None
    # The networkDestinationCidrBlock property
    network_destination_cidr_block: Optional[str] = None
    # The networkDestinationIPv4 property
    network_destination_i_pv4: Optional[str] = None
    # The networkDestinationIPv6 property
    network_destination_i_pv6: Optional[str] = None
    # The networkDestinationPort property
    network_destination_port: Optional[int] = None
    # The networkIPv4 property
    network_i_pv4: Optional[str] = None
    # The networkIPv6 property
    network_i_pv6: Optional[str] = None
    # The networkPort property
    network_port: Optional[int] = None
    # The networkProtocol property
    network_protocol: Optional[int] = None
    # The networkSourceAsn property
    network_source_asn: Optional[int] = None
    # The networkSourceCidrBlock property
    network_source_cidr_block: Optional[str] = None
    # The networkSourceIPv4 property
    network_source_i_pv4: Optional[str] = None
    # The networkSourceIPv6 property
    network_source_i_pv6: Optional[str] = None
    # The networkSourcePort property
    network_source_port: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Determines if the indicator should trigger an event that is visible to an end-user. When set to ‘true,’ security tools won't notify the end user that a ‘hit’ has occurred. This is most often treated as audit or silent mode by security products where they'll simply log that a match occurred but won't perform the action. Default value is false.
    passive_only: Optional[bool] = None
    # An integer representing the severity of the malicious behavior identified by the data within the indicator. Acceptable values are 0 – 5 where 5 is the most severe and zero isn't severe at all. Default value is 3.
    severity: Optional[int] = None
    # A JSON array of strings that stores arbitrary tags/keywords.
    tags: Optional[list[str]] = None
    # A string value representing a single security product to which the indicator should be applied. Acceptable values are: Azure Sentinel, Microsoft Defender ATP. Required
    target_product: Optional[str] = None
    # Each indicator must have a valid Indicator Threat Type. The possible values are: Botnet, C2, CryptoMining, Darknet, DDoS, MaliciousUrl, Malware, Phishing, Proxy, PUA, WatchList. Required.
    threat_type: Optional[str] = None
    # Traffic Light Protocol value for the indicator. The possible values are: unknown, white, green, amber, red. Required.
    tlp_level: Optional[TlpLevel] = None
    # The url property
    url: Optional[str] = None
    # The userAgent property
    user_agent: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TiIndicator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TiIndicator
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TiIndicator()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .diamond_model import DiamondModel
        from .entity import Entity
        from .file_hash_type import FileHashType
        from .ti_action import TiAction
        from .tlp_level import TlpLevel

        from .diamond_model import DiamondModel
        from .entity import Entity
        from .file_hash_type import FileHashType
        from .ti_action import TiAction
        from .tlp_level import TlpLevel

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(TiAction)),
            "activityGroupNames": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "diamondModel": lambda n : setattr(self, 'diamond_model', n.get_enum_value(DiamondModel)),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "emailEncoding": lambda n : setattr(self, 'email_encoding', n.get_str_value()),
            "emailLanguage": lambda n : setattr(self, 'email_language', n.get_str_value()),
            "emailRecipient": lambda n : setattr(self, 'email_recipient', n.get_str_value()),
            "emailSenderAddress": lambda n : setattr(self, 'email_sender_address', n.get_str_value()),
            "emailSenderName": lambda n : setattr(self, 'email_sender_name', n.get_str_value()),
            "emailSourceDomain": lambda n : setattr(self, 'email_source_domain', n.get_str_value()),
            "emailSourceIpAddress": lambda n : setattr(self, 'email_source_ip_address', n.get_str_value()),
            "emailSubject": lambda n : setattr(self, 'email_subject', n.get_str_value()),
            "emailXMailer": lambda n : setattr(self, 'email_x_mailer', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "fileCompileDateTime": lambda n : setattr(self, 'file_compile_date_time', n.get_datetime_value()),
            "fileCreatedDateTime": lambda n : setattr(self, 'file_created_date_time', n.get_datetime_value()),
            "fileHashType": lambda n : setattr(self, 'file_hash_type', n.get_enum_value(FileHashType)),
            "fileHashValue": lambda n : setattr(self, 'file_hash_value', n.get_str_value()),
            "fileMutexName": lambda n : setattr(self, 'file_mutex_name', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "filePacker": lambda n : setattr(self, 'file_packer', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "ingestedDateTime": lambda n : setattr(self, 'ingested_date_time', n.get_datetime_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "killChain": lambda n : setattr(self, 'kill_chain', n.get_collection_of_primitive_values(str)),
            "knownFalsePositives": lambda n : setattr(self, 'known_false_positives', n.get_str_value()),
            "lastReportedDateTime": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malwareFamilyNames": lambda n : setattr(self, 'malware_family_names', n.get_collection_of_primitive_values(str)),
            "networkCidrBlock": lambda n : setattr(self, 'network_cidr_block', n.get_str_value()),
            "networkDestinationAsn": lambda n : setattr(self, 'network_destination_asn', n.get_int_value()),
            "networkDestinationCidrBlock": lambda n : setattr(self, 'network_destination_cidr_block', n.get_str_value()),
            "networkDestinationIPv4": lambda n : setattr(self, 'network_destination_i_pv4', n.get_str_value()),
            "networkDestinationIPv6": lambda n : setattr(self, 'network_destination_i_pv6', n.get_str_value()),
            "networkDestinationPort": lambda n : setattr(self, 'network_destination_port', n.get_int_value()),
            "networkIPv4": lambda n : setattr(self, 'network_i_pv4', n.get_str_value()),
            "networkIPv6": lambda n : setattr(self, 'network_i_pv6', n.get_str_value()),
            "networkPort": lambda n : setattr(self, 'network_port', n.get_int_value()),
            "networkProtocol": lambda n : setattr(self, 'network_protocol', n.get_int_value()),
            "networkSourceAsn": lambda n : setattr(self, 'network_source_asn', n.get_int_value()),
            "networkSourceCidrBlock": lambda n : setattr(self, 'network_source_cidr_block', n.get_str_value()),
            "networkSourceIPv4": lambda n : setattr(self, 'network_source_i_pv4', n.get_str_value()),
            "networkSourceIPv6": lambda n : setattr(self, 'network_source_i_pv6', n.get_str_value()),
            "networkSourcePort": lambda n : setattr(self, 'network_source_port', n.get_int_value()),
            "passiveOnly": lambda n : setattr(self, 'passive_only', n.get_bool_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "targetProduct": lambda n : setattr(self, 'target_product', n.get_str_value()),
            "threatType": lambda n : setattr(self, 'threat_type', n.get_str_value()),
            "tlpLevel": lambda n : setattr(self, 'tlp_level', n.get_enum_value(TlpLevel)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_collection_of_primitive_values("activityGroupNames", self.activity_group_names)
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_int_value("confidence", self.confidence)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("diamondModel", self.diamond_model)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("emailEncoding", self.email_encoding)
        writer.write_str_value("emailLanguage", self.email_language)
        writer.write_str_value("emailRecipient", self.email_recipient)
        writer.write_str_value("emailSenderAddress", self.email_sender_address)
        writer.write_str_value("emailSenderName", self.email_sender_name)
        writer.write_str_value("emailSourceDomain", self.email_source_domain)
        writer.write_str_value("emailSourceIpAddress", self.email_source_ip_address)
        writer.write_str_value("emailSubject", self.email_subject)
        writer.write_str_value("emailXMailer", self.email_x_mailer)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_datetime_value("fileCompileDateTime", self.file_compile_date_time)
        writer.write_datetime_value("fileCreatedDateTime", self.file_created_date_time)
        writer.write_enum_value("fileHashType", self.file_hash_type)
        writer.write_str_value("fileHashValue", self.file_hash_value)
        writer.write_str_value("fileMutexName", self.file_mutex_name)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("filePacker", self.file_packer)
        writer.write_str_value("filePath", self.file_path)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("fileType", self.file_type)
        writer.write_datetime_value("ingestedDateTime", self.ingested_date_time)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_collection_of_primitive_values("killChain", self.kill_chain)
        writer.write_str_value("knownFalsePositives", self.known_false_positives)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_collection_of_primitive_values("malwareFamilyNames", self.malware_family_names)
        writer.write_str_value("networkCidrBlock", self.network_cidr_block)
        writer.write_int_value("networkDestinationAsn", self.network_destination_asn)
        writer.write_str_value("networkDestinationCidrBlock", self.network_destination_cidr_block)
        writer.write_str_value("networkDestinationIPv4", self.network_destination_i_pv4)
        writer.write_str_value("networkDestinationIPv6", self.network_destination_i_pv6)
        writer.write_int_value("networkDestinationPort", self.network_destination_port)
        writer.write_str_value("networkIPv4", self.network_i_pv4)
        writer.write_str_value("networkIPv6", self.network_i_pv6)
        writer.write_int_value("networkPort", self.network_port)
        writer.write_int_value("networkProtocol", self.network_protocol)
        writer.write_int_value("networkSourceAsn", self.network_source_asn)
        writer.write_str_value("networkSourceCidrBlock", self.network_source_cidr_block)
        writer.write_str_value("networkSourceIPv4", self.network_source_i_pv4)
        writer.write_str_value("networkSourceIPv6", self.network_source_i_pv6)
        writer.write_int_value("networkSourcePort", self.network_source_port)
        writer.write_bool_value("passiveOnly", self.passive_only)
        writer.write_int_value("severity", self.severity)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("targetProduct", self.target_product)
        writer.write_str_value("threatType", self.threat_type)
        writer.write_enum_value("tlpLevel", self.tlp_level)
        writer.write_str_value("url", self.url)
        writer.write_str_value("userAgent", self.user_agent)
    

