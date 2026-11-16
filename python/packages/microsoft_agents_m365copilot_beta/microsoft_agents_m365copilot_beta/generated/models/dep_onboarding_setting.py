from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
    from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
    from .dep_token_type import DepTokenType
    from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
    from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
    from .enrollment_profile import EnrollmentProfile
    from .entity import Entity
    from .imported_apple_device_identity import ImportedAppleDeviceIdentity

from .entity import Entity

@dataclass
class DepOnboardingSetting(Entity, Parsable):
    """
    The depOnboardingSetting represents an instance of the Apple DEP service being onboarded to Intune. The onboarded service instance manages an Apple Token used to synchronize data between Apple and Intune.
    """
    # The Apple ID used to obtain the current token.
    apple_identifier: Optional[str] = None
    # Consent granted for data sharing with Apple Dep Service
    data_sharing_consent_granted: Optional[bool] = None
    # Default iOS Enrollment Profile
    default_ios_enrollment_profile: Optional[DepIOSEnrollmentProfile] = None
    # Default MacOs Enrollment Profile
    default_mac_os_enrollment_profile: Optional[DepMacOSEnrollmentProfile] = None
    # Default TvOS Enrollment Profile
    default_tv_o_s_enrollment_profile: Optional[DepTvOSEnrollmentProfile] = None
    # Default VisionOS Enrollment Profile
    default_vision_o_s_enrollment_profile: Optional[DepVisionOSEnrollmentProfile] = None
    # The enrollment profiles.
    enrollment_profiles: Optional[list[EnrollmentProfile]] = None
    # The imported Apple device identities.
    imported_apple_device_identities: Optional[list[ImportedAppleDeviceIdentity]] = None
    # When the service was onboarded.
    last_modified_date_time: Optional[datetime.datetime] = None
    # When the service last syned with Intune
    last_successful_sync_date_time: Optional[datetime.datetime] = None
    # Error code reported by Apple during last dep sync.
    last_sync_error_code: Optional[int] = None
    # When Intune last requested a sync.
    last_sync_triggered_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[list[str]] = None
    # Whether or not the Dep token sharing is enabled with the School Data Sync service.
    share_token_with_school_data_sync_service: Optional[bool] = None
    # Gets synced device count
    synced_device_count: Optional[int] = None
    # When the token will expire.
    token_expiration_date_time: Optional[datetime.datetime] = None
    # Friendly Name for Dep Token
    token_name: Optional[str] = None
    # The tokenType property
    token_type: Optional[DepTokenType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepOnboardingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepOnboardingSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepOnboardingSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .dep_token_type import DepTokenType
        from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
        from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
        from .enrollment_profile import EnrollmentProfile
        from .entity import Entity
        from .imported_apple_device_identity import ImportedAppleDeviceIdentity

        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .dep_token_type import DepTokenType
        from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
        from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
        from .enrollment_profile import EnrollmentProfile
        from .entity import Entity
        from .imported_apple_device_identity import ImportedAppleDeviceIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "appleIdentifier": lambda n : setattr(self, 'apple_identifier', n.get_str_value()),
            "dataSharingConsentGranted": lambda n : setattr(self, 'data_sharing_consent_granted', n.get_bool_value()),
            "defaultIosEnrollmentProfile": lambda n : setattr(self, 'default_ios_enrollment_profile', n.get_object_value(DepIOSEnrollmentProfile)),
            "defaultMacOsEnrollmentProfile": lambda n : setattr(self, 'default_mac_os_enrollment_profile', n.get_object_value(DepMacOSEnrollmentProfile)),
            "defaultTvOSEnrollmentProfile": lambda n : setattr(self, 'default_tv_o_s_enrollment_profile', n.get_object_value(DepTvOSEnrollmentProfile)),
            "defaultVisionOSEnrollmentProfile": lambda n : setattr(self, 'default_vision_o_s_enrollment_profile', n.get_object_value(DepVisionOSEnrollmentProfile)),
            "enrollmentProfiles": lambda n : setattr(self, 'enrollment_profiles', n.get_collection_of_object_values(EnrollmentProfile)),
            "importedAppleDeviceIdentities": lambda n : setattr(self, 'imported_apple_device_identities', n.get_collection_of_object_values(ImportedAppleDeviceIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastSuccessfulSyncDateTime": lambda n : setattr(self, 'last_successful_sync_date_time', n.get_datetime_value()),
            "lastSyncErrorCode": lambda n : setattr(self, 'last_sync_error_code', n.get_int_value()),
            "lastSyncTriggeredDateTime": lambda n : setattr(self, 'last_sync_triggered_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "shareTokenWithSchoolDataSyncService": lambda n : setattr(self, 'share_token_with_school_data_sync_service', n.get_bool_value()),
            "syncedDeviceCount": lambda n : setattr(self, 'synced_device_count', n.get_int_value()),
            "tokenExpirationDateTime": lambda n : setattr(self, 'token_expiration_date_time', n.get_datetime_value()),
            "tokenName": lambda n : setattr(self, 'token_name', n.get_str_value()),
            "tokenType": lambda n : setattr(self, 'token_type', n.get_enum_value(DepTokenType)),
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
        writer.write_str_value("appleIdentifier", self.apple_identifier)
        writer.write_bool_value("dataSharingConsentGranted", self.data_sharing_consent_granted)
        writer.write_object_value("defaultIosEnrollmentProfile", self.default_ios_enrollment_profile)
        writer.write_object_value("defaultMacOsEnrollmentProfile", self.default_mac_os_enrollment_profile)
        writer.write_object_value("defaultTvOSEnrollmentProfile", self.default_tv_o_s_enrollment_profile)
        writer.write_object_value("defaultVisionOSEnrollmentProfile", self.default_vision_o_s_enrollment_profile)
        writer.write_collection_of_object_values("enrollmentProfiles", self.enrollment_profiles)
        writer.write_collection_of_object_values("importedAppleDeviceIdentities", self.imported_apple_device_identities)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastSuccessfulSyncDateTime", self.last_successful_sync_date_time)
        writer.write_int_value("lastSyncErrorCode", self.last_sync_error_code)
        writer.write_datetime_value("lastSyncTriggeredDateTime", self.last_sync_triggered_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("shareTokenWithSchoolDataSyncService", self.share_token_with_school_data_sync_service)
        writer.write_int_value("syncedDeviceCount", self.synced_device_count)
        writer.write_datetime_value("tokenExpirationDateTime", self.token_expiration_date_time)
        writer.write_str_value("tokenName", self.token_name)
        writer.write_enum_value("tokenType", self.token_type)
    

