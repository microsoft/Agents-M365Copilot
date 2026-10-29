from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class PlannerArchivalInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Read-only. Indicates whether the entity is archived.
    is_archived: Optional[bool] = None
    # Read-only. Reason why the entity was archived or unarchived.
    justification: Optional[str] = None
    # Read-only. Identity of the user who archived or unarchived the entity.
    modified_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which the entity's archive status changed.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Identity of the user who archived or unarchived the entity
    status_changed_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which the entity's archive status changed.
    status_changed_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerArchivalInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerArchivalInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerArchivalInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_object_value(IdentitySet)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "statusChangedBy": lambda n : setattr(self, 'status_changed_by', n.get_object_value(IdentitySet)),
            "statusChangedDateTime": lambda n : setattr(self, 'status_changed_date_time', n.get_datetime_value()),
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
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("statusChangedBy", self.status_changed_by)
        writer.write_datetime_value("statusChangedDateTime", self.status_changed_date_time)
        writer.write_additional_data_value(self.additional_data)
    

