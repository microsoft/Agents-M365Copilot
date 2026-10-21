from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_deployment_channel import AppleDeploymentChannel
    from .device_configuration import DeviceConfiguration
    from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
    from .wi_fi_proxy_setting import WiFiProxySetting
    from .wi_fi_security_type import WiFiSecurityType

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSWiFiConfiguration(DeviceConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the macOS device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSWiFiConfiguration"
    # Indicates whether to automatically connect to this network when it is in range of the device. When TRUE will skip the user prompt and automatically connect the device to Wi-Fi network. Default is false.
    connect_automatically: Optional[bool] = None
    # Indicates whether the device should connect to the network when it is not broadcasting its name (SSID). When TRUE, this profile forces the device to connect to a network that doesn't broadcast its SSID to all devices. Default is false.
    connect_when_network_name_is_hidden: Optional[bool] = None
    # Indicates the deployment channel type used to deploy the configuration profile. Once set, cannot be changed. Possible values are deviceChannel, and userChannel. Possible values are: deviceChannel, userChannel, unknownFutureValue.
    deployment_channel: Optional[AppleDeploymentChannel] = None
    # Indicates the Wi-Fi configuration profile name. Used to identify the configuration profile.
    network_name: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key: Optional[str] = None
    # Indicates URL of the proxy server automatic configuration (PAC) script when proxySettings is automatic. Used to find the location of PAC (Proxy Auto Configuration) file. Example: itproxy.contoso.com
    proxy_automatic_configuration_url: Optional[str] = None
    # Indicates IP Address or DNS hostname of the proxy server when manual configuration is selected. Used for proxy settings. Example: 10.0.0.2
    proxy_manual_address: Optional[str] = None
    # Indicates the proxy server TCP port to use when proxySettings is manual. Used for proxy settings. Example: 8080
    proxy_manual_port: Optional[int] = None
    # Wi-Fi Proxy Settings.
    proxy_settings: Optional[WiFiProxySetting] = None
    # This is the name of the Wi-Fi network that is broadcast to all devices.
    ssid: Optional[str] = None
    # Wi-Fi Security Types.
    wi_fi_security_type: Optional[WiFiSecurityType] = None
    # Indicates whether devices connecting with this Wi-Fi profile must use their physical MAC address instead of a randomized MAC address. When TRUE, it uses the actual Wi-Fi MAC address. When FALSE, it enables the MAC address randomization. Applies to macOS 15 and later. Default is false.
    wifi_require_physical_mac_address_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSEnterpriseWiFiConfiguration".casefold():
            from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration

            return MacOSEnterpriseWiFiConfiguration()
        return MacOSWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting
        from .wi_fi_security_type import WiFiSecurityType

        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting
        from .wi_fi_security_type import WiFiSecurityType

        fields: dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "deploymentChannel": lambda n : setattr(self, 'deployment_channel', n.get_enum_value(AppleDeploymentChannel)),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "proxyAutomaticConfigurationUrl": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxyManualAddress": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxyManualPort": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxySettings": lambda n : setattr(self, 'proxy_settings', n.get_enum_value(WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wiFiSecurityType": lambda n : setattr(self, 'wi_fi_security_type', n.get_enum_value(WiFiSecurityType)),
            "wifiRequirePhysicalMacAddressEnabled": lambda n : setattr(self, 'wifi_require_physical_mac_address_enabled', n.get_bool_value()),
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
        writer.write_enum_value("deploymentChannel", self.deployment_channel)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_str_value("proxyManualAddress", self.proxy_manual_address)
        writer.write_int_value("proxyManualPort", self.proxy_manual_port)
        writer.write_enum_value("proxySettings", self.proxy_settings)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wiFiSecurityType", self.wi_fi_security_type)
        writer.write_bool_value("wifiRequirePhysicalMacAddressEnabled", self.wifi_require_physical_mac_address_enabled)
    

