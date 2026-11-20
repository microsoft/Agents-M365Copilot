from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class MfaTelecomFraudMetric(Entity, Parsable):
    # The captchaFailureCount property
    captcha_failure_count: Optional[int] = None
    # The captchaNotTriggeredUserCount property
    captcha_not_triggered_user_count: Optional[int] = None
    # The captchaShownUserCount property
    captcha_shown_user_count: Optional[int] = None
    # The captchaSuccessCount property
    captcha_success_count: Optional[int] = None
    # The factDate property
    fact_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The telecomBlockedUserCount property
    telecom_blocked_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MfaTelecomFraudMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MfaTelecomFraudMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MfaTelecomFraudMetric()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "captchaFailureCount": lambda n : setattr(self, 'captcha_failure_count', n.get_int_value()),
            "captchaNotTriggeredUserCount": lambda n : setattr(self, 'captcha_not_triggered_user_count', n.get_int_value()),
            "captchaShownUserCount": lambda n : setattr(self, 'captcha_shown_user_count', n.get_int_value()),
            "captchaSuccessCount": lambda n : setattr(self, 'captcha_success_count', n.get_int_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "telecomBlockedUserCount": lambda n : setattr(self, 'telecom_blocked_user_count', n.get_int_value()),
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
        writer.write_int_value("captchaFailureCount", self.captcha_failure_count)
        writer.write_int_value("captchaNotTriggeredUserCount", self.captcha_not_triggered_user_count)
        writer.write_int_value("captchaShownUserCount", self.captcha_shown_user_count)
        writer.write_int_value("captchaSuccessCount", self.captcha_success_count)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_int_value("telecomBlockedUserCount", self.telecom_blocked_user_count)
    

