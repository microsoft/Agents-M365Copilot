from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .export_file_structure import ExportFileStructure
    from .export_options import ExportOptions
    from .review_set import ReviewSet

from .case_operation import CaseOperation

@dataclass
class CaseExportOperation(CaseOperation, Parsable):
    # The name of the Azure storage location where the export will be stored. This only applies to exports stored in your own Azure storage location.
    azure_blob_container: Optional[str] = None
    # The SAS token for the Azure storage location.  This only applies to exports stored in your own Azure storage location.
    azure_blob_token: Optional[str] = None
    # The description provided for the export.
    description: Optional[str] = None
    # The options provided for the export. For more information, see reviewSet: export. The possible values are: originalFiles, text, pdfReplacement, fileInfo, tags.
    export_options: Optional[ExportOptions] = None
    # The options provided specify the structure of the export. For more information, see reviewSet: export. The possible values are: none, directory, pst.
    export_structure: Optional[ExportFileStructure] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The output folder ID.
    output_folder_id: Optional[str] = None
    # The name provided for the export.
    output_name: Optional[str] = None
    # The review set the content is being exported from.
    review_set: Optional[ReviewSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CaseExportOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaseExportOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CaseExportOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .export_file_structure import ExportFileStructure
        from .export_options import ExportOptions
        from .review_set import ReviewSet

        from .case_operation import CaseOperation
        from .export_file_structure import ExportFileStructure
        from .export_options import ExportOptions
        from .review_set import ReviewSet

        fields: dict[str, Callable[[Any], None]] = {
            "azureBlobContainer": lambda n : setattr(self, 'azure_blob_container', n.get_str_value()),
            "azureBlobToken": lambda n : setattr(self, 'azure_blob_token', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_collection_of_enum_values(ExportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(ExportFileStructure)),
            "outputFolderId": lambda n : setattr(self, 'output_folder_id', n.get_str_value()),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
            "reviewSet": lambda n : setattr(self, 'review_set', n.get_object_value(ReviewSet)),
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
        writer.write_str_value("azureBlobContainer", self.azure_blob_container)
        writer.write_str_value("azureBlobToken", self.azure_blob_token)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputFolderId", self.output_folder_id)
        writer.write_str_value("outputName", self.output_name)
        writer.write_object_value("reviewSet", self.review_set)
    

