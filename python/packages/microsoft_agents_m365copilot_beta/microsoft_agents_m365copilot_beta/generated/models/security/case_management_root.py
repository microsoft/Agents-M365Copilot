from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .case_management.case import Case
    from .case_management.case_type_configuration import CaseTypeConfiguration

from ..entity import Entity

@dataclass
class CaseManagementRoot(Entity, Parsable):
    # The collection of case type configurations that define the statuses and custom fields available for each case type. Read-only. Supports $select, $count, and $expand of the statuses and customFields relationships.
    case_type_configurations: Optional[list[CaseTypeConfiguration]] = None
    # The collection of security cases managed through the case management entry point. Supports $filter, $orderby, $select, $top, and $skip.
    cases: Optional[list[Case]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CaseManagementRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaseManagementRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CaseManagementRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .case_management.case import Case
        from .case_management.case_type_configuration import CaseTypeConfiguration

        from ..entity import Entity
        from .case_management.case import Case
        from .case_management.case_type_configuration import CaseTypeConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "caseTypeConfigurations": lambda n : setattr(self, 'case_type_configurations', n.get_collection_of_object_values(CaseTypeConfiguration)),
            "cases": lambda n : setattr(self, 'cases', n.get_collection_of_object_values(Case)),
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
        writer.write_collection_of_object_values("caseTypeConfigurations", self.case_type_configurations)
        writer.write_collection_of_object_values("cases", self.cases)
    

