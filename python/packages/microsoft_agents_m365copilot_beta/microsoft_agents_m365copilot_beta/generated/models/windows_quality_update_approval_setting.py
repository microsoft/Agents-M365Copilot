from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_quality_update_cadence import WindowsQualityUpdateCadence
    from .windows_quality_update_category import WindowsQualityUpdateCategory
    from .windows_quality_update_policy_approval_method_type import WindowsQualityUpdatePolicyApprovalMethodType

@dataclass
class WindowsQualityUpdateApprovalSetting(AdditionalDataHolder, Parsable):
    """
    Entity to record approval settings for windows quality update policies
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Enum type to describe the approval type for different type of quality updates.
    approval_method_type: Optional[WindowsQualityUpdatePolicyApprovalMethodType] = None
    # The deferral days for auto approval type, not applicable for manual approve
    deferred_deployment_in_day: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The publishing cadence of the quality update. Possible values are: monthly, outOfBand. This property cannot be modified and is automatically populated when the catalog is created.
    windows_quality_update_cadence: Optional[WindowsQualityUpdateCadence] = None
    # Windows quality update category
    windows_quality_update_category: Optional[WindowsQualityUpdateCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateApprovalSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateApprovalSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateApprovalSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_quality_update_cadence import WindowsQualityUpdateCadence
        from .windows_quality_update_category import WindowsQualityUpdateCategory
        from .windows_quality_update_policy_approval_method_type import WindowsQualityUpdatePolicyApprovalMethodType

        from .windows_quality_update_cadence import WindowsQualityUpdateCadence
        from .windows_quality_update_category import WindowsQualityUpdateCategory
        from .windows_quality_update_policy_approval_method_type import WindowsQualityUpdatePolicyApprovalMethodType

        fields: dict[str, Callable[[Any], None]] = {
            "approvalMethodType": lambda n : setattr(self, 'approval_method_type', n.get_enum_value(WindowsQualityUpdatePolicyApprovalMethodType)),
            "deferredDeploymentInDay": lambda n : setattr(self, 'deferred_deployment_in_day', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "windowsQualityUpdateCadence": lambda n : setattr(self, 'windows_quality_update_cadence', n.get_enum_value(WindowsQualityUpdateCadence)),
            "windowsQualityUpdateCategory": lambda n : setattr(self, 'windows_quality_update_category', n.get_enum_value(WindowsQualityUpdateCategory)),
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
        writer.write_enum_value("approvalMethodType", self.approval_method_type)
        writer.write_int_value("deferredDeploymentInDay", self.deferred_deployment_in_day)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("windowsQualityUpdateCadence", self.windows_quality_update_cadence)
        writer.write_enum_value("windowsQualityUpdateCategory", self.windows_quality_update_category)
        writer.write_additional_data_value(self.additional_data)
    

