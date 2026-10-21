from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .integer_range import IntegerRange
    from .printer_feed_direction import PrinterFeedDirection
    from .printer_feed_orientation import PrinterFeedOrientation
    from .print_color_mode import PrintColorMode
    from .print_duplex_mode import PrintDuplexMode
    from .print_finishing import PrintFinishing
    from .print_margin import PrintMargin
    from .print_multipage_layout import PrintMultipageLayout
    from .print_orientation import PrintOrientation
    from .print_quality import PrintQuality
    from .print_scaling import PrintScaling

@dataclass
class PrinterDocumentConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The collate property
    collate: Optional[bool] = None
    # The colorMode property
    color_mode: Optional[PrintColorMode] = None
    # The copies property
    copies: Optional[int] = None
    # The dpi property
    dpi: Optional[int] = None
    # The duplexMode property
    duplex_mode: Optional[PrintDuplexMode] = None
    # The feedDirection property
    feed_direction: Optional[PrinterFeedDirection] = None
    # The feedOrientation property
    feed_orientation: Optional[PrinterFeedOrientation] = None
    # The finishings property
    finishings: Optional[list[PrintFinishing]] = None
    # The fitPdfToPage property
    fit_pdf_to_page: Optional[bool] = None
    # The inputBin property
    input_bin: Optional[str] = None
    # The margin property
    margin: Optional[PrintMargin] = None
    # The mediaSize property
    media_size: Optional[str] = None
    # The mediaType property
    media_type: Optional[str] = None
    # The multipageLayout property
    multipage_layout: Optional[PrintMultipageLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The orientation property
    orientation: Optional[PrintOrientation] = None
    # The outputBin property
    output_bin: Optional[str] = None
    # The pageRanges property
    page_ranges: Optional[list[IntegerRange]] = None
    # The pagesPerSheet property
    pages_per_sheet: Optional[int] = None
    # The quality property
    quality: Optional[PrintQuality] = None
    # The scaling property
    scaling: Optional[PrintScaling] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrinterDocumentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrinterDocumentConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrinterDocumentConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .integer_range import IntegerRange
        from .printer_feed_direction import PrinterFeedDirection
        from .printer_feed_orientation import PrinterFeedOrientation
        from .print_color_mode import PrintColorMode
        from .print_duplex_mode import PrintDuplexMode
        from .print_finishing import PrintFinishing
        from .print_margin import PrintMargin
        from .print_multipage_layout import PrintMultipageLayout
        from .print_orientation import PrintOrientation
        from .print_quality import PrintQuality
        from .print_scaling import PrintScaling

        from .integer_range import IntegerRange
        from .printer_feed_direction import PrinterFeedDirection
        from .printer_feed_orientation import PrinterFeedOrientation
        from .print_color_mode import PrintColorMode
        from .print_duplex_mode import PrintDuplexMode
        from .print_finishing import PrintFinishing
        from .print_margin import PrintMargin
        from .print_multipage_layout import PrintMultipageLayout
        from .print_orientation import PrintOrientation
        from .print_quality import PrintQuality
        from .print_scaling import PrintScaling

        fields: dict[str, Callable[[Any], None]] = {
            "collate": lambda n : setattr(self, 'collate', n.get_bool_value()),
            "colorMode": lambda n : setattr(self, 'color_mode', n.get_enum_value(PrintColorMode)),
            "copies": lambda n : setattr(self, 'copies', n.get_int_value()),
            "dpi": lambda n : setattr(self, 'dpi', n.get_int_value()),
            "duplexMode": lambda n : setattr(self, 'duplex_mode', n.get_enum_value(PrintDuplexMode)),
            "feedDirection": lambda n : setattr(self, 'feed_direction', n.get_enum_value(PrinterFeedDirection)),
            "feedOrientation": lambda n : setattr(self, 'feed_orientation', n.get_enum_value(PrinterFeedOrientation)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(PrintFinishing)),
            "fitPdfToPage": lambda n : setattr(self, 'fit_pdf_to_page', n.get_bool_value()),
            "inputBin": lambda n : setattr(self, 'input_bin', n.get_str_value()),
            "margin": lambda n : setattr(self, 'margin', n.get_object_value(PrintMargin)),
            "mediaSize": lambda n : setattr(self, 'media_size', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "multipageLayout": lambda n : setattr(self, 'multipage_layout', n.get_enum_value(PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(PrintOrientation)),
            "outputBin": lambda n : setattr(self, 'output_bin', n.get_str_value()),
            "pageRanges": lambda n : setattr(self, 'page_ranges', n.get_collection_of_object_values(IntegerRange)),
            "pagesPerSheet": lambda n : setattr(self, 'pages_per_sheet', n.get_int_value()),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(PrintQuality)),
            "scaling": lambda n : setattr(self, 'scaling', n.get_enum_value(PrintScaling)),
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
        writer.write_bool_value("collate", self.collate)
        writer.write_enum_value("colorMode", self.color_mode)
        writer.write_int_value("copies", self.copies)
        writer.write_int_value("dpi", self.dpi)
        writer.write_enum_value("duplexMode", self.duplex_mode)
        writer.write_enum_value("feedDirection", self.feed_direction)
        writer.write_enum_value("feedOrientation", self.feed_orientation)
        writer.write_collection_of_enum_values("finishings", self.finishings)
        writer.write_bool_value("fitPdfToPage", self.fit_pdf_to_page)
        writer.write_str_value("inputBin", self.input_bin)
        writer.write_object_value("margin", self.margin)
        writer.write_str_value("mediaSize", self.media_size)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_enum_value("multipageLayout", self.multipage_layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("orientation", self.orientation)
        writer.write_str_value("outputBin", self.output_bin)
        writer.write_collection_of_object_values("pageRanges", self.page_ranges)
        writer.write_int_value("pagesPerSheet", self.pages_per_sheet)
        writer.write_enum_value("quality", self.quality)
        writer.write_enum_value("scaling", self.scaling)
        writer.write_additional_data_value(self.additional_data)
    

