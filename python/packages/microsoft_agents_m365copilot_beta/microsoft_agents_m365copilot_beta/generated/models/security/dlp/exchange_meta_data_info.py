from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment_info import AttachmentInfo

@dataclass
class ExchangeMetaDataInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The attachmentDetails property
    attachment_details: Optional[list[AttachmentInfo]] = None
    # The bccRecipients property
    bcc_recipients: Optional[list[str]] = None
    # The ccRecipients property
    cc_recipients: Optional[list[str]] = None
    # The docId property
    doc_id: Optional[str] = None
    # The fileSize property
    file_size: Optional[int] = None
    # The from property
    from_: Optional[str] = None
    # The immutableEntryId property
    immutable_entry_id: Optional[str] = None
    # The isViewableByExternalUsers property
    is_viewable_by_external_users: Optional[bool] = None
    # The messageId property
    message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recipientCount property
    recipient_count: Optional[int] = None
    # The sensitivityLabelIds property
    sensitivity_label_ids: Optional[list[str]] = None
    # The sensitivityLabelNames property
    sensitivity_label_names: Optional[list[str]] = None
    # The sentDate property
    sent_date: Optional[datetime.date] = None
    # The subject property
    subject: Optional[str] = None
    # The toRecipients property
    to_recipients: Optional[list[str]] = None
    # The uniqueId property
    unique_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExchangeMetaDataInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExchangeMetaDataInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExchangeMetaDataInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attachment_info import AttachmentInfo

        from .attachment_info import AttachmentInfo

        fields: dict[str, Callable[[Any], None]] = {
            "attachmentDetails": lambda n : setattr(self, 'attachment_details', n.get_collection_of_object_values(AttachmentInfo)),
            "bccRecipients": lambda n : setattr(self, 'bcc_recipients', n.get_collection_of_primitive_values(str)),
            "ccRecipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_primitive_values(str)),
            "docId": lambda n : setattr(self, 'doc_id', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "from": lambda n : setattr(self, 'from_', n.get_str_value()),
            "immutableEntryId": lambda n : setattr(self, 'immutable_entry_id', n.get_str_value()),
            "isViewableByExternalUsers": lambda n : setattr(self, 'is_viewable_by_external_users', n.get_bool_value()),
            "messageId": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipientCount": lambda n : setattr(self, 'recipient_count', n.get_int_value()),
            "sensitivityLabelIds": lambda n : setattr(self, 'sensitivity_label_ids', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelNames": lambda n : setattr(self, 'sensitivity_label_names', n.get_collection_of_primitive_values(str)),
            "sentDate": lambda n : setattr(self, 'sent_date', n.get_date_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "toRecipients": lambda n : setattr(self, 'to_recipients', n.get_collection_of_primitive_values(str)),
            "uniqueId": lambda n : setattr(self, 'unique_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("attachmentDetails", self.attachment_details)
        writer.write_collection_of_primitive_values("bccRecipients", self.bcc_recipients)
        writer.write_collection_of_primitive_values("ccRecipients", self.cc_recipients)
        writer.write_str_value("docId", self.doc_id)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("from", self.from_)
        writer.write_str_value("immutableEntryId", self.immutable_entry_id)
        writer.write_bool_value("isViewableByExternalUsers", self.is_viewable_by_external_users)
        writer.write_str_value("messageId", self.message_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("recipientCount", self.recipient_count)
        writer.write_collection_of_primitive_values("sensitivityLabelIds", self.sensitivity_label_ids)
        writer.write_collection_of_primitive_values("sensitivityLabelNames", self.sensitivity_label_names)
        writer.write_date_value("sentDate", self.sent_date)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_primitive_values("toRecipients", self.to_recipients)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_additional_data_value(self.additional_data)
    

