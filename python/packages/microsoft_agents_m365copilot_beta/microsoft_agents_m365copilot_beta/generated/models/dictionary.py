from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary
    from .custom_metadata_dictionary import CustomMetadataDictionary
    from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
    from .networkaccess.extended_properties import ExtendedProperties
    from .open_complex_dictionary_type import OpenComplexDictionaryType
    from .partner.security.additional_data_dictionary import AdditionalDataDictionary
    from .planner_forms_dictionary import PlannerFormsDictionary
    from .result_template_dictionary import ResultTemplateDictionary
    from .security.workbook_content import WorkbookContent
    from .string_dictionary import StringDictionary
    from .waf_allowed_headers_dictionary import WafAllowedHeadersDictionary

@dataclass
class Dictionary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Dictionary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Dictionary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAppScopeAttributesDictionary".casefold():
            from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary

            return CustomAppScopeAttributesDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customMetadataDictionary".casefold():
            from .custom_metadata_dictionary import CustomMetadataDictionary

            return CustomMetadataDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileStorageContainerCustomPropertyDictionary".casefold():
            from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary

            return FileStorageContainerCustomPropertyDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.extendedProperties".casefold():
            from .networkaccess.extended_properties import ExtendedProperties

            return ExtendedProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openComplexDictionaryType".casefold():
            from .open_complex_dictionary_type import OpenComplexDictionaryType

            return OpenComplexDictionaryType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partner.security.additionalDataDictionary".casefold():
            from .partner.security.additional_data_dictionary import AdditionalDataDictionary

            return AdditionalDataDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerFormsDictionary".casefold():
            from .planner_forms_dictionary import PlannerFormsDictionary

            return PlannerFormsDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resultTemplateDictionary".casefold():
            from .result_template_dictionary import ResultTemplateDictionary

            return ResultTemplateDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.workbookContent".casefold():
            from .security.workbook_content import WorkbookContent

            return WorkbookContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stringDictionary".casefold():
            from .string_dictionary import StringDictionary

            return StringDictionary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.wafAllowedHeadersDictionary".casefold():
            from .waf_allowed_headers_dictionary import WafAllowedHeadersDictionary

            return WafAllowedHeadersDictionary()
        return Dictionary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary
        from .custom_metadata_dictionary import CustomMetadataDictionary
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .networkaccess.extended_properties import ExtendedProperties
        from .open_complex_dictionary_type import OpenComplexDictionaryType
        from .partner.security.additional_data_dictionary import AdditionalDataDictionary
        from .planner_forms_dictionary import PlannerFormsDictionary
        from .result_template_dictionary import ResultTemplateDictionary
        from .security.workbook_content import WorkbookContent
        from .string_dictionary import StringDictionary
        from .waf_allowed_headers_dictionary import WafAllowedHeadersDictionary

        from .custom_app_scope_attributes_dictionary import CustomAppScopeAttributesDictionary
        from .custom_metadata_dictionary import CustomMetadataDictionary
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .networkaccess.extended_properties import ExtendedProperties
        from .open_complex_dictionary_type import OpenComplexDictionaryType
        from .partner.security.additional_data_dictionary import AdditionalDataDictionary
        from .planner_forms_dictionary import PlannerFormsDictionary
        from .result_template_dictionary import ResultTemplateDictionary
        from .security.workbook_content import WorkbookContent
        from .string_dictionary import StringDictionary
        from .waf_allowed_headers_dictionary import WafAllowedHeadersDictionary

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

