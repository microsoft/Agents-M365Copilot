from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ddm_app_allow_downloads_over_cellular import DdmAppAllowDownloadsOverCellular
    from .ddm_app_automatic_app_updates import DdmAppAutomaticAppUpdates
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class IosDdmStoreAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign an iOS Declarative Device Management (DDM) Store App to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosDdmStoreAppAssignmentSettings"
    # Specifies whether the app may be downloaded over cellular connections. Possible values are: 'alwaysOn', 'alwaysOff', 'storeSettings'. By default, this value is set to 'storeSettings'.
    allow_downloads_over_cellular: Optional[DdmAppAllowDownloadsOverCellular] = None
    # Domain names to associate with the app
    associated_domains: Optional[list[str]] = None
    # When true, the system allows direct downloads for the AssociatedDomains. When false, the system will not allow direct downloads for the AssociatedDomains. Default is false.
    associated_domains_direct_download_allowed: Optional[bool] = None
    # Specifies whether the device automatically updates the app. Possible values are: 'alwaysOn', 'alwaysOff', 'storeSettings'. By default, this value is set to 'storeSettings'.
    automatic_app_updates: Optional[DdmAppAutomaticAppUpdates] = None
    # The cellular slice identifier, which can be the data network name (DNN) or app category. For DNN, encode the value as 'DNN:name', where 'name' is the carrier-provided DNN name. For app category, encode the value as 'AppCategory:category', where 'category' is a carrier-provided string such as 'Enterprise1'.
    cellular_slice_configuration_id: Optional[str] = None
    # The unique identifier of the content filter to associate with the app.
    content_filter_configuration_id: Optional[str] = None
    # The unique identifier of the DNS proxy to associate with the app.
    dns_proxy_configuration_id: Optional[str] = None
    # When true, indicates that the app should not be backed up to iCloud. When false, indicates that the app may be backed up to iCloud. Default is false.
    prevent_managed_app_backup: Optional[bool] = None
    # The unique identifier of the relay to associate with the app.
    relay_configuration_id: Optional[str] = None
    # When true, the device locks its screen after every transaction that requires a customer's card PIN. When false, the user can choose the behavior. Default value is false.
    tap_to_pay_screen_lock_enabled: Optional[bool] = None
    # Specifies the version of the Store app to install. When not set, the device installs the latest version. When set, the device installs the specified version. The device never installs an older version of the app over a newer version.
    version: Optional[int] = None
    # The unique identifier of the VPN Configuration to apply to the app.
    vpn_configuration_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosDdmStoreAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosDdmStoreAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosDdmStoreAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ddm_app_allow_downloads_over_cellular import DdmAppAllowDownloadsOverCellular
        from .ddm_app_automatic_app_updates import DdmAppAutomaticAppUpdates
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .ddm_app_allow_downloads_over_cellular import DdmAppAllowDownloadsOverCellular
        from .ddm_app_automatic_app_updates import DdmAppAutomaticAppUpdates
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "allowDownloadsOverCellular": lambda n : setattr(self, 'allow_downloads_over_cellular', n.get_enum_value(DdmAppAllowDownloadsOverCellular)),
            "associatedDomains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_primitive_values(str)),
            "associatedDomainsDirectDownloadAllowed": lambda n : setattr(self, 'associated_domains_direct_download_allowed', n.get_bool_value()),
            "automaticAppUpdates": lambda n : setattr(self, 'automatic_app_updates', n.get_enum_value(DdmAppAutomaticAppUpdates)),
            "cellularSliceConfigurationId": lambda n : setattr(self, 'cellular_slice_configuration_id', n.get_str_value()),
            "contentFilterConfigurationId": lambda n : setattr(self, 'content_filter_configuration_id', n.get_str_value()),
            "dnsProxyConfigurationId": lambda n : setattr(self, 'dns_proxy_configuration_id', n.get_str_value()),
            "preventManagedAppBackup": lambda n : setattr(self, 'prevent_managed_app_backup', n.get_bool_value()),
            "relayConfigurationId": lambda n : setattr(self, 'relay_configuration_id', n.get_str_value()),
            "tapToPayScreenLockEnabled": lambda n : setattr(self, 'tap_to_pay_screen_lock_enabled', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "vpnConfigurationId": lambda n : setattr(self, 'vpn_configuration_id', n.get_str_value()),
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
        writer.write_enum_value("allowDownloadsOverCellular", self.allow_downloads_over_cellular)
        writer.write_collection_of_primitive_values("associatedDomains", self.associated_domains)
        writer.write_bool_value("associatedDomainsDirectDownloadAllowed", self.associated_domains_direct_download_allowed)
        writer.write_enum_value("automaticAppUpdates", self.automatic_app_updates)
        writer.write_str_value("cellularSliceConfigurationId", self.cellular_slice_configuration_id)
        writer.write_str_value("contentFilterConfigurationId", self.content_filter_configuration_id)
        writer.write_str_value("dnsProxyConfigurationId", self.dns_proxy_configuration_id)
        writer.write_bool_value("preventManagedAppBackup", self.prevent_managed_app_backup)
        writer.write_str_value("relayConfigurationId", self.relay_configuration_id)
        writer.write_bool_value("tapToPayScreenLockEnabled", self.tap_to_pay_screen_lock_enabled)
        writer.write_int_value("version", self.version)
        writer.write_str_value("vpnConfigurationId", self.vpn_configuration_id)
    

