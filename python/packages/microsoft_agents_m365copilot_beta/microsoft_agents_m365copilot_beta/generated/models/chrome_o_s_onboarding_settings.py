from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .onboarding_status import OnboardingStatus

from .entity import Entity

@dataclass
class ChromeOSOnboardingSettings(Entity, Parsable):
    """
    Entity that represents a Chromebook tenant settings
    """
    # The ChromebookTenant's LastDirectorySyncDateTime
    last_directory_sync_date_time: Optional[datetime.datetime] = None
    # The ChromebookTenant's LastModifiedDateTime
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onboarding status of the tenant.
    onboarding_status: Optional[OnboardingStatus] = None
    # The ChromebookTenant's OwnerUserPrincipalName
    owner_user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChromeOSOnboardingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChromeOSOnboardingSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChromeOSOnboardingSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .onboarding_status import OnboardingStatus

        from .entity import Entity
        from .onboarding_status import OnboardingStatus

        fields: dict[str, Callable[[Any], None]] = {
            "lastDirectorySyncDateTime": lambda n : setattr(self, 'last_directory_sync_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(OnboardingStatus)),
            "ownerUserPrincipalName": lambda n : setattr(self, 'owner_user_principal_name', n.get_str_value()),
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
        writer.write_datetime_value("lastDirectorySyncDateTime", self.last_directory_sync_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_str_value("ownerUserPrincipalName", self.owner_user_principal_name)
    

