from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_pfx_intended_purpose import UserPfxIntendedPurpose
    from .user_pfx_padding_scheme import UserPfxPaddingScheme

from .entity import Entity

@dataclass
class UserPFXCertificate(Entity, Parsable):
    """
    Entity that encapsulates all information required for a user's PFX certificates.
    """
    # Date/time when this PFX certificate was imported.
    created_date_time: Optional[datetime.datetime] = None
    # Encrypted PFX blob.
    encrypted_pfx_blob: Optional[bytes] = None
    # Encrypted PFX password.
    encrypted_pfx_password: Optional[str] = None
    # Certificate's validity expiration date/time.
    expiration_date_time: Optional[datetime.datetime] = None
    # Supported values for the intended purpose of a user PFX certificate.
    intended_purpose: Optional[UserPfxIntendedPurpose] = None
    # Name of the key (within the provider) used to encrypt the blob.
    key_name: Optional[str] = None
    # Date/time when this PFX certificate was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported values for the padding scheme used by encryption provider.
    padding_scheme: Optional[UserPfxPaddingScheme] = None
    # Crypto provider used to encrypt this blob.
    provider_name: Optional[str] = None
    # Certificate's validity start date/time.
    start_date_time: Optional[datetime.datetime] = None
    # SHA-1 thumbprint of the PFX certificate.
    thumbprint: Optional[str] = None
    # User Principal Name of the PFX certificate.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserPFXCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserPFXCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserPFXCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_pfx_intended_purpose import UserPfxIntendedPurpose
        from .user_pfx_padding_scheme import UserPfxPaddingScheme

        from .entity import Entity
        from .user_pfx_intended_purpose import UserPfxIntendedPurpose
        from .user_pfx_padding_scheme import UserPfxPaddingScheme

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "encryptedPfxBlob": lambda n : setattr(self, 'encrypted_pfx_blob', n.get_bytes_value()),
            "encryptedPfxPassword": lambda n : setattr(self, 'encrypted_pfx_password', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "intendedPurpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(UserPfxIntendedPurpose)),
            "keyName": lambda n : setattr(self, 'key_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "paddingScheme": lambda n : setattr(self, 'padding_scheme', n.get_enum_value(UserPfxPaddingScheme)),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bytes_value("encryptedPfxBlob", self.encrypted_pfx_blob)
        writer.write_str_value("encryptedPfxPassword", self.encrypted_pfx_password)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_str_value("keyName", self.key_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("paddingScheme", self.padding_scheme)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

