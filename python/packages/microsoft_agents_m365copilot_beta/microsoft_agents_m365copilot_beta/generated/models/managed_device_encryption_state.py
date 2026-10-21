from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .advanced_bit_locker_state import AdvancedBitLockerState
    from .compliance_status import ComplianceStatus
    from .device_types import DeviceTypes
    from .encryption_readiness_state import EncryptionReadinessState
    from .encryption_report_policy_details import EncryptionReportPolicyDetails
    from .encryption_state import EncryptionState
    from .entity import Entity
    from .file_vault_state import FileVaultState

from .entity import Entity

@dataclass
class ManagedDeviceEncryptionState(Entity, Parsable):
    """
    Encryption report per device
    """
    # Advanced BitLocker State. Possible values are: success, noUserConsent, osVolumeUnprotected, osVolumeTpmRequired, osVolumeTpmOnlyRequired, osVolumeTpmPinRequired, osVolumeTpmStartupKeyRequired, osVolumeTpmPinStartupKeyRequired, osVolumeEncryptionMethodMismatch, recoveryKeyBackupFailed, fixedDriveNotEncrypted, fixedDriveEncryptionMethodMismatch, loggedOnUserNonAdmin, windowsRecoveryEnvironmentNotConfigured, tpmNotAvailable, tpmNotReady, networkError.
    advanced_bit_locker_states: Optional[AdvancedBitLockerState] = None
    # Device name
    device_name: Optional[str] = None
    # Device type.
    device_type: Optional[DeviceTypes] = None
    # The encryptionPolicySettingState property
    encryption_policy_setting_state: Optional[ComplianceStatus] = None
    # Encryption readiness state
    encryption_readiness_state: Optional[EncryptionReadinessState] = None
    # Encryption state
    encryption_state: Optional[EncryptionState] = None
    # FileVault State. Possible values are: success, driveEncryptedByUser, userDeferredEncryption, escrowNotEnabled.
    file_vault_states: Optional[FileVaultState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating system version of the device
    os_version: Optional[str] = None
    # Policy Details
    policy_details: Optional[list[EncryptionReportPolicyDetails]] = None
    # Device TPM Version
    tpm_specification_version: Optional[str] = None
    # User name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceEncryptionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceEncryptionState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceEncryptionState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .advanced_bit_locker_state import AdvancedBitLockerState
        from .compliance_status import ComplianceStatus
        from .device_types import DeviceTypes
        from .encryption_readiness_state import EncryptionReadinessState
        from .encryption_report_policy_details import EncryptionReportPolicyDetails
        from .encryption_state import EncryptionState
        from .entity import Entity
        from .file_vault_state import FileVaultState

        from .advanced_bit_locker_state import AdvancedBitLockerState
        from .compliance_status import ComplianceStatus
        from .device_types import DeviceTypes
        from .encryption_readiness_state import EncryptionReadinessState
        from .encryption_report_policy_details import EncryptionReportPolicyDetails
        from .encryption_state import EncryptionState
        from .entity import Entity
        from .file_vault_state import FileVaultState

        fields: dict[str, Callable[[Any], None]] = {
            "advancedBitLockerStates": lambda n : setattr(self, 'advanced_bit_locker_states', n.get_collection_of_enum_values(AdvancedBitLockerState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(DeviceTypes)),
            "encryptionPolicySettingState": lambda n : setattr(self, 'encryption_policy_setting_state', n.get_enum_value(ComplianceStatus)),
            "encryptionReadinessState": lambda n : setattr(self, 'encryption_readiness_state', n.get_enum_value(EncryptionReadinessState)),
            "encryptionState": lambda n : setattr(self, 'encryption_state', n.get_enum_value(EncryptionState)),
            "fileVaultStates": lambda n : setattr(self, 'file_vault_states', n.get_collection_of_enum_values(FileVaultState)),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policyDetails": lambda n : setattr(self, 'policy_details', n.get_collection_of_object_values(EncryptionReportPolicyDetails)),
            "tpmSpecificationVersion": lambda n : setattr(self, 'tpm_specification_version', n.get_str_value()),
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
        writer.write_enum_value("advancedBitLockerStates", self.advanced_bit_locker_states)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_enum_value("encryptionPolicySettingState", self.encryption_policy_setting_state)
        writer.write_enum_value("encryptionReadinessState", self.encryption_readiness_state)
        writer.write_enum_value("encryptionState", self.encryption_state)
        writer.write_enum_value("fileVaultStates", self.file_vault_states)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_collection_of_object_values("policyDetails", self.policy_details)
        writer.write_str_value("tpmSpecificationVersion", self.tpm_specification_version)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

