from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InvestigationActionUrl(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A machine-readable directive that describes how a client should run the step, in the form metricPath§operation§input§output (for example, b2BRegistrationMetrics.recent.inboundTotalUsers§single§§$verifiedDomains). Clients use this value to chain steps together and to interpret the output of the associated url.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A Microsoft Graph or Azure Resource Manager (ARM) URL template that the client invokes to retrieve the drill-in data for the step. The template can include placeholders such as {@id}, {startDate}, {endDate}, or {sourceDomain} that the client resolves from the related tenant, the caller context, or the output of earlier steps. This value can be empty for steps that only transform data returned by a previous step.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationActionUrl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationActionUrl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationActionUrl()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

