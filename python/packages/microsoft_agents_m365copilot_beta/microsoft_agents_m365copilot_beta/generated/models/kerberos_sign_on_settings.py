from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .kerberos_sign_on_mapping_attribute_type import KerberosSignOnMappingAttributeType

@dataclass
class KerberosSignOnSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Internal Application SPN of the application server. This SPN needs to be in the list of services to which the connector can present delegated credentials.
    kerberos_service_principal_name: Optional[str] = None
    # The Delegated Login Identity for the connector to use on behalf of your users. For more information, see Working with different on-premises and cloud identities . The possible values are: userPrincipalName, onPremisesUserPrincipalName, userPrincipalUsername, onPremisesUserPrincipalUsername, onPremisesSAMAccountName.
    kerberos_sign_on_mapping_attribute_type: Optional[KerberosSignOnMappingAttributeType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KerberosSignOnSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KerberosSignOnSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KerberosSignOnSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .kerberos_sign_on_mapping_attribute_type import KerberosSignOnMappingAttributeType

        from .kerberos_sign_on_mapping_attribute_type import KerberosSignOnMappingAttributeType

        fields: dict[str, Callable[[Any], None]] = {
            "kerberosServicePrincipalName": lambda n : setattr(self, 'kerberos_service_principal_name', n.get_str_value()),
            "kerberosSignOnMappingAttributeType": lambda n : setattr(self, 'kerberos_sign_on_mapping_attribute_type', n.get_enum_value(KerberosSignOnMappingAttributeType)),
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
        writer.write_str_value("kerberosServicePrincipalName", self.kerberos_service_principal_name)
        writer.write_enum_value("kerberosSignOnMappingAttributeType", self.kerberos_sign_on_mapping_attribute_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

