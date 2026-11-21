from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .id_jag_resource_server_uri_match_type import IdJagResourceServerUriMatchType
    from .id_jag_scope_mapping import IdJagScopeMapping
    from .id_jag_scope_mapping_type import IdJagScopeMappingType

@dataclass
class IdJagResourceServer(AdditionalDataHolder, Parsable):
    """
    Configures resource URI matching and Resource Authorization Server scope mapping for one ID-JAG resource server. Across entries, overlapping normalized resource domains are allowed only when every common accepted external scope resolves to the same Entra OAuth2 permission.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Required and non-null in each resource server entry. Matching precedence is exact, longest pathPrefix, then anyURI; absent applies only when no resource is supplied. Overlap is rejected when a common accepted external scope resolves to a different Entra OAuth2 permission across entries.
    resource_server_uri_match_type: Optional[IdJagResourceServerUriMatchType] = None
    # Required and non-null in each resource server entry. Non-empty for exact and pathPrefix; empty for absent and anyURI.
    resource_server_uris: Optional[list[str]] = None
    # Required and non-null in each resource server entry. Specifies direct, mapped, or passthrough scope behavior used to detect contradictory scope-to-permission outcomes across overlapping resource domains.
    scope_mapping_type: Optional[IdJagScopeMappingType] = None
    # Required and non-null in each resource server entry. Empty for direct, non-empty for mapped, and exactly one entry with an empty validResourceAuthorizationServerScopes collection for passthrough.
    scope_mappings: Optional[list[IdJagScopeMapping]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdJagResourceServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdJagResourceServer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdJagResourceServer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .id_jag_resource_server_uri_match_type import IdJagResourceServerUriMatchType
        from .id_jag_scope_mapping import IdJagScopeMapping
        from .id_jag_scope_mapping_type import IdJagScopeMappingType

        from .id_jag_resource_server_uri_match_type import IdJagResourceServerUriMatchType
        from .id_jag_scope_mapping import IdJagScopeMapping
        from .id_jag_scope_mapping_type import IdJagScopeMappingType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceServerUriMatchType": lambda n : setattr(self, 'resource_server_uri_match_type', n.get_enum_value(IdJagResourceServerUriMatchType)),
            "resourceServerUris": lambda n : setattr(self, 'resource_server_uris', n.get_collection_of_primitive_values(str)),
            "scopeMappingType": lambda n : setattr(self, 'scope_mapping_type', n.get_enum_value(IdJagScopeMappingType)),
            "scopeMappings": lambda n : setattr(self, 'scope_mappings', n.get_collection_of_object_values(IdJagScopeMapping)),
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
        writer.write_enum_value("resourceServerUriMatchType", self.resource_server_uri_match_type)
        writer.write_collection_of_primitive_values("resourceServerUris", self.resource_server_uris)
        writer.write_enum_value("scopeMappingType", self.scope_mapping_type)
        writer.write_collection_of_object_values("scopeMappings", self.scope_mappings)
        writer.write_additional_data_value(self.additional_data)
    

