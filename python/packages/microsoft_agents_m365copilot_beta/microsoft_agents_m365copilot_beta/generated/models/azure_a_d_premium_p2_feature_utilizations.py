from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_a_d_premium_feature_utilization import AzureADPremiumFeatureUtilization

@dataclass
class AzureADPremiumP2FeatureUtilizations(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The riskBasedConditionalAccess property
    risk_based_conditional_access: Optional[AzureADPremiumFeatureUtilization] = None
    # The riskBasedConditionalAccessGuestUsers property
    risk_based_conditional_access_guest_users: Optional[AzureADPremiumFeatureUtilization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureADPremiumP2FeatureUtilizations:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureADPremiumP2FeatureUtilizations
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureADPremiumP2FeatureUtilizations()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .azure_a_d_premium_feature_utilization import AzureADPremiumFeatureUtilization

        from .azure_a_d_premium_feature_utilization import AzureADPremiumFeatureUtilization

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskBasedConditionalAccess": lambda n : setattr(self, 'risk_based_conditional_access', n.get_object_value(AzureADPremiumFeatureUtilization)),
            "riskBasedConditionalAccessGuestUsers": lambda n : setattr(self, 'risk_based_conditional_access_guest_users', n.get_object_value(AzureADPremiumFeatureUtilization)),
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
        writer.write_object_value("riskBasedConditionalAccess", self.risk_based_conditional_access)
        writer.write_object_value("riskBasedConditionalAccessGuestUsers", self.risk_based_conditional_access_guest_users)
        writer.write_additional_data_value(self.additional_data)
    

