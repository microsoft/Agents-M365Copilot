from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .control_configuration import ControlConfiguration
    from .purview_insider_risk_management_level import PurviewInsiderRiskManagementLevel

from .control_configuration import ControlConfiguration

@dataclass
class InsiderRiskyUserApproval(ControlConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.insiderRiskyUserApproval"
    # Indicates whether approval is required for risky users.
    is_approval_required: Optional[bool] = None
    # The minimumRiskLevel property
    minimum_risk_level: Optional[PurviewInsiderRiskManagementLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InsiderRiskyUserApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InsiderRiskyUserApproval
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InsiderRiskyUserApproval()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .control_configuration import ControlConfiguration
        from .purview_insider_risk_management_level import PurviewInsiderRiskManagementLevel

        from .control_configuration import ControlConfiguration
        from .purview_insider_risk_management_level import PurviewInsiderRiskManagementLevel

        fields: dict[str, Callable[[Any], None]] = {
            "isApprovalRequired": lambda n : setattr(self, 'is_approval_required', n.get_bool_value()),
            "minimumRiskLevel": lambda n : setattr(self, 'minimum_risk_level', n.get_enum_value(PurviewInsiderRiskManagementLevel)),
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
        writer.write_bool_value("isApprovalRequired", self.is_approval_required)
        writer.write_enum_value("minimumRiskLevel", self.minimum_risk_level)
    

