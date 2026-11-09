from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .resource_quota_type import ResourceQuotaType

@dataclass
class ResourceQuota(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The maxPercentage property
    max_percentage: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceType property
    resource_type: Optional[ResourceQuotaType] = None
    # The total property
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourceQuota:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceQuota
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourceQuota()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .resource_quota_type import ResourceQuotaType

        from .resource_quota_type import ResourceQuotaType

        fields: dict[str, Callable[[Any], None]] = {
            "maxPercentage": lambda n : setattr(self, 'max_percentage', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_enum_value(ResourceQuotaType)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_int_value("maxPercentage", self.max_percentage)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("resourceType", self.resource_type)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

