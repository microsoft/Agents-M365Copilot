from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
    from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
    from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

from .entity import Entity

@dataclass
class WindowsDefenderApplicationControlSupplementalPolicy(Entity, Parsable):
    # The associated group assignments for the Windows Defender Application Control Supplemental Policy.
    assignments: Optional[list[WindowsDefenderApplicationControlSupplementalPolicyAssignment]] = None
    # Indicates the content of the Windows Defender Application Control Supplemental Policy in byte array format.
    content: Optional[bytes] = None
    # Indicates the file name associated with the content of the Windows Defender Application Control Supplemental Policy.
    content_file_name: Optional[str] = None
    # Indicates the created date and time when the Windows Defender Application Control Supplemental Policy was uploaded.
    creation_date_time: Optional[datetime.datetime] = None
    # WindowsDefenderApplicationControl supplemental policy deployment summary.
    deploy_summary: Optional[WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary] = None
    # The description of the Windows Defender Application Control Supplemental Policy.
    description: Optional[str] = None
    # The list of device deployment states for this WindowsDefenderApplicationControl supplemental policy.
    device_statuses: Optional[list[WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus]] = None
    # The display name of the Windows Defender Application Control Supplemental Policy.
    display_name: Optional[str] = None
    # Indicates the last modified date and time of the Windows Defender Application Control Supplemental Policy.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for the Windows Defender Application Control Supplemental Policy entity.
    role_scope_tag_ids: Optional[list[str]] = None
    # Indicates the Windows Defender Application Control Supplemental Policy's version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDefenderApplicationControlSupplementalPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderApplicationControlSupplementalPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDefenderApplicationControlSupplementalPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
        from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
        from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

        from .entity import Entity
        from .windows_defender_application_control_supplemental_policy_assignment import WindowsDefenderApplicationControlSupplementalPolicyAssignment
        from .windows_defender_application_control_supplemental_policy_deployment_status import WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
        from .windows_defender_application_control_supplemental_policy_deployment_summary import WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(WindowsDefenderApplicationControlSupplementalPolicyAssignment)),
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "contentFileName": lambda n : setattr(self, 'content_file_name', n.get_str_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "deploySummary": lambda n : setattr(self, 'deploy_summary', n.get_object_value(WindowsDefenderApplicationControlSupplementalPolicyDeploymentSummary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_bytes_value("content", self.content)
        writer.write_str_value("contentFileName", self.content_file_name)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("deploySummary", self.deploy_summary)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_str_value("version", self.version)
    

