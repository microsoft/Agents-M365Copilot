from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
    from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomExtensionHandler(Entity, Parsable):
    # Indicates which custom workflow extension is executed at this stage. Nullable. Supports $expand.
    custom_extension: Optional[CustomAccessPackageWorkflowExtension] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the stage of the access package assignment request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
    stage: Optional[AccessPackageCustomExtensionStage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomExtensionHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionHandler
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomExtensionHandler()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
        from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
        from .entity import Entity

        from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
        from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "customExtension": lambda n : setattr(self, 'custom_extension', n.get_object_value(CustomAccessPackageWorkflowExtension)),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(AccessPackageCustomExtensionStage)),
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
        writer.write_object_value("customExtension", self.custom_extension)
        writer.write_enum_value("stage", self.stage)
    

