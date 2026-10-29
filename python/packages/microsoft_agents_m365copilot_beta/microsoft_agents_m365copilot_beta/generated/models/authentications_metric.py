from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_failure import AuthenticationFailure
    from .entity import Entity

from .entity import Entity

@dataclass
class AuthenticationsMetric(Entity, Parsable):
    # The ID of the Microsoft Entra application. Supports $filter (eq).
    appid: Optional[str] = None
    # The number of authentication requests made in the specified period. Supports $filter (eq).
    attempts_count: Optional[int] = None
    # The authFlow property
    auth_flow: Optional[str] = None
    # The browser property
    browser: Optional[str] = None
    # The location where the customers authenticated from. Supports $filter (eq).
    country: Optional[str] = None
    # The date of the user insight.
    fact_date: Optional[datetime.date] = None
    # The failures property
    failures: Optional[list[AuthenticationFailure]] = None
    # The identityProvider property
    identity_provider: Optional[str] = None
    # The language property
    language: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The platform for the device that the customers used. Supports $filter (eq).
    os: Optional[str] = None
    # Number of successful authentication requests. Supports $filter (eq).
    success_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationsMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationsMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationsMetric()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_failure import AuthenticationFailure
        from .entity import Entity

        from .authentication_failure import AuthenticationFailure
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "appid": lambda n : setattr(self, 'appid', n.get_str_value()),
            "attemptsCount": lambda n : setattr(self, 'attempts_count', n.get_int_value()),
            "authFlow": lambda n : setattr(self, 'auth_flow', n.get_str_value()),
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "failures": lambda n : setattr(self, 'failures', n.get_collection_of_object_values(AuthenticationFailure)),
            "identityProvider": lambda n : setattr(self, 'identity_provider', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "successCount": lambda n : setattr(self, 'success_count', n.get_int_value()),
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
        writer.write_str_value("appid", self.appid)
        writer.write_int_value("attemptsCount", self.attempts_count)
        writer.write_str_value("authFlow", self.auth_flow)
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("country", self.country)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_collection_of_object_values("failures", self.failures)
        writer.write_str_value("identityProvider", self.identity_provider)
        writer.write_str_value("language", self.language)
        writer.write_str_value("os", self.os)
        writer.write_int_value("successCount", self.success_count)
    

