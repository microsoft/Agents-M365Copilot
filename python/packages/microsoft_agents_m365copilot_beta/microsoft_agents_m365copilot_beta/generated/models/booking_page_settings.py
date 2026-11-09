from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_page_access_control import BookingPageAccessControl

@dataclass
class BookingPageSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The accessControl property
    access_control: Optional[BookingPageAccessControl] = None
    # Custom color for the bookings page. The value should be in Hex format. Example: #123456.
    booking_page_color_code: Optional[str] = None
    # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
    business_time_zone: Optional[str] = None
    # The personal data collection and usage consent message in the bookings page.
    customer_consent_message: Optional[str] = None
    # Determines if the one-time password is required to create an appointment. The default value is false.
    enforce_one_time_password: Optional[bool] = None
    # Indicates if the business logo is displayed on the bookings page. The default value is false.
    is_business_logo_display_enabled: Optional[bool] = None
    # Enables personal data collection and the usage consent toggle on the bookings page. The default value is false.
    is_customer_consent_enabled: Optional[bool] = None
    # Ensures that the web crawlers don't index this page. The defaults value is false.
    is_search_engine_indexability_disabled: Optional[bool] = None
    # Displays the booking time slots in the business time zone. The default value is false.
    is_time_slot_time_zone_set_to_business_time_zone: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # RL of a webpage that provides the terms and conditions of the business. If a privacy policy isn't included, the following text appears on the bookings page as default: 'The policies and practices of <booking business's name> apply to the use of your data.
    privacy_policy_web_url: Optional[str] = None
    # URL of a webpage that provides the terms and conditions of the business.
    terms_and_conditions_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingPageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingPageSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingPageSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_page_access_control import BookingPageAccessControl

        from .booking_page_access_control import BookingPageAccessControl

        fields: dict[str, Callable[[Any], None]] = {
            "accessControl": lambda n : setattr(self, 'access_control', n.get_enum_value(BookingPageAccessControl)),
            "bookingPageColorCode": lambda n : setattr(self, 'booking_page_color_code', n.get_str_value()),
            "businessTimeZone": lambda n : setattr(self, 'business_time_zone', n.get_str_value()),
            "customerConsentMessage": lambda n : setattr(self, 'customer_consent_message', n.get_str_value()),
            "enforceOneTimePassword": lambda n : setattr(self, 'enforce_one_time_password', n.get_bool_value()),
            "isBusinessLogoDisplayEnabled": lambda n : setattr(self, 'is_business_logo_display_enabled', n.get_bool_value()),
            "isCustomerConsentEnabled": lambda n : setattr(self, 'is_customer_consent_enabled', n.get_bool_value()),
            "isSearchEngineIndexabilityDisabled": lambda n : setattr(self, 'is_search_engine_indexability_disabled', n.get_bool_value()),
            "isTimeSlotTimeZoneSetToBusinessTimeZone": lambda n : setattr(self, 'is_time_slot_time_zone_set_to_business_time_zone', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privacyPolicyWebUrl": lambda n : setattr(self, 'privacy_policy_web_url', n.get_str_value()),
            "termsAndConditionsWebUrl": lambda n : setattr(self, 'terms_and_conditions_web_url', n.get_str_value()),
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
        writer.write_enum_value("accessControl", self.access_control)
        writer.write_str_value("bookingPageColorCode", self.booking_page_color_code)
        writer.write_str_value("businessTimeZone", self.business_time_zone)
        writer.write_str_value("customerConsentMessage", self.customer_consent_message)
        writer.write_bool_value("enforceOneTimePassword", self.enforce_one_time_password)
        writer.write_bool_value("isBusinessLogoDisplayEnabled", self.is_business_logo_display_enabled)
        writer.write_bool_value("isCustomerConsentEnabled", self.is_customer_consent_enabled)
        writer.write_bool_value("isSearchEngineIndexabilityDisabled", self.is_search_engine_indexability_disabled)
        writer.write_bool_value("isTimeSlotTimeZoneSetToBusinessTimeZone", self.is_time_slot_time_zone_set_to_business_time_zone)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("privacyPolicyWebUrl", self.privacy_policy_web_url)
        writer.write_str_value("termsAndConditionsWebUrl", self.terms_and_conditions_web_url)
        writer.write_additional_data_value(self.additional_data)
    

