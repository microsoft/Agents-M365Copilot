from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SharePointMetaDataInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The aiFileActions property
    ai_file_actions: Optional[str] = None
    # The blockedUserForFileAccess property
    blocked_user_for_file_access: Optional[str] = None
    # The fileId property
    file_id: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    # The fileOwner property
    file_owner: Optional[str] = None
    # The filePathUrl property
    file_path_url: Optional[str] = None
    # The fileSize property
    file_size: Optional[int] = None
    # The from property
    from_: Optional[str] = None
    # The isJitTriggered property
    is_jit_triggered: Optional[bool] = None
    # The isViewableByExternalUsers property
    is_viewable_by_external_users: Optional[bool] = None
    # The isVisibleOnlyToOdbOwner property
    is_visible_only_to_odb_owner: Optional[bool] = None
    # The itemCreatedDate property
    item_created_date: Optional[datetime.date] = None
    # The itemLastModifiedDate property
    item_last_modified_date: Optional[datetime.date] = None
    # The itemLastSharedDate property
    item_last_shared_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The quarantineLocationFileUrl property
    quarantine_location_file_url: Optional[str] = None
    # The sensitivityLabelIds property
    sensitivity_label_ids: Optional[list[str]] = None
    # The sensitivityLabelNames property
    sensitivity_label_names: Optional[list[str]] = None
    # The sharedBy property
    shared_by: Optional[list[str]] = None
    # The sharedWith property
    shared_with: Optional[list[str]] = None
    # The siteAdmins property
    site_admins: Optional[list[str]] = None
    # The siteCollectionGuid property
    site_collection_guid: Optional[str] = None
    # The siteCollectionUrl property
    site_collection_url: Optional[str] = None
    # The uniqueId property
    unique_id: Optional[str] = None
    # The violatingAction property
    violating_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMetaDataInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMetaDataInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMetaDataInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "aiFileActions": lambda n : setattr(self, 'ai_file_actions', n.get_str_value()),
            "blockedUserForFileAccess": lambda n : setattr(self, 'blocked_user_for_file_access', n.get_str_value()),
            "fileId": lambda n : setattr(self, 'file_id', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "fileOwner": lambda n : setattr(self, 'file_owner', n.get_str_value()),
            "filePathUrl": lambda n : setattr(self, 'file_path_url', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "from": lambda n : setattr(self, 'from_', n.get_str_value()),
            "isJitTriggered": lambda n : setattr(self, 'is_jit_triggered', n.get_bool_value()),
            "isViewableByExternalUsers": lambda n : setattr(self, 'is_viewable_by_external_users', n.get_bool_value()),
            "isVisibleOnlyToOdbOwner": lambda n : setattr(self, 'is_visible_only_to_odb_owner', n.get_bool_value()),
            "itemCreatedDate": lambda n : setattr(self, 'item_created_date', n.get_date_value()),
            "itemLastModifiedDate": lambda n : setattr(self, 'item_last_modified_date', n.get_date_value()),
            "itemLastSharedDate": lambda n : setattr(self, 'item_last_shared_date', n.get_date_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quarantineLocationFileUrl": lambda n : setattr(self, 'quarantine_location_file_url', n.get_str_value()),
            "sensitivityLabelIds": lambda n : setattr(self, 'sensitivity_label_ids', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelNames": lambda n : setattr(self, 'sensitivity_label_names', n.get_collection_of_primitive_values(str)),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_collection_of_primitive_values(str)),
            "sharedWith": lambda n : setattr(self, 'shared_with', n.get_collection_of_primitive_values(str)),
            "siteAdmins": lambda n : setattr(self, 'site_admins', n.get_collection_of_primitive_values(str)),
            "siteCollectionGuid": lambda n : setattr(self, 'site_collection_guid', n.get_str_value()),
            "siteCollectionUrl": lambda n : setattr(self, 'site_collection_url', n.get_str_value()),
            "uniqueId": lambda n : setattr(self, 'unique_id', n.get_str_value()),
            "violatingAction": lambda n : setattr(self, 'violating_action', n.get_str_value()),
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
        writer.write_str_value("aiFileActions", self.ai_file_actions)
        writer.write_str_value("blockedUserForFileAccess", self.blocked_user_for_file_access)
        writer.write_str_value("fileId", self.file_id)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("fileOwner", self.file_owner)
        writer.write_str_value("filePathUrl", self.file_path_url)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("from", self.from_)
        writer.write_bool_value("isJitTriggered", self.is_jit_triggered)
        writer.write_bool_value("isViewableByExternalUsers", self.is_viewable_by_external_users)
        writer.write_bool_value("isVisibleOnlyToOdbOwner", self.is_visible_only_to_odb_owner)
        writer.write_date_value("itemCreatedDate", self.item_created_date)
        writer.write_date_value("itemLastModifiedDate", self.item_last_modified_date)
        writer.write_date_value("itemLastSharedDate", self.item_last_shared_date)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("quarantineLocationFileUrl", self.quarantine_location_file_url)
        writer.write_collection_of_primitive_values("sensitivityLabelIds", self.sensitivity_label_ids)
        writer.write_collection_of_primitive_values("sensitivityLabelNames", self.sensitivity_label_names)
        writer.write_collection_of_primitive_values("sharedBy", self.shared_by)
        writer.write_collection_of_primitive_values("sharedWith", self.shared_with)
        writer.write_collection_of_primitive_values("siteAdmins", self.site_admins)
        writer.write_str_value("siteCollectionGuid", self.site_collection_guid)
        writer.write_str_value("siteCollectionUrl", self.site_collection_url)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_str_value("violatingAction", self.violating_action)
        writer.write_additional_data_value(self.additional_data)
    

