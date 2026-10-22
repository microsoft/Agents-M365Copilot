from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .domain_name_source import DomainNameSource
    from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
    from .username_source import UsernameSource
    from .user_email_source import UserEmailSource
    from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
    from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class EasEmailProfileConfigurationBase(DeviceConfiguration, Parsable):
    """
    Apple device features configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.easEmailProfileConfigurationBase"
    # Custom domain name value used while generating an email profile before installing on the device.
    custom_domain_name: Optional[str] = None
    # UserDomainname attribute that is picked from AAD and injected into this profile before installing on the device. Possible values are: fullDomainName, netBiosDomainName.
    user_domain_name_source: Optional[DomainNameSource] = None
    # Name of the AAD field, that will be used to retrieve UserName for email profile. Possible values are: userPrincipalName, primarySmtpAddress, samAccountName.
    username_a_a_d_source: Optional[UsernameSource] = None
    # Possible values for username source or email source.
    username_source: Optional[UserEmailSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EasEmailProfileConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EasEmailProfileConfigurationBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEasEmailProfileConfiguration".casefold():
            from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration

            return IosEasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EasEmailProfileConfiguration".casefold():
            from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration

            return Windows10EasEmailProfileConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration".casefold():
            from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

            return WindowsPhoneEASEmailProfileConfiguration()
        return EasEmailProfileConfigurationBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .domain_name_source import DomainNameSource
        from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
        from .username_source import UsernameSource
        from .user_email_source import UserEmailSource
        from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
        from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

        from .device_configuration import DeviceConfiguration
        from .domain_name_source import DomainNameSource
        from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
        from .username_source import UsernameSource
        from .user_email_source import UserEmailSource
        from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
        from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "customDomainName": lambda n : setattr(self, 'custom_domain_name', n.get_str_value()),
            "userDomainNameSource": lambda n : setattr(self, 'user_domain_name_source', n.get_enum_value(DomainNameSource)),
            "usernameAADSource": lambda n : setattr(self, 'username_a_a_d_source', n.get_enum_value(UsernameSource)),
            "usernameSource": lambda n : setattr(self, 'username_source', n.get_enum_value(UserEmailSource)),
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
        writer.write_str_value("customDomainName", self.custom_domain_name)
        writer.write_enum_value("userDomainNameSource", self.user_domain_name_source)
        writer.write_enum_value("usernameAADSource", self.username_a_a_d_source)
        writer.write_enum_value("usernameSource", self.username_source)
    

