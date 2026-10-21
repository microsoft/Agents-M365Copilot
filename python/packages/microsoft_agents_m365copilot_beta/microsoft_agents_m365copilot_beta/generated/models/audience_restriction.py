from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
    from .app_management_restriction_state import AppManagementRestrictionState
    from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

@dataclass
class AudienceRestriction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of custom security attribute exemptions. If an actor user or service principal has the custom security attribute defined in this section, they're exempted from the restriction.  This means that calls the user or service principal makes to create or update apps are exempt from this policy enforcement.
    exclude_actors: Optional[AppManagementPolicyActorExemptions] = None
    # The isStateSetByMicrosoft property
    is_state_set_by_microsoft: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the date from which the policy restriction applies to newly created applications. For existing applications, the enforcement date can be retroactively applied.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The state property
    state: Optional[AppManagementRestrictionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AudienceRestriction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudienceRestriction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAdMultipleOrgsAudienceRestriction".casefold():
            from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

            return AzureAdMultipleOrgsAudienceRestriction()
        return AudienceRestriction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

        fields: dict[str, Callable[[Any], None]] = {
            "excludeActors": lambda n : setattr(self, 'exclude_actors', n.get_object_value(AppManagementPolicyActorExemptions)),
            "isStateSetByMicrosoft": lambda n : setattr(self, 'is_state_set_by_microsoft', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
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
        writer.write_object_value("excludeActors", self.exclude_actors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

