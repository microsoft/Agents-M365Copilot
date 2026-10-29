from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .teamwork_camera_configuration import TeamworkCameraConfiguration
    from .teamwork_device_software_versions import TeamworkDeviceSoftwareVersions
    from .teamwork_display_configuration import TeamworkDisplayConfiguration
    from .teamwork_hardware_configuration import TeamworkHardwareConfiguration
    from .teamwork_microphone_configuration import TeamworkMicrophoneConfiguration
    from .teamwork_speaker_configuration import TeamworkSpeakerConfiguration
    from .teamwork_system_configuration import TeamworkSystemConfiguration
    from .teamwork_teams_client_configuration import TeamworkTeamsClientConfiguration

from .entity import Entity

@dataclass
class TeamworkDeviceConfiguration(Entity, Parsable):
    # The camera configuration. Applicable only for Microsoft Teams Rooms-enabled devices.
    camera_configuration: Optional[TeamworkCameraConfiguration] = None
    # Identity of the user who created the device configuration document.
    created_by: Optional[IdentitySet] = None
    # The UTC date and time when the device configuration document was created.
    created_date_time: Optional[datetime.datetime] = None
    # The display configuration.
    display_configuration: Optional[TeamworkDisplayConfiguration] = None
    # The hardware configuration. Applicable only for Teams Rooms-enabled devices.
    hardware_configuration: Optional[TeamworkHardwareConfiguration] = None
    # Identity of the user who last modified the device configuration.
    last_modified_by: Optional[IdentitySet] = None
    # The UTC date and time when the device configuration was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The microphone configuration. Applicable only for Teams Rooms-enabled devices.
    microphone_configuration: Optional[TeamworkMicrophoneConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information related to software versions for the device, such as firmware, operating system, Teams client, and admin agent.
    software_versions: Optional[TeamworkDeviceSoftwareVersions] = None
    # The speaker configuration. Applicable only for Teams Rooms-enabled devices.
    speaker_configuration: Optional[TeamworkSpeakerConfiguration] = None
    # The system configuration. Not applicable for Teams Rooms-enabled devices.
    system_configuration: Optional[TeamworkSystemConfiguration] = None
    # The Teams client configuration. Applicable only for Teams Rooms-enabled devices.
    teams_client_configuration: Optional[TeamworkTeamsClientConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_camera_configuration import TeamworkCameraConfiguration
        from .teamwork_device_software_versions import TeamworkDeviceSoftwareVersions
        from .teamwork_display_configuration import TeamworkDisplayConfiguration
        from .teamwork_hardware_configuration import TeamworkHardwareConfiguration
        from .teamwork_microphone_configuration import TeamworkMicrophoneConfiguration
        from .teamwork_speaker_configuration import TeamworkSpeakerConfiguration
        from .teamwork_system_configuration import TeamworkSystemConfiguration
        from .teamwork_teams_client_configuration import TeamworkTeamsClientConfiguration

        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_camera_configuration import TeamworkCameraConfiguration
        from .teamwork_device_software_versions import TeamworkDeviceSoftwareVersions
        from .teamwork_display_configuration import TeamworkDisplayConfiguration
        from .teamwork_hardware_configuration import TeamworkHardwareConfiguration
        from .teamwork_microphone_configuration import TeamworkMicrophoneConfiguration
        from .teamwork_speaker_configuration import TeamworkSpeakerConfiguration
        from .teamwork_system_configuration import TeamworkSystemConfiguration
        from .teamwork_teams_client_configuration import TeamworkTeamsClientConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "cameraConfiguration": lambda n : setattr(self, 'camera_configuration', n.get_object_value(TeamworkCameraConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayConfiguration": lambda n : setattr(self, 'display_configuration', n.get_object_value(TeamworkDisplayConfiguration)),
            "hardwareConfiguration": lambda n : setattr(self, 'hardware_configuration', n.get_object_value(TeamworkHardwareConfiguration)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "microphoneConfiguration": lambda n : setattr(self, 'microphone_configuration', n.get_object_value(TeamworkMicrophoneConfiguration)),
            "softwareVersions": lambda n : setattr(self, 'software_versions', n.get_object_value(TeamworkDeviceSoftwareVersions)),
            "speakerConfiguration": lambda n : setattr(self, 'speaker_configuration', n.get_object_value(TeamworkSpeakerConfiguration)),
            "systemConfiguration": lambda n : setattr(self, 'system_configuration', n.get_object_value(TeamworkSystemConfiguration)),
            "teamsClientConfiguration": lambda n : setattr(self, 'teams_client_configuration', n.get_object_value(TeamworkTeamsClientConfiguration)),
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
        writer.write_object_value("cameraConfiguration", self.camera_configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("displayConfiguration", self.display_configuration)
        writer.write_object_value("hardwareConfiguration", self.hardware_configuration)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("microphoneConfiguration", self.microphone_configuration)
        writer.write_object_value("softwareVersions", self.software_versions)
        writer.write_object_value("speakerConfiguration", self.speaker_configuration)
        writer.write_object_value("systemConfiguration", self.system_configuration)
        writer.write_object_value("teamsClientConfiguration", self.teams_client_configuration)
    

