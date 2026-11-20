from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase

from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase

@dataclass
class AndroidDeviceComplianceLocalActionLockDeviceWithPasscode(AndroidDeviceComplianceLocalActionBase, Parsable):
    """
    Local Action Lock Device with Passcode Configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode"
    # Passcode to reset to Android device. This property is read-only.
    passcode: Optional[str] = None
    # Number of sign in failures before wiping device, the value can be 4-11. Valid values 4 to 11
    passcode_sign_in_failure_count_before_wipe: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceComplianceLocalActionLockDeviceWithPasscode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceComplianceLocalActionLockDeviceWithPasscode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceComplianceLocalActionLockDeviceWithPasscode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase

        from .android_device_compliance_local_action_base import AndroidDeviceComplianceLocalActionBase

        fields: dict[str, Callable[[Any], None]] = {
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
            "passcodeSignInFailureCountBeforeWipe": lambda n : setattr(self, 'passcode_sign_in_failure_count_before_wipe', n.get_int_value()),
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
        writer.write_int_value("passcodeSignInFailureCountBeforeWipe", self.passcode_sign_in_failure_count_before_wipe)
    

