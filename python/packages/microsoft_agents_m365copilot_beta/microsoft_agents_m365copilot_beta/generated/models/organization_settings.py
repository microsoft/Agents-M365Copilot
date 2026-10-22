from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .insights_settings import InsightsSettings
    from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings

from .entity import Entity

@dataclass
class OrganizationSettings(Entity, Parsable):
    # Contains the properties that are configured by an administrator as a tenant-level privacy control whether to identify duplicate contacts among a user's contacts list and suggest the user to merge those contacts to have a cleaner contacts list. List contactInsights returns the settings to display or return contact insights in an organization.
    contact_insights: Optional[InsightsSettings] = None
    # Contains the properties that are configured by an administrator for the visibility of Microsoft Graph-derived insights, between a user and other items in Microsoft 365, such as documents or sites. List itemInsights returns the settings to display or return item insights in an organization.
    item_insights: Optional[InsightsSettings] = None
    # The microsoftApplicationDataAccess property
    microsoft_application_data_access: Optional[MicrosoftApplicationDataAccessSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the properties that are configured by an administrator for the visibility of a list of people relevant and working with a user in Microsoft 365. List peopleInsights returns the settings to display or return people insights in an organization.
    people_insights: Optional[InsightsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .insights_settings import InsightsSettings
        from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings

        from .entity import Entity
        from .insights_settings import InsightsSettings
        from .microsoft_application_data_access_settings import MicrosoftApplicationDataAccessSettings

        fields: dict[str, Callable[[Any], None]] = {
            "contactInsights": lambda n : setattr(self, 'contact_insights', n.get_object_value(InsightsSettings)),
            "itemInsights": lambda n : setattr(self, 'item_insights', n.get_object_value(InsightsSettings)),
            "microsoftApplicationDataAccess": lambda n : setattr(self, 'microsoft_application_data_access', n.get_object_value(MicrosoftApplicationDataAccessSettings)),
            "peopleInsights": lambda n : setattr(self, 'people_insights', n.get_object_value(InsightsSettings)),
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
        writer.write_object_value("contactInsights", self.contact_insights)
        writer.write_object_value("itemInsights", self.item_insights)
        writer.write_object_value("microsoftApplicationDataAccess", self.microsoft_application_data_access)
        writer.write_object_value("peopleInsights", self.people_insights)
    

