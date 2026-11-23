from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IdJagScopeMapping(AdditionalDataHolder, Parsable):
    """
    Maps Resource Authorization Server scopes to an Entra OAuth2 permission.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Required and non-null in each scope mapping. An enabled delegated permission exposed by the resource application for ID-JAG use.
    oauth2_permission: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Required and non-null in each scope mapping. One or two equivalent, case-sensitive Resource Authorization Server scopes for mapped behavior; empty for the single passthrough mapping.
    valid_resource_authorization_server_scopes: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdJagScopeMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdJagScopeMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdJagScopeMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "oauth2Permission": lambda n : setattr(self, 'oauth2_permission', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "validResourceAuthorizationServerScopes": lambda n : setattr(self, 'valid_resource_authorization_server_scopes', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("oauth2Permission", self.oauth2_permission)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("validResourceAuthorizationServerScopes", self.valid_resource_authorization_server_scopes)
        writer.write_additional_data_value(self.additional_data)
    

