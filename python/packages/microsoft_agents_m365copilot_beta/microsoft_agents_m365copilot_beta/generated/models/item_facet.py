from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .allowed_audiences import AllowedAudiences
    from .educational_activity import EducationalActivity
    from .entity import Entity
    from .identity_set import IdentitySet
    from .inference_data import InferenceData
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
    from .person_data_sources import PersonDataSources
    from .person_interest import PersonInterest
    from .person_name import PersonName
    from .person_responsibility import PersonResponsibility
    from .person_website import PersonWebsite
    from .profile_source_annotation import ProfileSourceAnnotation
    from .project_participation import ProjectParticipation
    from .skill_proficiency import SkillProficiency
    from .user_account_information import UserAccountInformation
    from .web_account import WebAccount
    from .work_position import WorkPosition

from .entity import Entity

@dataclass
class ItemFacet(Entity, Parsable):
    # The audiences that are able to see the values contained within the associated entity. The possible values are: me, family, contacts, groupMembers, organization, federatedOrganizations, everyone, unknownFutureValue.
    allowed_audiences: Optional[AllowedAudiences] = None
    # Provides the identifier of the user and/or application that created the entity.
    created_by: Optional[IdentitySet] = None
    # Provides the dateTimeOffset for when the entity was created.
    created_date_time: Optional[datetime.datetime] = None
    # Contains inference detail if the entity is inferred by the creating or modifying application.
    inference: Optional[InferenceData] = None
    # The isSearchable property
    is_searchable: Optional[bool] = None
    # Provides the identifier of the user and/or application that last modified the entity.
    last_modified_by: Optional[IdentitySet] = None
    # Provides the dateTimeOffset for when the entity was created.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Where the values within an entity originated if synced from another service.
    source: Optional[PersonDataSources] = None
    # Where the values within an entity originated if synced from another source.
    sources: Optional[list[ProfileSourceAnnotation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemFacet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemFacet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationalActivity".casefold():
            from .educational_activity import EducationalActivity

            return EducationalActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAddress".casefold():
            from .item_address import ItemAddress

            return ItemAddress()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemEmail".casefold():
            from .item_email import ItemEmail

            return ItemEmail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPatent".casefold():
            from .item_patent import ItemPatent

            return ItemPatent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPhone".casefold():
            from .item_phone import ItemPhone

            return ItemPhone()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemPublication".casefold():
            from .item_publication import ItemPublication

            return ItemPublication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.languageProficiency".casefold():
            from .language_proficiency import LanguageProficiency

            return LanguageProficiency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAnnotation".casefold():
            from .person_annotation import PersonAnnotation

            return PersonAnnotation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAnnualEvent".casefold():
            from .person_annual_event import PersonAnnualEvent

            return PersonAnnualEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personAward".casefold():
            from .person_award import PersonAward

            return PersonAward()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personCertification".casefold():
            from .person_certification import PersonCertification

            return PersonCertification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personInterest".casefold():
            from .person_interest import PersonInterest

            return PersonInterest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personName".casefold():
            from .person_name import PersonName

            return PersonName()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personResponsibility".casefold():
            from .person_responsibility import PersonResponsibility

            return PersonResponsibility()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.personWebsite".casefold():
            from .person_website import PersonWebsite

            return PersonWebsite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.projectParticipation".casefold():
            from .project_participation import ProjectParticipation

            return ProjectParticipation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skillProficiency".casefold():
            from .skill_proficiency import SkillProficiency

            return SkillProficiency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userAccountInformation".casefold():
            from .user_account_information import UserAccountInformation

            return UserAccountInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webAccount".casefold():
            from .web_account import WebAccount

            return WebAccount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workPosition".casefold():
            from .work_position import WorkPosition

            return WorkPosition()
        return ItemFacet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .allowed_audiences import AllowedAudiences
        from .educational_activity import EducationalActivity
        from .entity import Entity
        from .identity_set import IdentitySet
        from .inference_data import InferenceData
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
        from .person_data_sources import PersonDataSources
        from .person_interest import PersonInterest
        from .person_name import PersonName
        from .person_responsibility import PersonResponsibility
        from .person_website import PersonWebsite
        from .profile_source_annotation import ProfileSourceAnnotation
        from .project_participation import ProjectParticipation
        from .skill_proficiency import SkillProficiency
        from .user_account_information import UserAccountInformation
        from .web_account import WebAccount
        from .work_position import WorkPosition

        from .allowed_audiences import AllowedAudiences
        from .educational_activity import EducationalActivity
        from .entity import Entity
        from .identity_set import IdentitySet
        from .inference_data import InferenceData
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
        from .person_data_sources import PersonDataSources
        from .person_interest import PersonInterest
        from .person_name import PersonName
        from .person_responsibility import PersonResponsibility
        from .person_website import PersonWebsite
        from .profile_source_annotation import ProfileSourceAnnotation
        from .project_participation import ProjectParticipation
        from .skill_proficiency import SkillProficiency
        from .user_account_information import UserAccountInformation
        from .web_account import WebAccount
        from .work_position import WorkPosition

        fields: dict[str, Callable[[Any], None]] = {
            "allowedAudiences": lambda n : setattr(self, 'allowed_audiences', n.get_collection_of_enum_values(AllowedAudiences)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "inference": lambda n : setattr(self, 'inference', n.get_object_value(InferenceData)),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(PersonDataSources)),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_object_values(ProfileSourceAnnotation)),
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
        writer.write_enum_value("allowedAudiences", self.allowed_audiences)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("inference", self.inference)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("source", self.source)
        writer.write_collection_of_object_values("sources", self.sources)
    

