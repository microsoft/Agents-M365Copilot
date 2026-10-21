from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .email_authentication_method import EmailAuthenticationMethod
    from .entity import Entity
    from .external_authentication_method import ExternalAuthenticationMethod
    from .fido2_authentication_method import Fido2AuthenticationMethod
    from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
    from .long_running_operation import LongRunningOperation
    from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
    from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
    from .password_authentication_method import PasswordAuthenticationMethod
    from .phone_authentication_method import PhoneAuthenticationMethod
    from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
    from .qr_code_pin_authentication_method import QrCodePinAuthenticationMethod
    from .resource_account_key_authentication_method import ResourceAccountKeyAuthenticationMethod
    from .sign_in_preferences import SignInPreferences
    from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
    from .strong_authentication_requirements import StrongAuthenticationRequirements
    from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
    from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

from .entity import Entity

@dataclass
class Authentication(Entity, Parsable):
    # Represents the email addresses registered to a user for authentication.
    email_methods: Optional[list[EmailAuthenticationMethod]] = None
    # Represents the external MFA registered to a user for authentication.
    external_authentication_methods: Optional[list[ExternalAuthenticationMethod]] = None
    # Represents the FIDO2 security keys registered to a user for authentication.
    fido2_methods: Optional[list[Fido2AuthenticationMethod]] = None
    # The hardware OATH time-based one-time password (TOTP) devices assigned to a user for authentication.
    hardware_oath_methods: Optional[list[HardwareOathAuthenticationMethod]] = None
    # Represents all authentication methods registered to a user.
    methods: Optional[list[AuthenticationMethod]] = None
    # The details of the Microsoft Authenticator app registered to a user for authentication.
    microsoft_authenticator_methods: Optional[list[MicrosoftAuthenticatorAuthenticationMethod]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the status of a long-running operation, such as a password reset operation.
    operations: Optional[list[LongRunningOperation]] = None
    # Represents the details of the password authentication method registered to a user for authentication.
    password_methods: Optional[list[PasswordAuthenticationMethod]] = None
    # Represents the Microsoft Authenticator Passwordless Phone Sign-in methods registered to a user for authentication.
    passwordless_microsoft_authenticator_methods: Optional[list[PasswordlessMicrosoftAuthenticatorAuthenticationMethod]] = None
    # Represents the phone registered to a user for authentication.
    phone_methods: Optional[list[PhoneAuthenticationMethod]] = None
    # Represents a platform credential instance registered to a user on Mac OS.
    platform_credential_methods: Optional[list[PlatformCredentialAuthenticationMethod]] = None
    # Represents a QR code authentication method registered to a user for authentication.
    qr_code_pin_method: Optional[QrCodePinAuthenticationMethod] = None
    # The settings and preferences for per-user Microsoft Entra multifactor authentication.
    requirements: Optional[StrongAuthenticationRequirements] = None
    # Represents the resource account key credentials registered to a user for authentication on shared devices.
    resource_account_key_authentication_methods: Optional[list[ResourceAccountKeyAuthenticationMethod]] = None
    # The settings and preferences for the sign-in experience of a user. Use this property to configure the user's default multifactor authentication (MFA) method.
    sign_in_preferences: Optional[SignInPreferences] = None
    # The software OATH time-based one-time password (TOTP) applications registered to a user for authentication.
    software_oath_methods: Optional[list[SoftwareOathAuthenticationMethod]] = None
    # Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes.
    temporary_access_pass_methods: Optional[list[TemporaryAccessPassAuthenticationMethod]] = None
    # Represents the Windows Hello for Business authentication method registered to a user for authentication.
    windows_hello_for_business_methods: Optional[list[WindowsHelloForBusinessAuthenticationMethod]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Authentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Authentication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Authentication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .email_authentication_method import EmailAuthenticationMethod
        from .entity import Entity
        from .external_authentication_method import ExternalAuthenticationMethod
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
        from .long_running_operation import LongRunningOperation
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
        from .password_authentication_method import PasswordAuthenticationMethod
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .qr_code_pin_authentication_method import QrCodePinAuthenticationMethod
        from .resource_account_key_authentication_method import ResourceAccountKeyAuthenticationMethod
        from .sign_in_preferences import SignInPreferences
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .strong_authentication_requirements import StrongAuthenticationRequirements
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

        from .authentication_method import AuthenticationMethod
        from .email_authentication_method import EmailAuthenticationMethod
        from .entity import Entity
        from .external_authentication_method import ExternalAuthenticationMethod
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
        from .long_running_operation import LongRunningOperation
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
        from .password_authentication_method import PasswordAuthenticationMethod
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .qr_code_pin_authentication_method import QrCodePinAuthenticationMethod
        from .resource_account_key_authentication_method import ResourceAccountKeyAuthenticationMethod
        from .sign_in_preferences import SignInPreferences
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .strong_authentication_requirements import StrongAuthenticationRequirements
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "emailMethods": lambda n : setattr(self, 'email_methods', n.get_collection_of_object_values(EmailAuthenticationMethod)),
            "externalAuthenticationMethods": lambda n : setattr(self, 'external_authentication_methods', n.get_collection_of_object_values(ExternalAuthenticationMethod)),
            "fido2Methods": lambda n : setattr(self, 'fido2_methods', n.get_collection_of_object_values(Fido2AuthenticationMethod)),
            "hardwareOathMethods": lambda n : setattr(self, 'hardware_oath_methods', n.get_collection_of_object_values(HardwareOathAuthenticationMethod)),
            "methods": lambda n : setattr(self, 'methods', n.get_collection_of_object_values(AuthenticationMethod)),
            "microsoftAuthenticatorMethods": lambda n : setattr(self, 'microsoft_authenticator_methods', n.get_collection_of_object_values(MicrosoftAuthenticatorAuthenticationMethod)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(LongRunningOperation)),
            "passwordMethods": lambda n : setattr(self, 'password_methods', n.get_collection_of_object_values(PasswordAuthenticationMethod)),
            "passwordlessMicrosoftAuthenticatorMethods": lambda n : setattr(self, 'passwordless_microsoft_authenticator_methods', n.get_collection_of_object_values(PasswordlessMicrosoftAuthenticatorAuthenticationMethod)),
            "phoneMethods": lambda n : setattr(self, 'phone_methods', n.get_collection_of_object_values(PhoneAuthenticationMethod)),
            "platformCredentialMethods": lambda n : setattr(self, 'platform_credential_methods', n.get_collection_of_object_values(PlatformCredentialAuthenticationMethod)),
            "qrCodePinMethod": lambda n : setattr(self, 'qr_code_pin_method', n.get_object_value(QrCodePinAuthenticationMethod)),
            "requirements": lambda n : setattr(self, 'requirements', n.get_object_value(StrongAuthenticationRequirements)),
            "resourceAccountKeyAuthenticationMethods": lambda n : setattr(self, 'resource_account_key_authentication_methods', n.get_collection_of_object_values(ResourceAccountKeyAuthenticationMethod)),
            "signInPreferences": lambda n : setattr(self, 'sign_in_preferences', n.get_object_value(SignInPreferences)),
            "softwareOathMethods": lambda n : setattr(self, 'software_oath_methods', n.get_collection_of_object_values(SoftwareOathAuthenticationMethod)),
            "temporaryAccessPassMethods": lambda n : setattr(self, 'temporary_access_pass_methods', n.get_collection_of_object_values(TemporaryAccessPassAuthenticationMethod)),
            "windowsHelloForBusinessMethods": lambda n : setattr(self, 'windows_hello_for_business_methods', n.get_collection_of_object_values(WindowsHelloForBusinessAuthenticationMethod)),
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
        writer.write_collection_of_object_values("emailMethods", self.email_methods)
        writer.write_collection_of_object_values("externalAuthenticationMethods", self.external_authentication_methods)
        writer.write_collection_of_object_values("fido2Methods", self.fido2_methods)
        writer.write_collection_of_object_values("hardwareOathMethods", self.hardware_oath_methods)
        writer.write_collection_of_object_values("methods", self.methods)
        writer.write_collection_of_object_values("microsoftAuthenticatorMethods", self.microsoft_authenticator_methods)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("passwordMethods", self.password_methods)
        writer.write_collection_of_object_values("passwordlessMicrosoftAuthenticatorMethods", self.passwordless_microsoft_authenticator_methods)
        writer.write_collection_of_object_values("phoneMethods", self.phone_methods)
        writer.write_collection_of_object_values("platformCredentialMethods", self.platform_credential_methods)
        writer.write_object_value("qrCodePinMethod", self.qr_code_pin_method)
        writer.write_object_value("requirements", self.requirements)
        writer.write_collection_of_object_values("resourceAccountKeyAuthenticationMethods", self.resource_account_key_authentication_methods)
        writer.write_object_value("signInPreferences", self.sign_in_preferences)
        writer.write_collection_of_object_values("softwareOathMethods", self.software_oath_methods)
        writer.write_collection_of_object_values("temporaryAccessPassMethods", self.temporary_access_pass_methods)
        writer.write_collection_of_object_values("windowsHelloForBusinessMethods", self.windows_hello_for_business_methods)
    

