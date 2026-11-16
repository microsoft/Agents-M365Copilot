from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mfa_failure import MfaFailure

from .entity import Entity

@dataclass
class MfaCompletionMetric(Entity, Parsable):
    # The ID of the Microsoft Entra application. Supports $filter (eq).
    app_id: Optional[str] = None
    # Number of users who attempted to sign up. Supports $filter (eq).
    attempts_count: Optional[int] = None
    # The country property
    country: Optional[str] = None
    # The date of the user insight.
    fact_date: Optional[datetime.date] = None
    # The identityProvider property
    identity_provider: Optional[str] = None
    # The language property
    language: Optional[str] = None
    # The mfaFailures property
    mfa_failures: Optional[list[MfaFailure]] = None
    # The MFA authentication method used by the customers. Supports $filter (eq).
    mfa_method: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The platform of the device that the customers used. Supports $filter (eq).
    os: Optional[str] = None
    # Number of users who signed up successfully. Supports $filter (eq).
    success_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MfaCompletionMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MfaCompletionMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MfaCompletionMetric()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mfa_failure import MfaFailure

        from .entity import Entity
        from .mfa_failure import MfaFailure

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "attemptsCount": lambda n : setattr(self, 'attempts_count', n.get_int_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "identityProvider": lambda n : setattr(self, 'identity_provider', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "mfaFailures": lambda n : setattr(self, 'mfa_failures', n.get_collection_of_object_values(MfaFailure)),
            "mfaMethod": lambda n : setattr(self, 'mfa_method', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_int_value("attemptsCount", self.attempts_count)
        writer.write_str_value("country", self.country)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_str_value("identityProvider", self.identity_provider)
        writer.write_str_value("language", self.language)
        writer.write_collection_of_object_values("mfaFailures", self.mfa_failures)
        writer.write_str_value("mfaMethod", self.mfa_method)
        writer.write_str_value("os", self.os)
        writer.write_int_value("successCount", self.success_count)
    

