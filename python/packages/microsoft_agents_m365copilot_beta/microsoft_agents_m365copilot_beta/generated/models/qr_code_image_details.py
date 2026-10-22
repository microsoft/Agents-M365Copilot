from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .error_correction_level import ErrorCorrectionLevel

@dataclass
class QrCodeImageDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The binary representation of the QR code.
    binary_value: Optional[bytes] = None
    # Specifies how much of the QR code can be corrupted while still maintaining its readable. The possible values are: l  (Low), m (Medium), q (Quartile), h ( High), unknownFutureValue.
    error_correction_level: Optional[ErrorCorrectionLevel] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Base64-encoded raw content of the QR code.
    raw_content: Optional[bytes] = None
    # Version to create QR code image.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrCodeImageDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrCodeImageDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrCodeImageDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .error_correction_level import ErrorCorrectionLevel

        from .error_correction_level import ErrorCorrectionLevel

        fields: dict[str, Callable[[Any], None]] = {
            "binaryValue": lambda n : setattr(self, 'binary_value', n.get_bytes_value()),
            "errorCorrectionLevel": lambda n : setattr(self, 'error_correction_level', n.get_enum_value(ErrorCorrectionLevel)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rawContent": lambda n : setattr(self, 'raw_content', n.get_bytes_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bytes_value("binaryValue", self.binary_value)
        writer.write_enum_value("errorCorrectionLevel", self.error_correction_level)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bytes_value("rawContent", self.raw_content)
        writer.write_int_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

