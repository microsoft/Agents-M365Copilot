from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .investigation_action_url import InvestigationActionUrl

@dataclass
class InvestigationActionStep(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The follow-on API reference for the step, containing the URL template and a machine-readable execution directive that a client uses to retrieve the drill-in data.
    action_url: Optional[InvestigationActionUrl] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The one-based order, as a string, in which the step should be evaluated by a client. Steps are intended to be run in ascending stepNumber order because later steps can depend on the output of earlier steps. This value is the key of the resource.
    step_number: Optional[str] = None
    # Human-readable guidance that explains what the step does and why it's useful for investigating the related metric.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationActionStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationActionStep
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationActionStep()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .investigation_action_url import InvestigationActionUrl

        from .investigation_action_url import InvestigationActionUrl

        fields: dict[str, Callable[[Any], None]] = {
            "actionUrl": lambda n : setattr(self, 'action_url', n.get_object_value(InvestigationActionUrl)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stepNumber": lambda n : setattr(self, 'step_number', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_object_value("actionUrl", self.action_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("stepNumber", self.step_number)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

