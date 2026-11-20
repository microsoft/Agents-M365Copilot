from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin_consent_state import AdminConsentState

@dataclass
class AdminConsent(AdditionalDataHolder, Parsable):
    """
    Admin consent information.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Admin consent state.
    share_a_p_n_s_data: Optional[AdminConsentState] = None
    # Admin consent state.
    share_user_experience_analytics_data: Optional[AdminConsentState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminConsent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminConsent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminConsent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .admin_consent_state import AdminConsentState

        from .admin_consent_state import AdminConsentState

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "shareAPNSData": lambda n : setattr(self, 'share_a_p_n_s_data', n.get_enum_value(AdminConsentState)),
            "shareUserExperienceAnalyticsData": lambda n : setattr(self, 'share_user_experience_analytics_data', n.get_enum_value(AdminConsentState)),
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
        writer.write_enum_value("shareAPNSData", self.share_a_p_n_s_data)
        writer.write_enum_value("shareUserExperienceAnalyticsData", self.share_user_experience_analytics_data)
        writer.write_additional_data_value(self.additional_data)
    

