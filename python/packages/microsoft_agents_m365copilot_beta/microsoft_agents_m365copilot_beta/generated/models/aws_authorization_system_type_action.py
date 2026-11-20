from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_type_action import AuthorizationSystemTypeAction
    from .authorization_system_type_service import AuthorizationSystemTypeService

from .authorization_system_type_action import AuthorizationSystemTypeAction

@dataclass
class AwsAuthorizationSystemTypeAction(AuthorizationSystemTypeAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The service property
    service: Optional[AuthorizationSystemTypeService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsAuthorizationSystemTypeAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsAuthorizationSystemTypeAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsAuthorizationSystemTypeAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .authorization_system_type_service import AuthorizationSystemTypeService

        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .authorization_system_type_service import AuthorizationSystemTypeService

        fields: dict[str, Callable[[Any], None]] = {
            "service": lambda n : setattr(self, 'service', n.get_object_value(AuthorizationSystemTypeService)),
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
        writer.write_object_value("service", self.service)
    

