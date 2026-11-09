from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .advanced_config_state import AdvancedConfigState
    from .include_target import IncludeTarget

@dataclass
class ReportSuspiciousActivitySettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The includeTarget property
    include_target: Optional[IncludeTarget] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[AdvancedConfigState] = None
    # Specifies the number the user enters on their phone to report the MFA prompt as suspicious.
    voice_reporting_code: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReportSuspiciousActivitySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReportSuspiciousActivitySettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReportSuspiciousActivitySettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .advanced_config_state import AdvancedConfigState
        from .include_target import IncludeTarget

        from .advanced_config_state import AdvancedConfigState
        from .include_target import IncludeTarget

        fields: dict[str, Callable[[Any], None]] = {
            "includeTarget": lambda n : setattr(self, 'include_target', n.get_object_value(IncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AdvancedConfigState)),
            "voiceReportingCode": lambda n : setattr(self, 'voice_reporting_code', n.get_int_value()),
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
        writer.write_object_value("includeTarget", self.include_target)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_int_value("voiceReportingCode", self.voice_reporting_code)
        writer.write_additional_data_value(self.additional_data)
    

