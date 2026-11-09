from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DataProcessorServiceForWindowsFeaturesOnboarding(AdditionalDataHolder, Parsable):
    """
    A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When TRUE, the tenant has enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. When FALSE, the tenant has not enabled MEM features utilizing Data Processor Service for Windows (DPSW) data. Default value is FALSE.
    are_data_processor_service_for_windows_features_enabled: Optional[bool] = None
    # Indicates whether the tenant has required Windows license. When TRUE, the tenant has the required Windows license. When FALSE, the tenant does not have the required Windows license. Default value is FALSE.
    has_valid_windows_license: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataProcessorServiceForWindowsFeaturesOnboarding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataProcessorServiceForWindowsFeaturesOnboarding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DataProcessorServiceForWindowsFeaturesOnboarding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "areDataProcessorServiceForWindowsFeaturesEnabled": lambda n : setattr(self, 'are_data_processor_service_for_windows_features_enabled', n.get_bool_value()),
            "hasValidWindowsLicense": lambda n : setattr(self, 'has_valid_windows_license', n.get_bool_value()),
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
        writer.write_bool_value("areDataProcessorServiceForWindowsFeaturesEnabled", self.are_data_processor_service_for_windows_features_enabled)
        writer.write_bool_value("hasValidWindowsLicense", self.has_valid_windows_license)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

