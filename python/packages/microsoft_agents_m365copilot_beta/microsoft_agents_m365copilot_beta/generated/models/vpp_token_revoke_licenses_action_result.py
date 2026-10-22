from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vpp_token_action_failure_reason import VppTokenActionFailureReason
    from .vpp_token_action_result import VppTokenActionResult

from .vpp_token_action_result import VppTokenActionResult

@dataclass
class VppTokenRevokeLicensesActionResult(VppTokenActionResult, Parsable):
    """
    The status of the revoke licenses action performed on the Apple Volume Purchase Program token.
    """
    # Possible types of reasons for an Apple Volume Purchase Program token action failure.
    action_failure_reason: Optional[VppTokenActionFailureReason] = None
    # A count of the number of licenses that failed to revoke.
    failed_licenses_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A count of the number of licenses that were attempted to revoke.
    total_licenses_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VppTokenRevokeLicensesActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VppTokenRevokeLicensesActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VppTokenRevokeLicensesActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vpp_token_action_failure_reason import VppTokenActionFailureReason
        from .vpp_token_action_result import VppTokenActionResult

        from .vpp_token_action_failure_reason import VppTokenActionFailureReason
        from .vpp_token_action_result import VppTokenActionResult

        fields: dict[str, Callable[[Any], None]] = {
            "actionFailureReason": lambda n : setattr(self, 'action_failure_reason', n.get_enum_value(VppTokenActionFailureReason)),
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
        writer.write_enum_value("actionFailureReason", self.action_failure_reason)
        writer.write_int_value("failedLicensesCount", self.failed_licenses_count)
        writer.write_int_value("totalLicensesCount", self.total_licenses_count)
    

