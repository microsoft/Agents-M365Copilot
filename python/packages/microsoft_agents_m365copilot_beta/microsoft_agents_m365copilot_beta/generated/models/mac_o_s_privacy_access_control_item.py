from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enablement import Enablement
    from .mac_o_s_apple_event_receiver import MacOSAppleEventReceiver
    from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

@dataclass
class MacOSPrivacyAccessControlItem(AdditionalDataHolder, Parsable):
    """
    Represents per-process privacy preferences.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Possible values of a property
    accessibility: Optional[Enablement] = None
    # Possible values of a property
    address_book: Optional[Enablement] = None
    # Allow or deny the app or process to send a restricted Apple event to another app or process. You will need to know the identifier, identifier type, and code requirement of the receiving app or process. This collection can contain a maximum of 500 elements.
    apple_events_allowed_receivers: Optional[list[MacOSAppleEventReceiver]] = None
    # Block access to camera app.
    block_camera: Optional[bool] = None
    # Block the app or process from listening to events from input devices such as mouse, keyboard, and trackpad.Requires macOS 10.15 or later.
    block_listen_event: Optional[bool] = None
    # Block access to microphone.
    block_microphone: Optional[bool] = None
    # Block app from capturing contents of system display. Requires macOS 10.15 or later.
    block_screen_capture: Optional[bool] = None
    # Possible values of a property
    calendar: Optional[Enablement] = None
    # Enter the code requirement, which can be obtained with the command 'codesign –display -r –' in the Terminal app. Include everything after '=>'.
    code_requirement: Optional[str] = None
    # The display name of the app, process, or executable.
    display_name: Optional[str] = None
    # Possible values of a property
    file_provider_presence: Optional[Enablement] = None
    # The bundle ID or path of the app, process, or executable.
    identifier: Optional[str] = None
    # Process identifier types for MacOS Privacy Preferences
    identifier_type: Optional[MacOSProcessIdentifierType] = None
    # Possible values of a property
    media_library: Optional[Enablement] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Possible values of a property
    photos: Optional[Enablement] = None
    # Possible values of a property
    post_event: Optional[Enablement] = None
    # Possible values of a property
    reminders: Optional[Enablement] = None
    # Possible values of a property
    speech_recognition: Optional[Enablement] = None
    # Statically validates the code requirement. Use this setting if the process invalidates its dynamic code signature.
    static_code_validation: Optional[bool] = None
    # Possible values of a property
    system_policy_all_files: Optional[Enablement] = None
    # Possible values of a property
    system_policy_desktop_folder: Optional[Enablement] = None
    # Possible values of a property
    system_policy_documents_folder: Optional[Enablement] = None
    # Possible values of a property
    system_policy_downloads_folder: Optional[Enablement] = None
    # Possible values of a property
    system_policy_network_volumes: Optional[Enablement] = None
    # Possible values of a property
    system_policy_removable_volumes: Optional[Enablement] = None
    # Possible values of a property
    system_policy_system_admin_files: Optional[Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSPrivacyAccessControlItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSPrivacyAccessControlItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSPrivacyAccessControlItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enablement import Enablement
        from .mac_o_s_apple_event_receiver import MacOSAppleEventReceiver
        from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

        from .enablement import Enablement
        from .mac_o_s_apple_event_receiver import MacOSAppleEventReceiver
        from .mac_o_s_process_identifier_type import MacOSProcessIdentifierType

        fields: dict[str, Callable[[Any], None]] = {
            "accessibility": lambda n : setattr(self, 'accessibility', n.get_enum_value(Enablement)),
            "addressBook": lambda n : setattr(self, 'address_book', n.get_enum_value(Enablement)),
            "appleEventsAllowedReceivers": lambda n : setattr(self, 'apple_events_allowed_receivers', n.get_collection_of_object_values(MacOSAppleEventReceiver)),
            "blockCamera": lambda n : setattr(self, 'block_camera', n.get_bool_value()),
            "blockListenEvent": lambda n : setattr(self, 'block_listen_event', n.get_bool_value()),
            "blockMicrophone": lambda n : setattr(self, 'block_microphone', n.get_bool_value()),
            "blockScreenCapture": lambda n : setattr(self, 'block_screen_capture', n.get_bool_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_enum_value(Enablement)),
            "codeRequirement": lambda n : setattr(self, 'code_requirement', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fileProviderPresence": lambda n : setattr(self, 'file_provider_presence', n.get_enum_value(Enablement)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "identifierType": lambda n : setattr(self, 'identifier_type', n.get_enum_value(MacOSProcessIdentifierType)),
            "mediaLibrary": lambda n : setattr(self, 'media_library', n.get_enum_value(Enablement)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "photos": lambda n : setattr(self, 'photos', n.get_enum_value(Enablement)),
            "postEvent": lambda n : setattr(self, 'post_event', n.get_enum_value(Enablement)),
            "reminders": lambda n : setattr(self, 'reminders', n.get_enum_value(Enablement)),
            "speechRecognition": lambda n : setattr(self, 'speech_recognition', n.get_enum_value(Enablement)),
            "staticCodeValidation": lambda n : setattr(self, 'static_code_validation', n.get_bool_value()),
            "systemPolicyAllFiles": lambda n : setattr(self, 'system_policy_all_files', n.get_enum_value(Enablement)),
            "systemPolicyDesktopFolder": lambda n : setattr(self, 'system_policy_desktop_folder', n.get_enum_value(Enablement)),
            "systemPolicyDocumentsFolder": lambda n : setattr(self, 'system_policy_documents_folder', n.get_enum_value(Enablement)),
            "systemPolicyDownloadsFolder": lambda n : setattr(self, 'system_policy_downloads_folder', n.get_enum_value(Enablement)),
            "systemPolicyNetworkVolumes": lambda n : setattr(self, 'system_policy_network_volumes', n.get_enum_value(Enablement)),
            "systemPolicyRemovableVolumes": lambda n : setattr(self, 'system_policy_removable_volumes', n.get_enum_value(Enablement)),
            "systemPolicySystemAdminFiles": lambda n : setattr(self, 'system_policy_system_admin_files', n.get_enum_value(Enablement)),
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
        writer.write_enum_value("accessibility", self.accessibility)
        writer.write_enum_value("addressBook", self.address_book)
        writer.write_collection_of_object_values("appleEventsAllowedReceivers", self.apple_events_allowed_receivers)
        writer.write_bool_value("blockCamera", self.block_camera)
        writer.write_bool_value("blockListenEvent", self.block_listen_event)
        writer.write_bool_value("blockMicrophone", self.block_microphone)
        writer.write_bool_value("blockScreenCapture", self.block_screen_capture)
        writer.write_enum_value("calendar", self.calendar)
        writer.write_str_value("codeRequirement", self.code_requirement)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("fileProviderPresence", self.file_provider_presence)
        writer.write_str_value("identifier", self.identifier)
        writer.write_enum_value("identifierType", self.identifier_type)
        writer.write_enum_value("mediaLibrary", self.media_library)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("photos", self.photos)
        writer.write_enum_value("postEvent", self.post_event)
        writer.write_enum_value("reminders", self.reminders)
        writer.write_enum_value("speechRecognition", self.speech_recognition)
        writer.write_bool_value("staticCodeValidation", self.static_code_validation)
        writer.write_enum_value("systemPolicyAllFiles", self.system_policy_all_files)
        writer.write_enum_value("systemPolicyDesktopFolder", self.system_policy_desktop_folder)
        writer.write_enum_value("systemPolicyDocumentsFolder", self.system_policy_documents_folder)
        writer.write_enum_value("systemPolicyDownloadsFolder", self.system_policy_downloads_folder)
        writer.write_enum_value("systemPolicyNetworkVolumes", self.system_policy_network_volumes)
        writer.write_enum_value("systemPolicyRemovableVolumes", self.system_policy_removable_volumes)
        writer.write_enum_value("systemPolicySystemAdminFiles", self.system_policy_system_admin_files)
        writer.write_additional_data_value(self.additional_data)
    

