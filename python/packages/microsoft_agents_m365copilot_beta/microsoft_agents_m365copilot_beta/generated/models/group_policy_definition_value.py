from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_configuration_type import GroupPolicyConfigurationType
    from .group_policy_definition import GroupPolicyDefinition
    from .group_policy_presentation_value import GroupPolicyPresentationValue

from .entity import Entity

@dataclass
class GroupPolicyDefinitionValue(Entity, Parsable):
    """
    The definition value entity stores the value for a single group policy definition.
    """
    # Group Policy Configuration Type
    configuration_type: Optional[GroupPolicyConfigurationType] = None
    # The date and time the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # The associated group policy definition with the value.
    definition: Optional[GroupPolicyDefinition] = None
    # Enables or disables the associated group policy definition.
    enabled: Optional[bool] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The associated group policy presentation values with the definition value.
    presentation_values: Optional[list[GroupPolicyPresentationValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyDefinitionValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinitionValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyDefinitionValue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_configuration_type import GroupPolicyConfigurationType
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_presentation_value import GroupPolicyPresentationValue

        from .entity import Entity
        from .group_policy_configuration_type import GroupPolicyConfigurationType
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_presentation_value import GroupPolicyPresentationValue

        fields: dict[str, Callable[[Any], None]] = {
            "configurationType": lambda n : setattr(self, 'configuration_type', n.get_enum_value(GroupPolicyConfigurationType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(GroupPolicyDefinition)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "presentationValues": lambda n : setattr(self, 'presentation_values', n.get_collection_of_object_values(GroupPolicyPresentationValue)),
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
        writer.write_enum_value("configurationType", self.configuration_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definition", self.definition)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("presentationValues", self.presentation_values)
    

