from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .access_package_assignment_required_rule import AccessPackageAssignmentRequiredRule
    from .inactivity_rule import InactivityRule
    from .invitation_redemption_rule import InvitationRedemptionRule
    from .periodic_attestation_rule import PeriodicAttestationRule
    from .sponsor_presence_rule import SponsorPresenceRule

from ..entity import Entity

@dataclass
class LifecyclePolicyRule(Entity, Parsable):
    # The optional grace period, in days, that starts when the rule violation is first detected. The allowed range is 0 through 30. If omitted or set to null, the gracePeriodInDays value of the containing lifecycle policy applies. A value of 0 means no additional grace period. If multiple rules remain violated, the earliest rule grace-period expiry starts the policy action sequence; the policy-level grace period isn't added again.
    grace_period_in_days: Optional[int] = None
    # Indicates whether the rule is enabled and evaluated as part of its policy.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if not mapping_value:
            return LifecyclePolicyRule()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.accessPackageAssignmentRequiredRule".casefold():
            from .access_package_assignment_required_rule import AccessPackageAssignmentRequiredRule

            return AccessPackageAssignmentRequiredRule()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.inactivityRule".casefold():
            from .inactivity_rule import InactivityRule

            return InactivityRule()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.invitationRedemptionRule".casefold():
            from .invitation_redemption_rule import InvitationRedemptionRule

            return InvitationRedemptionRule()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.periodicAttestationRule".casefold():
            from .periodic_attestation_rule import PeriodicAttestationRule

            return PeriodicAttestationRule()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.sponsorPresenceRule".casefold():
            from .sponsor_presence_rule import SponsorPresenceRule

            return SponsorPresenceRule()
        return LifecyclePolicyRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .access_package_assignment_required_rule import AccessPackageAssignmentRequiredRule
        from .inactivity_rule import InactivityRule
        from .invitation_redemption_rule import InvitationRedemptionRule
        from .periodic_attestation_rule import PeriodicAttestationRule
        from .sponsor_presence_rule import SponsorPresenceRule

        from ..entity import Entity
        from .access_package_assignment_required_rule import AccessPackageAssignmentRequiredRule
        from .inactivity_rule import InactivityRule
        from .invitation_redemption_rule import InvitationRedemptionRule
        from .periodic_attestation_rule import PeriodicAttestationRule
        from .sponsor_presence_rule import SponsorPresenceRule

        fields: dict[str, Callable[[Any], None]] = {
            "gracePeriodInDays": lambda n : setattr(self, 'grace_period_in_days', n.get_int_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
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
        writer.write_int_value("gracePeriodInDays", self.grace_period_in_days)
        writer.write_bool_value("isEnabled", self.is_enabled)
    

