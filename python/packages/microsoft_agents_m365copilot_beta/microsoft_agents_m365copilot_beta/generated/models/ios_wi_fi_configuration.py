from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
    from .wi_fi_proxy_setting import WiFiProxySetting
    from .wi_fi_security_type import WiFiSecurityType

from .device_configuration import DeviceConfiguration

@dataclass
class IosWiFiConfiguration(DeviceConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the iOS device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user. This profile provides limited and simpler security types than Enterprise Wi-Fi profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosWiFiConfiguration"
    # Connect automatically when this network is in range. Setting this to true will skip the user prompt and automatically connect the device to Wi-Fi network.
    connect_automatically: Optional[bool] = None
    # Connect when the network is not broadcasting its name (SSID). When set to true, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices.
    connect_when_network_name_is_hidden: Optional[bool] = None
    # If set to true, forces devices connecting using this Wi-Fi profile to present their actual Wi-Fi MAC address instead of a random MAC address. Applies to iOS 14 and later.
    disable_mac_address_randomization: Optional[bool] = None
    # Network Name
    network_name: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key: Optional[str] = None
    # URL of the proxy server automatic configuration script when automatic configuration is selected. This URL is typically the location of PAC (Proxy Auto Configuration) file.
    proxy_automatic_configuration_url: Optional[str] = None
    # IP Address or DNS hostname of the proxy server when manual configuration is selected.
    proxy_manual_address: Optional[str] = None
    # Port of the proxy server when manual configuration is selected.
    proxy_manual_port: Optional[int] = None
    # Wi-Fi Proxy Settings.
    proxy_settings: Optional[WiFiProxySetting] = None
    # This is the name of the Wi-Fi network that is broadcast to all devices.
    ssid: Optional[str] = None
    # Wi-Fi Security Types.
    wi_fi_security_type: Optional[WiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosEnterpriseWiFiConfiguration".casefold():
            from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration

            return IosEnterpriseWiFiConfiguration()
        return IosWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting
        from .wi_fi_security_type import WiFiSecurityType

        from .device_configuration import DeviceConfiguration
        from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting
        from .wi_fi_security_type import WiFiSecurityType

        fields: dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "disableMacAddressRandomization": lambda n : setattr(self, 'disable_mac_address_randomization', n.get_bool_value()),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "proxyAutomaticConfigurationUrl": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxyManualAddress": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxyManualPort": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxySettings": lambda n : setattr(self, 'proxy_settings', n.get_enum_value(WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wiFiSecurityType": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(WiFiSecurityType)),
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
        writer.write_bool_value("disableMacAddressRandomization", self.disable_mac_address_randomization)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_str_value("proxyManualAddress", self.proxy_manual_address)
        writer.write_int_value("proxyManualPort", self.proxy_manual_port)
        writer.write_enum_value("proxySettings", self.proxy_settings)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wiFiSecurityType", self.wi_fi_security_type)
    

