from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_address import EmailAddress
    from .extension import Extension
    from .followup_flag import FollowupFlag
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .phone import Phone
    from .physical_address import PhysicalAddress
    from .profile_photo import ProfilePhoto
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
    from .typed_email_address import TypedEmailAddress
    from .website import Website

from .outlook_item import OutlookItem

@dataclass
class Contact(OutlookItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.contact"
    # The name of the contact's assistant.
    assistant_name: Optional[str] = None
    # The contact's birthday. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    birthday: Optional[datetime.datetime] = None
    # The names of the contact's children.
    children: Optional[list[str]] = None
    # The name of the contact's company.
    company_name: Optional[str] = None
    # The contact's department.
    department: Optional[str] = None
    # The contact's display name. You can specify the display name in a create or update operation. Later updates to other properties might cause an automatically generated value to overwrite the displayName value you specified. To preserve a pre-existing value, always include it as displayName in an update operation.
    display_name: Optional[str] = None
    # The contact's email addresses.
    email_addresses: Optional[list[TypedEmailAddress]] = None
    # The collection of open extensions defined for the contact. Nullable.
    extensions: Optional[list[Extension]] = None
    # The name the contact is filed under.
    file_as: Optional[str] = None
    # The flag value that indicates the status, start date, due date, or completion date for the contact.
    flag: Optional[FollowupFlag] = None
    # The contact's gender.
    gender: Optional[str] = None
    # The contact's suffix.
    generation: Optional[str] = None
    # The contact's given name.
    given_name: Optional[str] = None
    # The contact's instant messaging (IM) addresses.
    im_addresses: Optional[list[str]] = None
    # The contact's initials.
    initials: Optional[str] = None
    # The isFavorite property
    is_favorite: Optional[bool] = None
    # The contact’s job title.
    job_title: Optional[str] = None
    # The name of the contact's manager.
    manager: Optional[str] = None
    # The contact's middle name.
    middle_name: Optional[str] = None
    # The collection of multi-value extended properties defined for the contact. Read-only. Nullable.
    multi_value_extended_properties: Optional[list[MultiValueLegacyExtendedProperty]] = None
    # The contact's nickname.
    nick_name: Optional[str] = None
    # The location of the contact's office.
    office_location: Optional[str] = None
    # The ID of the contact's parent folder.
    parent_folder_id: Optional[str] = None
    # The user's notes about the contact.
    personal_notes: Optional[str] = None
    # Phone numbers associated with the contact, for example, home phone, mobile phone, and business phone.
    phones: Optional[list[Phone]] = None
    # Optional contact picture. You can get or set a photo for a contact.
    photo: Optional[ProfilePhoto] = None
    # Addresses associated with the contact, for example, home address and business address.
    postal_addresses: Optional[list[PhysicalAddress]] = None
    # The primary email address of the contact.
    primary_email_address: Optional[EmailAddress] = None
    # The contact's profession.
    profession: Optional[str] = None
    # The secondary email address of the contact.
    secondary_email_address: Optional[EmailAddress] = None
    # The collection of single-value extended properties defined for the contact. Read-only. Nullable.
    single_value_extended_properties: Optional[list[SingleValueLegacyExtendedProperty]] = None
    # The name of the contact's spouse/partner.
    spouse_name: Optional[str] = None
    # The contact's surname.
    surname: Optional[str] = None
    # The tertiary email address of the contact.
    tertiary_email_address: Optional[EmailAddress] = None
    # The contact's title.
    title: Optional[str] = None
    # Web sites associated with the contact.
    websites: Optional[list[Website]] = None
    # The contact's wedding anniversary.
    wedding_anniversary: Optional[datetime.date] = None
    # The phonetic Japanese company name of the contact.
    yomi_company_name: Optional[str] = None
    # The phonetic Japanese given name (first name) of the contact.
    yomi_given_name: Optional[str] = None
    # The phonetic Japanese surname (last name)  of the contact.
    yomi_surname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Contact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Contact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Contact()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_address import EmailAddress
        from .extension import Extension
        from .followup_flag import FollowupFlag
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .phone import Phone
        from .physical_address import PhysicalAddress
        from .profile_photo import ProfilePhoto
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .typed_email_address import TypedEmailAddress
        from .website import Website

        from .email_address import EmailAddress
        from .extension import Extension
        from .followup_flag import FollowupFlag
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .phone import Phone
        from .physical_address import PhysicalAddress
        from .profile_photo import ProfilePhoto
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .typed_email_address import TypedEmailAddress
        from .website import Website

        fields: dict[str, Callable[[Any], None]] = {
            "assistantName": lambda n : setattr(self, 'assistant_name', n.get_str_value()),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_primitive_values(str)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_object_values(TypedEmailAddress)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "fileAs": lambda n : setattr(self, 'file_as', n.get_str_value()),
            "flag": lambda n : setattr(self, 'flag', n.get_object_value(FollowupFlag)),
            "gender": lambda n : setattr(self, 'gender', n.get_str_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "imAddresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "initials": lambda n : setattr(self, 'initials', n.get_str_value()),
            "isFavorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_str_value()),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "nickName": lambda n : setattr(self, 'nick_name', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "personalNotes": lambda n : setattr(self, 'personal_notes', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "postalAddresses": lambda n : setattr(self, 'postal_addresses', n.get_collection_of_object_values(PhysicalAddress)),
            "primaryEmailAddress": lambda n : setattr(self, 'primary_email_address', n.get_object_value(EmailAddress)),
            "profession": lambda n : setattr(self, 'profession', n.get_str_value()),
            "secondaryEmailAddress": lambda n : setattr(self, 'secondary_email_address', n.get_object_value(EmailAddress)),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "spouseName": lambda n : setattr(self, 'spouse_name', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "tertiaryEmailAddress": lambda n : setattr(self, 'tertiary_email_address', n.get_object_value(EmailAddress)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(Website)),
            "weddingAnniversary": lambda n : setattr(self, 'wedding_anniversary', n.get_date_value()),
            "yomiCompanyName": lambda n : setattr(self, 'yomi_company_name', n.get_str_value()),
            "yomiGivenName": lambda n : setattr(self, 'yomi_given_name', n.get_str_value()),
            "yomiSurname": lambda n : setattr(self, 'yomi_surname', n.get_str_value()),
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
        writer.write_str_value("assistantName", self.assistant_name)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_collection_of_primitive_values("children", self.children)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("emailAddresses", self.email_addresses)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("fileAs", self.file_as)
        writer.write_object_value("flag", self.flag)
        writer.write_str_value("gender", self.gender)
        writer.write_str_value("generation", self.generation)
        writer.write_str_value("givenName", self.given_name)
        writer.write_collection_of_primitive_values("imAddresses", self.im_addresses)
        writer.write_str_value("initials", self.initials)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("manager", self.manager)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("nickName", self.nick_name)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_str_value("personalNotes", self.personal_notes)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("postalAddresses", self.postal_addresses)
        writer.write_object_value("primaryEmailAddress", self.primary_email_address)
        writer.write_str_value("profession", self.profession)
        writer.write_object_value("secondaryEmailAddress", self.secondary_email_address)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_str_value("spouseName", self.spouse_name)
        writer.write_str_value("surname", self.surname)
        writer.write_object_value("tertiaryEmailAddress", self.tertiary_email_address)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_object_values("websites", self.websites)
        writer.write_date_value("weddingAnniversary", self.wedding_anniversary)
        writer.write_str_value("yomiCompanyName", self.yomi_company_name)
        writer.write_str_value("yomiGivenName", self.yomi_given_name)
        writer.write_str_value("yomiSurname", self.yomi_surname)
    

