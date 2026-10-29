from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audit_identity_type import AuditIdentityType

@dataclass
class AuditActivityPerformer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The appId property
    app_id: Optional[str] = None
    # The blueprintId property
    blueprint_id: Optional[str] = None
    # The identityType property
    identity_type: Optional[AuditIdentityType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditActivityPerformer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditActivityPerformer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditActivityPerformer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audit_identity_type import AuditIdentityType

        from .audit_identity_type import AuditIdentityType

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "blueprintId": lambda n : setattr(self, 'blueprint_id', n.get_str_value()),
            "identityType": lambda n : setattr(self, 'identity_type', n.get_enum_value(AuditIdentityType)),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("blueprintId", self.blueprint_id)
        writer.write_enum_value("identityType", self.identity_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

