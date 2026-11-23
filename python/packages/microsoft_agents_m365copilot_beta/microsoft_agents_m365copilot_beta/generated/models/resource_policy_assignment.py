from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_policy_reference import AssignedPolicyReference
    from .enforcement_mode import EnforcementMode

@dataclass
class ResourcePolicyAssignment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignedPolicy property
    assigned_policy: Optional[AssignedPolicyReference] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The deletedDateTime property
    deleted_date_time: Optional[datetime.datetime] = None
    # The enforcementMode property
    enforcement_mode: Optional[EnforcementMode] = None
    # The isEnabled property
    is_enabled: Optional[bool] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope property
    scope: Optional[str] = None
    # The uniqueName property
    unique_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourcePolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourcePolicyAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourcePolicyAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_policy_reference import AssignedPolicyReference
        from .enforcement_mode import EnforcementMode

        from .assigned_policy_reference import AssignedPolicyReference
        from .enforcement_mode import EnforcementMode

        fields: dict[str, Callable[[Any], None]] = {
            "assignedPolicy": lambda n : setattr(self, 'assigned_policy', n.get_object_value(AssignedPolicyReference)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "enforcementMode": lambda n : setattr(self, 'enforcement_mode', n.get_enum_value(EnforcementMode)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
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
        writer.write_object_value("assignedPolicy", self.assigned_policy)
        writer.write_enum_value("enforcementMode", self.enforcement_mode)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("uniqueName", self.unique_name)
        writer.write_additional_data_value(self.additional_data)
    

