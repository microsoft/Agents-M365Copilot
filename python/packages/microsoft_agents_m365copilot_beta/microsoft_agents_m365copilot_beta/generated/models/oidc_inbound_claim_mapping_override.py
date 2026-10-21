from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .oidc_address_inbound_claims import OidcAddressInboundClaims

@dataclass
class OidcInboundClaimMappingOverride(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # End-user's preferred postal address. The value of the address member is a JSON RFC8259 structure containing some or all of the members defined in the resource type
    address: Optional[OidcAddressInboundClaims] = None
    # End-user's preferred e-mail address. Its value MUST conform to the RFC 5322 addr-spec syntax.
    email: Optional[str] = None
    # True if the end-user's e-mail address has been verified by the identity provider; otherwise, false. When this claim value is true, this means that your identity provider took affirmative steps to ensure that this e-mail address was controlled by the end-user at the time the verification was performed. If this claim value is false, or not mapped with any claim of the identity provider, the user is asked to verify email during sign-up if email is required in the user flow.
    email_verified: Optional[str] = None
    # Surname(s) or family name of the end-user.
    family_name: Optional[str] = None
    # Given name(s) or first name(s) of the end-user.
    given_name: Optional[str] = None
    # End-user's full name in displayable form including all name parts, possibly including titles and suffixes, ordered according to the end-user's locale and preferences.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The claim provides the phone number for the user.
    phone_number: Optional[str] = None
    # True if the end-user's phone number has been verified; otherwise, false. When this claim value is true, this means that your identity provider took affirmative steps to verify the phone number.
    phone_number_verified: Optional[str] = None
    # Subject - Identifier for the end-user at the Issuer.
    sub: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OidcInboundClaimMappingOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OidcInboundClaimMappingOverride
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OidcInboundClaimMappingOverride()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .oidc_address_inbound_claims import OidcAddressInboundClaims

        from .oidc_address_inbound_claims import OidcAddressInboundClaims

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(OidcAddressInboundClaims)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "email_verified": lambda n : setattr(self, 'email_verified', n.get_str_value()),
            "family_name": lambda n : setattr(self, 'family_name', n.get_str_value()),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phone_number_verified": lambda n : setattr(self, 'phone_number_verified', n.get_str_value()),
            "sub": lambda n : setattr(self, 'sub', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_str_value("email", self.email)
        writer.write_str_value("email_verified", self.email_verified)
        writer.write_str_value("family_name", self.family_name)
        writer.write_str_value("given_name", self.given_name)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("phone_number", self.phone_number)
        writer.write_str_value("phone_number_verified", self.phone_number_verified)
        writer.write_str_value("sub", self.sub)
        writer.write_additional_data_value(self.additional_data)
    

