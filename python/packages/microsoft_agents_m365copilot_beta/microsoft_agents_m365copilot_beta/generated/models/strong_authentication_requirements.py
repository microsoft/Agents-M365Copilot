from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .per_user_mfa_state import PerUserMfaState

@dataclass
class StrongAuthenticationRequirements(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Sets the per-user MFA state for the user. The possible values are: disabled, enforced, enabled, unknownFutureValue. When you update a user's MFA state to enabled and the user has already registered an MFA method, their state changes automatically to enforced.
    per_user_mfa_state: Optional[PerUserMfaState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StrongAuthenticationRequirements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StrongAuthenticationRequirements
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StrongAuthenticationRequirements()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .per_user_mfa_state import PerUserMfaState

        from .per_user_mfa_state import PerUserMfaState

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "perUserMfaState": lambda n : setattr(self, 'per_user_mfa_state', n.get_enum_value(PerUserMfaState)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("perUserMfaState", self.per_user_mfa_state)
        writer.write_additional_data_value(self.additional_data)
    

