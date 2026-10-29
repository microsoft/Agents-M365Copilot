from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_methods_policy import AuthenticationMethodsPolicy
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .compliant_network_named_location import CompliantNetworkNamedLocation
    from .conditional_access_policy import ConditionalAccessPolicy
    from .country_named_location import CountryNamedLocation
    from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
    from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
    from .delegated_admin_service_provider_constraints import DelegatedAdminServiceProviderConstraints
    from .ip_named_location import IpNamedLocation
    from .named_location import NamedLocation
    from .private_link_named_location import PrivateLinkNamedLocation
    from .service_provider_constraints import ServiceProviderConstraints
    from .service_tag_named_location import ServiceTagNamedLocation
    from .what_if_analysis_result import WhatIfAnalysisResult

@dataclass
class PolicyDeletableItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Shows the last date and time the policy was deleted.
    deleted_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyDeletableItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyDeletableItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodsPolicy".casefold():
            from .authentication_methods_policy import AuthenticationMethodsPolicy

            return AuthenticationMethodsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthPolicy".casefold():
            from .authentication_strength_policy import AuthenticationStrengthPolicy

            return AuthenticationStrengthPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.compliantNetworkNamedLocation".casefold():
            from .compliant_network_named_location import CompliantNetworkNamedLocation

            return CompliantNetworkNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessPolicy".casefold():
            from .conditional_access_policy import ConditionalAccessPolicy

            return ConditionalAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.countryNamedLocation".casefold():
            from .country_named_location import CountryNamedLocation

            return CountryNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicyConfigurationPartner".casefold():
            from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner

            return CrossTenantAccessPolicyConfigurationPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantIdentitySyncPolicyPartner".casefold():
            from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner

            return CrossTenantIdentitySyncPolicyPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminServiceProviderConstraints".casefold():
            from .delegated_admin_service_provider_constraints import DelegatedAdminServiceProviderConstraints

            return DelegatedAdminServiceProviderConstraints()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ipNamedLocation".casefold():
            from .ip_named_location import IpNamedLocation

            return IpNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.namedLocation".casefold():
            from .named_location import NamedLocation

            return NamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privateLinkNamedLocation".casefold():
            from .private_link_named_location import PrivateLinkNamedLocation

            return PrivateLinkNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceProviderConstraints".casefold():
            from .service_provider_constraints import ServiceProviderConstraints

            return ServiceProviderConstraints()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceTagNamedLocation".casefold():
            from .service_tag_named_location import ServiceTagNamedLocation

            return ServiceTagNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.whatIfAnalysisResult".casefold():
            from .what_if_analysis_result import WhatIfAnalysisResult

            return WhatIfAnalysisResult()
        return PolicyDeletableItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .compliant_network_named_location import CompliantNetworkNamedLocation
        from .conditional_access_policy import ConditionalAccessPolicy
        from .country_named_location import CountryNamedLocation
        from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
        from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
        from .delegated_admin_service_provider_constraints import DelegatedAdminServiceProviderConstraints
        from .ip_named_location import IpNamedLocation
        from .named_location import NamedLocation
        from .private_link_named_location import PrivateLinkNamedLocation
        from .service_provider_constraints import ServiceProviderConstraints
        from .service_tag_named_location import ServiceTagNamedLocation
        from .what_if_analysis_result import WhatIfAnalysisResult

        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .compliant_network_named_location import CompliantNetworkNamedLocation
        from .conditional_access_policy import ConditionalAccessPolicy
        from .country_named_location import CountryNamedLocation
        from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
        from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
        from .delegated_admin_service_provider_constraints import DelegatedAdminServiceProviderConstraints
        from .ip_named_location import IpNamedLocation
        from .named_location import NamedLocation
        from .private_link_named_location import PrivateLinkNamedLocation
        from .service_provider_constraints import ServiceProviderConstraints
        from .service_tag_named_location import ServiceTagNamedLocation
        from .what_if_analysis_result import WhatIfAnalysisResult

        fields: dict[str, Callable[[Any], None]] = {
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

