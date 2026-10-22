from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class CreationInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identity of the user (or application) that created the entity.
    created_by: Optional[IdentitySet] = None
    # Date and time the entity was created.
    created_date_time: Optional[datetime.datetime] = None
    # Identifier of the entity in an external system, if it originated outside Planner.
    external_id: Optional[str] = None
    # URL of the entity in the external system, if applicable.
    external_url: Optional[str] = None
    # Version of the entity in the external system, if applicable.
    external_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier of the scenario or workflow that created the entity.
    scenario_id: Optional[str] = None
    # Scope the entity was created in.
    scope: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreationInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreationInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "externalUrl": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "externalVersion": lambda n : setattr(self, 'external_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scenarioId": lambda n : setattr(self, 'scenario_id', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("externalVersion", self.external_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("scenarioId", self.scenario_id)
        writer.write_str_value("scope", self.scope)
        writer.write_additional_data_value(self.additional_data)
    

