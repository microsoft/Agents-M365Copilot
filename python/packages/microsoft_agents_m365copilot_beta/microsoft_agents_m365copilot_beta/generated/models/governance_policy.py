from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .governance_criteria import GovernanceCriteria
    from .governance_notification_policy import GovernanceNotificationPolicy

@dataclass
class GovernancePolicy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The decisionMakerCriteria property
    decision_maker_criteria: Optional[list[GovernanceCriteria]] = None
    # The notificationPolicy property
    notification_policy: Optional[GovernanceNotificationPolicy] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .governance_criteria import GovernanceCriteria
        from .governance_notification_policy import GovernanceNotificationPolicy

        from .governance_criteria import GovernanceCriteria
        from .governance_notification_policy import GovernanceNotificationPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "decisionMakerCriteria": lambda n : setattr(self, 'decision_maker_criteria', n.get_collection_of_object_values(GovernanceCriteria)),
            "notificationPolicy": lambda n : setattr(self, 'notification_policy', n.get_object_value(GovernanceNotificationPolicy)),
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
        writer.write_collection_of_object_values("decisionMakerCriteria", self.decision_maker_criteria)
        writer.write_object_value("notificationPolicy", self.notification_policy)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

