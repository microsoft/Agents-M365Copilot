from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class GroupPolicyUploadedLanguageFile(AdditionalDataHolder, Parsable):
    """
    The entity represents an ADML (Administrative Template language) XML file uploaded by Administrator.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The contents of the uploaded ADML file.
    content: Optional[bytes] = None
    # The file name of the uploaded ADML file.
    file_name: Optional[str] = None
    # Key of the entity.
    id: Optional[str] = None
    # The language code of the uploaded ADML file.
    language_code: Optional[str] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyUploadedLanguageFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedLanguageFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyUploadedLanguageFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "languageCode": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("languageCode", self.language_code)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

