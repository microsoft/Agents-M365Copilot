from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow
    from .class_group_provisioning_flow import ClassGroupProvisioningFlow
    from .readiness_status import ReadinessStatus
    from .security_group_provisioning_flow import SecurityGroupProvisioningFlow
    from .user_provisioning_flow import UserProvisioningFlow

from ..entity import Entity

@dataclass
class ProvisioningFlow(Entity, Parsable):
    # The date and time when the provisioning flow was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the provisioning flow was most recently changed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of the activity from creation through to ready to do work. The possible values are: notReady, ready, failed, disabled, expired, unknownFutureValue.
    readiness_status: Optional[ReadinessStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisioningFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.administrativeUnitProvisioningFlow".casefold():
            from .administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow

            return AdministrativeUnitProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.classGroupProvisioningFlow".casefold():
            from .class_group_provisioning_flow import ClassGroupProvisioningFlow

            return ClassGroupProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.securityGroupProvisioningFlow".casefold():
            from .security_group_provisioning_flow import SecurityGroupProvisioningFlow

            return SecurityGroupProvisioningFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.userProvisioningFlow".casefold():
            from .user_provisioning_flow import UserProvisioningFlow

            return UserProvisioningFlow()
        return ProvisioningFlow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow
        from .class_group_provisioning_flow import ClassGroupProvisioningFlow
        from .readiness_status import ReadinessStatus
        from .security_group_provisioning_flow import SecurityGroupProvisioningFlow
        from .user_provisioning_flow import UserProvisioningFlow

        from ..entity import Entity
        from .administrative_unit_provisioning_flow import AdministrativeUnitProvisioningFlow
        from .class_group_provisioning_flow import ClassGroupProvisioningFlow
        from .readiness_status import ReadinessStatus
        from .security_group_provisioning_flow import SecurityGroupProvisioningFlow
        from .user_provisioning_flow import UserProvisioningFlow

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "readinessStatus": lambda n : setattr(self, 'readiness_status', n.get_enum_value(ReadinessStatus)),
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
    

