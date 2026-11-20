from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LifecyclePolicyNotificationSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The email addresses used when no targeted notification recipient has a valid email address. These addresses aren't copied on every notification or used alongside a valid targeted recipient.
    additional_fallback_recipients: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offsets, in days after an identity becomes non-compliant, at which notifications are sent.
    offsets_after_non_compliance_in_days: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyNotificationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyNotificationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicyNotificationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "additionalFallbackRecipients": lambda n : setattr(self, 'additional_fallback_recipients', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offsetsAfterNonComplianceInDays": lambda n : setattr(self, 'offsets_after_non_compliance_in_days', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("additionalFallbackRecipients", self.additional_fallback_recipients)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("offsetsAfterNonComplianceInDays", self.offsets_after_non_compliance_in_days)
        writer.write_additional_data_value(self.additional_data)
    

