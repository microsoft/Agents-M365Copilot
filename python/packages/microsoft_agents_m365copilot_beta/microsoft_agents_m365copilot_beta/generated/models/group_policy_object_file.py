from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class GroupPolicyObjectFile(Entity, Parsable):
    """
    The Group Policy Object file uploaded by admin.
    """
    # The Group Policy Object file content.
    content: Optional[str] = None
    # The date and time at which the GroupPolicy was first uploaded.
    created_date_time: Optional[datetime.datetime] = None
    # The Group Policy Object GUID from GPO Xml content
    group_policy_object_id: Optional[UUID] = None
    # The date and time at which the GroupPolicyObjectFile was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The distinguished name of the OU.
    ou_distinguished_name: Optional[str] = None
    # The list of scope tags for the configuration.
    role_scope_tag_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyObjectFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyObjectFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyObjectFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "groupPolicyObjectId": lambda n : setattr(self, 'group_policy_object_id', n.get_uuid_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "ouDistinguishedName": lambda n : setattr(self, 'ou_distinguished_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_uuid_value("groupPolicyObjectId", self.group_policy_object_id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("ouDistinguishedName", self.ou_distinguished_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

