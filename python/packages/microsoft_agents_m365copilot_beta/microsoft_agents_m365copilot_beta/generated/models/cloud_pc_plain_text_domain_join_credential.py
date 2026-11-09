from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential

from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential

@dataclass
class CloudPcPlainTextDomainJoinCredential(CloudPcDomainJoinCredential, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcPlainTextDomainJoinCredential"
    # The password associated with the domainUserPrincipalName. Required in requests. Not returned in responses.
    domain_password: Optional[str] = None
    # The user principal name of an Active Directory account that has sufficient permissions to join devices to the domain. The value must be in UPN format, for example, domainjoin@ad.contoso.com. Required.
    domain_user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcPlainTextDomainJoinCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcPlainTextDomainJoinCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcPlainTextDomainJoinCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential

        from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential

        fields: dict[str, Callable[[Any], None]] = {
            "domainPassword": lambda n : setattr(self, 'domain_password', n.get_str_value()),
            "domainUserPrincipalName": lambda n : setattr(self, 'domain_user_principal_name', n.get_str_value()),
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
        writer.write_str_value("domainPassword", self.domain_password)
        writer.write_str_value("domainUserPrincipalName", self.domain_user_principal_name)
    

