from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class Windows10EnrollmentCompletionPageConfiguration(DeviceEnrollmentConfiguration, Parsable):
    """
    Windows 10 Enrollment Status Page Configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration"
    # When TRUE, allows device reset on installation failure. When false, reset is blocked. The default is false.
    allow_device_reset_on_install_failure: Optional[bool] = None
    # When TRUE, allows the user to continue using the device on installation failure. When false, blocks the user on installation failure. The default is false.
    allow_device_use_on_install_failure: Optional[bool] = None
    # When TRUE, allows log collection on installation failure. When false, log collection is not allowed. The default is false.
    allow_log_collection_on_install_failure: Optional[bool] = None
    # When TRUE, ESP (Enrollment Status Page) installs all required apps targeted during technician phase and ignores any failures for non-blocking apps. When FALSE, ESP fails on any error during app install. The default is false.
    allow_non_blocking_app_installation: Optional[bool] = None
    # When TRUE, blocks user from retrying the setup on installation failure. When false, user is allowed to retry. The default is false.
    block_device_setup_retry_by_user: Optional[bool] = None
    # The custom error message to show upon installation failure. Max length is 10000. example: 'Setup could not be completed. Please try again or contact your support person for help.'
    custom_error_message: Optional[str] = None
    # When TRUE, disables showing installation progress for first user post enrollment. When false, enables showing progress. The default is false.
    disable_user_status_tracking_after_first_user: Optional[bool] = None
    # The installation progress timeout in minutes. Default is 60 minutes.
    install_progress_timeout_in_minutes: Optional[int] = None
    # Allows quality updates installation during OOBE
    install_quality_updates: Optional[bool] = None
    # Selected applications to track the installation status. It is in the form of an array of GUIDs.
    selected_mobile_app_ids: Optional[list[str]] = None
    # When TRUE, shows installation progress to user. When false, hides installation progress. The default is false.
    show_installation_progress: Optional[bool] = None
    # When TRUE, installation progress is tracked for only Autopilot enrollment scenarios. When false, other scenarios are tracked as well. The default is false.
    track_install_progress_for_autopilot_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10EnrollmentCompletionPageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EnrollmentCompletionPageConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10EnrollmentCompletionPageConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "allowDeviceResetOnInstallFailure": lambda n : setattr(self, 'allow_device_reset_on_install_failure', n.get_bool_value()),
            "allowDeviceUseOnInstallFailure": lambda n : setattr(self, 'allow_device_use_on_install_failure', n.get_bool_value()),
            "allowLogCollectionOnInstallFailure": lambda n : setattr(self, 'allow_log_collection_on_install_failure', n.get_bool_value()),
            "allowNonBlockingAppInstallation": lambda n : setattr(self, 'allow_non_blocking_app_installation', n.get_bool_value()),
            "blockDeviceSetupRetryByUser": lambda n : setattr(self, 'block_device_setup_retry_by_user', n.get_bool_value()),
            "customErrorMessage": lambda n : setattr(self, 'custom_error_message', n.get_str_value()),
            "disableUserStatusTrackingAfterFirstUser": lambda n : setattr(self, 'disable_user_status_tracking_after_first_user', n.get_bool_value()),
            "installProgressTimeoutInMinutes": lambda n : setattr(self, 'install_progress_timeout_in_minutes', n.get_int_value()),
            "installQualityUpdates": lambda n : setattr(self, 'install_quality_updates', n.get_bool_value()),
            "selectedMobileAppIds": lambda n : setattr(self, 'selected_mobile_app_ids', n.get_collection_of_primitive_values(str)),
            "showInstallationProgress": lambda n : setattr(self, 'show_installation_progress', n.get_bool_value()),
            "trackInstallProgressForAutopilotOnly": lambda n : setattr(self, 'track_install_progress_for_autopilot_only', n.get_bool_value()),
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
        writer.write_bool_value("allowDeviceResetOnInstallFailure", self.allow_device_reset_on_install_failure)
        writer.write_bool_value("allowDeviceUseOnInstallFailure", self.allow_device_use_on_install_failure)
        writer.write_bool_value("allowLogCollectionOnInstallFailure", self.allow_log_collection_on_install_failure)
        writer.write_bool_value("allowNonBlockingAppInstallation", self.allow_non_blocking_app_installation)
        writer.write_bool_value("blockDeviceSetupRetryByUser", self.block_device_setup_retry_by_user)
        writer.write_str_value("customErrorMessage", self.custom_error_message)
        writer.write_bool_value("disableUserStatusTrackingAfterFirstUser", self.disable_user_status_tracking_after_first_user)
        writer.write_int_value("installProgressTimeoutInMinutes", self.install_progress_timeout_in_minutes)
        writer.write_bool_value("installQualityUpdates", self.install_quality_updates)
        writer.write_collection_of_primitive_values("selectedMobileAppIds", self.selected_mobile_app_ids)
        writer.write_bool_value("showInstallationProgress", self.show_installation_progress)
        writer.write_bool_value("trackInstallProgressForAutopilotOnly", self.track_install_progress_for_autopilot_only)
    

