from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app import MobileApp
    from .resultant_app_state import ResultantAppState
    from .resultant_app_state_detail import ResultantAppStateDetail

from .entity import Entity

@dataclass
class MobileAppInstallStatus(Entity, Parsable):
    """
    Contains properties for the installation state of a mobile app for a device. This will be deprecated starting May, 2023 (Intune Release 2305).
    """
    # The navigation link to the mobile app.
    app: Optional[MobileApp] = None
    # Device ID
    device_id: Optional[str] = None
    # Device name
    device_name: Optional[str] = None
    # Human readable version of the application
    display_version: Optional[str] = None
    # The error code for install or uninstall failures.
    error_code: Optional[int] = None
    # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
    install_state: Optional[ResultantAppState] = None
    # Enum indicating additional details regarding why an application has a particular install state.
    install_state_detail: Optional[ResultantAppStateDetail] = None
    # Last sync date time
    last_sync_date_time: Optional[datetime.datetime] = None
    # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
    mobile_app_install_status_value: Optional[ResultantAppState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # OS Description
    os_description: Optional[str] = None
    # OS Version
    os_version: Optional[str] = None
    # Device User Name
    user_name: Optional[str] = None
    # User Principal Name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppInstallStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppInstallStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppInstallStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app import MobileApp
        from .resultant_app_state import ResultantAppState
        from .resultant_app_state_detail import ResultantAppStateDetail

        from .entity import Entity
        from .mobile_app import MobileApp
        from .resultant_app_state import ResultantAppState
        from .resultant_app_state_detail import ResultantAppStateDetail

        fields: dict[str, Callable[[Any], None]] = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(MobileApp)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "displayVersion": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "installState": lambda n : setattr(self, 'install_state', n.get_enum_value(ResultantAppState)),
            "installStateDetail": lambda n : setattr(self, 'install_state_detail', n.get_enum_value(ResultantAppStateDetail)),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "mobileAppInstallStatusValue": lambda n : setattr(self, 'mobile_app_install_status_value', n.get_enum_value(ResultantAppState)),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_object_value("app", self.app)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_enum_value("installState", self.install_state)
        writer.write_enum_value("installStateDetail", self.install_state_detail)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("mobileAppInstallStatusValue", self.mobile_app_install_status_value)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

