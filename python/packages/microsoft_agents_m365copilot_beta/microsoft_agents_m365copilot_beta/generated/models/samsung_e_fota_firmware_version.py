from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SamsungEFotaFirmwareVersion(AdditionalDataHolder, Parsable):
    """
    The firmware version from Samsung for a specific device model, sales code, and CSC (Consumer Software Customization). Used to create Samsung E-FOTA deployments.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Android Processor version name. This property is populated by Samsung. Eg. 'G960U1UES9FVD1'. Default value: null. Read-only.
    android_processor_version_name: Optional[str] = None
    # The Consumer Software Customization which is a specific code associated with the region or carrier customization of a Samsung device. This property is populated by Samsung. Eg. 'OYM'. Read-only. Returned by default.
    consumer_software_customization_code: Optional[str] = None
    # The firmware description. This property is populated by Samsung. Default value: null. Read-only.
    description: Optional[str] = None
    # Samsung device model. This property is populated by Samsung. Eg. 'SM-960F'. Read-only. Returned by default.
    device_model_name: Optional[str] = None
    # The firmware version. This property is populated by Samsung Eg. 'T575XXU4EAAA/T575OXM4EAAA/T575XXU4EAAA'. Default value: null. Read-only.
    firmware_version: Optional[str] = None
    # Firmware ID from Samsung. This property is populated by Samsung. Eg. 'FW2022033111797487'. Read-only. Returned by default.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The OS version name. This property is populated by Samsung. Eg. 'Pie(Android 9)'. Default value: null. Read-only.
    os_version_name: Optional[str] = None
    # Firmware release date. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. This property is populated by Samsung. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Default value: null. Read-only.
    release_date_time: Optional[datetime.datetime] = None
    # The firmware request type. This property is populated by Samsung Eg. 'NORMAL'. Default value: null. Read-only.
    request_firmware_type_name: Optional[str] = None
    # Sales code of a Samsung device that corresponds to its georgraphic area or carrier network. This property is populated by Samsung. Eg. 'TMB'. Read-only. Returned by default.
    sales_code: Optional[str] = None
    # The firmware security patch. This property is populated by Samsung Eg. '2023-09-07 07:50:57'. Default value: null. Read-only.
    security_patch_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SamsungEFotaFirmwareVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SamsungEFotaFirmwareVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SamsungEFotaFirmwareVersion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "androidProcessorVersionName": lambda n : setattr(self, 'android_processor_version_name', n.get_str_value()),
            "consumerSoftwareCustomizationCode": lambda n : setattr(self, 'consumer_software_customization_code', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceModelName": lambda n : setattr(self, 'device_model_name', n.get_str_value()),
            "firmwareVersion": lambda n : setattr(self, 'firmware_version', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osVersionName": lambda n : setattr(self, 'os_version_name', n.get_str_value()),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "requestFirmwareTypeName": lambda n : setattr(self, 'request_firmware_type_name', n.get_str_value()),
            "salesCode": lambda n : setattr(self, 'sales_code', n.get_str_value()),
            "securityPatchVersion": lambda n : setattr(self, 'security_patch_version', n.get_str_value()),
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
        writer.write_str_value("androidProcessorVersionName", self.android_processor_version_name)
        writer.write_str_value("consumerSoftwareCustomizationCode", self.consumer_software_customization_code)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceModelName", self.device_model_name)
        writer.write_str_value("firmwareVersion", self.firmware_version)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osVersionName", self.os_version_name)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_str_value("requestFirmwareTypeName", self.request_firmware_type_name)
        writer.write_str_value("salesCode", self.sales_code)
        writer.write_str_value("securityPatchVersion", self.security_patch_version)
        writer.write_additional_data_value(self.additional_data)
    

