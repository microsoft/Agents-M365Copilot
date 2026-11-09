from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .logon_type import LogonType
    from .user_account_security_type import UserAccountSecurityType

@dataclass
class LogonUser(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Domain of user account used to logon.
    account_domain: Optional[str] = None
    # Account name of user account used to logon.
    account_name: Optional[str] = None
    # User Account type, per Windows definition. The possible values are: unknown, standard, power, administrator.
    account_type: Optional[UserAccountSecurityType] = None
    # DateTime at which the earliest logon by this user account occurred (provider-determined period). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # DateTime at which the latest logon by this user account occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # User logon ID.
    logon_id: Optional[str] = None
    # Collection of the logon types observed for the logged on user from when first to last seen. The possible values are: unknown, interactive, remoteInteractive, network, batch, service.
    logon_types: Optional[list[LogonType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LogonUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LogonUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LogonUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .logon_type import LogonType
        from .user_account_security_type import UserAccountSecurityType

        from .logon_type import LogonType
        from .user_account_security_type import UserAccountSecurityType

        fields: dict[str, Callable[[Any], None]] = {
            "accountDomain": lambda n : setattr(self, 'account_domain', n.get_str_value()),
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "accountType": lambda n : setattr(self, 'account_type', n.get_enum_value(UserAccountSecurityType)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "logonId": lambda n : setattr(self, 'logon_id', n.get_str_value()),
            "logonTypes": lambda n : setattr(self, 'logon_types', n.get_collection_of_enum_values(LogonType)),
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
        writer.write_str_value("accountDomain", self.account_domain)
        writer.write_str_value("accountName", self.account_name)
        writer.write_enum_value("accountType", self.account_type)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("logonId", self.logon_id)
        writer.write_collection_of_enum_values("logonTypes", self.logon_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

