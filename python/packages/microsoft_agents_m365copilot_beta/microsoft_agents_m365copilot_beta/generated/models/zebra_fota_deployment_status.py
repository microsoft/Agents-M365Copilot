from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .zebra_fota_deployment_state import ZebraFotaDeploymentState
    from .zebra_fota_error_code import ZebraFotaErrorCode

@dataclass
class ZebraFotaDeploymentStatus(AdditionalDataHolder, Parsable):
    """
    Describes the status for a single FOTA deployment.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A boolean that indicates if a cancellation was requested on the deployment. NOTE: A cancellation request does not guarantee that the deployment was canceled.
    cancel_requested: Optional[bool] = None
    # The date and time when this deployment was completed or canceled. The actual date time is determined by the value of state. If the state is canceled, this property holds the cancellation date/time. If the the state is completed, this property holds the completion date/time. If the deployment is not completed before the deployment end date, then completed date/time and end date/time are the same. This is always in the deployment timezone. Note: An installation that is in progress can continue past the deployment end date.
    complete_or_canceled_date_time: Optional[datetime.datetime] = None
    # An error code indicating the failure reason, when the deployment state is createFailed. Possible values: See zebraFotaErrorCode enum.
    error_code: Optional[ZebraFotaErrorCode] = None
    #  Date and time when the deployment status was updated from Zebra
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the state of Zebra FOTA deployment.
    state: Optional[ZebraFotaDeploymentState] = None
    # An integer that indicates the total number of devices where installation was successful.
    total_awaiting_install: Optional[int] = None
    # An integer that indicates the total number of devices where installation was canceled.
    total_canceled: Optional[int] = None
    # An integer that indicates the total number of devices that have a job in the CREATED state. Typically indicates jobs that did not reach the devices. 
    total_created: Optional[int] = None
    # An integer that indicates the total number of devices in the deployment.
    total_devices: Optional[int] = None
    # An integer that indicates the total number of devices where installation was successful.
    total_downloading: Optional[int] = None
    # An integer that indicates the total number of devices that have failed to download the new OS file.
    total_failed_download: Optional[int] = None
    # An integer that indicates the total number of devices that have failed to install the new OS file.
    total_failed_install: Optional[int] = None
    # An integer that indicates the total number of devices that received the json and are scheduled. 
    total_scheduled: Optional[int] = None
    # An integer that indicates the total number of devices where installation was successful.
    total_succeeded_install: Optional[int] = None
    # An integer that indicates the total number of devices where no deployment status or end state has not received, even after the scheduled end date was reached.
    total_unknown: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ZebraFotaDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeploymentStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ZebraFotaDeploymentStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .zebra_fota_deployment_state import ZebraFotaDeploymentState
        from .zebra_fota_error_code import ZebraFotaErrorCode

        from .zebra_fota_deployment_state import ZebraFotaDeploymentState
        from .zebra_fota_error_code import ZebraFotaErrorCode

        fields: dict[str, Callable[[Any], None]] = {
            "cancelRequested": lambda n : setattr(self, 'cancel_requested', n.get_bool_value()),
            "completeOrCanceledDateTime": lambda n : setattr(self, 'complete_or_canceled_date_time', n.get_datetime_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(ZebraFotaErrorCode)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ZebraFotaDeploymentState)),
            "totalAwaitingInstall": lambda n : setattr(self, 'total_awaiting_install', n.get_int_value()),
            "totalCanceled": lambda n : setattr(self, 'total_canceled', n.get_int_value()),
            "totalCreated": lambda n : setattr(self, 'total_created', n.get_int_value()),
            "totalDevices": lambda n : setattr(self, 'total_devices', n.get_int_value()),
            "totalDownloading": lambda n : setattr(self, 'total_downloading', n.get_int_value()),
            "totalFailedDownload": lambda n : setattr(self, 'total_failed_download', n.get_int_value()),
            "totalFailedInstall": lambda n : setattr(self, 'total_failed_install', n.get_int_value()),
            "totalScheduled": lambda n : setattr(self, 'total_scheduled', n.get_int_value()),
            "totalSucceededInstall": lambda n : setattr(self, 'total_succeeded_install', n.get_int_value()),
            "totalUnknown": lambda n : setattr(self, 'total_unknown', n.get_int_value()),
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
        writer.write_bool_value("cancelRequested", self.cancel_requested)
        writer.write_datetime_value("completeOrCanceledDateTime", self.complete_or_canceled_date_time)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_int_value("totalAwaitingInstall", self.total_awaiting_install)
        writer.write_int_value("totalCanceled", self.total_canceled)
        writer.write_int_value("totalCreated", self.total_created)
        writer.write_int_value("totalDevices", self.total_devices)
        writer.write_int_value("totalDownloading", self.total_downloading)
        writer.write_int_value("totalFailedDownload", self.total_failed_download)
        writer.write_int_value("totalFailedInstall", self.total_failed_install)
        writer.write_int_value("totalScheduled", self.total_scheduled)
        writer.write_int_value("totalSucceededInstall", self.total_succeeded_install)
        writer.write_int_value("totalUnknown", self.total_unknown)
        writer.write_additional_data_value(self.additional_data)
    

