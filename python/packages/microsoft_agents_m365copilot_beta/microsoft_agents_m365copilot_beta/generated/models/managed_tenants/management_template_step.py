from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..action_url import ActionUrl
    from ..entity import Entity
    from .management_category import ManagementCategory
    from .management_template import ManagementTemplate
    from .management_template_step_version import ManagementTemplateStepVersion

from ..entity import Entity

@dataclass
class ManagementTemplateStep(Entity, Parsable):
    # The acceptedVersion property
    accepted_version: Optional[ManagementTemplateStepVersion] = None
    # The category property
    category: Optional[ManagementCategory] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The informationLinks property
    information_links: Optional[list[ActionUrl]] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The managementTemplate property
    management_template: Optional[ManagementTemplate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The portalLink property
    portal_link: Optional[ActionUrl] = None
    # The priority property
    priority: Optional[int] = None
    # The userImpact property
    user_impact: Optional[str] = None
    # The versions property
    versions: Optional[list[ManagementTemplateStepVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementTemplateStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStep
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateStep()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..action_url import ActionUrl
        from ..entity import Entity
        from .management_category import ManagementCategory
        from .management_template import ManagementTemplate
        from .management_template_step_version import ManagementTemplateStepVersion

        from ..action_url import ActionUrl
        from ..entity import Entity
        from .management_category import ManagementCategory
        from .management_template import ManagementTemplate
        from .management_template_step_version import ManagementTemplateStepVersion

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedVersion": lambda n : setattr(self, 'accepted_version', n.get_object_value(ManagementTemplateStepVersion)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ManagementCategory)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationLinks": lambda n : setattr(self, 'information_links', n.get_collection_of_object_values(ActionUrl)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "managementTemplate": lambda n : setattr(self, 'management_template', n.get_object_value(ManagementTemplate)),
            "portalLink": lambda n : setattr(self, 'portal_link', n.get_object_value(ActionUrl)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "userImpact": lambda n : setattr(self, 'user_impact', n.get_str_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(ManagementTemplateStepVersion)),
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
        writer.write_object_value("acceptedVersion", self.accepted_version)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("informationLinks", self.information_links)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_object_value("managementTemplate", self.management_template)
        writer.write_object_value("portalLink", self.portal_link)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("userImpact", self.user_impact)
        writer.write_collection_of_object_values("versions", self.versions)
    

