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
class DataSharingConsent(Entity, Parsable):
    """
    Data sharing consent information.
    """
    # The time consent was granted for this account
    grant_date_time: Optional[datetime.datetime] = None
    # The granted state for the data sharing consent
    granted: Optional[bool] = None
    # The Upn of the user that granted consent for this account
    granted_by_upn: Optional[str] = None
    # The UserId of the user that granted consent for this account
    granted_by_user_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The display name of the service work flow
    service_display_name: Optional[str] = None
    # The TermsUrl for the data sharing consent
    terms_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataSharingConsent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataSharingConsent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DataSharingConsent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "grantDateTime": lambda n : setattr(self, 'grant_date_time', n.get_datetime_value()),
            "granted": lambda n : setattr(self, 'granted', n.get_bool_value()),
            "grantedByUpn": lambda n : setattr(self, 'granted_by_upn', n.get_str_value()),
            "grantedByUserId": lambda n : setattr(self, 'granted_by_user_id', n.get_str_value()),
            "serviceDisplayName": lambda n : setattr(self, 'service_display_name', n.get_str_value()),
            "termsUrl": lambda n : setattr(self, 'terms_url', n.get_str_value()),
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
        writer.write_datetime_value("grantDateTime", self.grant_date_time)
        writer.write_bool_value("granted", self.granted)
        writer.write_str_value("grantedByUpn", self.granted_by_upn)
        writer.write_str_value("grantedByUserId", self.granted_by_user_id)
        writer.write_str_value("serviceDisplayName", self.service_display_name)
        writer.write_str_value("termsUrl", self.terms_url)
    

