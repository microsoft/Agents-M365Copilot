from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .investigation_input_type import InvestigationInputType

from .entity import Entity

@dataclass
class PlaybookDefinition(Entity, Parsable):
    """
    A predefined playbook available to the caller. id is a service-generated, persisted GUID string; uniqueName preserves its backend catalog name. Sessions reference this first-class catalog entity through playbookDefinition@odata.bind.
    """
    # The input kinds accepted by this playbook. The possible values are: defenderIncidentId, defenderAlertId, defenderThreatIntelligenceId, azureSubscriptionId, azureIdentityId, keyword, unknownFutureValue. unknownFutureValue isn't a valid value when creating a session. Read-only.
    accepted_input_types: Optional[list[InvestigationInputType]] = None
    # The description of the work performed by the playbook. Read-only.
    description: Optional[str] = None
    # The human-readable name of the playbook. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The immutable, unique catalog name, such as investigate-incident. Distinct from id. Alternate-key addressing isn't supported. Read-only.
    unique_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlaybookDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlaybookDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlaybookDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .investigation_input_type import InvestigationInputType

        from .entity import Entity
        from .investigation_input_type import InvestigationInputType

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedInputTypes": lambda n : setattr(self, 'accepted_input_types', n.get_collection_of_enum_values(InvestigationInputType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
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
        writer.write_str_value("uniqueName", self.unique_name)
    

