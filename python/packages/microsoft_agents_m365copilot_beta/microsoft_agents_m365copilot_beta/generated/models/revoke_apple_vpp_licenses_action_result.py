from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_action_result import DeviceActionResult

from .device_action_result import DeviceActionResult

@dataclass
class RevokeAppleVppLicensesActionResult(DeviceActionResult, Parsable):
    """
    Revoke Apple Vpp licenses action result
    """
    # Total number of Apple Vpp licenses that failed to revoke
    failed_licenses_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total number of Apple Vpp licenses associated
    total_licenses_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RevokeAppleVppLicensesActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RevokeAppleVppLicensesActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RevokeAppleVppLicensesActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_action_result import DeviceActionResult

        from .device_action_result import DeviceActionResult

        fields: dict[str, Callable[[Any], None]] = {
            "failedLicensesCount": lambda n : setattr(self, 'failed_licenses_count', n.get_int_value()),
            "totalLicensesCount": lambda n : setattr(self, 'total_licenses_count', n.get_int_value()),
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
        writer.write_int_value("failedLicensesCount", self.failed_licenses_count)
        writer.write_int_value("totalLicensesCount", self.total_licenses_count)
    

