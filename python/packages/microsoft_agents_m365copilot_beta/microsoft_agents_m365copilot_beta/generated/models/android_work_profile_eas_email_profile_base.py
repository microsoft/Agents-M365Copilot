from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_username_source import AndroidUsernameSource
    from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
    from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
    from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
    from .device_configuration import DeviceConfiguration
    from .eas_authentication_method import EasAuthenticationMethod
    from .email_sync_duration import EmailSyncDuration
    from .user_email_source import UserEmailSource

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidWorkProfileEasEmailProfileBase(DeviceConfiguration, Parsable):
    """
    Base for Android Work Profile EAS Email profiles
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidWorkProfileEasEmailProfileBase"
    # Exchange Active Sync authentication method.
    authentication_method: Optional[EasAuthenticationMethod] = None
    # Possible values for email sync duration.
    duration_of_email_to_sync: Optional[EmailSyncDuration] = None
    # Possible values for username source or email source.
    email_address_source: Optional[UserEmailSource] = None
    # Exchange location (URL) that the mail app connects to.
    host_name: Optional[str] = None
    # Identity certificate.
    identity_certificate: Optional[AndroidWorkProfileCertificateProfileBase] = None
    # Indicates whether or not to use SSL.
    require_ssl: Optional[bool] = None
    # Android username source.
    username_source: Optional[AndroidUsernameSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidWorkProfileEasEmailProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileEasEmailProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGmailEasConfiguration".casefold():
            from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration

            return AndroidWorkProfileGmailEasConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileNineWorkEasConfiguration".casefold():
            from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration

            return AndroidWorkProfileNineWorkEasConfiguration()
        return AndroidWorkProfileEasEmailProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_username_source import AndroidUsernameSource
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
        from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
        from .device_configuration import DeviceConfiguration
        from .eas_authentication_method import EasAuthenticationMethod
        from .email_sync_duration import EmailSyncDuration
        from .user_email_source import UserEmailSource

        from .android_username_source import AndroidUsernameSource
        from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
        from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
        from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
        from .device_configuration import DeviceConfiguration
        from .eas_authentication_method import EasAuthenticationMethod
        from .email_sync_duration import EmailSyncDuration
        from .user_email_source import UserEmailSource

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(EasAuthenticationMethod)),
            "durationOfEmailToSync": lambda n : setattr(self, 'duration_of_email_to_sync', n.get_enum_value(EmailSyncDuration)),
            "emailAddressSource": lambda n : setattr(self, 'email_address_source', n.get_enum_value(UserEmailSource)),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(AndroidWorkProfileCertificateProfileBase)),
            "requireSsl": lambda n : setattr(self, 'require_ssl', n.get_bool_value()),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("durationOfEmailToSync", self.duration_of_email_to_sync)
        writer.write_enum_value("emailAddressSource", self.email_address_source)
        writer.write_str_value("hostName", self.host_name)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_bool_value("requireSsl", self.require_ssl)
        writer.write_enum_value("usernameSource", self.username_source)
    

