from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label import Label
    from .property_type import PropertyType
    from .ranking_hint import RankingHint

@dataclass
class Property_(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A set of aliases or friendly names for the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string might not contain control characters, whitespace, or any of the following special characters: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^. Optional.
    aliases: Optional[list[str]] = None
    # The description property
    description: Optional[str] = None
    # Specifies if the property will be matched exactly for queries. Exact matching can only be set to true for nonsearchable properties of type string or stringCollection. Optional.
    is_exact_match_required: Optional[bool] = None
    # Specifies if the property is queryable. Queryable properties can be used in Keyword Query Language (KQL) queries. Optional.
    is_queryable: Optional[bool] = None
    # Specifies if the property is refinable.  Refinable properties can be used to filter search results in the Search API and add a refiner control in the Microsoft Search user experience. Optional.
    is_refinable: Optional[bool] = None
    # Specifies if the property is retrievable. Retrievable properties are returned in the result set when items are returned by the search API. Retrievable properties are also available to add to the display template used to render search results. Optional.
    is_retrievable: Optional[bool] = None
    # Specifies if the property is searchable. Only properties of type string or stringCollection can be searchable. Nonsearchable properties aren't added to the search index. Optional.
    is_searchable: Optional[bool] = None
    # Specifies one or more well-known tags added against a property. Labels help Microsoft Search understand the semantics of the data in the connection. Adding appropriate labels would result in an enhanced search experience (for example, better relevance). Optional.. The possible values are: title, url, createdBy, lastModifiedBy, authors, createdDateTime, lastModifiedDateTime, fileName, fileExtension, unknownFutureValue, containerName, containerUrl, iconUrl, assignedTo, dueDate, closedDate, closedBy, reportedBy, sprintName, severity, state, priority, secondaryId, itemParentId, parentUrl, tags, itemType, itemPath, numReactions. Use the Prefer: include-unknown-enum-members request header to retrieve additional values defined in this evolvable enum.For people connectors you can include : personEmails, personAddresses, personAnniversaries, personName, personNote, personPhones, personCurrentPosition, personWebAccounts, personWebSite, personSkills, personProjects, personAccount, personAwards, personCertifications, personAssistants, personColleagues, personManager, personAlternateContacts, personEmergencyContacts.
    labels: Optional[list[Label]] = None
    # The name of the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, the property name may not contain control characters, whitespace, or any of the following special characters: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^.  Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the property ranking hint. Developers can specify which properties are most important, allowing Microsoft Search to determine the search relevance of the content.
    ranking_hint: Optional[RankingHint] = None
    # The type property
    type: Optional[PropertyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Property_:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Property_
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Property_()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .label import Label
        from .property_type import PropertyType
        from .ranking_hint import RankingHint

        from .label import Label
        from .property_type import PropertyType
        from .ranking_hint import RankingHint

        fields: dict[str, Callable[[Any], None]] = {
            "aliases": lambda n : setattr(self, 'aliases', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "isExactMatchRequired": lambda n : setattr(self, 'is_exact_match_required', n.get_bool_value()),
            "isQueryable": lambda n : setattr(self, 'is_queryable', n.get_bool_value()),
            "isRefinable": lambda n : setattr(self, 'is_refinable', n.get_bool_value()),
            "isRetrievable": lambda n : setattr(self, 'is_retrievable', n.get_bool_value()),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_enum_values(Label)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rankingHint": lambda n : setattr(self, 'ranking_hint', n.get_object_value(RankingHint)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PropertyType)),
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
        writer.write_collection_of_primitive_values("aliases", self.aliases)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isExactMatchRequired", self.is_exact_match_required)
        writer.write_bool_value("isQueryable", self.is_queryable)
        writer.write_bool_value("isRefinable", self.is_refinable)
        writer.write_bool_value("isRetrievable", self.is_retrievable)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_collection_of_enum_values("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("rankingHint", self.ranking_hint)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

