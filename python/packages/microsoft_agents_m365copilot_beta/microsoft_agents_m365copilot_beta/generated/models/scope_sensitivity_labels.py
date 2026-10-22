from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all_scope_sensitivity_labels import AllScopeSensitivityLabels
    from .enumerated_scope_sensitivity_labels import EnumeratedScopeSensitivityLabels
    from .label_kind import LabelKind

@dataclass
class ScopeSensitivityLabels(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the kind of sensitivity label that is included. Possible values: all means all sensitivity labels are allowed, or enumerated means a selected set of sensitivity labels from a single resource application are allowed. Required.
    label_kind: Optional[LabelKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScopeSensitivityLabels:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScopeSensitivityLabels
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allScopeSensitivityLabels".casefold():
            from .all_scope_sensitivity_labels import AllScopeSensitivityLabels

            return AllScopeSensitivityLabels()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enumeratedScopeSensitivityLabels".casefold():
            from .enumerated_scope_sensitivity_labels import EnumeratedScopeSensitivityLabels

            return EnumeratedScopeSensitivityLabels()
        return ScopeSensitivityLabels()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .all_scope_sensitivity_labels import AllScopeSensitivityLabels
        from .enumerated_scope_sensitivity_labels import EnumeratedScopeSensitivityLabels
        from .label_kind import LabelKind

        from .all_scope_sensitivity_labels import AllScopeSensitivityLabels
        from .enumerated_scope_sensitivity_labels import EnumeratedScopeSensitivityLabels
        from .label_kind import LabelKind

        fields: dict[str, Callable[[Any], None]] = {
            "labelKind": lambda n : setattr(self, 'label_kind', n.get_enum_value(LabelKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("labelKind", self.label_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

