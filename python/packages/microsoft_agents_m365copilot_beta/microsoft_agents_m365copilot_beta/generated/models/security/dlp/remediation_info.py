from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .remediation_activity_type import RemediationActivityType

@dataclass
class RemediationInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The alertId property
    alert_id: Optional[str] = None
    # The bccRecipients property
    bcc_recipients: Optional[list[str]] = None
    # The ccRecipients property
    cc_recipients: Optional[list[str]] = None
    # The iwUser property
    iw_user: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recipients property
    recipients: Optional[list[str]] = None
    # The remediationActivity property
    remediation_activity: Optional[RemediationActivityType] = None
    # The sender property
    sender: Optional[str] = None
    # The subject property
    subject: Optional[str] = None
    # The templateName property
    template_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemediationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemediationInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemediationInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .remediation_activity_type import RemediationActivityType

        from .remediation_activity_type import RemediationActivityType

        fields: dict[str, Callable[[Any], None]] = {
            "alertId": lambda n : setattr(self, 'alert_id', n.get_str_value()),
            "bccRecipients": lambda n : setattr(self, 'bcc_recipients', n.get_collection_of_primitive_values(str)),
            "ccRecipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_primitive_values(str)),
            "iwUser": lambda n : setattr(self, 'iw_user', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_primitive_values(str)),
            "remediationActivity": lambda n : setattr(self, 'remediation_activity', n.get_enum_value(RemediationActivityType)),
            "sender": lambda n : setattr(self, 'sender', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "templateName": lambda n : setattr(self, 'template_name', n.get_str_value()),
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
        writer.write_str_value("alertId", self.alert_id)
        writer.write_collection_of_primitive_values("bccRecipients", self.bcc_recipients)
        writer.write_collection_of_primitive_values("ccRecipients", self.cc_recipients)
        writer.write_str_value("iwUser", self.iw_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("recipients", self.recipients)
        writer.write_enum_value("remediationActivity", self.remediation_activity)
        writer.write_str_value("sender", self.sender)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("templateName", self.template_name)
        writer.write_additional_data_value(self.additional_data)
    

