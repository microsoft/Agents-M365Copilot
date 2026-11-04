from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .authorization_system_info import AuthorizationSystemInfo
    from .external_system_access_methods import ExternalSystemAccessMethods
    from .finding import Finding

from .finding import Finding

@dataclass
class AwsExternalSystemAccessFinding(Finding, Parsable):
    # The accessMethods property
    access_methods: Optional[ExternalSystemAccessMethods] = None
    # The affectedSystem property
    affected_system: Optional[AuthorizationSystem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The systemWithAccess property
    system_with_access: Optional[AuthorizationSystemInfo] = None
    # The number of identities in the external system that are trusted, if not all. Supports $orderby.
    trusted_identity_count: Optional[int] = None
    # Flag that determines if all identities in the external system are trusted, or only a subset.
    trusts_all_identities: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsExternalSystemAccessFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsExternalSystemAccessFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsExternalSystemAccessFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .authorization_system_info import AuthorizationSystemInfo
        from .external_system_access_methods import ExternalSystemAccessMethods
        from .finding import Finding

        from .authorization_system import AuthorizationSystem
        from .authorization_system_info import AuthorizationSystemInfo
        from .external_system_access_methods import ExternalSystemAccessMethods
        from .finding import Finding

        fields: dict[str, Callable[[Any], None]] = {
            "accessMethods": lambda n : setattr(self, 'access_methods', n.get_collection_of_enum_values(ExternalSystemAccessMethods)),
            "affectedSystem": lambda n : setattr(self, 'affected_system', n.get_object_value(AuthorizationSystem)),
            "systemWithAccess": lambda n : setattr(self, 'system_with_access', n.get_object_value(AuthorizationSystemInfo)),
            "trustedIdentityCount": lambda n : setattr(self, 'trusted_identity_count', n.get_int_value()),
            "trustsAllIdentities": lambda n : setattr(self, 'trusts_all_identities', n.get_bool_value()),
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
        writer.write_enum_value("accessMethods", self.access_methods)
        writer.write_object_value("affectedSystem", self.affected_system)
        writer.write_object_value("systemWithAccess", self.system_with_access)
        writer.write_int_value("trustedIdentityCount", self.trusted_identity_count)
        writer.write_bool_value("trustsAllIdentities", self.trusts_all_identities)
    

