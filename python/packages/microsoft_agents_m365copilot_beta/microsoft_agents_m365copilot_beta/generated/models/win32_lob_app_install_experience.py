from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run_as_account_type import RunAsAccountType
    from .win32_lob_app_in_use_action_type import Win32LobAppInUseActionType
    from .win32_lob_app_restart_behavior import Win32LobAppRestartBehavior

@dataclass
class Win32LobAppInstallExperience(AdditionalDataHolder, Parsable):
    """
    Contains installation experience properties for a Win32 App
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the type of restart action.
    device_restart_behavior: Optional[Win32LobAppRestartBehavior] = None
    # Indicates whether app-in-use detection is enabled before app enforcement, and if enabled, the action to take when the app is detected to be in-use. Null indicates the feature is not enabled. Possible values are: `notEnabled`, `fail`, `terminateWithoutUserInteraction`, `terminateWithUserInteraction`.
    in_use_behavior: Optional[Win32LobAppInUseActionType] = None
    # The number of minutes the system will wait for install program to finish. Default value is 60 minutes.
    max_run_time_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[RunAsAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppInstallExperience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppInstallExperience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppInstallExperience()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .run_as_account_type import RunAsAccountType
        from .win32_lob_app_in_use_action_type import Win32LobAppInUseActionType
        from .win32_lob_app_restart_behavior import Win32LobAppRestartBehavior

        from .run_as_account_type import RunAsAccountType
        from .win32_lob_app_in_use_action_type import Win32LobAppInUseActionType
        from .win32_lob_app_restart_behavior import Win32LobAppRestartBehavior

        fields: dict[str, Callable[[Any], None]] = {
            "deviceRestartBehavior": lambda n : setattr(self, 'device_restart_behavior', n.get_enum_value(Win32LobAppRestartBehavior)),
            "inUseBehavior": lambda n : setattr(self, 'in_use_behavior', n.get_enum_value(Win32LobAppInUseActionType)),
            "maxRunTimeInMinutes": lambda n : setattr(self, 'max_run_time_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(RunAsAccountType)),
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
        writer.write_enum_value("deviceRestartBehavior", self.device_restart_behavior)
        writer.write_enum_value("inUseBehavior", self.in_use_behavior)
        writer.write_int_value("maxRunTimeInMinutes", self.max_run_time_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_additional_data_value(self.additional_data)
    

