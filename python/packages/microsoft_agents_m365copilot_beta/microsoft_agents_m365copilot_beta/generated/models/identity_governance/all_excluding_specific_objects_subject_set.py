from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..directory_object import DirectoryObject
    from ..subject_set import SubjectSet

from ..subject_set import SubjectSet

@dataclass
class AllExcludingSpecificObjectsSubjectSet(SubjectSet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.allExcludingSpecificObjectsSubjectSet"
    # The excludedObjects property
    excluded_objects: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AllExcludingSpecificObjectsSubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AllExcludingSpecificObjectsSubjectSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AllExcludingSpecificObjectsSubjectSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..directory_object import DirectoryObject
        from ..subject_set import SubjectSet

        from ..directory_object import DirectoryObject
        from ..subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "excludedObjects": lambda n : setattr(self, 'excluded_objects', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_collection_of_object_values("excludedObjects", self.excluded_objects)
    

