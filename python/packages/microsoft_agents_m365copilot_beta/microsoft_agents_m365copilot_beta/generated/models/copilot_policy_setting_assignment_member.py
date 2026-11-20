from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_policy_setting_directory_object_type import CopilotPolicySettingDirectoryObjectType

@dataclass
class CopilotPolicySettingAssignmentMember(AdditionalDataHolder, Parsable):
    """
    A directory object included in a Copilot policy setting assignment.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the assigned user or group.
    directory_object_id: Optional[str] = None
    # The directory object type of a Copilot policy setting assignment member.
    directory_object_type: Optional[CopilotPolicySettingDirectoryObjectType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPolicySettingAssignmentMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPolicySettingAssignmentMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPolicySettingAssignmentMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_policy_setting_directory_object_type import CopilotPolicySettingDirectoryObjectType

        from .copilot_policy_setting_directory_object_type import CopilotPolicySettingDirectoryObjectType

        fields: dict[str, Callable[[Any], None]] = {
            "directoryObjectId": lambda n : setattr(self, 'directory_object_id', n.get_str_value()),
            "directoryObjectType": lambda n : setattr(self, 'directory_object_type', n.get_enum_value(CopilotPolicySettingDirectoryObjectType)),
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
        writer.write_str_value("directoryObjectId", self.directory_object_id)
        writer.write_enum_value("directoryObjectType", self.directory_object_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

