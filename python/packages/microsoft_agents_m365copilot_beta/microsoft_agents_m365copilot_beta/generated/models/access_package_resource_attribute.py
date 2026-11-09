from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
    from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

@dataclass
class AccessPackageResourceAttribute(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information about how to set the attribute, currently a accessPackageUserDirectoryAttributeStore object type.
    attribute_destination: Optional[AccessPackageResourceAttributeDestination] = None
    # The name of the attribute in the end system. If the destination is accessPackageUserDirectoryAttributeStore, then a user property such as jobTitle or a directory schema extension for the user object type, such as extension2b676109c7c74ae2b41549205f1947edpersonalTitle.
    attribute_name: Optional[str] = None
    # Information about how to populate the attribute value when an accessPackageAssignmentRequest is being fulfilled, currently a accessPackageResourceAttributeQuestion object type.
    attribute_source: Optional[AccessPackageResourceAttributeSource] = None
    # Unique identifier for the attribute on the access package resource. Read-only.
    id: Optional[str] = None
    # Specifies whether or not an existing attribute value can be edited by the requester.
    is_editable: Optional[bool] = None
    # Specifies whether the attribute will remain in the end system after an assignment ends.
    is_persisted_on_assignment_removal: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceAttribute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceAttribute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        fields: dict[str, Callable[[Any], None]] = {
            "attributeDestination": lambda n : setattr(self, 'attribute_destination', n.get_object_value(AccessPackageResourceAttributeDestination)),
            "attributeName": lambda n : setattr(self, 'attribute_name', n.get_str_value()),
            "attributeSource": lambda n : setattr(self, 'attribute_source', n.get_object_value(AccessPackageResourceAttributeSource)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isEditable": lambda n : setattr(self, 'is_editable', n.get_bool_value()),
            "isPersistedOnAssignmentRemoval": lambda n : setattr(self, 'is_persisted_on_assignment_removal', n.get_bool_value()),
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
        writer.write_object_value("attributeDestination", self.attribute_destination)
        writer.write_str_value("attributeName", self.attribute_name)
        writer.write_object_value("attributeSource", self.attribute_source)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isEditable", self.is_editable)
        writer.write_bool_value("isPersistedOnAssignmentRemoval", self.is_persisted_on_assignment_removal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

