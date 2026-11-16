from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkOnPremisesCalendarSyncConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The fully qualified domain name (FQDN) of the Skype for Business Server. Use the Exchange domain if the Skype for Business SIP domain is different from the Exchange domain of the user.
    domain: Optional[str] = None
    # The domain and username of the console device, for example, Seattle/RanierConf.
    domain_user_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Simple Mail Transfer Protocol (SMTP) address of the user account. This is only required if a different user principal name (UPN) is used to sign in to Exchange other than Microsoft Teams and Skype for Business. This is a common scenario in a hybrid environment where an on-premises Exchange server is used.
    smtp_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkOnPremisesCalendarSyncConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkOnPremisesCalendarSyncConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkOnPremisesCalendarSyncConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "domainUserName": lambda n : setattr(self, 'domain_user_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "smtpAddress": lambda n : setattr(self, 'smtp_address', n.get_str_value()),
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
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("domainUserName", self.domain_user_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("smtpAddress", self.smtp_address)
        writer.write_additional_data_value(self.additional_data)
    

