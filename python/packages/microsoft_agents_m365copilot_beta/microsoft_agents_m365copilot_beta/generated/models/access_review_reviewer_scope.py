from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_reviewer_scope_type import AccessReviewReviewerScopeType
    from .access_review_scope import AccessReviewScope

from .access_review_scope import AccessReviewScope

@dataclass
class AccessReviewReviewerScope(AccessReviewScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewReviewerScope"
    # The query specifying who will be the reviewer.
    query: Optional[str] = None
    # In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query, for example, ./manager, is specified. Possible value: decisions.
    query_root: Optional[str] = None
    # The type of query. Examples include MicrosoftGraph and ARM.
    query_type: Optional[str] = None
    # The reviewerId property
    reviewer_id: Optional[str] = None
    # The scopeType property
    scope_type: Optional[AccessReviewReviewerScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewReviewerScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewReviewerScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewReviewerScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_reviewer_scope_type import AccessReviewReviewerScopeType
        from .access_review_scope import AccessReviewScope

        from .access_review_reviewer_scope_type import AccessReviewReviewerScopeType
        from .access_review_scope import AccessReviewScope

        fields: dict[str, Callable[[Any], None]] = {
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "queryRoot": lambda n : setattr(self, 'query_root', n.get_str_value()),
            "queryType": lambda n : setattr(self, 'query_type', n.get_str_value()),
            "reviewerId": lambda n : setattr(self, 'reviewer_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_enum_value(AccessReviewReviewerScopeType)),
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
        writer.write_str_value("query", self.query)
        writer.write_str_value("queryRoot", self.query_root)
        writer.write_str_value("queryType", self.query_type)
        writer.write_str_value("reviewerId", self.reviewer_id)
        writer.write_enum_value("scopeType", self.scope_type)
    

