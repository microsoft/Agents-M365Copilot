from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .metered_connection_limit_type import MeteredConnectionLimitType
    from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
    from .wi_fi_proxy_setting import WiFiProxySetting
    from .wi_fi_security_type import WiFiSecurityType

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsWifiConfiguration(DeviceConfiguration, Parsable):
    """
    Device Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsWifiConfiguration"
    # Specify whether the wifi connection should connect automatically when in range.
    connect_automatically: Optional[bool] = None
    # Specify whether the wifi connection should connect to more preferred networks when already connected to this one.  Requires ConnectAutomatically to be true.
    connect_to_preferred_network: Optional[bool] = None
    # Specify whether the wifi connection should connect automatically even when the SSID is not broadcasting.
    connect_when_network_name_is_hidden: Optional[bool] = None
    # Specify whether to force FIPS compliance.
    force_f_i_p_s_compliance: Optional[bool] = None
    # Specify the metered connection limit type for the wifi connection. Possible values are: unrestricted, fixed, variable.
    metered_connection_limit: Optional[MeteredConnectionLimitType] = None
    # Specify the network configuration name.
    network_name: Optional[str] = None
    # This is the pre-shared key for WPA Personal Wi-Fi network.
    pre_shared_key: Optional[str] = None
    # Specify the URL for the proxy server configuration script.
    proxy_automatic_configuration_url: Optional[str] = None
    # Specify the IP address for the proxy server.
    proxy_manual_address: Optional[str] = None
    # Specify the port for the proxy server.
    proxy_manual_port: Optional[int] = None
    # Specify the proxy setting for Wi-Fi configuration. Possible values are: none, manual, automatic, unknownFutureValue.
    proxy_setting: Optional[WiFiProxySetting] = None
    # Specify the SSID of the wifi connection.
    ssid: Optional[str] = None
    # Specify the Wifi Security Type. Possible values are: open, wpaPersonal, wpaEnterprise, wep, wpa2Personal, wpa2Enterprise, unknownFutureValue, wpa3Personal.
    wifi_security_type: Optional[WiFiSecurityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsWifiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWifiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration".casefold():
            from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration

            return WindowsWifiEnterpriseEAPConfiguration()
        return WindowsWifiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .metered_connection_limit_type import MeteredConnectionLimitType
        from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting
        from .wi_fi_security_type import WiFiSecurityType

        from .device_configuration import DeviceConfiguration
        from .metered_connection_limit_type import MeteredConnectionLimitType
        from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
        from .wi_fi_proxy_setting import WiFiProxySetting
        from .wi_fi_security_type import WiFiSecurityType

        fields: dict[str, Callable[[Any], None]] = {
            "connectAutomatically": lambda n : setattr(self, 'connect_automatically', n.get_bool_value()),
            "connectToPreferredNetwork": lambda n : setattr(self, 'connect_to_preferred_network', n.get_bool_value()),
            "connectWhenNetworkNameIsHidden": lambda n : setattr(self, 'connect_when_network_name_is_hidden', n.get_bool_value()),
            "forceFIPSCompliance": lambda n : setattr(self, 'force_f_i_p_s_compliance', n.get_bool_value()),
            "meteredConnectionLimit": lambda n : setattr(self, 'metered_connection_limit', n.get_enum_value(MeteredConnectionLimitType)),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "proxyAutomaticConfigurationUrl": lambda n : setattr(self, 'proxy_automatic_configuration_url', n.get_str_value()),
            "proxyManualAddress": lambda n : setattr(self, 'proxy_manual_address', n.get_str_value()),
            "proxyManualPort": lambda n : setattr(self, 'proxy_manual_port', n.get_int_value()),
            "proxySetting": lambda n : setattr(self, 'proxy_setting', n.get_enum_value(WiFiProxySetting)),
            "ssid": lambda n : setattr(self, 'ssid', n.get_str_value()),
            "wifiSecurityType": lambda n : setattr(self, 'wifi_security_type', n.get_enum_value(WiFiSecurityType)),
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
        writer.write_bool_value("connectToPreferredNetwork", self.connect_to_preferred_network)
        writer.write_bool_value("connectWhenNetworkNameIsHidden", self.connect_when_network_name_is_hidden)
        writer.write_bool_value("forceFIPSCompliance", self.force_f_i_p_s_compliance)
        writer.write_enum_value("meteredConnectionLimit", self.metered_connection_limit)
        writer.write_str_value("networkName", self.network_name)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_str_value("proxyAutomaticConfigurationUrl", self.proxy_automatic_configuration_url)
        writer.write_str_value("proxyManualAddress", self.proxy_manual_address)
        writer.write_int_value("proxyManualPort", self.proxy_manual_port)
        writer.write_enum_value("proxySetting", self.proxy_setting)
        writer.write_str_value("ssid", self.ssid)
        writer.write_enum_value("wifiSecurityType", self.wifi_security_type)
    

