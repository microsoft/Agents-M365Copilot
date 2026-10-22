from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert import Alert
    from .entity_definition_input import EntityDefinitionInput

from .alert import Alert

@dataclass
class ManualAlert(Alert, Parsable):
    # The entities associated with the alert. Each item specifies a security entity (such as a user, device, or IP address), its identifier, and its role in the alert context.
    entity_definitions: Optional[list[EntityDefinitionInput]] = None
    # When true, excludes the alert from automatic correlation. Default is false.
    is_excluded_from_correlation: Optional[bool] = None
    # ID of an existing incident to link to. If not provided, a new incident is created automatically.
    link_to_incident: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Sentinel workspace identifier for workspace routing.
    sentinel_workspace: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManualAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManualAlert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManualAlert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert import Alert
        from .entity_definition_input import EntityDefinitionInput

        from .alert import Alert
        from .entity_definition_input import EntityDefinitionInput

        fields: dict[str, Callable[[Any], None]] = {
            "entityDefinitions": lambda n : setattr(self, 'entity_definitions', n.get_collection_of_object_values(EntityDefinitionInput)),
            "isExcludedFromCorrelation": lambda n : setattr(self, 'is_excluded_from_correlation', n.get_bool_value()),
            "linkToIncident": lambda n : setattr(self, 'link_to_incident', n.get_int_value()),
            "sentinelWorkspace": lambda n : setattr(self, 'sentinel_workspace', n.get_str_value()),
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
        writer.write_collection_of_object_values("entityDefinitions", self.entity_definitions)
        writer.write_bool_value("isExcludedFromCorrelation", self.is_excluded_from_correlation)
        writer.write_int_value("linkToIncident", self.link_to_incident)
        writer.write_str_value("sentinelWorkspace", self.sentinel_workspace)
    

