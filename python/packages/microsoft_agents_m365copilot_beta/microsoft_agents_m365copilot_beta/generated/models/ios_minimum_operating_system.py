from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IosMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    Contains properties of the minimum operating system required for an iOS mobile app.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 10.0 or later is required to install the app. If 'False', iOS Version 10.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v10_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 11.0 or later is required to install the app. If 'False', iOS Version 11.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v11_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 12.0 or later is required to install the app. If 'False', iOS Version 12.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v12_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 13.0 or later is required to install the app. If 'False', iOS Version 13.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v13_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 14.0 or later is required to install the app. If 'False', iOS Version 14.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v14_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 15.0 or later is required to install the app. If 'False', iOS Version 15.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v15_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 16.0 or later is required to install the app. If 'False', iOS Version 16.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v16_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 17.0 or later is required to install the app. If 'False', iOS Version 17.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v17_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 18.0 or later is required to install the app. If 'False', iOS Version 18.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v18_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 26.0 or later is required to install the app. If 'False', iOS Version 26.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v26_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 27.0 or later is required to install the app. If 'False', iOS Version 27.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v27_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 8.0 or later is required to install the app. If 'False', iOS Version 8.0  is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v8_0: Optional[bool] = None
    # Indicates the minimum iOS version support required for the managed device. When 'True', iOS with OS Version 9.0 or later is required to install the app. If 'False', iOS Version 9.0 is not the minimum version. Default value is False. Exactly one of the minimum operating system boolean values will be TRUE.
    v9_0: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosMinimumOperatingSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v11_0": lambda n : setattr(self, 'v11_0', n.get_bool_value()),
            "v12_0": lambda n : setattr(self, 'v12_0', n.get_bool_value()),
            "v13_0": lambda n : setattr(self, 'v13_0', n.get_bool_value()),
            "v14_0": lambda n : setattr(self, 'v14_0', n.get_bool_value()),
            "v15_0": lambda n : setattr(self, 'v15_0', n.get_bool_value()),
            "v16_0": lambda n : setattr(self, 'v16_0', n.get_bool_value()),
            "v17_0": lambda n : setattr(self, 'v17_0', n.get_bool_value()),
            "v18_0": lambda n : setattr(self, 'v18_0', n.get_bool_value()),
            "v26_0": lambda n : setattr(self, 'v26_0', n.get_bool_value()),
            "v27_0": lambda n : setattr(self, 'v27_0', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
            "v9_0": lambda n : setattr(self, 'v9_0', n.get_bool_value()),
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
        writer.write_bool_value("v10_0", self.v10_0)
        writer.write_bool_value("v11_0", self.v11_0)
        writer.write_bool_value("v12_0", self.v12_0)
        writer.write_bool_value("v13_0", self.v13_0)
        writer.write_bool_value("v14_0", self.v14_0)
        writer.write_bool_value("v15_0", self.v15_0)
        writer.write_bool_value("v16_0", self.v16_0)
        writer.write_bool_value("v17_0", self.v17_0)
        writer.write_bool_value("v18_0", self.v18_0)
        writer.write_bool_value("v26_0", self.v26_0)
        writer.write_bool_value("v27_0", self.v27_0)
        writer.write_bool_value("v8_0", self.v8_0)
        writer.write_bool_value("v9_0", self.v9_0)
        writer.write_additional_data_value(self.additional_data)
    

