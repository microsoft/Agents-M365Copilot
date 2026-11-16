from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment import Assignment
    from .usage_right import UsageRight
    from .waiting_member import WaitingMember

@dataclass
class DeviceCloudLicensing(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignments property
    assignments: Optional[list[Assignment]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The usageRights property
    usage_rights: Optional[list[UsageRight]] = None
    # The waitingMembers property
    waiting_members: Optional[list[WaitingMember]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceCloudLicensing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCloudLicensing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceCloudLicensing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assignment import Assignment
        from .usage_right import UsageRight
        from .waiting_member import WaitingMember

        from .assignment import Assignment
        from .usage_right import UsageRight
        from .waiting_member import WaitingMember

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(Assignment)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "usageRights": lambda n : setattr(self, 'usage_rights', n.get_collection_of_object_values(UsageRight)),
            "waitingMembers": lambda n : setattr(self, 'waiting_members', n.get_collection_of_object_values(WaitingMember)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("usageRights", self.usage_rights)
        writer.write_collection_of_object_values("waitingMembers", self.waiting_members)
        writer.write_additional_data_value(self.additional_data)
    

