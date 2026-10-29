from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class EndpointMetaDataInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The application property
    application: Optional[str] = None
    # The applicationSourceExecutableName property
    application_source_executable_name: Optional[str] = None
    # The destinationLocationType property
    destination_location_type: Optional[str] = None
    # The deviceName property
    device_name: Optional[str] = None
    # The dlpAuditEventMetadata property
    dlp_audit_event_metadata: Optional[str] = None
    # The endpointOperation property
    endpoint_operation: Optional[str] = None
    # The enforcementMode property
    enforcement_mode: Optional[str] = None
    # The fileExtension property
    file_extension: Optional[str] = None
    # The fileSize property
    file_size: Optional[int] = None
    # The fileType property
    file_type: Optional[str] = None
    # The groupId property
    group_id: Optional[str] = None
    # The groupName property
    group_name: Optional[str] = None
    # The isEaV2Enriched property
    is_ea_v2_enriched: Optional[bool] = None
    # The isHidden property
    is_hidden: Optional[bool] = None
    # The isJitTriggered property
    is_jit_triggered: Optional[bool] = None
    # The isRmseEncrypted property
    is_rmse_encrypted: Optional[bool] = None
    # The isViewableByExternalUsers property
    is_viewable_by_external_users: Optional[bool] = None
    # The justification property
    justification: Optional[str] = None
    # The markOfTheWebData property
    mark_of_the_web_data: Optional[str] = None
    # The mdatpDeviceId property
    mdatp_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The originatingDomain property
    originating_domain: Optional[str] = None
    # The parentArchiveHash property
    parent_archive_hash: Optional[str] = None
    # The platform property
    platform: Optional[str] = None
    # The policyMatchDetails property
    policy_match_details: Optional[list[str]] = None
    # The policyMatchInfo property
    policy_match_info: Optional[str] = None
    # The previousFileName property
    previous_file_name: Optional[str] = None
    # The removableMediaDeviceAttributes property
    removable_media_device_attributes: Optional[str] = None
    # The sensitiveInfoTypeData property
    sensitive_info_type_data: Optional[list[str]] = None
    # The sensitivityLabelEventData property
    sensitivity_label_event_data: Optional[str] = None
    # The sensitivityLabelIds property
    sensitivity_label_ids: Optional[list[str]] = None
    # The sensitivityLabelNames property
    sensitivity_label_names: Optional[list[str]] = None
    # The sha1 property
    sha1: Optional[str] = None
    # The sha256 property
    sha256: Optional[str] = None
    # The sourceLocationType property
    source_location_type: Optional[str] = None
    # The targetDomain property
    target_domain: Optional[str] = None
    # The targetFilePath property
    target_file_path: Optional[str] = None
    # The targetPrinterName property
    target_printer_name: Optional[str] = None
    # The targetUrl property
    target_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndpointMetaDataInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndpointMetaDataInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndpointMetaDataInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_str_value()),
            "applicationSourceExecutableName": lambda n : setattr(self, 'application_source_executable_name', n.get_str_value()),
            "destinationLocationType": lambda n : setattr(self, 'destination_location_type', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "dlpAuditEventMetadata": lambda n : setattr(self, 'dlp_audit_event_metadata', n.get_str_value()),
            "endpointOperation": lambda n : setattr(self, 'endpoint_operation', n.get_str_value()),
            "enforcementMode": lambda n : setattr(self, 'enforcement_mode', n.get_str_value()),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "isEaV2Enriched": lambda n : setattr(self, 'is_ea_v2_enriched', n.get_bool_value()),
            "isHidden": lambda n : setattr(self, 'is_hidden', n.get_bool_value()),
            "isJitTriggered": lambda n : setattr(self, 'is_jit_triggered', n.get_bool_value()),
            "isRmseEncrypted": lambda n : setattr(self, 'is_rmse_encrypted', n.get_bool_value()),
            "isViewableByExternalUsers": lambda n : setattr(self, 'is_viewable_by_external_users', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "markOfTheWebData": lambda n : setattr(self, 'mark_of_the_web_data', n.get_str_value()),
            "mdatpDeviceId": lambda n : setattr(self, 'mdatp_device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "originatingDomain": lambda n : setattr(self, 'originating_domain', n.get_str_value()),
            "parentArchiveHash": lambda n : setattr(self, 'parent_archive_hash', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "policyMatchDetails": lambda n : setattr(self, 'policy_match_details', n.get_collection_of_primitive_values(str)),
            "policyMatchInfo": lambda n : setattr(self, 'policy_match_info', n.get_str_value()),
            "previousFileName": lambda n : setattr(self, 'previous_file_name', n.get_str_value()),
            "removableMediaDeviceAttributes": lambda n : setattr(self, 'removable_media_device_attributes', n.get_str_value()),
            "sensitiveInfoTypeData": lambda n : setattr(self, 'sensitive_info_type_data', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelEventData": lambda n : setattr(self, 'sensitivity_label_event_data', n.get_str_value()),
            "sensitivityLabelIds": lambda n : setattr(self, 'sensitivity_label_ids', n.get_collection_of_primitive_values(str)),
            "sensitivityLabelNames": lambda n : setattr(self, 'sensitivity_label_names', n.get_collection_of_primitive_values(str)),
            "sha1": lambda n : setattr(self, 'sha1', n.get_str_value()),
            "sha256": lambda n : setattr(self, 'sha256', n.get_str_value()),
            "sourceLocationType": lambda n : setattr(self, 'source_location_type', n.get_str_value()),
            "targetDomain": lambda n : setattr(self, 'target_domain', n.get_str_value()),
            "targetFilePath": lambda n : setattr(self, 'target_file_path', n.get_str_value()),
            "targetPrinterName": lambda n : setattr(self, 'target_printer_name', n.get_str_value()),
            "targetUrl": lambda n : setattr(self, 'target_url', n.get_str_value()),
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
        writer.write_str_value("application", self.application)
        writer.write_str_value("applicationSourceExecutableName", self.application_source_executable_name)
        writer.write_str_value("destinationLocationType", self.destination_location_type)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("dlpAuditEventMetadata", self.dlp_audit_event_metadata)
        writer.write_str_value("endpointOperation", self.endpoint_operation)
        writer.write_str_value("enforcementMode", self.enforcement_mode)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("fileType", self.file_type)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("groupName", self.group_name)
        writer.write_bool_value("isEaV2Enriched", self.is_ea_v2_enriched)
        writer.write_bool_value("isHidden", self.is_hidden)
        writer.write_bool_value("isJitTriggered", self.is_jit_triggered)
        writer.write_bool_value("isRmseEncrypted", self.is_rmse_encrypted)
        writer.write_bool_value("isViewableByExternalUsers", self.is_viewable_by_external_users)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("markOfTheWebData", self.mark_of_the_web_data)
        writer.write_str_value("mdatpDeviceId", self.mdatp_device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("originatingDomain", self.originating_domain)
        writer.write_str_value("parentArchiveHash", self.parent_archive_hash)
        writer.write_str_value("platform", self.platform)
        writer.write_collection_of_primitive_values("policyMatchDetails", self.policy_match_details)
        writer.write_str_value("policyMatchInfo", self.policy_match_info)
        writer.write_str_value("previousFileName", self.previous_file_name)
        writer.write_str_value("removableMediaDeviceAttributes", self.removable_media_device_attributes)
        writer.write_collection_of_primitive_values("sensitiveInfoTypeData", self.sensitive_info_type_data)
        writer.write_str_value("sensitivityLabelEventData", self.sensitivity_label_event_data)
        writer.write_collection_of_primitive_values("sensitivityLabelIds", self.sensitivity_label_ids)
        writer.write_collection_of_primitive_values("sensitivityLabelNames", self.sensitivity_label_names)
        writer.write_str_value("sha1", self.sha1)
        writer.write_str_value("sha256", self.sha256)
        writer.write_str_value("sourceLocationType", self.source_location_type)
        writer.write_str_value("targetDomain", self.target_domain)
        writer.write_str_value("targetFilePath", self.target_file_path)
        writer.write_str_value("targetPrinterName", self.target_printer_name)
        writer.write_str_value("targetUrl", self.target_url)
        writer.write_additional_data_value(self.additional_data)
    

