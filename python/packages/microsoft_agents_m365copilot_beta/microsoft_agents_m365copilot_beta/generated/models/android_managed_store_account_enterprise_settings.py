from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_enrollment_company_code import AndroidEnrollmentCompanyCode
    from .android_managed_store_account_app_sync_status import AndroidManagedStoreAccountAppSyncStatus
    from .android_managed_store_account_bind_status import AndroidManagedStoreAccountBindStatus
    from .android_managed_store_account_enrollment_target import AndroidManagedStoreAccountEnrollmentTarget
    from .entity import Entity
    from .managed_google_play_enterprise_type import ManagedGooglePlayEnterpriseType

from .entity import Entity

@dataclass
class AndroidManagedStoreAccountEnterpriseSettings(Entity, Parsable):
    """
    Enterprise settings for an Android managed store account.
    """
    # Company codes for AndroidManagedStoreAccountEnterpriseSettings
    android_device_owner_fully_managed_enrollment_enabled: Optional[bool] = None
    # Bind status of the tenant with the Google EMM API
    bind_status: Optional[AndroidManagedStoreAccountBindStatus] = None
    # Company codes for AndroidManagedStoreAccountEnterpriseSettings
    company_codes: Optional[list[AndroidEnrollmentCompanyCode]] = None
    # Indicates if this account is flighting for Android Device Owner Management with CloudDPC.
    device_owner_management_enabled: Optional[bool] = None
    # Android for Work device management targeting type for the account
    enrollment_target: Optional[AndroidManagedStoreAccountEnrollmentTarget] = None
    # Last completion time for app sync
    last_app_sync_date_time: Optional[datetime.datetime] = None
    # Sync status of the tenant with the Google EMM API
    last_app_sync_status: Optional[AndroidManagedStoreAccountAppSyncStatus] = None
    # Last modification time for Android enterprise settings
    last_modified_date_time: Optional[datetime.datetime] = None
    # Bind Type of the tenant with the Google EMM API
    managed_google_play_enterprise_type: Optional[ManagedGooglePlayEnterpriseType] = None
    # Initial scope tags for MGP apps
    managed_google_play_initial_scope_tag_ids: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Organization name used when onboarding Android Enterprise
    owner_organization_name: Optional[str] = None
    # Owner UPN that created the enterprise
    owner_user_principal_name: Optional[str] = None
    # Specifies which AAD groups can enroll devices in Android for Work device management if enrollmentTarget is set to 'Targeted'
    target_group_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedStoreAccountEnterpriseSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAccountEnterpriseSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedStoreAccountEnterpriseSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_enrollment_company_code import AndroidEnrollmentCompanyCode
        from .android_managed_store_account_app_sync_status import AndroidManagedStoreAccountAppSyncStatus
        from .android_managed_store_account_bind_status import AndroidManagedStoreAccountBindStatus
        from .android_managed_store_account_enrollment_target import AndroidManagedStoreAccountEnrollmentTarget
        from .entity import Entity
        from .managed_google_play_enterprise_type import ManagedGooglePlayEnterpriseType

        from .android_enrollment_company_code import AndroidEnrollmentCompanyCode
        from .android_managed_store_account_app_sync_status import AndroidManagedStoreAccountAppSyncStatus
        from .android_managed_store_account_bind_status import AndroidManagedStoreAccountBindStatus
        from .android_managed_store_account_enrollment_target import AndroidManagedStoreAccountEnrollmentTarget
        from .entity import Entity
        from .managed_google_play_enterprise_type import ManagedGooglePlayEnterpriseType

        fields: dict[str, Callable[[Any], None]] = {
            "androidDeviceOwnerFullyManagedEnrollmentEnabled": lambda n : setattr(self, 'android_device_owner_fully_managed_enrollment_enabled', n.get_bool_value()),
            "bindStatus": lambda n : setattr(self, 'bind_status', n.get_enum_value(AndroidManagedStoreAccountBindStatus)),
            "companyCodes": lambda n : setattr(self, 'company_codes', n.get_collection_of_object_values(AndroidEnrollmentCompanyCode)),
            "deviceOwnerManagementEnabled": lambda n : setattr(self, 'device_owner_management_enabled', n.get_bool_value()),
            "enrollmentTarget": lambda n : setattr(self, 'enrollment_target', n.get_enum_value(AndroidManagedStoreAccountEnrollmentTarget)),
            "lastAppSyncDateTime": lambda n : setattr(self, 'last_app_sync_date_time', n.get_datetime_value()),
            "lastAppSyncStatus": lambda n : setattr(self, 'last_app_sync_status', n.get_enum_value(AndroidManagedStoreAccountAppSyncStatus)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedGooglePlayEnterpriseType": lambda n : setattr(self, 'managed_google_play_enterprise_type', n.get_enum_value(ManagedGooglePlayEnterpriseType)),
            "managedGooglePlayInitialScopeTagIds": lambda n : setattr(self, 'managed_google_play_initial_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "ownerOrganizationName": lambda n : setattr(self, 'owner_organization_name', n.get_str_value()),
            "ownerUserPrincipalName": lambda n : setattr(self, 'owner_user_principal_name', n.get_str_value()),
            "targetGroupIds": lambda n : setattr(self, 'target_group_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("androidDeviceOwnerFullyManagedEnrollmentEnabled", self.android_device_owner_fully_managed_enrollment_enabled)
        writer.write_enum_value("bindStatus", self.bind_status)
        writer.write_collection_of_object_values("companyCodes", self.company_codes)
        writer.write_bool_value("deviceOwnerManagementEnabled", self.device_owner_management_enabled)
        writer.write_enum_value("enrollmentTarget", self.enrollment_target)
        writer.write_datetime_value("lastAppSyncDateTime", self.last_app_sync_date_time)
        writer.write_enum_value("lastAppSyncStatus", self.last_app_sync_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("managedGooglePlayEnterpriseType", self.managed_google_play_enterprise_type)
        writer.write_collection_of_primitive_values("managedGooglePlayInitialScopeTagIds", self.managed_google_play_initial_scope_tag_ids)
        writer.write_str_value("ownerOrganizationName", self.owner_organization_name)
        writer.write_str_value("ownerUserPrincipalName", self.owner_user_principal_name)
        writer.write_collection_of_primitive_values("targetGroupIds", self.target_group_ids)
    

