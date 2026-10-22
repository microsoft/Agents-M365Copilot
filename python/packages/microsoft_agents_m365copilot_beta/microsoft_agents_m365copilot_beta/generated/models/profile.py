from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .educational_activity import EducationalActivity
    from .entity import Entity
    from .item_address import ItemAddress
    from .item_email import ItemEmail
    from .item_patent import ItemPatent
    from .item_phone import ItemPhone
    from .item_publication import ItemPublication
    from .language_proficiency import LanguageProficiency
    from .person_annotation import PersonAnnotation
    from .person_annual_event import PersonAnnualEvent
    from .person_award import PersonAward
    from .person_certification import PersonCertification
    from .person_interest import PersonInterest
    from .person_name import PersonName
    from .person_website import PersonWebsite
    from .project_participation import ProjectParticipation
    from .skill_proficiency import SkillProficiency
    from .user_account_information import UserAccountInformation
    from .web_account import WebAccount
    from .work_position import WorkPosition

from .entity import Entity

@dataclass
class Profile(Entity, Parsable):
    # The account property
    account: Optional[list[UserAccountInformation]] = None
    # Represents details of addresses associated with the user.
    addresses: Optional[list[ItemAddress]] = None
    # Represents the details of meaningful dates associated with a person.
    anniversaries: Optional[list[PersonAnnualEvent]] = None
    # Represents the details of awards or honors associated with a person.
    awards: Optional[list[PersonAward]] = None
    # Represents the details of certifications associated with a person.
    certifications: Optional[list[PersonCertification]] = None
    # Represents data that a user has supplied related to undergraduate, graduate, postgraduate or other educational activities.
    educational_activities: Optional[list[EducationalActivity]] = None
    # Represents detailed information about email addresses associated with the user.
    emails: Optional[list[ItemEmail]] = None
    # Provides detailed information about interests the user has associated with themselves in various services.
    interests: Optional[list[PersonInterest]] = None
    # Represents detailed information about languages that a user has added to their profile.
    languages: Optional[list[LanguageProficiency]] = None
    # Represents the names a user has added to their profile.
    names: Optional[list[PersonName]] = None
    # Represents notes that a user has added to their profile.
    notes: Optional[list[PersonAnnotation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents patents that a user has added to their profile.
    patents: Optional[list[ItemPatent]] = None
    # Represents detailed information about phone numbers associated with a user in various services.
    phones: Optional[list[ItemPhone]] = None
    # Represents detailed information about work positions associated with a user's profile.
    positions: Optional[list[WorkPosition]] = None
    # Represents detailed information about projects associated with a user.
    projects: Optional[list[ProjectParticipation]] = None
    # Represents details of any publications a user has added to their profile.
    publications: Optional[list[ItemPublication]] = None
    # Represents detailed information about skills associated with a user in various services.
    skills: Optional[list[SkillProficiency]] = None
    # Represents web accounts the user has indicated they use or has added to their user profile.
    web_accounts: Optional[list[WebAccount]] = None
    # Represents detailed information about websites associated with a user in various services.
    websites: Optional[list[PersonWebsite]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Profile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Profile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Profile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .educational_activity import EducationalActivity
        from .entity import Entity
        from .item_address import ItemAddress
        from .item_email import ItemEmail
        from .item_patent import ItemPatent
        from .item_phone import ItemPhone
        from .item_publication import ItemPublication
        from .language_proficiency import LanguageProficiency
        from .person_annotation import PersonAnnotation
        from .person_annual_event import PersonAnnualEvent
        from .person_award import PersonAward
        from .person_certification import PersonCertification
        from .person_interest import PersonInterest
        from .person_name import PersonName
        from .person_website import PersonWebsite
        from .project_participation import ProjectParticipation
        from .skill_proficiency import SkillProficiency
        from .user_account_information import UserAccountInformation
        from .web_account import WebAccount
        from .work_position import WorkPosition

        from .educational_activity import EducationalActivity
        from .entity import Entity
        from .item_address import ItemAddress
        from .item_email import ItemEmail
        from .item_patent import ItemPatent
        from .item_phone import ItemPhone
        from .item_publication import ItemPublication
        from .language_proficiency import LanguageProficiency
        from .person_annotation import PersonAnnotation
        from .person_annual_event import PersonAnnualEvent
        from .person_award import PersonAward
        from .person_certification import PersonCertification
        from .person_interest import PersonInterest
        from .person_name import PersonName
        from .person_website import PersonWebsite
        from .project_participation import ProjectParticipation
        from .skill_proficiency import SkillProficiency
        from .user_account_information import UserAccountInformation
        from .web_account import WebAccount
        from .work_position import WorkPosition

        fields: dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_collection_of_object_values(UserAccountInformation)),
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(ItemAddress)),
            "anniversaries": lambda n : setattr(self, 'anniversaries', n.get_collection_of_object_values(PersonAnnualEvent)),
            "awards": lambda n : setattr(self, 'awards', n.get_collection_of_object_values(PersonAward)),
            "certifications": lambda n : setattr(self, 'certifications', n.get_collection_of_object_values(PersonCertification)),
            "educationalActivities": lambda n : setattr(self, 'educational_activities', n.get_collection_of_object_values(EducationalActivity)),
            "emails": lambda n : setattr(self, 'emails', n.get_collection_of_object_values(ItemEmail)),
            "interests": lambda n : setattr(self, 'interests', n.get_collection_of_object_values(PersonInterest)),
            "languages": lambda n : setattr(self, 'languages', n.get_collection_of_object_values(LanguageProficiency)),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(PersonName)),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_object_values(PersonAnnotation)),
            "patents": lambda n : setattr(self, 'patents', n.get_collection_of_object_values(ItemPatent)),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(ItemPhone)),
            "positions": lambda n : setattr(self, 'positions', n.get_collection_of_object_values(WorkPosition)),
            "projects": lambda n : setattr(self, 'projects', n.get_collection_of_object_values(ProjectParticipation)),
            "publications": lambda n : setattr(self, 'publications', n.get_collection_of_object_values(ItemPublication)),
            "skills": lambda n : setattr(self, 'skills', n.get_collection_of_object_values(SkillProficiency)),
            "webAccounts": lambda n : setattr(self, 'web_accounts', n.get_collection_of_object_values(WebAccount)),
            "websites": lambda n : setattr(self, 'websites', n.get_collection_of_object_values(PersonWebsite)),
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
        writer.write_collection_of_object_values("account", self.account)
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_collection_of_object_values("anniversaries", self.anniversaries)
        writer.write_collection_of_object_values("awards", self.awards)
        writer.write_collection_of_object_values("certifications", self.certifications)
        writer.write_collection_of_object_values("educationalActivities", self.educational_activities)
        writer.write_collection_of_object_values("emails", self.emails)
        writer.write_collection_of_object_values("interests", self.interests)
        writer.write_collection_of_object_values("languages", self.languages)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("notes", self.notes)
        writer.write_collection_of_object_values("patents", self.patents)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_collection_of_object_values("positions", self.positions)
        writer.write_collection_of_object_values("projects", self.projects)
        writer.write_collection_of_object_values("publications", self.publications)
        writer.write_collection_of_object_values("skills", self.skills)
        writer.write_collection_of_object_values("webAccounts", self.web_accounts)
        writer.write_collection_of_object_values("websites", self.websites)
    

