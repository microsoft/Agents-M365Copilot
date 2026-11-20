from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .kerberos_sign_on_settings import KerberosSignOnSettings
    from .single_sign_on_mode import SingleSignOnMode

@dataclass
class OnPremisesPublishingSingleSignOn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Kerberos Constrained Delegation settings for applications that use Integrated Window Authentication.
    kerberos_sign_on_settings: Optional[KerberosSignOnSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The preferred single-sign on mode for the application. The possible values are: none, onPremisesKerberos, aadHeaderBased,pingHeaderBased, oAuthToken.
    single_sign_on_mode: Optional[SingleSignOnMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesPublishingSingleSignOn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishingSingleSignOn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesPublishingSingleSignOn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .kerberos_sign_on_settings import KerberosSignOnSettings
        from .single_sign_on_mode import SingleSignOnMode

        from .kerberos_sign_on_settings import KerberosSignOnSettings
        from .single_sign_on_mode import SingleSignOnMode

        fields: dict[str, Callable[[Any], None]] = {
            "kerberosSignOnSettings": lambda n : setattr(self, 'kerberos_sign_on_settings', n.get_object_value(KerberosSignOnSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "singleSignOnMode": lambda n : setattr(self, 'single_sign_on_mode', n.get_enum_value(SingleSignOnMode)),
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
        writer.write_object_value("kerberosSignOnSettings", self.kerberos_sign_on_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("singleSignOnMode", self.single_sign_on_mode)
        writer.write_additional_data_value(self.additional_data)
    

