from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .email_threat_submission import EmailThreatSubmission
    from .email_threat_submission_policy import EmailThreatSubmissionPolicy
    from .file_threat_submission import FileThreatSubmission
    from .url_threat_submission import UrlThreatSubmission

from ..entity import Entity

@dataclass
class ThreatSubmissionRoot(Entity, Parsable):
    # The emailThreatSubmissionPolicies property
    email_threat_submission_policies: Optional[list[EmailThreatSubmissionPolicy]] = None
    # The emailThreats property
    email_threats: Optional[list[EmailThreatSubmission]] = None
    # The fileThreats property
    file_threats: Optional[list[FileThreatSubmission]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The urlThreats property
    url_threats: Optional[list[UrlThreatSubmission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatSubmissionRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatSubmissionRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThreatSubmissionRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .email_threat_submission import EmailThreatSubmission
        from .email_threat_submission_policy import EmailThreatSubmissionPolicy
        from .file_threat_submission import FileThreatSubmission
        from .url_threat_submission import UrlThreatSubmission

        from ..entity import Entity
        from .email_threat_submission import EmailThreatSubmission
        from .email_threat_submission_policy import EmailThreatSubmissionPolicy
        from .file_threat_submission import FileThreatSubmission
        from .url_threat_submission import UrlThreatSubmission

        fields: dict[str, Callable[[Any], None]] = {
            "emailThreatSubmissionPolicies": lambda n : setattr(self, 'email_threat_submission_policies', n.get_collection_of_object_values(EmailThreatSubmissionPolicy)),
            "emailThreats": lambda n : setattr(self, 'email_threats', n.get_collection_of_object_values(EmailThreatSubmission)),
            "fileThreats": lambda n : setattr(self, 'file_threats', n.get_collection_of_object_values(FileThreatSubmission)),
            "urlThreats": lambda n : setattr(self, 'url_threats', n.get_collection_of_object_values(UrlThreatSubmission)),
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
        writer.write_collection_of_object_values("emailThreatSubmissionPolicies", self.email_threat_submission_policies)
        writer.write_collection_of_object_values("emailThreats", self.email_threats)
        writer.write_collection_of_object_values("fileThreats", self.file_threats)
        writer.write_collection_of_object_values("urlThreats", self.url_threats)
    

