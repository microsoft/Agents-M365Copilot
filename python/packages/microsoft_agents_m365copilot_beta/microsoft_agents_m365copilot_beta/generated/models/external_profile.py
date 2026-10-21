from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .external_user_profile import ExternalUserProfile
    from .pending_external_user_profile import PendingExternalUserProfile
    from .physical_office_address import PhysicalOfficeAddress

from .directory_object import DirectoryObject

@dataclass
class ExternalProfile(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalProfile"
    # The office address of the external user profile.
    address: Optional[PhysicalOfficeAddress] = None
    # The company name of the external user profile. Supports $filter (eq, startswith).
    company_name: Optional[str] = None
    # The object ID of the user who created the external user profile. Read-only. Not nullable.
    created_by: Optional[str] = None
    # Date and time when this external user was created. Not nullable. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The department of the external user profile.
    department: Optional[str] = None
    # The display name of the external user profile.
    display_name: Optional[str] = None
    # Represents whether the external user profile is discoverable in the directory. When true, this external profile shows up in Teams search.
    is_discoverable: Optional[bool] = None
    # Represents whether the external user profile is enabled in the directory. This property is peer to the accountEnabled property on the user object.
    is_enabled: Optional[bool] = None
    # The job title of the external user profile.
    job_title: Optional[str] = None
    # The phone number of the external user profile. Must be in E164 format.
    phone_number: Optional[str] = None
    # The object ID of the supervisor of the external user profile. Supports $filter (eq, startswith).
    supervisor_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalUserProfile".casefold():
            from .external_user_profile import ExternalUserProfile

            return ExternalUserProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pendingExternalUserProfile".casefold():
            from .pending_external_user_profile import PendingExternalUserProfile

            return PendingExternalUserProfile()
        return ExternalProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .external_user_profile import ExternalUserProfile
        from .pending_external_user_profile import PendingExternalUserProfile
        from .physical_office_address import PhysicalOfficeAddress

        from .directory_object import DirectoryObject
        from .external_user_profile import ExternalUserProfile
        from .pending_external_user_profile import PendingExternalUserProfile
        from .physical_office_address import PhysicalOfficeAddress

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalOfficeAddress)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDiscoverable": lambda n : setattr(self, 'is_discoverable', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "supervisorId": lambda n : setattr(self, 'supervisor_id', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDiscoverable", self.is_discoverable)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("supervisorId", self.supervisor_id)
    

