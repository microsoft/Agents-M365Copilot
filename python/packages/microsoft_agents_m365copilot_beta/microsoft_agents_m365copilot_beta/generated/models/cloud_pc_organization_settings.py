from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_operating_system import CloudPcOperatingSystem
    from .cloud_pc_user_account_type import CloudPcUserAccountType
    from .cloud_pc_windows_settings import CloudPcWindowsSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcOrganizationSettings(Entity, Parsable):
    # Specifies whether new Cloud PCs will be automatically enrolled in Microsoft Endpoint Manager (MEM). The default value is false.
    enable_m_e_m_auto_enroll: Optional[bool] = None
    # True if the provisioned Cloud PC can be accessed by single sign-on. False indicates that the provisioned Cloud PC doesn't support this feature. Default value is false. Windows 365 users can use single sign-on to authenticate to Microsoft Entra ID with passwordless options (for example, FIDO keys) to access their Cloud PC. Optional.
    enable_single_sign_on: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The version of the operating system (OS) to provision on Cloud PCs. The possible values are: windows10, windows11, unknownFutureValue.
    os_version: Optional[CloudPcOperatingSystem] = None
    # The account type of the user on provisioned Cloud PCs. The possible values are: standardUser, administrator, unknownFutureValue.
    user_account_type: Optional[CloudPcUserAccountType] = None
    # Represents the Cloud PC organization settings for a tenant. A tenant has only one cloudPcOrganizationSettings object. The default language value en-US.
    windows_settings: Optional[CloudPcWindowsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcOrganizationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOrganizationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOrganizationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_operating_system import CloudPcOperatingSystem
        from .cloud_pc_user_account_type import CloudPcUserAccountType
        from .cloud_pc_windows_settings import CloudPcWindowsSettings
        from .entity import Entity

        from .cloud_pc_operating_system import CloudPcOperatingSystem
        from .cloud_pc_user_account_type import CloudPcUserAccountType
        from .cloud_pc_windows_settings import CloudPcWindowsSettings
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "enableMEMAutoEnroll": lambda n : setattr(self, 'enable_m_e_m_auto_enroll', n.get_bool_value()),
            "enableSingleSignOn": lambda n : setattr(self, 'enable_single_sign_on', n.get_bool_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_enum_value(CloudPcOperatingSystem)),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(CloudPcUserAccountType)),
            "windowsSettings": lambda n : setattr(self, 'windows_settings', n.get_object_value(CloudPcWindowsSettings)),
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
        writer.write_bool_value("enableMEMAutoEnroll", self.enable_m_e_m_auto_enroll)
        writer.write_bool_value("enableSingleSignOn", self.enable_single_sign_on)
        writer.write_enum_value("osVersion", self.os_version)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_object_value("windowsSettings", self.windows_settings)
    

