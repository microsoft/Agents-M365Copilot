from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AuthenticationDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The type of authentication method used to perform this step of authentication. Possible values: Password, SMS, Voice, Authenticator App, Software OATH token, Satisfied by token, Previously satisfied.
    authentication_method: Optional[str] = None
    # Details about the authentication method used to perform this authentication step. For example, phone number (for SMS and voice), device name (for Authenticator app), and password source (for example, cloud, AD FS, PTA, PHS).
    authentication_method_detail: Optional[str] = None
    # Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    authentication_step_date_time: Optional[datetime.datetime] = None
    # The step of authentication that this satisfied. For example, primary authentication, or multifactor authentication.
    authentication_step_requirement: Optional[str] = None
    # Details about why the step succeeded or failed. For examples, user is blocked, fraud code entered, no phone input - timed out, phone unreachable, or claim in token.
    authentication_step_result_detail: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the status of the authentication step. Possible values: succeeded, failed.
    succeeded: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_str_value()),
            "authenticationMethodDetail": lambda n : setattr(self, 'authentication_method_detail', n.get_str_value()),
            "authenticationStepDateTime": lambda n : setattr(self, 'authentication_step_date_time', n.get_datetime_value()),
            "authenticationStepRequirement": lambda n : setattr(self, 'authentication_step_requirement', n.get_str_value()),
            "authenticationStepResultDetail": lambda n : setattr(self, 'authentication_step_result_detail', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_bool_value()),
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
        writer.write_str_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("authenticationMethodDetail", self.authentication_method_detail)
        writer.write_datetime_value("authenticationStepDateTime", self.authentication_step_date_time)
        writer.write_str_value("authenticationStepRequirement", self.authentication_step_requirement)
        writer.write_str_value("authenticationStepResultDetail", self.authentication_step_result_detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("succeeded", self.succeeded)
        writer.write_additional_data_value(self.additional_data)
    

