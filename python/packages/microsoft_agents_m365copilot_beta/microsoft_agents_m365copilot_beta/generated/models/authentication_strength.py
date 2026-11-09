from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_strength_result import AuthenticationStrengthResult

@dataclass
class AuthenticationStrength(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the authentication strength.
    authentication_strength_id: Optional[str] = None
    # The result of the authentication strength. The possible values are: notSet, skippedForProofUp, satisfied, singleChallengeRequired, multipleChallengesRequired, singleRegistrationRequired, multipleRegistrationsRequired, cannotSatisfyDueToCombinationConfiguration, cannotSatisfy, unknownFutureValue.
    authentication_strength_result: Optional[AuthenticationStrengthResult] = None
    # The name of the authentication strength.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationStrength:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrength
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationStrength()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_strength_result import AuthenticationStrengthResult

        from .authentication_strength_result import AuthenticationStrengthResult

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationStrengthId": lambda n : setattr(self, 'authentication_strength_id', n.get_str_value()),
            "authenticationStrengthResult": lambda n : setattr(self, 'authentication_strength_result', n.get_enum_value(AuthenticationStrengthResult)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("authenticationStrengthId", self.authentication_strength_id)
        writer.write_enum_value("authenticationStrengthResult", self.authentication_strength_result)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

