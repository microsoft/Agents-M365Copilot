from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .scheduling_group_info import SchedulingGroupInfo
    from .shifts_team_info import ShiftsTeamInfo
    from .shifts_user_info import ShiftsUserInfo
    from .shift_item import ShiftItem

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class Shift(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.shift"
    # Draft changes in the shift. Draft changes are only visible to managers. The changes are visible to employees when they're shared, which copies the changes from the draftShift to the sharedShift property.
    draft_shift: Optional[ShiftItem] = None
    # The shift is marked for deletion, a process that is finalized when the schedule is shared.
    is_staged_for_deletion: Optional[bool] = None
    # ID of the scheduling group the shift is part of. Required.
    scheduling_group_id: Optional[str] = None
    # Information of the scheduling group the shift is part of.
    scheduling_group_info: Optional[SchedulingGroupInfo] = None
    # The shared version of this shift that is viewable by both employees and managers. Updates to the sharedShift property send notifications to users in the Teams client.
    shared_shift: Optional[ShiftItem] = None
    # Information of the team that the shift is in.
    team_info: Optional[ShiftsTeamInfo] = None
    # ID of the user assigned to the shift. Required.
    user_id: Optional[str] = None
    # Information of the user assigned to the shift.
    user_info: Optional[ShiftsUserInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Shift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Shift
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Shift()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .scheduling_group_info import SchedulingGroupInfo
        from .shifts_team_info import ShiftsTeamInfo
        from .shifts_user_info import ShiftsUserInfo
        from .shift_item import ShiftItem

        from .change_tracked_entity import ChangeTrackedEntity
        from .scheduling_group_info import SchedulingGroupInfo
        from .shifts_team_info import ShiftsTeamInfo
        from .shifts_user_info import ShiftsUserInfo
        from .shift_item import ShiftItem

        fields: dict[str, Callable[[Any], None]] = {
            "draftShift": lambda n : setattr(self, 'draft_shift', n.get_object_value(ShiftItem)),
            "isStagedForDeletion": lambda n : setattr(self, 'is_staged_for_deletion', n.get_bool_value()),
            "schedulingGroupId": lambda n : setattr(self, 'scheduling_group_id', n.get_str_value()),
            "schedulingGroupInfo": lambda n : setattr(self, 'scheduling_group_info', n.get_object_value(SchedulingGroupInfo)),
            "sharedShift": lambda n : setattr(self, 'shared_shift', n.get_object_value(ShiftItem)),
            "teamInfo": lambda n : setattr(self, 'team_info', n.get_object_value(ShiftsTeamInfo)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userInfo": lambda n : setattr(self, 'user_info', n.get_object_value(ShiftsUserInfo)),
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
        writer.write_object_value("draftShift", self.draft_shift)
        writer.write_bool_value("isStagedForDeletion", self.is_staged_for_deletion)
        writer.write_str_value("schedulingGroupId", self.scheduling_group_id)
        writer.write_object_value("sharedShift", self.shared_shift)
        writer.write_str_value("userId", self.user_id)
    

