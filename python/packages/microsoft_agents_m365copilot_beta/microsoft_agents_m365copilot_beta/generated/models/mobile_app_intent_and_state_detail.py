from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_intent import MobileAppIntent
    from .mobile_app_supported_device_type import MobileAppSupportedDeviceType
    from .resultant_app_state import ResultantAppState

@dataclass
class MobileAppIntentAndStateDetail(AdditionalDataHolder, Parsable):
    """
    Mobile App Intent and Install State for a given device.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # MobieApp identifier.
    application_id: Optional[str] = None
    # The admin provided or imported title of the app.
    display_name: Optional[str] = None
    # Human readable version of the application
    display_version: Optional[str] = None
    # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
    install_state: Optional[ResultantAppState] = None
    # Indicates the status of the mobile app on the device.
    mobile_app_intent: Optional[MobileAppIntent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The supported platforms for the app.
    supported_device_types: Optional[list[MobileAppSupportedDeviceType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppIntentAndStateDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppIntentAndStateDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppIntentAndStateDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_intent import MobileAppIntent
        from .mobile_app_supported_device_type import MobileAppSupportedDeviceType
        from .resultant_app_state import ResultantAppState

        from .mobile_app_intent import MobileAppIntent
        from .mobile_app_supported_device_type import MobileAppSupportedDeviceType
        from .resultant_app_state import ResultantAppState

        fields: dict[str, Callable[[Any], None]] = {
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "displayVersion": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "installState": lambda n : setattr(self, 'install_state', n.get_enum_value(ResultantAppState)),
            "mobileAppIntent": lambda n : setattr(self, 'mobile_app_intent', n.get_enum_value(MobileAppIntent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportedDeviceTypes": lambda n : setattr(self, 'supported_device_types', n.get_collection_of_object_values(MobileAppSupportedDeviceType)),
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
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_enum_value("installState", self.install_state)
        writer.write_enum_value("mobileAppIntent", self.mobile_app_intent)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("supportedDeviceTypes", self.supported_device_types)
        writer.write_additional_data_value(self.additional_data)
    

