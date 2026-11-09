from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .accounts_with_access import AccountsWithAccess
    from .authorization_system_resource import AuthorizationSystemResource
    from .aws_access_type import AwsAccessType
    from .finding import Finding

from .finding import Finding

@dataclass
class ExternallyAccessibleAwsStorageBucketFinding(Finding, Parsable):
    # The accessibility property
    accessibility: Optional[AwsAccessType] = None
    # The accountsWithAccess property
    accounts_with_access: Optional[AccountsWithAccess] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The storageBucket property
    storage_bucket: Optional[AuthorizationSystemResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternallyAccessibleAwsStorageBucketFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternallyAccessibleAwsStorageBucketFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternallyAccessibleAwsStorageBucketFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .accounts_with_access import AccountsWithAccess
        from .authorization_system_resource import AuthorizationSystemResource
        from .aws_access_type import AwsAccessType
        from .finding import Finding

        from .accounts_with_access import AccountsWithAccess
        from .authorization_system_resource import AuthorizationSystemResource
        from .aws_access_type import AwsAccessType
        from .finding import Finding

        fields: dict[str, Callable[[Any], None]] = {
            "accessibility": lambda n : setattr(self, 'accessibility', n.get_enum_value(AwsAccessType)),
            "accountsWithAccess": lambda n : setattr(self, 'accounts_with_access', n.get_object_value(AccountsWithAccess)),
            "storageBucket": lambda n : setattr(self, 'storage_bucket', n.get_object_value(AuthorizationSystemResource)),
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
        writer.write_enum_value("accessibility", self.accessibility)
        writer.write_object_value("accountsWithAccess", self.accounts_with_access)
        writer.write_object_value("storageBucket", self.storage_bucket)
    

