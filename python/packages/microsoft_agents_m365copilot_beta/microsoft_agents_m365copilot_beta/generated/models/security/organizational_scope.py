from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .scope_type import ScopeType

@dataclass
class OrganizationalScope(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # List of device groups to which the custom detection rule applies.
    device_groups: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of groups to which the custom detection rule applies. Deprecated. Use deviceGroups instead. This property will be removed from this resource on October 1, 2026.
    scope_names: Optional[list[str]] = None
    # The scopeType property
    scope_type: Optional[ScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationalScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationalScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .scope_type import ScopeType

        from .scope_type import ScopeType

        fields: dict[str, Callable[[Any], None]] = {
            "deviceGroups": lambda n : setattr(self, 'device_groups', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scopeNames": lambda n : setattr(self, 'scope_names', n.get_collection_of_primitive_values(str)),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_enum_value(ScopeType)),
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
        writer.write_collection_of_primitive_values("deviceGroups", self.device_groups)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("scopeNames", self.scope_names)
        writer.write_enum_value("scopeType", self.scope_type)
        writer.write_additional_data_value(self.additional_data)
    

