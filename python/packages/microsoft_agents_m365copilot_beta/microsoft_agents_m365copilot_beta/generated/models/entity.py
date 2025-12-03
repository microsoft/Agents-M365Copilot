from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent import Agent
    from .ai_interaction import AiInteraction
    from .ai_interaction_history import AiInteractionHistory
    from .ai_online_meeting import AiOnlineMeeting
    from .ai_user import AiUser
    from .call_ai_insight import CallAiInsight
    from .copilot_admin import CopilotAdmin
    from .copilot_admin_catalog import CopilotAdminCatalog
    from .copilot_admin_limited_mode import CopilotAdminLimitedMode
    from .copilot_admin_setting import CopilotAdminSetting
    from .copilot_communications_root import CopilotCommunicationsRoot
    from .copilot_package import CopilotPackage
    from .copilot_package_detail import CopilotPackageDetail
    from .copilot_people_admin_setting import CopilotPeopleAdminSetting
    from .copilot_report_root import CopilotReportRoot
    from .copilot_setting import CopilotSetting
    from .enhanced_personalization_setting import EnhancedPersonalizationSetting
    from .multi_activity_subscription import MultiActivitySubscription
    from .realtime_activity_feed_root import RealtimeActivityFeedRoot
    from .realtime_activity_meeting import RealtimeActivityMeeting
    from .real_time_transcript import RealTimeTranscript

@dataclass
class Entity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The unique identifier for an entity. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Entity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Entity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agent".casefold():
            from .agent import Agent

            return Agent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteraction".casefold():
            from .ai_interaction import AiInteraction

            return AiInteraction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteractionHistory".casefold():
            from .ai_interaction_history import AiInteractionHistory

            return AiInteractionHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiOnlineMeeting".casefold():
            from .ai_online_meeting import AiOnlineMeeting

            return AiOnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiUser".casefold():
            from .ai_user import AiUser

            return AiUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callAiInsight".casefold():
            from .call_ai_insight import CallAiInsight

            return CallAiInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdmin".casefold():
            from .copilot_admin import CopilotAdmin

            return CopilotAdmin()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminCatalog".casefold():
            from .copilot_admin_catalog import CopilotAdminCatalog

            return CopilotAdminCatalog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminLimitedMode".casefold():
            from .copilot_admin_limited_mode import CopilotAdminLimitedMode

            return CopilotAdminLimitedMode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminSetting".casefold():
            from .copilot_admin_setting import CopilotAdminSetting

            return CopilotAdminSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotCommunicationsRoot".casefold():
            from .copilot_communications_root import CopilotCommunicationsRoot

            return CopilotCommunicationsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotPackage".casefold():
            from .copilot_package import CopilotPackage

            return CopilotPackage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotPackageDetail".casefold():
            from .copilot_package_detail import CopilotPackageDetail

            return CopilotPackageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotPeopleAdminSetting".casefold():
            from .copilot_people_admin_setting import CopilotPeopleAdminSetting

            return CopilotPeopleAdminSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotReportRoot".casefold():
            from .copilot_report_root import CopilotReportRoot

            return CopilotReportRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotSetting".casefold():
            from .copilot_setting import CopilotSetting

            return CopilotSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enhancedPersonalizationSetting".casefold():
            from .enhanced_personalization_setting import EnhancedPersonalizationSetting

            return EnhancedPersonalizationSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiActivitySubscription".casefold():
            from .multi_activity_subscription import MultiActivitySubscription

            return MultiActivitySubscription()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.realtimeActivityFeedRoot".casefold():
            from .realtime_activity_feed_root import RealtimeActivityFeedRoot

            return RealtimeActivityFeedRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.realtimeActivityMeeting".casefold():
            from .realtime_activity_meeting import RealtimeActivityMeeting

            return RealtimeActivityMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.realTimeTranscript".casefold():
            from .real_time_transcript import RealTimeTranscript

            return RealTimeTranscript()
        return Entity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent import Agent
        from .ai_interaction import AiInteraction
        from .ai_interaction_history import AiInteractionHistory
        from .ai_online_meeting import AiOnlineMeeting
        from .ai_user import AiUser
        from .call_ai_insight import CallAiInsight
        from .copilot_admin import CopilotAdmin
        from .copilot_admin_catalog import CopilotAdminCatalog
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .copilot_admin_setting import CopilotAdminSetting
        from .copilot_communications_root import CopilotCommunicationsRoot
        from .copilot_package import CopilotPackage
        from .copilot_package_detail import CopilotPackageDetail
        from .copilot_people_admin_setting import CopilotPeopleAdminSetting
        from .copilot_report_root import CopilotReportRoot
        from .copilot_setting import CopilotSetting
        from .enhanced_personalization_setting import EnhancedPersonalizationSetting
        from .multi_activity_subscription import MultiActivitySubscription
        from .realtime_activity_feed_root import RealtimeActivityFeedRoot
        from .realtime_activity_meeting import RealtimeActivityMeeting
        from .real_time_transcript import RealTimeTranscript

        from .agent import Agent
        from .ai_interaction import AiInteraction
        from .ai_interaction_history import AiInteractionHistory
        from .ai_online_meeting import AiOnlineMeeting
        from .ai_user import AiUser
        from .call_ai_insight import CallAiInsight
        from .copilot_admin import CopilotAdmin
        from .copilot_admin_catalog import CopilotAdminCatalog
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .copilot_admin_setting import CopilotAdminSetting
        from .copilot_communications_root import CopilotCommunicationsRoot
        from .copilot_package import CopilotPackage
        from .copilot_package_detail import CopilotPackageDetail
        from .copilot_people_admin_setting import CopilotPeopleAdminSetting
        from .copilot_report_root import CopilotReportRoot
        from .copilot_setting import CopilotSetting
        from .enhanced_personalization_setting import EnhancedPersonalizationSetting
        from .multi_activity_subscription import MultiActivitySubscription
        from .realtime_activity_feed_root import RealtimeActivityFeedRoot
        from .realtime_activity_meeting import RealtimeActivityMeeting
        from .real_time_transcript import RealTimeTranscript

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

