from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsEnrollmentStatusScreenSettings(AdditionalDataHolder, Parsable):
    """
    Enrollment status screen setting
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Allow or block user to use device before profile and app installation complete
    allow_device_use_before_profile_and_app_install_complete: Optional[bool] = None
    # Allow the user to continue using the device on installation failure
    allow_device_use_on_install_failure: Optional[bool] = None
    # Allow or block log collection on installation failure
    allow_log_collection_on_install_failure: Optional[bool] = None
    # Allow the user to retry the setup on installation failure
    block_device_setup_retry_by_user: Optional[bool] = None
    # Set custom error message to show upon installation failure
    custom_error_message: Optional[str] = None
    # Show or hide installation progress to user
    hide_installation_progress: Optional[bool] = None
    # Set installation progress timeout in minutes
    install_progress_timeout_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsEnrollmentStatusScreenSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsEnrollmentStatusScreenSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsEnrollmentStatusScreenSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowDeviceUseBeforeProfileAndAppInstallComplete": lambda n : setattr(self, 'allow_device_use_before_profile_and_app_install_complete', n.get_bool_value()),
            "allowDeviceUseOnInstallFailure": lambda n : setattr(self, 'allow_device_use_on_install_failure', n.get_bool_value()),
            "allowLogCollectionOnInstallFailure": lambda n : setattr(self, 'allow_log_collection_on_install_failure', n.get_bool_value()),
            "blockDeviceSetupRetryByUser": lambda n : setattr(self, 'block_device_setup_retry_by_user', n.get_bool_value()),
            "customErrorMessage": lambda n : setattr(self, 'custom_error_message', n.get_str_value()),
            "hideInstallationProgress": lambda n : setattr(self, 'hide_installation_progress', n.get_bool_value()),
            "installProgressTimeoutInMinutes": lambda n : setattr(self, 'install_progress_timeout_in_minutes', n.get_int_value()),
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
        writer.write_bool_value("allowDeviceUseBeforeProfileAndAppInstallComplete", self.allow_device_use_before_profile_and_app_install_complete)
        writer.write_bool_value("allowDeviceUseOnInstallFailure", self.allow_device_use_on_install_failure)
        writer.write_bool_value("allowLogCollectionOnInstallFailure", self.allow_log_collection_on_install_failure)
        writer.write_bool_value("blockDeviceSetupRetryByUser", self.block_device_setup_retry_by_user)
        writer.write_str_value("customErrorMessage", self.custom_error_message)
        writer.write_bool_value("hideInstallationProgress", self.hide_installation_progress)
        writer.write_int_value("installProgressTimeoutInMinutes", self.install_progress_timeout_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

