from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_definition_file import GroupPolicyDefinitionFile
    from .group_policy_operation import GroupPolicyOperation
    from .group_policy_uploaded_definition_file_status import GroupPolicyUploadedDefinitionFileStatus
    from .group_policy_uploaded_language_file import GroupPolicyUploadedLanguageFile

from .group_policy_definition_file import GroupPolicyDefinitionFile

@dataclass
class GroupPolicyUploadedDefinitionFile(GroupPolicyDefinitionFile, Parsable):
    """
    The entity represents an ADMX (Administrative Template) XML file uploaded by Administrator. The ADMX file contains a collection of group policy definitions and their locations by category path. The group policy definition file also contains the languages supported as determined by the language dependent ADML (Administrative Template) language files.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyUploadedDefinitionFile"
    # The contents of the uploaded ADMX file.
    content: Optional[bytes] = None
    # The default language of the uploaded ADMX file.
    default_language_code: Optional[str] = None
    # The list of operations on the uploaded ADMX file.
    group_policy_operations: Optional[list[GroupPolicyOperation]] = None
    # The list of ADML files associated with the uploaded ADMX file.
    group_policy_uploaded_language_files: Optional[list[GroupPolicyUploadedLanguageFile]] = None
    # Type of Group Policy uploaded definition file status.
    status: Optional[GroupPolicyUploadedDefinitionFileStatus] = None
    # The uploaded time of the uploaded ADMX file.
    upload_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyUploadedDefinitionFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedDefinitionFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyUploadedDefinitionFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .group_policy_operation import GroupPolicyOperation
        from .group_policy_uploaded_definition_file_status import GroupPolicyUploadedDefinitionFileStatus
        from .group_policy_uploaded_language_file import GroupPolicyUploadedLanguageFile

        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .group_policy_operation import GroupPolicyOperation
        from .group_policy_uploaded_definition_file_status import GroupPolicyUploadedDefinitionFileStatus
        from .group_policy_uploaded_language_file import GroupPolicyUploadedLanguageFile

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "defaultLanguageCode": lambda n : setattr(self, 'default_language_code', n.get_str_value()),
            "groupPolicyOperations": lambda n : setattr(self, 'group_policy_operations', n.get_collection_of_object_values(GroupPolicyOperation)),
            "groupPolicyUploadedLanguageFiles": lambda n : setattr(self, 'group_policy_uploaded_language_files', n.get_collection_of_object_values(GroupPolicyUploadedLanguageFile)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(GroupPolicyUploadedDefinitionFileStatus)),
            "uploadDateTime": lambda n : setattr(self, 'upload_date_time', n.get_datetime_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_str_value("defaultLanguageCode", self.default_language_code)
        writer.write_collection_of_object_values("groupPolicyOperations", self.group_policy_operations)
        writer.write_collection_of_object_values("groupPolicyUploadedLanguageFiles", self.group_policy_uploaded_language_files)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("uploadDateTime", self.upload_date_time)
    

