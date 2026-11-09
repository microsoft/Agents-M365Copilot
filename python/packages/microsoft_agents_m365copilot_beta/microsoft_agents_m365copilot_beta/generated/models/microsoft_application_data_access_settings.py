from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class MicrosoftApplicationDataAccessSettings(Entity, Parsable):
    # The ID of a Microsoft Entra security group for which the members are allowed to access Microsoft 365 data using only Microsoft 365 apps, but not other Microsoft apps such as Edge.  This is only applicable if isEnabledForAllMicrosoftApplications is set to true.
    disabled_for_group: Optional[str] = None
    # When set to true, all users in the organization can access in a Microsoft app any Microsoft 365 data that the user has been authorized to access. The Microsoft app can be a Microsoft 365 app (for example, Excel, Outlook) or non-Microsoft 365 app (for example, Edge). The default is true.  It is possible to disable this access for a subset of users in a Microsoft Entra security group, by specifying the group in the disabledForGroup property.  When set to false, all users can access authorized Microsoft 365 data only in a Microsoft 365 app.
    is_enabled_for_all_microsoft_applications: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftApplicationDataAccessSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftApplicationDataAccessSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftApplicationDataAccessSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "disabledForGroup": lambda n : setattr(self, 'disabled_for_group', n.get_str_value()),
            "isEnabledForAllMicrosoftApplications": lambda n : setattr(self, 'is_enabled_for_all_microsoft_applications', n.get_bool_value()),
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
        writer.write_str_value("disabledForGroup", self.disabled_for_group)
        writer.write_bool_value("isEnabledForAllMicrosoftApplications", self.is_enabled_for_all_microsoft_applications)
    

