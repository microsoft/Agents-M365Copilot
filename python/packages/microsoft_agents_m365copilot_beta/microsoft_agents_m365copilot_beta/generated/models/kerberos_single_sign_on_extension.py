from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .single_sign_on_extension import SingleSignOnExtension

from .single_sign_on_extension import SingleSignOnExtension

@dataclass
class KerberosSingleSignOnExtension(SingleSignOnExtension, Parsable):
    """
    Represents a Kerberos-type Single Sign-On extension profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.kerberosSingleSignOnExtension"
    # Gets or sets the Active Directory site.
    active_directory_site_code: Optional[str] = None
    # Enables or disables whether the Kerberos extension can automatically determine its site name.
    block_active_directory_site_auto_discovery: Optional[bool] = None
    # Enables or disables Keychain usage.
    block_automatic_login: Optional[bool] = None
    # Gets or sets the Generic Security Services name of the Kerberos cache to use for this profile.
    cache_name: Optional[str] = None
    # Gets or sets a list of app Bundle IDs allowed to access the Kerberos Ticket Granting Ticket.
    credential_bundle_id_access_control_list: Optional[list[str]] = None
    # Gets or sets a list of realms for custom domain-realm mapping. Realms are case sensitive.
    domain_realms: Optional[list[str]] = None
    # Gets or sets a list of hosts or domain names for which the app extension performs SSO.
    domains: Optional[list[str]] = None
    # When true, this profile's realm will be selected as the default. Necessary if multiple Kerberos-type profiles are configured.
    is_default_realm: Optional[bool] = None
    # Enables or disables password changes.
    password_block_modification: Optional[bool] = None
    # Gets or sets the URL that the user will be sent to when they initiate a password change.
    password_change_url: Optional[str] = None
    # Enables or disables password syncing. This won't affect users logged in with a mobile account on macOS.
    password_enable_local_sync: Optional[bool] = None
    # Overrides the default password expiration in days. For most domains, this value is calculated automatically.
    password_expiration_days: Optional[int] = None
    # Gets or sets the number of days until the user is notified that their password will expire (default is 15).
    password_expiration_notification_days: Optional[int] = None
    # Gets or sets the minimum number of days until a user can change their password again.
    password_minimum_age_days: Optional[int] = None
    # Gets or sets the minimum length of a password.
    password_minimum_length: Optional[int] = None
    # Gets or sets the number of previous passwords to block.
    password_previous_password_block_count: Optional[int] = None
    # Enables or disables whether passwords must meet Active Directory's complexity requirements.
    password_require_active_directory_complexity: Optional[bool] = None
    # Gets or sets a description of the password complexity requirements.
    password_requirements_description: Optional[str] = None
    # Gets or sets the case-sensitive realm name for this profile.
    realm: Optional[str] = None
    # Gets or sets whether to require authentication via Touch ID, Face ID, or a passcode to access the keychain entry.
    require_user_presence: Optional[bool] = None
    # Gets or sets the principle user name to use for this profile. The realm name does not need to be included.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KerberosSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KerberosSingleSignOnExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KerberosSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .single_sign_on_extension import SingleSignOnExtension

        from .single_sign_on_extension import SingleSignOnExtension

        fields: dict[str, Callable[[Any], None]] = {
            "activeDirectorySiteCode": lambda n : setattr(self, 'active_directory_site_code', n.get_str_value()),
            "blockActiveDirectorySiteAutoDiscovery": lambda n : setattr(self, 'block_active_directory_site_auto_discovery', n.get_bool_value()),
            "blockAutomaticLogin": lambda n : setattr(self, 'block_automatic_login', n.get_bool_value()),
            "cacheName": lambda n : setattr(self, 'cache_name', n.get_str_value()),
            "credentialBundleIdAccessControlList": lambda n : setattr(self, 'credential_bundle_id_access_control_list', n.get_collection_of_primitive_values(str)),
            "domainRealms": lambda n : setattr(self, 'domain_realms', n.get_collection_of_primitive_values(str)),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "isDefaultRealm": lambda n : setattr(self, 'is_default_realm', n.get_bool_value()),
            "passwordBlockModification": lambda n : setattr(self, 'password_block_modification', n.get_bool_value()),
            "passwordChangeUrl": lambda n : setattr(self, 'password_change_url', n.get_str_value()),
            "passwordEnableLocalSync": lambda n : setattr(self, 'password_enable_local_sync', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordExpirationNotificationDays": lambda n : setattr(self, 'password_expiration_notification_days', n.get_int_value()),
            "passwordMinimumAgeDays": lambda n : setattr(self, 'password_minimum_age_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequireActiveDirectoryComplexity": lambda n : setattr(self, 'password_require_active_directory_complexity', n.get_bool_value()),
            "passwordRequirementsDescription": lambda n : setattr(self, 'password_requirements_description', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "requireUserPresence": lambda n : setattr(self, 'require_user_presence', n.get_bool_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("activeDirectorySiteCode", self.active_directory_site_code)
        writer.write_bool_value("blockActiveDirectorySiteAutoDiscovery", self.block_active_directory_site_auto_discovery)
        writer.write_bool_value("blockAutomaticLogin", self.block_automatic_login)
        writer.write_str_value("cacheName", self.cache_name)
        writer.write_collection_of_primitive_values("credentialBundleIdAccessControlList", self.credential_bundle_id_access_control_list)
        writer.write_collection_of_primitive_values("domainRealms", self.domain_realms)
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_bool_value("isDefaultRealm", self.is_default_realm)
        writer.write_bool_value("passwordBlockModification", self.password_block_modification)
        writer.write_str_value("passwordChangeUrl", self.password_change_url)
        writer.write_bool_value("passwordEnableLocalSync", self.password_enable_local_sync)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordExpirationNotificationDays", self.password_expiration_notification_days)
        writer.write_int_value("passwordMinimumAgeDays", self.password_minimum_age_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequireActiveDirectoryComplexity", self.password_require_active_directory_complexity)
        writer.write_str_value("passwordRequirementsDescription", self.password_requirements_description)
        writer.write_str_value("realm", self.realm)
        writer.write_bool_value("requireUserPresence", self.require_user_presence)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

