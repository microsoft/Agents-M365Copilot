from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
    from .android_device_owner_wi_fi_security_type import AndroidDeviceOwnerWiFiSecurityType
    from .device_configuration import DeviceConfiguration
    from .mac_address_randomization_mode import MacAddressRandomizationMode
    from .wi_fi_proxy_setting import WiFiProxySetting

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidDeviceOwnerWiFiConfiguration(DeviceConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Android device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user. This profile provides limited and simpler security types than Enterprise Wi-Fi profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerWiFiConfiguration"
    # Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
    connect_automatically: Optional[bool] = None
    # When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
    connect_when_network_name_is_hidden: Optional[bool] = None
    # The MAC address randomization mode for Android device Wi-Fi configuration. Possible values include automatic and hardware. Default value is automatic. Possible values are: automatic, hardware, unknownFutureValue.
    mac_address_randomization_mode: Optional[MacAddressRandomizationMode] = None
    # Network Name
    network_name: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key_is_set: Optional[bool] = None
    # Specify the proxy server configuration script URL.
    proxy_automatic_configuration_url: Optional[str] = None
    # List of hosts to exclude using the proxy on connections for. These hosts can use wildcards such as .example.com.
    proxy_exclusion_list: Optional[str] = None
    # Specify the proxy server IP address. Android documentation does not specify IPv4 or IPv6. For example: 192.168.1.1.
    proxy_manual_address: Optional[str] = None
    # Specify the proxy server port.
    proxy_manual_port: Optional[int] = None
    # Wi-Fi Proxy Settings.
    proxy_settings: Optional[WiFiProxySetting] = None
    # This is the name of the Wi-Fi network that is broadcast to all devices.
    ssid: Optional[str] = None
    # Wi-Fi Security Types for Android Device Owner.
    wi_fi_security_type: Optional[AndroidDeviceOwnerWiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration".casefold():
            from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration

            return AndroidDeviceOwnerEnterpriseWiFiConfiguration()
        return AndroidDeviceOwnerWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
        from .android_device_owner_wi_fi_security_type import AndroidDeviceOwnerWiFiSecurityType
        from .device_configuration import DeviceConfiguration
        from .mac_address_randomization_mode import MacAddressRandomizationMode
        from .wi_fi_proxy_setting import WiFiProxySetting

        from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
        from .android_device_owner_wi_fi_security_type import AndroidDeviceOwnerWiFiSecurityType
        from .device_configuration import DeviceConfiguration
        from .mac_address_randomization_mode import MacAddressRandomizationMode
        from .wi_fi_proxy_setting import WiFiProxySetting

        fields: dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "macAddressRandomizationMode": lambda n : setattr(self, 'mac_address_randomization_mode', n.get_enum_value(MacAddressRandomizationMode)),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "preSharedKeyIsSet": lambda n : setattr(self, 'pre_shared_key_is_set', n.get_bool_value()),
            "proxyAutomaticConfigurationUrl": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxyExclusionList": lambda n : setattr(self, 'proxy_exclusion_list', n.get_str_value()),
            "proxyManualAddress": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxyManualPort": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxySettings": lambda n : setattr(self, 'proxy_settings', n.get_enum_value(WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wiFiSecurityType": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(AndroidDeviceOwnerWiFiSecurityType)),
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
        writer.write_enum_value("macAddressRandomizationMode", self.mac_address_randomization_mode)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_bool_value("preSharedKeyIsSet", self.pre_shared_key_is_set)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_str_value("proxyExclusionList", self.proxy_exclusion_list)
        writer.write_str_value("proxyManualAddress", self.proxy_manual_address)
        writer.write_int_value("proxyManualPort", self.proxy_manual_port)
        writer.write_enum_value("proxySettings", self.proxy_settings)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wiFiSecurityType", self.wi_fi_security_type)
    

