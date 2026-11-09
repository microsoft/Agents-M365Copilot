from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trust_framework_key_status import TrustFrameworkKeyStatus

@dataclass
class TrustFrameworkKey(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # RSA Key - private exponent. The field isn't readable.
    d: Optional[str] = None
    # RSA Key - first exponent. The field isn't readable.
    dp: Optional[str] = None
    # RSA Key - second exponent. The field isn't readable.
    dq: Optional[str] = None
    # RSA Key - public exponent.
    e: Optional[str] = None
    # This value is a NumericDate as defined in RFC 7519. That is, a JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.
    exp: Optional[int] = None
    # Symmetric Key for oct key type. The field isn't readable.
    k: Optional[str] = None
    # The unique identifier for the key.
    kid: Optional[str] = None
    # The kty (key type) parameter identifies the cryptographic algorithm family used with the key. The valid values are rsa, oct.
    kty: Optional[str] = None
    # RSA Key - modulus.
    n: Optional[str] = None
    # This value is a NumericDate as defined in RFC 7519. That is, a JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.
    nbf: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # RSA Key - first prime. The field isn't readable.
    p: Optional[str] = None
    # RSA Key - second prime. The field isn't readable.
    q: Optional[str] = None
    # RSA Key - Coefficient. The field isn't readable.
    qi: Optional[str] = None
    # Status of the key. The possible values are: enabled, disabled, unknownFutureValue.
    status: Optional[TrustFrameworkKeyStatus] = None
    # The use (public key use) parameter identifies the intended use of the public key. The use parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. The possible values are: sig (signature), enc (encryption).
    use: Optional[str] = None
    # The x5c (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates. For more information, see RFC 5280.
    x5c: Optional[list[str]] = None
    # The x5t (X.509 certificate SHA-1 thumbprint) parameter is a base64url-encoded SHA-1 thumbprint (also known as digest) of the DER encoding of an X.509 certificate. For more information, see RFC 5280.
    x5t: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrustFrameworkKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrustFrameworkKey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrustFrameworkKey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .trust_framework_key_status import TrustFrameworkKeyStatus

        from .trust_framework_key_status import TrustFrameworkKeyStatus

        fields: dict[str, Callable[[Any], None]] = {
            "d": lambda n : setattr(self, 'd', n.get_str_value()),
            "dp": lambda n : setattr(self, 'dp', n.get_str_value()),
            "dq": lambda n : setattr(self, 'dq', n.get_str_value()),
            "e": lambda n : setattr(self, 'e', n.get_str_value()),
            "exp": lambda n : setattr(self, 'exp', n.get_int_value()),
            "k": lambda n : setattr(self, 'k', n.get_str_value()),
            "kid": lambda n : setattr(self, 'kid', n.get_str_value()),
            "kty": lambda n : setattr(self, 'kty', n.get_str_value()),
            "n": lambda n : setattr(self, 'n', n.get_str_value()),
            "nbf": lambda n : setattr(self, 'nbf', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "p": lambda n : setattr(self, 'p', n.get_str_value()),
            "q": lambda n : setattr(self, 'q', n.get_str_value()),
            "qi": lambda n : setattr(self, 'qi', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TrustFrameworkKeyStatus)),
            "use": lambda n : setattr(self, 'use', n.get_str_value()),
            "x5c": lambda n : setattr(self, 'x5c', n.get_collection_of_primitive_values(str)),
            "x5t": lambda n : setattr(self, 'x5t', n.get_str_value()),
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
        writer.write_str_value("d", self.d)
        writer.write_str_value("dp", self.dp)
        writer.write_str_value("dq", self.dq)
        writer.write_str_value("e", self.e)
        writer.write_int_value("exp", self.exp)
        writer.write_str_value("k", self.k)
        writer.write_str_value("kid", self.kid)
        writer.write_str_value("kty", self.kty)
        writer.write_str_value("n", self.n)
        writer.write_int_value("nbf", self.nbf)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("p", self.p)
        writer.write_str_value("q", self.q)
        writer.write_str_value("qi", self.qi)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("use", self.use)
        writer.write_collection_of_primitive_values("x5c", self.x5c)
        writer.write_str_value("x5t", self.x5t)
        writer.write_additional_data_value(self.additional_data)
    

