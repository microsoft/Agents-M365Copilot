from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dep_profile_delay_auto_rotation_setting import DepProfileDelayAutoRotationSetting

@dataclass
class DepProfileAdminAccountPasswordRotationSetting(AdditionalDataHolder, Parsable):
    """
    Settings for local admin account password automatic rotation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the number of days between 1-180 since the last rotation after which to rotate the local admin password.
    auto_rotation_period_in_days: Optional[int] = None
    # Settings for delaying automatic password rotation upon retrieval.
    dep_profile_delay_auto_rotation_setting: Optional[DepProfileDelayAutoRotationSetting] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepProfileAdminAccountPasswordRotationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepProfileAdminAccountPasswordRotationSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepProfileAdminAccountPasswordRotationSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dep_profile_delay_auto_rotation_setting import DepProfileDelayAutoRotationSetting

        from .dep_profile_delay_auto_rotation_setting import DepProfileDelayAutoRotationSetting

        fields: dict[str, Callable[[Any], None]] = {
            "autoRotationPeriodInDays": lambda n : setattr(self, 'auto_rotation_period_in_days', n.get_int_value()),
            "depProfileDelayAutoRotationSetting": lambda n : setattr(self, 'dep_profile_delay_auto_rotation_setting', n.get_object_value(DepProfileDelayAutoRotationSetting)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("autoRotationPeriodInDays", self.auto_rotation_period_in_days)
        writer.write_object_value("depProfileDelayAutoRotationSetting", self.dep_profile_delay_auto_rotation_setting)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

