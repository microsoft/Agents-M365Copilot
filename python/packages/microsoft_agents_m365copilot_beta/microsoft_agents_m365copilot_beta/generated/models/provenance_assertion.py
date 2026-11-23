from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provenance_assertion_type import ProvenanceAssertionType

@dataclass
class ProvenanceAssertion(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The reason supplied for a manual attestation.
    attestation_reason: Optional[str] = None
    # The date and time of the provenance event represented by this assertion.
    event_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provenanceType property
    provenance_type: Optional[ProvenanceAssertionType] = None
    # The identifier of the credential from which this credential was derived.
    source_credential_id: Optional[str] = None
    # The type of credential from which this credential was derived.
    source_credential_type: Optional[str] = None
    # The identifier of the identityVerificationEvent that supports this assertion.
    verification_event_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvenanceAssertion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvenanceAssertion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvenanceAssertion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .provenance_assertion_type import ProvenanceAssertionType

        from .provenance_assertion_type import ProvenanceAssertionType

        fields: dict[str, Callable[[Any], None]] = {
            "attestationReason": lambda n : setattr(self, 'attestation_reason', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provenanceType": lambda n : setattr(self, 'provenance_type', n.get_enum_value(ProvenanceAssertionType)),
            "sourceCredentialId": lambda n : setattr(self, 'source_credential_id', n.get_str_value()),
            "sourceCredentialType": lambda n : setattr(self, 'source_credential_type', n.get_str_value()),
            "verificationEventId": lambda n : setattr(self, 'verification_event_id', n.get_str_value()),
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
        writer.write_str_value("attestationReason", self.attestation_reason)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("provenanceType", self.provenance_type)
        writer.write_str_value("sourceCredentialId", self.source_credential_id)
        writer.write_str_value("sourceCredentialType", self.source_credential_type)
        writer.write_str_value("verificationEventId", self.verification_event_id)
        writer.write_additional_data_value(self.additional_data)
    

