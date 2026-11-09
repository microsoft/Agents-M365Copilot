from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SharedAppleDeviceUser(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Data quota
    data_quota: Optional[int] = None
    # Data to sync
    data_to_sync: Optional[bool] = None
    # Data quota
    data_used: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharedAppleDeviceUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharedAppleDeviceUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharedAppleDeviceUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dataQuota": lambda n : setattr(self, 'data_quota', n.get_int_value()),
            "dataToSync": lambda n : setattr(self, 'data_to_sync', n.get_bool_value()),
            "dataUsed": lambda n : setattr(self, 'data_used', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_int_value("dataQuota", self.data_quota)
        writer.write_bool_value("dataToSync", self.data_to_sync)
        writer.write_int_value("dataUsed", self.data_used)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

