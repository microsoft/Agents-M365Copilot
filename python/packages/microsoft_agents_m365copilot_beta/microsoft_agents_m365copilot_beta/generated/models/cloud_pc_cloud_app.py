from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_cloud_app_action_failed_error_code import CloudPcCloudAppActionFailedErrorCode
    from .cloud_pc_cloud_app_detail import CloudPcCloudAppDetail
    from .cloud_pc_cloud_app_status import CloudPcCloudAppStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcCloudApp(Entity, Parsable):
    # The error code if publishing, unpublishing, or resetting a cloud app fails. The possible values are: cloudAppQuotaExceeded, cloudPcLicenseNotFound, internalServerError, appDiscoveryFailed, unknownFutureValue, iconPathInvalid, filePathInvalid. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: iconPathInvalid, filePathInvalid. The default value is null. Supports $filter, $select, $orderBy. Read-only.
    action_failed_error_code: Optional[CloudPcCloudAppActionFailedErrorCode] = None
    # The error message when the IT admin failed to publish, unpublish, update, or reset a cloud app. For example: 'Publish failed because it exceeds the 500 cloud apps limitation under the policy. You need to unpublish some cloud apps under this policy in order to publish this cloud app again.' Read-only.
    action_failed_error_message: Optional[str] = None
    # The date and time when the cloud app was added to this tenant and became visible in the admin portal. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. An IT admin can't set or modify it. Supports $filter, $select, and $orderBy. Read-only.
    added_date_time: Optional[datetime.datetime] = None
    # The appDetail property
    app_detail: Optional[CloudPcCloudAppDetail] = None
    # The appStatus property
    app_status: Optional[CloudPcCloudAppStatus] = None
    # Indicates whether this cloud app is available to end users through the end-user portal or the Windows App. The default value is false. It changes to true if the cloud app is successfully published, and reverts to false when the admin unpublishes the cloud app. Supports $filter, $select, and $orderBy.
    available_to_user: Optional[bool] = None
    # The description associated with the cloud app. The maximum allowed length for this property is 512 characters. Supports $filter, $select, and $orderBy.
    description: Optional[str] = None
    # Name of the discovered app associated with the cloud app. For example, Paint, Supports $filter, $select, and $orderBy. Read-only.
    discovered_app_name: Optional[str] = None
    # The display name for the cloud app. The display name for the cloud app, which appears on the end-user portal and must be unique within a single provisioning policy. It uses the discovered app name as the default value. The maximum allowed length for this property is 64 characters. For example, Paint. Supports $filter, $select, and $orderBy.
    display_name: Optional[str] = None
    # The latest date time when the admin published the cloud app. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. An IT admin can't set or modify it. Supports $filter, $select, and $orderBy. Read-only.
    last_published_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the provisioning policy associated with this cloud app. For example, 96133506-c05b-4dbb-a150-ed4adc59895f. Supports $filter, $select, and $orderBy. Required.
    provisioning_policy_id: Optional[str] = None
    # The list of scope tag IDs for this cloud app. Inherited from the provisioning policy when the app is created or updated. Read-only.
    scope_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcCloudApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcCloudApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcCloudApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_cloud_app_action_failed_error_code import CloudPcCloudAppActionFailedErrorCode
        from .cloud_pc_cloud_app_detail import CloudPcCloudAppDetail
        from .cloud_pc_cloud_app_status import CloudPcCloudAppStatus
        from .entity import Entity

        from .cloud_pc_cloud_app_action_failed_error_code import CloudPcCloudAppActionFailedErrorCode
        from .cloud_pc_cloud_app_detail import CloudPcCloudAppDetail
        from .cloud_pc_cloud_app_status import CloudPcCloudAppStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "actionFailedErrorCode": lambda n : setattr(self, 'action_failed_error_code', n.get_enum_value(CloudPcCloudAppActionFailedErrorCode)),
            "actionFailedErrorMessage": lambda n : setattr(self, 'action_failed_error_message', n.get_str_value()),
            "addedDateTime": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "appDetail": lambda n : setattr(self, 'app_detail', n.get_object_value(CloudPcCloudAppDetail)),
            "appStatus": lambda n : setattr(self, 'app_status', n.get_enum_value(CloudPcCloudAppStatus)),
            "availableToUser": lambda n : setattr(self, 'available_to_user', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoveredAppName": lambda n : setattr(self, 'discovered_app_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastPublishedDateTime": lambda n : setattr(self, 'last_published_date_time', n.get_datetime_value()),
            "provisioningPolicyId": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "scopeIds": lambda n : setattr(self, 'scope_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("actionFailedErrorCode", self.action_failed_error_code)
        writer.write_str_value("actionFailedErrorMessage", self.action_failed_error_message)
        writer.write_datetime_value("addedDateTime", self.added_date_time)
        writer.write_object_value("appDetail", self.app_detail)
        writer.write_enum_value("appStatus", self.app_status)
        writer.write_bool_value("availableToUser", self.available_to_user)
        writer.write_str_value("description", self.description)
        writer.write_str_value("discoveredAppName", self.discovered_app_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastPublishedDateTime", self.last_published_date_time)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_collection_of_primitive_values("scopeIds", self.scope_ids)
    

