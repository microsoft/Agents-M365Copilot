from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_certificate_profile_base import AndroidCertificateProfileBase
    from .android_username_source import AndroidUsernameSource
    from .device_configuration import DeviceConfiguration
    from .domain_name_source import DomainNameSource
    from .eas_authentication_method import EasAuthenticationMethod
    from .email_sync_duration import EmailSyncDuration
    from .email_sync_schedule import EmailSyncSchedule
    from .user_email_source import UserEmailSource

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidEasEmailProfileConfiguration(DeviceConfiguration, Parsable):
    """
    By providing configurations in this profile you can instruct the native email client on KNOX devices to communicate with an Exchange server and get email, contacts, calendar, tasks, and notes. Furthermore, you can also specify how much email to sync and how often the device should sync.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidEasEmailProfileConfiguration"
    # Exchange ActiveSync account name, displayed to users as name of EAS (this) profile.
    account_name: Optional[str] = None
    # Exchange Active Sync authentication method.
    authentication_method: Optional[EasAuthenticationMethod] = None
    # Custom domain name value used while generating an email profile before installing on the device.
    custom_domain_name: Optional[str] = None
    # Possible values for email sync duration.
    duration_of_email_to_sync: Optional[EmailSyncDuration] = None
    # Possible values for username source or email source.
    email_address_source: Optional[UserEmailSource] = None
    # Possible values for email sync schedule.
    email_sync_schedule: Optional[EmailSyncSchedule] = None
    # Exchange location (URL) that the native mail app connects to.
    host_name: Optional[str] = None
    # Identity certificate.
    identity_certificate: Optional[AndroidCertificateProfileBase] = None
    # Indicates whether or not to use S/MIME certificate.
    require_smime: Optional[bool] = None
    # Indicates whether or not to use SSL.
    require_ssl: Optional[bool] = None
    # S/MIME signing certificate.
    smime_signing_certificate: Optional[AndroidCertificateProfileBase] = None
    # Toggles syncing the calendar. If set to false calendar is turned off on the device.
    sync_calendar: Optional[bool] = None
    # Toggles syncing contacts. If set to false contacts are turned off on the device.
    sync_contacts: Optional[bool] = None
    # Toggles syncing notes. If set to false notes are turned off on the device.
    sync_notes: Optional[bool] = None
    # Toggles syncing tasks. If set to false tasks are turned off on the device.
    sync_tasks: Optional[bool] = None
    # UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
    user_domain_name_source: Optional[DomainNameSource] = None
    # Android username source.
    username_source: Optional[AndroidUsernameSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidEasEmailProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidEasEmailProfileConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidEasEmailProfileConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_username_source import AndroidUsernameSource
        from .device_configuration import DeviceConfiguration
        from .domain_name_source import DomainNameSource
        from .eas_authentication_method import EasAuthenticationMethod
        from .email_sync_duration import EmailSyncDuration
        from .email_sync_schedule import EmailSyncSchedule
        from .user_email_source import UserEmailSource

        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .android_username_source import AndroidUsernameSource
        from .device_configuration import DeviceConfiguration
        from .domain_name_source import DomainNameSource
        from .eas_authentication_method import EasAuthenticationMethod
        from .email_sync_duration import EmailSyncDuration
        from .email_sync_schedule import EmailSyncSchedule
        from .user_email_source import UserEmailSource

        fields: dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(EasAuthenticationMethod)),
            "customDomainName": lambda n : setattr(self, 'custom_domain_name', n.get_str_value()),
            "durationOfEmailToSync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(EmailSyncDuration)),
            "emailAddressSource": lambda n : setattr(self, 'email_address_source', n.get_enum_value(UserEmailSource)),
            "emailSyncSchedule": lambda n : setattr(self, 'email_sync_schedule', n.get_enum_value(EmailSyncSchedule)),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(AndroidCertificateProfileBase)),
            "requireSmime": lambda n : setattr(self, 'require_smime', n.get_bool_value()),
            "requireSsl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
            "smimeSigningCertificate": lambda n : setattr(self, 'smime_signing_certificate', n.get_object_value(AndroidCertificateProfileBase)),
            "syncCalendar": lambda n : setattr(self, 'sync_calendar', n.get_bool_value()),
            "syncContacts": lambda n : setattr(self, 'sync_contacts', n.get_bool_value()),
            "syncNotes": lambda n : setattr(self, 'sync_notes', n.get_bool_value()),
            "syncTasks": lambda n : setattr(self, 'sync_tasks', n.get_bool_value()),
            "userDomainNameSource": lambda n : setattr(self, 'user_domain_name_source', n.get_enum_value(DomainNameSource)),
            "usernameSource": lambda n : setattr(self, 'username_source', n.get_enum_value(AndroidUsernameSource)),
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
        writer.write_str_value("accountName", self.account_name)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("customDomainName", self.custom_domain_name)
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_enum_value("emailSyncSchedule", self.email_sync_schedule)
        writer.write_str_value("hostName", self.host_name)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("requireSmime", self.require_smime)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_object_value("smimeSigningCertificate", self.smime_signing_certificate)
        writer.write_bool_value("syncCalendar", self.sync_calendar)
        writer.write_bool_value("syncContacts", self.sync_contacts)
        writer.write_bool_value("syncNotes", self.sync_notes)
        writer.write_bool_value("syncTasks", self.sync_tasks)
        writer.write_enum_value("userDomainNameSource", self.user_domain_name_source)
        writer.write_enum_value("usernameSource", self.username_source)
    

