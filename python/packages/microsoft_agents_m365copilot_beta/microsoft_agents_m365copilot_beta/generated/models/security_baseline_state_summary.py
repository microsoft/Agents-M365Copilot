from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary

from .entity import Entity

@dataclass
class SecurityBaselineStateSummary(Entity, Parsable):
    """
    The security baseline compliance state summary for the security baseline of the account.
    """
    # Number of conflict devices
    conflict_count: Optional[int] = None
    # Number of error devices
    error_count: Optional[int] = None
    # Number of not applicable devices
    not_applicable_count: Optional[int] = None
    # Number of not secure devices
    not_secure_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of secure devices
    secure_count: Optional[int] = None
    # Number of unknown devices
    unknown_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityBaselineStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineStateSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityBaselineCategoryStateSummary".casefold():
            from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary

            return SecurityBaselineCategoryStateSummary()
        return SecurityBaselineStateSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary

        from .entity import Entity
        from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary

        fields: dict[str, Callable[[Any], None]] = {
            "conflictCount": lambda n : setattr(self, 'conflict_count', n.get_int_value()),
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "notApplicableCount": lambda n : setattr(self, 'not_applicable_count', n.get_int_value()),
            "notSecureCount": lambda n : setattr(self, 'not_secure_count', n.get_int_value()),
            "secureCount": lambda n : setattr(self, 'secure_count', n.get_int_value()),
            "unknownCount": lambda n : setattr(self, 'unknown_count', n.get_int_value()),
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
        writer.write_int_value("conflictCount", self.conflict_count)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_int_value("notApplicableCount", self.not_applicable_count)
        writer.write_int_value("notSecureCount", self.not_secure_count)
        writer.write_int_value("secureCount", self.secure_count)
        writer.write_int_value("unknownCount", self.unknown_count)
    

