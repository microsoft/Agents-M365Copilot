from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_base import CustomClaimBase
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomClaimsPolicy(Entity, Parsable):
    # If specified, it overrides the content of the audience claim for WS-Federation and SAML2 protocols. A custom signing key must be used for audienceOverride to be applied, otherwise, the audienceOverride value is ignored. The value provided must be in the format of an absolute URI.
    audience_override: Optional[str] = None
    # Defines which claims are present in the tokens affected by the policy, in addition to the basic claim and the core claim set. Inherited from customclaimbase.
    claims: Optional[list[CustomClaimBase]] = None
    # Indicates whether the application ID is added to the claim. It is relevant only for SAML2.0 and if a custom signing key is used. the default value is true. Optional.
    include_application_id_in_issuer: Optional[bool] = None
    # Determines whether the basic claim set is included in tokens affected by this policy. If set to true, all claims in the basic claim set are emitted in tokens affected by the policy. By default the basic claim set isn't in the tokens unless they're explicitly configured in this policy.
    include_basic_claim_set: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomClaimsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomClaimsPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomClaimsPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_base import CustomClaimBase
        from .entity import Entity

        from .custom_claim_base import CustomClaimBase
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "audienceOverride": lambda n : setattr(self, 'audience_override', n.get_str_value()),
            "claims": lambda n : setattr(self, 'claims', n.get_collection_of_object_values(CustomClaimBase)),
            "includeApplicationIdInIssuer": lambda n : setattr(self, 'include_application_id_in_issuer', n.get_bool_value()),
            "includeBasicClaimSet": lambda n : setattr(self, 'include_basic_claim_set', n.get_bool_value()),
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
        writer.write_str_value("audienceOverride", self.audience_override)
        writer.write_collection_of_object_values("claims", self.claims)
        writer.write_bool_value("includeApplicationIdInIssuer", self.include_application_id_in_issuer)
        writer.write_bool_value("includeBasicClaimSet", self.include_basic_claim_set)
    

