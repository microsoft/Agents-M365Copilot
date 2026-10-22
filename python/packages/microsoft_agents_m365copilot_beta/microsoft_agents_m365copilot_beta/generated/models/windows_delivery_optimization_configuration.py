from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
    from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource
    from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize
    from .delivery_optimization_restrict_peer_selection_by_options import DeliveryOptimizationRestrictPeerSelectionByOptions
    from .device_configuration import DeviceConfiguration
    from .enablement import Enablement
    from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsDeliveryOptimizationConfiguration(DeviceConfiguration, Parsable):
    """
    Windows Delivery Optimization configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsDeliveryOptimizationConfiguration"
    # Specifies number of seconds to delay an HTTP source in a background download that is allowed to use peer-to-peer. Valid values 0 to 4294967295
    background_download_from_http_delay_in_seconds: Optional[int] = None
    # Specifies foreground and background bandwidth usage using percentages, absolutes, or hours.
    bandwidth_mode: Optional[DeliveryOptimizationBandwidth] = None
    # Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a background download. Valid values 0 to 2592000.
    cache_server_background_download_fallback_to_http_delay_in_seconds: Optional[int] = None
    # Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a foreground download. Valid values 0 to 2592000.​
    cache_server_foreground_download_fallback_to_http_delay_in_seconds: Optional[int] = None
    # Specifies cache servers host names.
    cache_server_host_names: Optional[list[str]] = None
    # Delivery optimization mode for peer distribution
    delivery_optimization_mode: Optional[WindowsDeliveryOptimizationMode] = None
    # Specifies number of seconds to delay an HTTP source in a foreground download that is allowed to use peer-to-peer (0-86400). Valid values 0 to 86400
    foreground_download_from_http_delay_in_seconds: Optional[int] = None
    # Specifies to restrict peer selection to a specfic source.
    group_id_source: Optional[DeliveryOptimizationGroupIdSource] = None
    # Specifies the maximum time in days that each file is held in the Delivery Optimization cache after downloading successfully (0-3650). Valid values 0 to 3650
    maximum_cache_age_in_days: Optional[int] = None
    # Specifies the maximum cache size that Delivery Optimization either as a percentage or in GB.
    maximum_cache_size: Optional[DeliveryOptimizationMaxCacheSize] = None
    # Specifies the minimum battery percentage to allow the device to upload data (0-100). Valid values 0 to 100
    minimum_battery_percentage_allowed_to_upload: Optional[int] = None
    # Specifies the minimum disk size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
    minimum_disk_size_allowed_to_peer_in_gigabytes: Optional[int] = None
    # Specifies the minimum content file size in MB enabled to use Peer Caching (1-100000). Valid values 1 to 100000
    minimum_file_size_to_cache_in_megabytes: Optional[int] = None
    # Specifies the minimum RAM size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
    minimum_ram_allowed_to_peer_in_gigabytes: Optional[int] = None
    # Specifies the drive that Delivery Optimization should use for its cache.
    modify_cache_location: Optional[str] = None
    # Values to restrict peer selection by.
    restrict_peer_selection_by: Optional[DeliveryOptimizationRestrictPeerSelectionByOptions] = None
    # Possible values of a property
    vpn_peer_caching: Optional[Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDeliveryOptimizationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDeliveryOptimizationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDeliveryOptimizationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
        from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource
        from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize
        from .delivery_optimization_restrict_peer_selection_by_options import DeliveryOptimizationRestrictPeerSelectionByOptions
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode

        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
        from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource
        from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize
        from .delivery_optimization_restrict_peer_selection_by_options import DeliveryOptimizationRestrictPeerSelectionByOptions
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode

        fields: dict[str, Callable[[Any], None]] = {
            "backgroundDownloadFromHttpDelayInSeconds": lambda n : setattr(self, 'background_download_from_http_delay_in_seconds', n.get_int_value()),
            "bandwidthMode": lambda n : setattr(self, 'bandwidth_mode', n.get_object_value(DeliveryOptimizationBandwidth)),
            "cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds": lambda n : setattr(self, 'cache_server_background_download_fallback_to_http_delay_in_seconds', n.get_int_value()),
            "cacheServerForegroundDownloadFallbackToHttpDelayInSeconds": lambda n : setattr(self, 'cache_server_foreground_download_fallback_to_http_delay_in_seconds', n.get_int_value()),
            "cacheServerHostNames": lambda n : setattr(self, 'cache_server_host_names', n.get_collection_of_primitive_values(str)),
            "deliveryOptimizationMode": lambda n : setattr(self, 'delivery_optimization_mode', n.get_enum_value(WindowsDeliveryOptimizationMode)),
            "foregroundDownloadFromHttpDelayInSeconds": lambda n : setattr(self, 'foreground_download_from_http_delay_in_seconds', n.get_int_value()),
            "groupIdSource": lambda n : setattr(self, 'group_id_source', n.get_object_value(DeliveryOptimizationGroupIdSource)),
            "maximumCacheAgeInDays": lambda n : setattr(self, 'maximum_cache_age_in_days', n.get_int_value()),
            "maximumCacheSize": lambda n : setattr(self, 'maximum_cache_size', n.get_object_value(DeliveryOptimizationMaxCacheSize)),
            "minimumBatteryPercentageAllowedToUpload": lambda n : setattr(self, 'minimum_battery_percentage_allowed_to_upload', n.get_int_value()),
            "minimumDiskSizeAllowedToPeerInGigabytes": lambda n : setattr(self, 'minimum_disk_size_allowed_to_peer_in_gigabytes', n.get_int_value()),
            "minimumFileSizeToCacheInMegabytes": lambda n : setattr(self, 'minimum_file_size_to_cache_in_megabytes', n.get_int_value()),
            "minimumRamAllowedToPeerInGigabytes": lambda n : setattr(self, 'minimum_ram_allowed_to_peer_in_gigabytes', n.get_int_value()),
            "modifyCacheLocation": lambda n : setattr(self, 'modify_cache_location', n.get_str_value()),
            "restrictPeerSelectionBy": lambda n : setattr(self, 'restrict_peer_selection_by', n.get_enum_value(DeliveryOptimizationRestrictPeerSelectionByOptions)),
            "vpnPeerCaching": lambda n : setattr(self, 'vpn_peer_caching', n.get_enum_value(Enablement)),
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
        writer.write_int_value("backgroundDownloadFromHttpDelayInSeconds", self.background_download_from_http_delay_in_seconds)
        writer.write_object_value("bandwidthMode", self.bandwidth_mode)
        writer.write_int_value("cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds", self.cache_server_background_download_fallback_to_http_delay_in_seconds)
        writer.write_int_value("cacheServerForegroundDownloadFallbackToHttpDelayInSeconds", self.cache_server_foreground_download_fallback_to_http_delay_in_seconds)
        writer.write_collection_of_primitive_values("cacheServerHostNames", self.cache_server_host_names)
        writer.write_enum_value("deliveryOptimizationMode", self.delivery_optimization_mode)
        writer.write_int_value("foregroundDownloadFromHttpDelayInSeconds", self.foreground_download_from_http_delay_in_seconds)
        writer.write_object_value("groupIdSource", self.group_id_source)
        writer.write_int_value("maximumCacheAgeInDays", self.maximum_cache_age_in_days)
        writer.write_object_value("maximumCacheSize", self.maximum_cache_size)
        writer.write_int_value("minimumBatteryPercentageAllowedToUpload", self.minimum_battery_percentage_allowed_to_upload)
        writer.write_int_value("minimumDiskSizeAllowedToPeerInGigabytes", self.minimum_disk_size_allowed_to_peer_in_gigabytes)
        writer.write_int_value("minimumFileSizeToCacheInMegabytes", self.minimum_file_size_to_cache_in_megabytes)
        writer.write_int_value("minimumRamAllowedToPeerInGigabytes", self.minimum_ram_allowed_to_peer_in_gigabytes)
        writer.write_str_value("modifyCacheLocation", self.modify_cache_location)
        writer.write_enum_value("restrictPeerSelectionBy", self.restrict_peer_selection_by)
        writer.write_enum_value("vpnPeerCaching", self.vpn_peer_caching)
    

