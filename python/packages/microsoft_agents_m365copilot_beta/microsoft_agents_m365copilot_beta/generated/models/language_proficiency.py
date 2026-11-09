from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet
    from .language_proficiency_level import LanguageProficiencyLevel

from .item_facet import ItemFacet

@dataclass
class LanguageProficiency(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.languageProficiency"
    # Contains the long-form name for the language.
    display_name: Optional[str] = None
    # The proficiency property
    proficiency: Optional[LanguageProficiencyLevel] = None
    # Represents the users reading comprehension for the language represented by the object. The possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
    reading: Optional[LanguageProficiencyLevel] = None
    # Represents the users spoken proficiency for the language represented by the object. The possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
    spoken: Optional[LanguageProficiencyLevel] = None
    # Contains the four-character BCP47 name for the language (en-US, no-NB, en-AU).
    tag: Optional[str] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # Represents the users written proficiency for the language represented by the object. The possible values are: elementary, conversational, limitedWorking, professionalWorking, fullProfessional, nativeOrBilingual, unknownFutureValue.
    written: Optional[LanguageProficiencyLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LanguageProficiency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LanguageProficiency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LanguageProficiency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet
        from .language_proficiency_level import LanguageProficiencyLevel

        from .item_facet import ItemFacet
        from .language_proficiency_level import LanguageProficiencyLevel

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "proficiency": lambda n : setattr(self, 'proficiency', n.get_enum_value(LanguageProficiencyLevel)),
            "reading": lambda n : setattr(self, 'reading', n.get_enum_value(LanguageProficiencyLevel)),
            "spoken": lambda n : setattr(self, 'spoken', n.get_enum_value(LanguageProficiencyLevel)),
            "tag": lambda n : setattr(self, 'tag', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "written": lambda n : setattr(self, 'written', n.get_enum_value(LanguageProficiencyLevel)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("proficiency", self.proficiency)
        writer.write_enum_value("reading", self.reading)
        writer.write_enum_value("spoken", self.spoken)
        writer.write_str_value("tag", self.tag)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_enum_value("written", self.written)
    

