from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExcludedApps(AdditionalDataHolder, Parsable):
    """
    Contains properties for Excluded Office365 Apps.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The value for if MS Office Access should be excluded or not.
    access: Optional[bool] = None
    # The value for if Microsoft Search as default should be excluded or not.
    bing: Optional[bool] = None
    # The value for if MS Office Excel should be excluded or not.
    excel: Optional[bool] = None
    # The value for if MS Office OneDrive for Business - Groove should be excluded or not.
    groove: Optional[bool] = None
    # The value for if MS Office InfoPath should be excluded or not.
    info_path: Optional[bool] = None
    # The value for if MS Office Skype for Business - Lync should be excluded or not.
    lync: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The value for if MS Office OneDrive should be excluded or not.
    one_drive: Optional[bool] = None
    # The value for if MS Office OneNote should be excluded or not.
    one_note: Optional[bool] = None
    # The value for if MS Office Outlook should be excluded or not.
    outlook: Optional[bool] = None
    # The value for if MS Office PowerPoint should be excluded or not.
    power_point: Optional[bool] = None
    # The value for if MS Office Publisher should be excluded or not.
    publisher: Optional[bool] = None
    # The value for if MS Office SharePointDesigner should be excluded or not.
    share_point_designer: Optional[bool] = None
    # The value for if MS Office Teams should be excluded or not.
    teams: Optional[bool] = None
    # The value for if MS Office Visio should be excluded or not.
    visio: Optional[bool] = None
    # The value for if MS Office Word should be excluded or not.
    word: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExcludedApps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExcludedApps
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExcludedApps()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_bool_value()),
            "bing": lambda n : setattr(self, 'bing', n.get_bool_value()),
            "excel": lambda n : setattr(self, 'excel', n.get_bool_value()),
            "groove": lambda n : setattr(self, 'groove', n.get_bool_value()),
            "infoPath": lambda n : setattr(self, 'info_path', n.get_bool_value()),
            "lync": lambda n : setattr(self, 'lync', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oneDrive": lambda n : setattr(self, 'one_drive', n.get_bool_value()),
            "oneNote": lambda n : setattr(self, 'one_note', n.get_bool_value()),
            "outlook": lambda n : setattr(self, 'outlook', n.get_bool_value()),
            "powerPoint": lambda n : setattr(self, 'power_point', n.get_bool_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_bool_value()),
            "sharePointDesigner": lambda n : setattr(self, 'share_point_designer', n.get_bool_value()),
            "teams": lambda n : setattr(self, 'teams', n.get_bool_value()),
            "visio": lambda n : setattr(self, 'visio', n.get_bool_value()),
            "word": lambda n : setattr(self, 'word', n.get_bool_value()),
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
        writer.write_bool_value("access", self.access)
        writer.write_bool_value("bing", self.bing)
        writer.write_bool_value("excel", self.excel)
        writer.write_bool_value("groove", self.groove)
        writer.write_bool_value("infoPath", self.info_path)
        writer.write_bool_value("lync", self.lync)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("oneDrive", self.one_drive)
        writer.write_bool_value("oneNote", self.one_note)
        writer.write_bool_value("outlook", self.outlook)
        writer.write_bool_value("powerPoint", self.power_point)
        writer.write_bool_value("publisher", self.publisher)
        writer.write_bool_value("sharePointDesigner", self.share_point_designer)
        writer.write_bool_value("teams", self.teams)
        writer.write_bool_value("visio", self.visio)
        writer.write_bool_value("word", self.word)
        writer.write_additional_data_value(self.additional_data)
    

