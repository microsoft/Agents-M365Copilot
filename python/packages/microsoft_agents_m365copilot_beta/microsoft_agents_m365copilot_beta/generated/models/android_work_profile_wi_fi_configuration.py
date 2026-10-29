from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_wi_fi_security_type import AndroidWiFiSecurityType
    from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
    from .device_configuration import DeviceConfiguration
    from .wi_fi_proxy_setting import WiFiProxySetting

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidWorkProfileWiFiConfiguration(DeviceConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Android Work Profile device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user. This profile provides limited and simpler security types than Enterprise Wi-Fi profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidWorkProfileWiFiConfiguration"
    # When set to true, device will connect automatically to the Wi-Fi network when in range, skipping the user prompt. When false, user will need to connect manually through Settings on the Android device. Default value is false.
    connect_automatically: Optional[bool] = None
    # When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices. When false, device will not automatically connect to hidden networks. Default value is false.
    connect_when_network_name_is_hidden: Optional[bool] = None
    # The name of the Wi-Fi network.
    network_name: Optional[str] = None
    # Specify the pre-shared key for a WEP or WPA personal Wi-Fi network. Restrictions depend on the value set for wiFiSecurityType. If WEP type security is used, then preSharedKey must be a valid passphrase (5 or 13 characters) or a valid HEX key (10 or 26 hexidecimal characters). If WPA security type is used, then preSharedKey can be any string between 8 and 64 characters long.
    pre_shared_key: Optional[str] = None
    # When set to true, indicates that the pre-shared key is configured. When set to false, indicates that pre-shared key is not configured (any values set for preSharedKey will be ignored). Default value is false.
    pre_shared_key_is_set: Optional[bool] = None
    # URL of the proxy server automatic configuration script when automatic configuration is selected. This URL is typically the location of PAC (Proxy Auto Configuration) file.
    proxy_automatic_configuration_url: Optional[str] = None
    # Wi-Fi Proxy Settings.
    proxy_settings: Optional[WiFiProxySetting] = None
    # This is the name of the Wi-Fi network that is broadcast to all devices.
    ssid: Optional[str] = None
    # The possible security types for Android Wi-Fi profiles. Default value 'Open', indicates no authentication required for the network. The security protocols supported are WEP, WPA and WPA2. 'WpaEnterprise' and 'Wpa2Enterprise' options are available for Enterprise Wi-Fi profiles. 'Wep' and 'WpaPersonal' (supports WPA and WPA2) options are available for Basic Wi-Fi profiles.
    wi_fi_security_type: Optional[AndroidWiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidWorkProfileWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileEnterpriseWiFiConfiguration".casefold():
            from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration

            return AndroidWorkProfileEnterpriseWiFiConfiguration()
        return AndroidWorkProfileWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_wi_fi_security_type import AndroidWiFiSecurityType
        from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
        from .device_configuration import DeviceConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting

        from .android_wi_fi_security_type import AndroidWiFiSecurityType
        from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
        from .device_configuration import DeviceConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting

        fields: dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "preSharedKeyIsSet": lambda n : setattr(self, 'pre_shared_key_is_set', n.get_bool_value()),
            "proxyAutomaticConfigurationUrl": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxySettings": lambda n : setattr(self, 'proxy_settings', n.get_enum_value(WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wiFiSecurityType": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(AndroidWiFiSecurityType)),
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
        writer.write_bool_value("connectAutomatically", self.connect_automatically)
        writer.write_bool_value("connectWhenNetworkNameIsHidden", self.connect_when_network_name_is_hidden)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_bool_value("preSharedKeyIsSet", self.pre_shared_key_is_set)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_enum_value("proxySettings", self.proxy_settings)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wiFiSecurityType", self.wi_fi_security_type)
    

