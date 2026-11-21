from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .verification_state import VerificationState

@dataclass
class VerificationEventDetail(AdditionalDataHolder, Parsable):
    """
    Verification details for an identity verification event, including the provider and temporal metadata.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time when this verification expires, in ISO 8601 format. Must be after verifiedDateTime. Compare this value with the current time to determine expiry. Immutable.
    expires_date_time: Optional[datetime.datetime] = None
    # The unique credential reference in URN format, such as urn:pic:73b78a00-5b9e-4f8c-85dd-b60a08dc1123. Used for deduplication so repeated presentation of the same credential produces one event. Maximum 256 characters. Immutable.
    external_credential_id: Optional[str] = None
    # The date and time when the provider issued the underlying credential, in ISO 8601 format. Must not be in the future. Distinct from verifiedDateTime. Immutable.
    issued_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The verification provider or attestation authority, such as Contoso Identity Services. May be null when state is issued. Maximum 200 characters. Immutable.
    source: Optional[str] = None
    # The state property
    state: Optional[VerificationState] = None
    # The date and time when identity verification was performed, in ISO 8601 format. Must not be in the future. May be null when state is issued. Immutable.
    verified_date_time: Optional[datetime.datetime] = None
    # The identifier of the verified identity profile in the provider's system, in UUID format. Immutable.
    verified_id_profile_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerificationEventDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerificationEventDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerificationEventDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .verification_state import VerificationState

        from .verification_state import VerificationState

        fields: dict[str, Callable[[Any], None]] = {
            "expiresDateTime": lambda n : setattr(self, 'expires_date_time', n.get_datetime_value()),
            "externalCredentialId": lambda n : setattr(self, 'external_credential_id', n.get_str_value()),
            "issuedDateTime": lambda n : setattr(self, 'issued_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(VerificationState)),
            "verifiedDateTime": lambda n : setattr(self, 'verified_date_time', n.get_datetime_value()),
            "verifiedIdProfileId": lambda n : setattr(self, 'verified_id_profile_id', n.get_str_value()),
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
        writer.write_datetime_value("expiresDateTime", self.expires_date_time)
        writer.write_str_value("externalCredentialId", self.external_credential_id)
        writer.write_datetime_value("issuedDateTime", self.issued_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("source", self.source)
        writer.write_enum_value("state", self.state)
        writer.write_datetime_value("verifiedDateTime", self.verified_date_time)
        writer.write_str_value("verifiedIdProfileId", self.verified_id_profile_id)
        writer.write_additional_data_value(self.additional_data)
    

