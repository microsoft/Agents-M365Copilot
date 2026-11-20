from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DepProfileDelayAutoRotationSetting(AdditionalDataHolder, Parsable):
    """
    Settings related to auto rotation of local admin account password after password retrieval through Graph. These are optional settings
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the admin account password should be rotated when retrieved by IT Admin through Intune.
    on_retrieval_auto_rotate_password_enabled: Optional[bool] = None
    # Indicates how long in hours (between 1 and 24 hours) after password retrieval through Graph should automatic rotation be initiated for the admin account password.
    on_retrieval_delay_auto_rotate_password_in_hours: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepProfileDelayAutoRotationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepProfileDelayAutoRotationSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DepProfileDelayAutoRotationSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onRetrievalAutoRotatePasswordEnabled": lambda n : setattr(self, 'on_retrieval_auto_rotate_password_enabled', n.get_bool_value()),
            "onRetrievalDelayAutoRotatePasswordInHours": lambda n : setattr(self, 'on_retrieval_delay_auto_rotate_password_in_hours', n.get_int_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("onRetrievalAutoRotatePasswordEnabled", self.on_retrieval_auto_rotate_password_enabled)
        writer.write_int_value("onRetrievalDelayAutoRotatePasswordInHours", self.on_retrieval_delay_auto_rotate_password_in_hours)
        writer.write_additional_data_value(self.additional_data)
    

