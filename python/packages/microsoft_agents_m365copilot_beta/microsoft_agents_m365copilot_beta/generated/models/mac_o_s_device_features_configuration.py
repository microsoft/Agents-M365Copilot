from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .ip_range import IpRange
    from .key_value_pair import KeyValuePair
    from .mac_o_s_associated_domains_item import MacOSAssociatedDomainsItem
    from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
    from .mac_o_s_content_caching_client_policy import MacOSContentCachingClientPolicy
    from .mac_o_s_content_caching_parent_selection_policy import MacOSContentCachingParentSelectionPolicy
    from .mac_o_s_content_caching_peer_policy import MacOSContentCachingPeerPolicy
    from .mac_o_s_content_caching_type import MacOSContentCachingType
    from .mac_o_s_launch_item import MacOSLaunchItem
    from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
    from .single_sign_on_extension import SingleSignOnExtension

from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

@dataclass
class MacOSDeviceFeaturesConfiguration(AppleDeviceFeaturesConfigurationBase, Parsable):
    """
    MacOS device features configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSDeviceFeaturesConfiguration"
    # Whether to show admin host information on the login window.
    admin_show_host_info: Optional[bool] = None
    # Gets or sets a list that maps apps to their associated domains. Application identifiers must be unique. This collection can contain a maximum of 500 elements.
    app_associated_domains: Optional[list[MacOSAssociatedDomainsItem]] = None
    # DEPRECATED: use appAssociatedDomains instead. Gets or sets a list that maps apps to their associated domains. The key should match the app's ID, and the value should be a string in the form of 'service:domain' where domain is a fully qualified hostname (e.g. webcredentials:example.com). This collection can contain a maximum of 500 elements.
    associated_domains: Optional[list[KeyValuePair]] = None
    # Whether to show the name and password dialog or a list of users on the login window.
    authorized_users_list_hidden: Optional[bool] = None
    # Whether to hide admin users in the authorized users list on the login window.
    authorized_users_list_hide_admin_users: Optional[bool] = None
    # Whether to show only network and system users in the authorized users list on the login window.
    authorized_users_list_hide_local_users: Optional[bool] = None
    # Whether to hide mobile users in the authorized users list on the login window.
    authorized_users_list_hide_mobile_accounts: Optional[bool] = None
    # Whether to show network users in the authorized users list on the login window.
    authorized_users_list_include_network_users: Optional[bool] = None
    # Whether to show other users in the authorized users list on the login window.
    authorized_users_list_show_other_managed_users: Optional[bool] = None
    # List of applications, files, folders, and other items to launch when the user logs in. This collection can contain a maximum of 500 elements.
    auto_launch_items: Optional[list[MacOSLaunchItem]] = None
    # Whether the Other user will disregard use of the console special user name.
    console_access_disabled: Optional[bool] = None
    # Prevents content caches from purging content to free up disk space for other apps.
    content_caching_block_deletion: Optional[bool] = None
    # A list of custom IP ranges content caches will use to listen for clients. This collection can contain a maximum of 500 elements.
    content_caching_client_listen_ranges: Optional[list[IpRange]] = None
    # Determines which clients a content cache will serve.
    content_caching_client_policy: Optional[MacOSContentCachingClientPolicy] = None
    # The path to the directory used to store cached content. The value must be (or end with) /Library/Application Support/Apple/AssetCache/Data
    content_caching_data_path: Optional[str] = None
    # Disables internet connection sharing.
    content_caching_disable_connection_sharing: Optional[bool] = None
    # Enables content caching and prevents it from being disabled by the user.
    content_caching_enabled: Optional[bool] = None
    # Forces internet connection sharing. contentCachingDisableConnectionSharing overrides this setting.
    content_caching_force_connection_sharing: Optional[bool] = None
    # Prevent the device from sleeping if content caching is enabled.
    content_caching_keep_awake: Optional[bool] = None
    # Enables logging of IP addresses and ports of clients that request cached content.
    content_caching_log_client_identities: Optional[bool] = None
    # The maximum number of bytes of disk space that will be used for the content cache. A value of 0 (default) indicates unlimited disk space.
    content_caching_max_size_bytes: Optional[int] = None
    # Determines how content caches select a parent cache.
    content_caching_parent_selection_policy: Optional[MacOSContentCachingParentSelectionPolicy] = None
    # A list of IP addresses representing parent content caches.
    content_caching_parents: Optional[list[str]] = None
    # A list of custom IP ranges content caches will use to query for content from peers caches. This collection can contain a maximum of 500 elements.
    content_caching_peer_filter_ranges: Optional[list[IpRange]] = None
    # A list of custom IP ranges content caches will use to listen for peer caches. This collection can contain a maximum of 500 elements.
    content_caching_peer_listen_ranges: Optional[list[IpRange]] = None
    # Determines which content caches other content caches will peer with.
    content_caching_peer_policy: Optional[MacOSContentCachingPeerPolicy] = None
    # Sets the port used for content caching. If the value is 0, a random available port will be selected. Valid values 0 to 65535
    content_caching_port: Optional[int] = None
    # A list of custom IP ranges that Apple's content caching service should use to match clients to content caches. This collection can contain a maximum of 500 elements.
    content_caching_public_ranges: Optional[list[IpRange]] = None
    # Display content caching alerts as system notifications.
    content_caching_show_alerts: Optional[bool] = None
    # Indicates the type of content allowed to be cached by Apple's content caching service.
    content_caching_type: Optional[MacOSContentCachingType] = None
    # Whether the Log Out menu item on the login window will be disabled while the user is logged in.
    log_out_disabled_while_logged_in: Optional[bool] = None
    # Custom text to be displayed on the login window.
    login_window_text: Optional[str] = None
    # Gets or sets a single sign-on extension profile.
    mac_o_s_single_sign_on_extension: Optional[MacOSSingleSignOnExtension] = None
    # Whether the Power Off menu item on the login window will be disabled while the user is logged in.
    power_off_disabled_while_logged_in: Optional[bool] = None
    # Whether to hide the Restart button item on the login window.
    restart_disabled: Optional[bool] = None
    # Whether the Restart menu item on the login window will be disabled while the user is logged in.
    restart_disabled_while_logged_in: Optional[bool] = None
    # Whether to disable the immediate screen lock functions.
    screen_lock_disable_immediate: Optional[bool] = None
    # Whether to hide the Shut Down button item on the login window.
    shut_down_disabled: Optional[bool] = None
    # Whether the Shut Down menu item on the login window will be disabled while the user is logged in.
    shut_down_disabled_while_logged_in: Optional[bool] = None
    # Gets or sets a single sign-on extension profile. Deprecated: use MacOSSingleSignOnExtension instead.
    single_sign_on_extension: Optional[SingleSignOnExtension] = None
    # PKINIT Certificate for the authentication with single sign-on extensions.
    single_sign_on_extension_pkinit_certificate: Optional[MacOSCertificateProfileBase] = None
    # Whether to hide the Sleep menu item on the login window.
    sleep_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSDeviceFeaturesConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .ip_range import IpRange
        from .key_value_pair import KeyValuePair
        from .mac_o_s_associated_domains_item import MacOSAssociatedDomainsItem
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_content_caching_client_policy import MacOSContentCachingClientPolicy
        from .mac_o_s_content_caching_parent_selection_policy import MacOSContentCachingParentSelectionPolicy
        from .mac_o_s_content_caching_peer_policy import MacOSContentCachingPeerPolicy
        from .mac_o_s_content_caching_type import MacOSContentCachingType
        from .mac_o_s_launch_item import MacOSLaunchItem
        from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
        from .single_sign_on_extension import SingleSignOnExtension

        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .ip_range import IpRange
        from .key_value_pair import KeyValuePair
        from .mac_o_s_associated_domains_item import MacOSAssociatedDomainsItem
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_content_caching_client_policy import MacOSContentCachingClientPolicy
        from .mac_o_s_content_caching_parent_selection_policy import MacOSContentCachingParentSelectionPolicy
        from .mac_o_s_content_caching_peer_policy import MacOSContentCachingPeerPolicy
        from .mac_o_s_content_caching_type import MacOSContentCachingType
        from .mac_o_s_launch_item import MacOSLaunchItem
        from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
        from .single_sign_on_extension import SingleSignOnExtension

        fields: dict[str, Callable[[Any], None]] = {
            "adminShowHostInfo": lambda n : setattr(self, 'admin_show_host_info', n.get_bool_value()),
            "appAssociatedDomains": lambda n : setattr(self, 'app_associated_domains', n.get_collection_of_object_values(MacOSAssociatedDomainsItem)),
            "associatedDomains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_object_values(KeyValuePair)),
            "authorizedUsersListHidden": lambda n : setattr(self, 'authorized_users_list_hidden', n.get_bool_value()),
            "authorizedUsersListHideAdminUsers": lambda n : setattr(self, 'authorized_users_list_hide_admin_users', n.get_bool_value()),
            "authorizedUsersListHideLocalUsers": lambda n : setattr(self, 'authorized_users_list_hide_local_users', n.get_bool_value()),
            "authorizedUsersListHideMobileAccounts": lambda n : setattr(self, 'authorized_users_list_hide_mobile_accounts', n.get_bool_value()),
            "authorizedUsersListIncludeNetworkUsers": lambda n : setattr(self, 'authorized_users_list_include_network_users', n.get_bool_value()),
            "authorizedUsersListShowOtherManagedUsers": lambda n : setattr(self, 'authorized_users_list_show_other_managed_users', n.get_bool_value()),
            "autoLaunchItems": lambda n : setattr(self, 'auto_launch_items', n.get_collection_of_object_values(MacOSLaunchItem)),
            "consoleAccessDisabled": lambda n : setattr(self, 'console_access_disabled', n.get_bool_value()),
            "contentCachingBlockDeletion": lambda n : setattr(self, 'content_caching_block_deletion', n.get_bool_value()),
            "contentCachingClientListenRanges": lambda n : setattr(self, 'content_caching_client_listen_ranges', n.get_collection_of_object_values(IpRange)),
            "contentCachingClientPolicy": lambda n : setattr(self, 'content_caching_client_policy', n.get_enum_value(MacOSContentCachingClientPolicy)),
            "contentCachingDataPath": lambda n : setattr(self, 'content_caching_data_path', n.get_str_value()),
            "contentCachingDisableConnectionSharing": lambda n : setattr(self, 'content_caching_disable_connection_sharing', n.get_bool_value()),
            "contentCachingEnabled": lambda n : setattr(self, 'content_caching_enabled', n.get_bool_value()),
            "contentCachingForceConnectionSharing": lambda n : setattr(self, 'content_caching_force_connection_sharing', n.get_bool_value()),
            "contentCachingKeepAwake": lambda n : setattr(self, 'content_caching_keep_awake', n.get_bool_value()),
            "contentCachingLogClientIdentities": lambda n : setattr(self, 'content_caching_log_client_identities', n.get_bool_value()),
            "contentCachingMaxSizeBytes": lambda n : setattr(self, 'content_caching_max_size_bytes', n.get_int_value()),
            "contentCachingParentSelectionPolicy": lambda n : setattr(self, 'content_caching_parent_selection_policy', n.get_enum_value(MacOSContentCachingParentSelectionPolicy)),
            "contentCachingParents": lambda n : setattr(self, 'content_caching_parents', n.get_collection_of_primitive_values(str)),
            "contentCachingPeerFilterRanges": lambda n : setattr(self, 'content_caching_peer_filter_ranges', n.get_collection_of_object_values(IpRange)),
            "contentCachingPeerListenRanges": lambda n : setattr(self, 'content_caching_peer_listen_ranges', n.get_collection_of_object_values(IpRange)),
            "contentCachingPeerPolicy": lambda n : setattr(self, 'content_caching_peer_policy', n.get_enum_value(MacOSContentCachingPeerPolicy)),
            "contentCachingPort": lambda n : setattr(self, 'content_caching_port', n.get_int_value()),
            "contentCachingPublicRanges": lambda n : setattr(self, 'content_caching_public_ranges', n.get_collection_of_object_values(IpRange)),
            "contentCachingShowAlerts": lambda n : setattr(self, 'content_caching_show_alerts', n.get_bool_value()),
            "contentCachingType": lambda n : setattr(self, 'content_caching_type', n.get_enum_value(MacOSContentCachingType)),
            "logOutDisabledWhileLoggedIn": lambda n : setattr(self, 'log_out_disabled_while_logged_in', n.get_bool_value()),
            "loginWindowText": lambda n : setattr(self, 'login_window_text', n.get_str_value()),
            "macOSSingleSignOnExtension": lambda n : setattr(self, 'mac_o_s_single_sign_on_extension', n.get_object_value(MacOSSingleSignOnExtension)),
            "powerOffDisabledWhileLoggedIn": lambda n : setattr(self, 'power_off_disabled_while_logged_in', n.get_bool_value()),
            "restartDisabled": lambda n : setattr(self, 'restart_disabled', n.get_bool_value()),
            "restartDisabledWhileLoggedIn": lambda n : setattr(self, 'restart_disabled_while_logged_in', n.get_bool_value()),
            "screenLockDisableImmediate": lambda n : setattr(self, 'screen_lock_disable_immediate', n.get_bool_value()),
            "shutDownDisabled": lambda n : setattr(self, 'shut_down_disabled', n.get_bool_value()),
            "shutDownDisabledWhileLoggedIn": lambda n : setattr(self, 'shut_down_disabled_while_logged_in', n.get_bool_value()),
            "singleSignOnExtension": lambda n : setattr(self, 'single_sign_on_extension', n.get_object_value(SingleSignOnExtension)),
            "singleSignOnExtensionPkinitCertificate": lambda n : setattr(self, 'single_sign_on_extension_pkinit_certificate', n.get_object_value(MacOSCertificateProfileBase)),
            "sleepDisabled": lambda n : setattr(self, 'sleep_disabled', n.get_bool_value()),
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
        writer.write_bool_value("adminShowHostInfo", self.admin_show_host_info)
        writer.write_collection_of_object_values("appAssociatedDomains", self.app_associated_domains)
        writer.write_collection_of_object_values("associatedDomains", self.associated_domains)
        writer.write_bool_value("authorizedUsersListHidden", self.authorized_users_list_hidden)
        writer.write_bool_value("authorizedUsersListHideAdminUsers", self.authorized_users_list_hide_admin_users)
        writer.write_bool_value("authorizedUsersListHideLocalUsers", self.authorized_users_list_hide_local_users)
        writer.write_bool_value("authorizedUsersListHideMobileAccounts", self.authorized_users_list_hide_mobile_accounts)
        writer.write_bool_value("authorizedUsersListIncludeNetworkUsers", self.authorized_users_list_include_network_users)
        writer.write_bool_value("authorizedUsersListShowOtherManagedUsers", self.authorized_users_list_show_other_managed_users)
        writer.write_collection_of_object_values("autoLaunchItems", self.auto_launch_items)
        writer.write_bool_value("consoleAccessDisabled", self.console_access_disabled)
        writer.write_bool_value("contentCachingBlockDeletion", self.content_caching_block_deletion)
        writer.write_collection_of_object_values("contentCachingClientListenRanges", self.content_caching_client_listen_ranges)
        writer.write_enum_value("contentCachingClientPolicy", self.content_caching_client_policy)
        writer.write_str_value("contentCachingDataPath", self.content_caching_data_path)
        writer.write_bool_value("contentCachingDisableConnectionSharing", self.content_caching_disable_connection_sharing)
        writer.write_bool_value("contentCachingEnabled", self.content_caching_enabled)
        writer.write_bool_value("contentCachingForceConnectionSharing", self.content_caching_force_connection_sharing)
        writer.write_bool_value("contentCachingKeepAwake", self.content_caching_keep_awake)
        writer.write_bool_value("contentCachingLogClientIdentities", self.content_caching_log_client_identities)
        writer.write_int_value("contentCachingMaxSizeBytes", self.content_caching_max_size_bytes)
        writer.write_enum_value("contentCachingParentSelectionPolicy", self.content_caching_parent_selection_policy)
        writer.write_collection_of_primitive_values("contentCachingParents", self.content_caching_parents)
        writer.write_collection_of_object_values("contentCachingPeerFilterRanges", self.content_caching_peer_filter_ranges)
        writer.write_collection_of_object_values("contentCachingPeerListenRanges", self.content_caching_peer_listen_ranges)
        writer.write_enum_value("contentCachingPeerPolicy", self.content_caching_peer_policy)
        writer.write_int_value("contentCachingPort", self.content_caching_port)
        writer.write_collection_of_object_values("contentCachingPublicRanges", self.content_caching_public_ranges)
        writer.write_bool_value("contentCachingShowAlerts", self.content_caching_show_alerts)
        writer.write_enum_value("contentCachingType", self.content_caching_type)
        writer.write_bool_value("logOutDisabledWhileLoggedIn", self.log_out_disabled_while_logged_in)
        writer.write_str_value("loginWindowText", self.login_window_text)
        writer.write_object_value("macOSSingleSignOnExtension", self.mac_o_s_single_sign_on_extension)
        writer.write_bool_value("powerOffDisabledWhileLoggedIn", self.power_off_disabled_while_logged_in)
        writer.write_bool_value("restartDisabled", self.restart_disabled)
        writer.write_bool_value("restartDisabledWhileLoggedIn", self.restart_disabled_while_logged_in)
        writer.write_bool_value("screenLockDisableImmediate", self.screen_lock_disable_immediate)
        writer.write_bool_value("shutDownDisabled", self.shut_down_disabled)
        writer.write_bool_value("shutDownDisabledWhileLoggedIn", self.shut_down_disabled_while_logged_in)
        writer.write_object_value("singleSignOnExtension", self.single_sign_on_extension)
        writer.write_object_value("singleSignOnExtensionPkinitCertificate", self.single_sign_on_extension_pkinit_certificate)
        writer.write_bool_value("sleepDisabled", self.sleep_disabled)
    

