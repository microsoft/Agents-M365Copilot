from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value import KeyValue

@dataclass
class GovernanceRoleAssignmentRequestStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the role assignment request. The value can be InProgress or Closed.
    status: Optional[str] = None
    # The details of the status of the role assignment request. It represents the evaluation results of different rules.
    status_details: Optional[list[KeyValue]] = None
    # The sub status of the role assignment request. The values can be Accepted, PendingEvaluation, Granted, Denied, PendingProvisioning, Provisioned, PendingRevocation, Revoked, Canceled, Failed, PendingApprovalProvisioning, PendingApproval, FailedAsResourceIsLocked, PendingAdminDecision, AdminApproved, AdminDenied, TimedOut, and ProvisioningStarted.
    sub_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceRoleAssignmentRequestStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleAssignmentRequestStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceRoleAssignmentRequestStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_value import KeyValue

        from .key_value import KeyValue

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_collection_of_object_values(KeyValue)),
            "subStatus": lambda n : setattr(self, 'sub_status', n.get_str_value()),
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
        writer.write_str_value("status", self.status)
        writer.write_collection_of_object_values("statusDetails", self.status_details)
        writer.write_str_value("subStatus", self.sub_status)
        writer.write_additional_data_value(self.additional_data)
    

