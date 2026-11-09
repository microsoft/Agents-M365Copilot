from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class EncryptionReportPolicyDetails(AdditionalDataHolder, Parsable):
    """
    Policy Details for Encryption Report
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Policy Id for Encryption Report
    policy_id: Optional[str] = None
    # Policy Name for Encryption Report
    policy_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EncryptionReportPolicyDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptionReportPolicyDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EncryptionReportPolicyDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
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
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_additional_data_value(self.additional_data)
    

