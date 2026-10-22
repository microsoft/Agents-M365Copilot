from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_key_origin import ApplicationKeyOrigin
    from .application_key_type import ApplicationKeyType
    from .application_key_usage import ApplicationKeyUsage
    from .entity import Entity
    from .sign_in_activity import SignInActivity

from .entity import Entity

@dataclass
class AppCredentialSignInActivity(Entity, Parsable):
    # The globally unique appId (also called client ID on the Microsoft Entra admin center) of the credentialed application.
    app_id: Optional[str] = None
    # The ID of the credential application instance.
    app_object_id: Optional[str] = None
    # The date and time when the credential was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The credentialOrigin property
    credential_origin: Optional[ApplicationKeyOrigin] = None
    # The date and time when the credential is set to expire. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration_date_time: Optional[datetime.datetime] = None
    # The key ID of the credential.
    key_id: Optional[str] = None
    # Specifies the key type. The possible values are: clientSecret, certificate, unknownFutureValue.
    key_type: Optional[ApplicationKeyType] = None
    # Specifies what the key was used for. The possible values are: sign, verify, unknownFutureValue.
    key_usage: Optional[ApplicationKeyUsage] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the accessed resource.
    resource_id: Optional[str] = None
    # The ID of the service principal.
    service_principal_object_id: Optional[str] = None
    # The signInActivity property
    sign_in_activity: Optional[SignInActivity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppCredentialSignInActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppCredentialSignInActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppCredentialSignInActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_key_origin import ApplicationKeyOrigin
        from .application_key_type import ApplicationKeyType
        from .application_key_usage import ApplicationKeyUsage
        from .entity import Entity
        from .sign_in_activity import SignInActivity

        from .application_key_origin import ApplicationKeyOrigin
        from .application_key_type import ApplicationKeyType
        from .application_key_usage import ApplicationKeyUsage
        from .entity import Entity
        from .sign_in_activity import SignInActivity

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appObjectId": lambda n : setattr(self, 'app_object_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "credentialOrigin": lambda n : setattr(self, 'credential_origin', n.get_enum_value(ApplicationKeyOrigin)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "keyId": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "keyType": lambda n : setattr(self, 'key_type', n.get_enum_value(ApplicationKeyType)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_enum_value(ApplicationKeyUsage)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "servicePrincipalObjectId": lambda n : setattr(self, 'service_principal_object_id', n.get_str_value()),
            "signInActivity": lambda n : setattr(self, 'sign_in_activity', n.get_object_value(SignInActivity)),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("appObjectId", self.app_object_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("credentialOrigin", self.credential_origin)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("keyId", self.key_id)
        writer.write_enum_value("keyType", self.key_type)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("servicePrincipalObjectId", self.service_principal_object_id)
        writer.write_object_value("signInActivity", self.sign_in_activity)
    

