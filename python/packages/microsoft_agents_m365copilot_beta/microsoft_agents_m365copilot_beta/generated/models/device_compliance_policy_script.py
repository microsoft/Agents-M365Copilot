from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceCompliancePolicyScript(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Device compliance script Id.
    device_compliance_script_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Json of the rules.
    rules_content: Optional[bytes] = None
    # Indicates the interval, in minutes, at which the custom compliance script is evaluated on the device. Allowed range from 1 to 480. Nullable.
    run_interval_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceCompliancePolicyScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyScript
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceCompliancePolicyScript()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deviceComplianceScriptId": lambda n : setattr(self, 'device_compliance_script_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rulesContent": lambda n : setattr(self, 'rules_content', n.get_bytes_value()),
            "runIntervalInMinutes": lambda n : setattr(self, 'run_interval_in_minutes', n.get_int_value()),
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
        writer.write_str_value("deviceComplianceScriptId", self.device_compliance_script_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bytes_value("rulesContent", self.rules_content)
        writer.write_int_value("runIntervalInMinutes", self.run_interval_in_minutes)
        writer.write_additional_data_value(self.additional_data)
    

