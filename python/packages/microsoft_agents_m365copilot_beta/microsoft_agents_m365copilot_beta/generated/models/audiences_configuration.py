from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audience_restriction import AudienceRestriction
    from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

@dataclass
class AudiencesConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Setting to allow or disallow creation of apps with multitenant signInAudience.
    azure_ad_multiple_orgs: Optional[AzureAdMultipleOrgsAudienceRestriction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Setting to allow or disallow creation of apps with personal Microsoft account signInAudience.
    personal_microsoft_account: Optional[AudienceRestriction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AudiencesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudiencesConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AudiencesConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audience_restriction import AudienceRestriction
        from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

        from .audience_restriction import AudienceRestriction
        from .azure_ad_multiple_orgs_audience_restriction import AzureAdMultipleOrgsAudienceRestriction

        fields: dict[str, Callable[[Any], None]] = {
            "azureAdMultipleOrgs": lambda n : setattr(self, 'azure_ad_multiple_orgs', n.get_object_value(AzureAdMultipleOrgsAudienceRestriction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "personalMicrosoftAccount": lambda n : setattr(self, 'personal_microsoft_account', n.get_object_value(AudienceRestriction)),
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
        writer.write_object_value("azureAdMultipleOrgs", self.azure_ad_multiple_orgs)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("personalMicrosoftAccount", self.personal_microsoft_account)
        writer.write_additional_data_value(self.additional_data)
    

