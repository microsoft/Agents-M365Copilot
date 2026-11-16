from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet
    from .person_name_pronounciation import PersonNamePronounciation

from .item_facet import ItemFacet

@dataclass
class PersonName(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.personName"
    # Provides an ordered rendering of firstName and lastName depending on the locale of the user or their device.
    display_name: Optional[str] = None
    # First name of the user.
    first: Optional[str] = None
    # Initials of the user.
    initials: Optional[str] = None
    # Contains the name for the language (en-US, no-NB, en-AU) following IETF BCP47 format.
    language_tag: Optional[str] = None
    # Last name of the user.
    last: Optional[str] = None
    # Maiden name of the user.
    maiden: Optional[str] = None
    # Middle name of the user.
    middle: Optional[str] = None
    # Nickname of the user.
    nickname: Optional[str] = None
    # Guidance on how to pronounce the users name.
    pronunciation: Optional[PersonNamePronounciation] = None
    # Designators used after the users name (eg: PhD.)
    suffix: Optional[str] = None
    # Honorifics used to prefix a users name (eg: Dr, Sir, Madam, Mrs.)
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersonName:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersonName
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersonName()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet
        from .person_name_pronounciation import PersonNamePronounciation

        from .item_facet import ItemFacet
        from .person_name_pronounciation import PersonNamePronounciation

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "first": lambda n : setattr(self, 'first', n.get_str_value()),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "last": lambda n : setattr(self, 'last', n.get_str_value()),
            "maiden": lambda n : setattr(self, 'maiden', n.get_str_value()),
            "middle": lambda n : setattr(self, 'middle', n.get_str_value()),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
            "pronunciation": lambda n : setattr(self, 'pronunciation', n.get_object_value(PersonNamePronounciation)),
            "suffix": lambda n : setattr(self, 'suffix', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("first", self.first)
        writer.write_str_value("initials", self.initials)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("last", self.last)
        writer.write_str_value("maiden", self.maiden)
        writer.write_str_value("middle", self.middle)
        writer.write_str_value("nickname", self.nickname)
        writer.write_object_value("pronunciation", self.pronunciation)
        writer.write_str_value("suffix", self.suffix)
        writer.write_str_value("title", self.title)
    

