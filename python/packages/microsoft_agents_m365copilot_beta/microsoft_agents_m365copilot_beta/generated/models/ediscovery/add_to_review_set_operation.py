from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .review_set import ReviewSet
    from .source_collection import SourceCollection

from .case_operation import CaseOperation

@dataclass
class AddToReviewSetOperation(CaseOperation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The review set to which items matching the source collection query are added to.
    review_set: Optional[ReviewSet] = None
    # The sourceCollection that items are being added from.
    source_collection: Optional[SourceCollection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AddToReviewSetOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AddToReviewSetOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .review_set import ReviewSet
        from .source_collection import SourceCollection

        from .case_operation import CaseOperation
        from .review_set import ReviewSet
        from .source_collection import SourceCollection

        fields: dict[str, Callable[[Any], None]] = {
            "reviewSet": lambda n : setattr(self, 'review_set', n.get_object_value(ReviewSet)),
            "sourceCollection": lambda n : setattr(self, 'source_collection', n.get_object_value(SourceCollection)),
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
        writer.write_object_value("reviewSet", self.review_set)
        writer.write_object_value("sourceCollection", self.source_collection)
    

