from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case import Case
    from .exposure_case_automation import ExposureCaseAutomation
    from .exposure_case_git_hub import ExposureCaseGitHub
    from .exposure_case_seemplicity import ExposureCaseSeemplicity
    from .third_party_work_item import ThirdPartyWorkItem

from .case import Case

@dataclass
class ExposureCase(Case, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.exposureCase"
    # The assignedTo property
    assigned_to: Optional[str] = None
    # The automation property
    automation: Optional[ExposureCaseAutomation] = None
    # The description property
    description: Optional[str] = None
    # The dueDateTime property
    due_date_time: Optional[datetime.datetime] = None
    # The emailNotificationRecipients property
    email_notification_recipients: Optional[list[str]] = None
    # The github property
    github: Optional[ExposureCaseGitHub] = None
    # The isGracePeriodEnabled property
    is_grace_period_enabled: Optional[bool] = None
    # The priority property
    priority: Optional[str] = None
    # The seemplicity property
    seemplicity: Optional[ExposureCaseSeemplicity] = None
    # The thirdPartyWorkItem property
    third_party_work_item: Optional[ThirdPartyWorkItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExposureCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExposureCase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExposureCase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case import Case
        from .exposure_case_automation import ExposureCaseAutomation
        from .exposure_case_git_hub import ExposureCaseGitHub
        from .exposure_case_seemplicity import ExposureCaseSeemplicity
        from .third_party_work_item import ThirdPartyWorkItem

        from .case import Case
        from .exposure_case_automation import ExposureCaseAutomation
        from .exposure_case_git_hub import ExposureCaseGitHub
        from .exposure_case_seemplicity import ExposureCaseSeemplicity
        from .third_party_work_item import ThirdPartyWorkItem

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "automation": lambda n : setattr(self, 'automation', n.get_object_value(ExposureCaseAutomation)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "emailNotificationRecipients": lambda n : setattr(self, 'email_notification_recipients', n.get_collection_of_primitive_values(str)),
            "github": lambda n : setattr(self, 'github', n.get_object_value(ExposureCaseGitHub)),
            "isGracePeriodEnabled": lambda n : setattr(self, 'is_grace_period_enabled', n.get_bool_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_str_value()),
            "seemplicity": lambda n : setattr(self, 'seemplicity', n.get_object_value(ExposureCaseSeemplicity)),
            "thirdPartyWorkItem": lambda n : setattr(self, 'third_party_work_item', n.get_object_value(ThirdPartyWorkItem)),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_object_value("automation", self.automation)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_collection_of_primitive_values("emailNotificationRecipients", self.email_notification_recipients)
        writer.write_object_value("github", self.github)
        writer.write_bool_value("isGracePeriodEnabled", self.is_grace_period_enabled)
        writer.write_str_value("priority", self.priority)
        writer.write_object_value("seemplicity", self.seemplicity)
        writer.write_object_value("thirdPartyWorkItem", self.third_party_work_item)
    

