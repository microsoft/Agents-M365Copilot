from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .credential_single_sign_on_extension import CredentialSingleSignOnExtension
    from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
    from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
    from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
    from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
    from .ios_single_sign_on_extension import IosSingleSignOnExtension
    from .kerberos_single_sign_on_extension import KerberosSingleSignOnExtension
    from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
    from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
    from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
    from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
    from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
    from .redirect_single_sign_on_extension import RedirectSingleSignOnExtension

@dataclass
class SingleSignOnExtension(AdditionalDataHolder, Parsable):
    """
    Represents an Apple Single Sign-On Extension.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SingleSignOnExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.credentialSingleSignOnExtension".casefold():
            from .credential_single_sign_on_extension import CredentialSingleSignOnExtension

            return CredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosAzureAdSingleSignOnExtension".casefold():
            from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension

            return IosAzureAdSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCredentialSingleSignOnExtension".casefold():
            from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension

            return IosCredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosKerberosSingleSignOnExtension".casefold():
            from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension

            return IosKerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosRedirectSingleSignOnExtension".casefold():
            from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension

            return IosRedirectSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosSingleSignOnExtension".casefold():
            from .ios_single_sign_on_extension import IosSingleSignOnExtension

            return IosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.kerberosSingleSignOnExtension".casefold():
            from .kerberos_single_sign_on_extension import KerberosSingleSignOnExtension

            return KerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSAzureAdSingleSignOnExtension".casefold():
            from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension

            return MacOSAzureAdSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCredentialSingleSignOnExtension".casefold():
            from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension

            return MacOSCredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSKerberosSingleSignOnExtension".casefold():
            from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension

            return MacOSKerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSRedirectSingleSignOnExtension".casefold():
            from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension

            return MacOSRedirectSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSingleSignOnExtension".casefold():
            from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension

            return MacOSSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redirectSingleSignOnExtension".casefold():
            from .redirect_single_sign_on_extension import RedirectSingleSignOnExtension

            return RedirectSingleSignOnExtension()
        return SingleSignOnExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .credential_single_sign_on_extension import CredentialSingleSignOnExtension
        from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
        from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
        from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
        from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
        from .ios_single_sign_on_extension import IosSingleSignOnExtension
        from .kerberos_single_sign_on_extension import KerberosSingleSignOnExtension
        from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
        from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
        from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
        from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
        from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
        from .redirect_single_sign_on_extension import RedirectSingleSignOnExtension

        from .credential_single_sign_on_extension import CredentialSingleSignOnExtension
        from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
        from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
        from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
        from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
        from .ios_single_sign_on_extension import IosSingleSignOnExtension
        from .kerberos_single_sign_on_extension import KerberosSingleSignOnExtension
        from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
        from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
        from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
        from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
        from .mac_o_s_single_sign_on_extension import MacOSSingleSignOnExtension
        from .redirect_single_sign_on_extension import RedirectSingleSignOnExtension

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

