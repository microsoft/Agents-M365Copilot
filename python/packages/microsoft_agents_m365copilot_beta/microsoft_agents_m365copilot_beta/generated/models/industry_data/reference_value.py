from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_format_reference_value import FileFormatReferenceValue
    from .identifier_type_reference_value import IdentifierTypeReferenceValue
    from .reference_definition import ReferenceDefinition
    from .role_reference_value import RoleReferenceValue
    from .section_role_reference_value import SectionRoleReferenceValue
    from .user_match_target_reference_value import UserMatchTargetReferenceValue
    from .year_reference_value import YearReferenceValue

@dataclass
class ReferenceValue(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The code of the desired referenceDefinition entry.
    code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The value property
    value: Optional[ReferenceDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReferenceValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.fileFormatReferenceValue".casefold():
            from .file_format_reference_value import FileFormatReferenceValue

            return FileFormatReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.identifierTypeReferenceValue".casefold():
            from .identifier_type_reference_value import IdentifierTypeReferenceValue

            return IdentifierTypeReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.roleReferenceValue".casefold():
            from .role_reference_value import RoleReferenceValue

            return RoleReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.sectionRoleReferenceValue".casefold():
            from .section_role_reference_value import SectionRoleReferenceValue

            return SectionRoleReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.userMatchTargetReferenceValue".casefold():
            from .user_match_target_reference_value import UserMatchTargetReferenceValue

            return UserMatchTargetReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.yearReferenceValue".casefold():
            from .year_reference_value import YearReferenceValue

            return YearReferenceValue()
        return ReferenceValue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_format_reference_value import FileFormatReferenceValue
        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .reference_definition import ReferenceDefinition
        from .role_reference_value import RoleReferenceValue
        from .section_role_reference_value import SectionRoleReferenceValue
        from .user_match_target_reference_value import UserMatchTargetReferenceValue
        from .year_reference_value import YearReferenceValue

        from .file_format_reference_value import FileFormatReferenceValue
        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .reference_definition import ReferenceDefinition
        from .role_reference_value import RoleReferenceValue
        from .section_role_reference_value import SectionRoleReferenceValue
        from .user_match_target_reference_value import UserMatchTargetReferenceValue
        from .year_reference_value import YearReferenceValue

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(ReferenceDefinition)),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

