from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provenance_asserted_by import ProvenanceAssertedBy
    from .provenance_assertion import ProvenanceAssertion
    from .provenance_chain_status import ProvenanceChainStatus
    from .provenance_classification import ProvenanceClassification

@dataclass
class CredentialProvenance(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifies the actor that established the provenance. This property is computed by the service.
    asserted_by: Optional[ProvenanceAssertedBy] = None
    # The assertions that support the credential's provenance classification.
    assertions: Optional[list[ProvenanceAssertion]] = None
    # The current integrity status of the credential's chain of trust.
    chain_status: Optional[ProvenanceChainStatus] = None
    # The classification property
    classification: Optional[ProvenanceClassification] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CredentialProvenance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CredentialProvenance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CredentialProvenance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .provenance_asserted_by import ProvenanceAssertedBy
        from .provenance_assertion import ProvenanceAssertion
        from .provenance_chain_status import ProvenanceChainStatus
        from .provenance_classification import ProvenanceClassification

        from .provenance_asserted_by import ProvenanceAssertedBy
        from .provenance_assertion import ProvenanceAssertion
        from .provenance_chain_status import ProvenanceChainStatus
        from .provenance_classification import ProvenanceClassification

        fields: dict[str, Callable[[Any], None]] = {
            "assertedBy": lambda n : setattr(self, 'asserted_by', n.get_object_value(ProvenanceAssertedBy)),
            "assertions": lambda n : setattr(self, 'assertions', n.get_collection_of_object_values(ProvenanceAssertion)),
            "chainStatus": lambda n : setattr(self, 'chain_status', n.get_object_value(ProvenanceChainStatus)),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(ProvenanceClassification)),
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
        writer.write_collection_of_object_values("assertions", self.assertions)
        writer.write_object_value("chainStatus", self.chain_status)
        writer.write_enum_value("classification", self.classification)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

