from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_drift_resource_type import AccessDriftResourceType
    from .application_drift_resource_info import ApplicationDriftResourceInfo
    from .group_drift_resource_info import GroupDriftResourceInfo

@dataclass
class DriftResourceInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The identifier of the entitlement management catalog that contains the resource.
    catalog_identifier: Optional[str] = None
    # The display name of the entitlement management catalog.
    catalog_name: Optional[str] = None
    # The display name of the governed resource.
    display_name: Optional[str] = None
    # The unique identifier of the governed resource.
    identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type property
    type: Optional[AccessDriftResourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriftResourceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriftResourceInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationDriftResourceInfo".casefold():
            from .application_drift_resource_info import ApplicationDriftResourceInfo

            return ApplicationDriftResourceInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupDriftResourceInfo".casefold():
            from .group_drift_resource_info import GroupDriftResourceInfo

            return GroupDriftResourceInfo()
        return DriftResourceInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_drift_resource_type import AccessDriftResourceType
        from .application_drift_resource_info import ApplicationDriftResourceInfo
        from .group_drift_resource_info import GroupDriftResourceInfo

        from .access_drift_resource_type import AccessDriftResourceType
        from .application_drift_resource_info import ApplicationDriftResourceInfo
        from .group_drift_resource_info import GroupDriftResourceInfo

        fields: dict[str, Callable[[Any], None]] = {
            "catalogIdentifier": lambda n : setattr(self, 'catalog_identifier', n.get_str_value()),
            "catalogName": lambda n : setattr(self, 'catalog_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AccessDriftResourceType)),
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
        writer.write_str_value("catalogIdentifier", self.catalog_identifier)
        writer.write_str_value("catalogName", self.catalog_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

