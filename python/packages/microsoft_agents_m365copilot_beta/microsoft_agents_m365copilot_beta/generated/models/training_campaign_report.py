from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training_campaign_report_overview import TrainingCampaignReportOverview
    from .user_simulation_details import UserSimulationDetails

@dataclass
class TrainingCampaignReport(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The overview of the attack simulation and training campaign.
    campaign_users: Optional[list[UserSimulationDetails]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The overview property
    overview: Optional[TrainingCampaignReportOverview] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrainingCampaignReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingCampaignReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrainingCampaignReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .training_campaign_report_overview import TrainingCampaignReportOverview
        from .user_simulation_details import UserSimulationDetails

        from .training_campaign_report_overview import TrainingCampaignReportOverview
        from .user_simulation_details import UserSimulationDetails

        fields: dict[str, Callable[[Any], None]] = {
            "campaignUsers": lambda n : setattr(self, 'campaign_users', n.get_collection_of_object_values(UserSimulationDetails)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overview": lambda n : setattr(self, 'overview', n.get_object_value(TrainingCampaignReportOverview)),
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
        writer.write_collection_of_object_values("campaignUsers", self.campaign_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("overview", self.overview)
        writer.write_additional_data_value(self.additional_data)
    

