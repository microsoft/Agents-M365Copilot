from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item_target import AccessReviewInstanceDecisionItemTarget

from .access_review_instance_decision_item_target import AccessReviewInstanceDecisionItemTarget

@dataclass
class AccessReviewInstanceDecisionItemServicePrincipalTarget(AccessReviewInstanceDecisionItemTarget, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalTarget"
    # The appId for the service principal entity being reviewed.
    app_id: Optional[str] = None
    # The display name of the service principal whose access is being reviewed.
    service_principal_display_name: Optional[str] = None
    # The identifier of the service principal whose access is being reviewed.
    service_principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewInstanceDecisionItemServicePrincipalTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemServicePrincipalTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInstanceDecisionItemServicePrincipalTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item_target import AccessReviewInstanceDecisionItemTarget

        from .access_review_instance_decision_item_target import AccessReviewInstanceDecisionItemTarget

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "servicePrincipalDisplayName": lambda n : setattr(self, 'service_principal_display_name', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("servicePrincipalDisplayName", self.service_principal_display_name)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
    

