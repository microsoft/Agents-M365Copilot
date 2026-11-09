from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .person_relationship import PersonRelationship

@dataclass
class RelatedPerson(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name of the person.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The possible values are: manager, colleague, directReport, dotLineReport, assistant, dotLineManager, alternateContact, friend, spouse, sibling, child, parent, sponsor, emergencyContact, other, unknownFutureValue.
    relationship: Optional[PersonRelationship] = None
    # Information (free-text) describing the relationship between the user and the related person. This property provides additional context beyond the predefined relationship values and can be used by clients, including AI-powered experiences, to better understand and reason about the relationship.
    relationship_label: Optional[str] = None
    # The user's directory object ID (Microsoft Entra ID or CID).
    user_id: Optional[str] = None
    # Email address or reference to person within the organization.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedPerson:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedPerson
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelatedPerson()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .person_relationship import PersonRelationship

        from .person_relationship import PersonRelationship

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(PersonRelationship)),
            "relationshipLabel": lambda n : setattr(self, 'relationship_label', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("relationship", self.relationship)
        writer.write_str_value("relationshipLabel", self.relationship_label)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

