from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_model_type import ContentModelType
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class ContentModel(Entity, Parsable):
    # Identity of the user, device, or applicationthat created the item. Read-only.
    created_by: Optional[IdentitySet] = None
    # Date and time of item creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Identity of the user, device, or application that modified the item. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time of item last modification. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The type of the contentModel. The possible values are: teachingMethod, layoutMethod, freeformSelectionMethod, prebuiltContractModel, prebuiltInvoiceModel, prebuiltReceiptModel, unknownFutureValue.
    model_type: Optional[ContentModelType] = None
    # The name of the contentModel.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentModel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_model_type import ContentModelType
        from .entity import Entity
        from .identity_set import IdentitySet

        from .content_model_type import ContentModelType
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "modelType": lambda n : setattr(self, 'model_type', n.get_enum_value(ContentModelType)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("modelType", self.model_type)
        writer.write_str_value("name", self.name)
    

