from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .quality_update_cadence import QualityUpdateCadence
    from .quality_update_classification import QualityUpdateClassification
    from .windows_update_filter import WindowsUpdateFilter

from .windows_update_filter import WindowsUpdateFilter

@dataclass
class QualityUpdateFilter(WindowsUpdateFilter, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.qualityUpdateFilter"
    # Specifies the cadence for publishing quality updates of the filter. The possible values are: monthly, outOfBand, unknownFutureValue.
    cadence: Optional[QualityUpdateCadence] = None
    # Specifies the quality update classification of the filter. The possible values are: all, security, nonSecurity, unknownFutureValue.
    classification: Optional[QualityUpdateClassification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QualityUpdateFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QualityUpdateFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QualityUpdateFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .quality_update_cadence import QualityUpdateCadence
        from .quality_update_classification import QualityUpdateClassification
        from .windows_update_filter import WindowsUpdateFilter

        from .quality_update_cadence import QualityUpdateCadence
        from .quality_update_classification import QualityUpdateClassification
        from .windows_update_filter import WindowsUpdateFilter

        fields: dict[str, Callable[[Any], None]] = {
            "cadence": lambda n : setattr(self, 'cadence', n.get_enum_value(QualityUpdateCadence)),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(QualityUpdateClassification)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("cadence", self.cadence)
        writer.write_enum_value("classification", self.classification)
    

