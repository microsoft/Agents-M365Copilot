from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privilege_management_elevation_type import PrivilegeManagementElevationType
    from .privilege_management_end_user_type import PrivilegeManagementEndUserType
    from .privilege_management_process_type import PrivilegeManagementProcessType

from .entity import Entity

@dataclass
class PrivilegeManagementElevation(Entity, Parsable):
    """
    The endpoint privilege management elevation result entity representing a single elevation action on a client device.
    """
    # The certificate payload of the application. This is computed by hashing the certificate information on the client. Example: 32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a50
    certificate_payload: Optional[str] = None
    # The company name of the application. This value is set by the creator of the application. Example: Microsoft Corporation
    company_name: Optional[str] = None
    # The Intune deviceId. Unique identifier for the managed device. Example: 92ce5047-9553-4731-817f-9b401a999a1b
    device_id: Optional[str] = None
    # The name associated with the device in the intune database. Example: JOHNDOE-LAPTOP.
    device_name: Optional[str] = None
    # Indicates the type of elevation occured
    elevation_type: Optional[PrivilegeManagementElevationType] = None
    # The date and time when the application was elevated. Example:2014-01-01T00:00:00Z
    event_date_time: Optional[datetime.datetime] = None
    # The file description of the application. This value is set by the creator of the application. Example: Editor of multiple coding languages.
    file_description: Optional[str] = None
    # The full file path of the application including the filename and file extension. Example: C:/Program Files/vscode.exe
    file_path: Optional[str] = None
    # The version of the application. This value is set by the creator of the application. Example: 6.2211.1035.1000
    file_version: Optional[str] = None
    # The sha256 hash of the application. Example: 32c220482c68413fbf8290e3b1e49b0a85901cfcd62ab0738760568a2a6e8a57
    hash: Optional[str] = None
    # The internal name of the application. This value is set by the creator of the application. Example: VS code
    internal_name: Optional[str] = None
    # The justification to elevate the application. This is an input by the user when the privilegeManagementElevationType is of type userConfirmedElevation or support approved elevation. This will be null in all other scenarios. The length is capped at 256 char, enforced on the client side. Example: To install debug tool..
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of parent process associated with the elevated process. This is always populated for both parent and child process types
    parent_process_name: Optional[str] = None
    # Unique Identifier of the policy configured to run the application with elevated access
    policy_id: Optional[str] = None
    # The name of the policy configured to run the application in elevated access
    policy_name: Optional[str] = None
    # Indicates the type of elevated process
    process_type: Optional[PrivilegeManagementProcessType] = None
    # The product name of the application. This value is set by the creator of the application. Example: Visual Studio
    product_name: Optional[str] = None
    # The result of the elevation action with 0 being success, and everything else being exit code if the elevation was unsuccessful. The value will always be 0 on all unmanaged elevation. Example: 0. Valid values 0 to 2147483647
    result: Optional[int] = None
    # Unique identifier of the rule configured to run the application with elevated access
    rule_id: Optional[str] = None
    # To identify if the elevation is initiated by system or user interaction
    system_initiated_elevation: Optional[bool] = None
    # The User Principal Name of the user who performed the elevation. Example: john@domain.com
    upn: Optional[str] = None
    # The type of user account on Windows that was used to performed the elevation.
    user_type: Optional[PrivilegeManagementEndUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegeManagementElevation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegeManagementElevation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegeManagementElevation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privilege_management_elevation_type import PrivilegeManagementElevationType
        from .privilege_management_end_user_type import PrivilegeManagementEndUserType
        from .privilege_management_process_type import PrivilegeManagementProcessType

        from .entity import Entity
        from .privilege_management_elevation_type import PrivilegeManagementElevationType
        from .privilege_management_end_user_type import PrivilegeManagementEndUserType
        from .privilege_management_process_type import PrivilegeManagementProcessType

        fields: dict[str, Callable[[Any], None]] = {
            "certificatePayload": lambda n : setattr(self, 'certificate_payload', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "elevationType": lambda n : setattr(self, 'elevation_type', n.get_enum_value(PrivilegeManagementElevationType)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "fileDescription": lambda n : setattr(self, 'file_description', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "fileVersion": lambda n : setattr(self, 'file_version', n.get_str_value()),
            "hash": lambda n : setattr(self, 'hash', n.get_str_value()),
            "internalName": lambda n : setattr(self, 'internal_name', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "parentProcessName": lambda n : setattr(self, 'parent_process_name', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "processType": lambda n : setattr(self, 'process_type', n.get_enum_value(PrivilegeManagementProcessType)),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_int_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_str_value()),
            "systemInitiatedElevation": lambda n : setattr(self, 'system_initiated_elevation', n.get_bool_value()),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(PrivilegeManagementEndUserType)),
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
        writer.write_str_value("certificatePayload", self.certificate_payload)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("elevationType", self.elevation_type)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("fileDescription", self.file_description)
        writer.write_str_value("filePath", self.file_path)
        writer.write_str_value("fileVersion", self.file_version)
        writer.write_str_value("hash", self.hash)
        writer.write_str_value("internalName", self.internal_name)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("parentProcessName", self.parent_process_name)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_enum_value("processType", self.process_type)
        writer.write_str_value("productName", self.product_name)
        writer.write_int_value("result", self.result)
        writer.write_str_value("ruleId", self.rule_id)
        writer.write_bool_value("systemInitiatedElevation", self.system_initiated_elevation)
        writer.write_str_value("upn", self.upn)
        writer.write_enum_value("userType", self.user_type)
    

