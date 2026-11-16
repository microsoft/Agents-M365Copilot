from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .entity import Entity
    from .risk_profile import RiskProfile

from .entity import Entity

@dataclass
class PermissionsCreepIndexDistribution(Entity, Parsable):
    # The authorizationSystem property
    authorization_system: Optional[AuthorizationSystem] = None
    # Defines when the PCI distribution was created.
    created_date_time: Optional[datetime.datetime] = None
    # The highRiskProfile property
    high_risk_profile: Optional[RiskProfile] = None
    # The lowRiskProfile property
    low_risk_profile: Optional[RiskProfile] = None
    # The mediumRiskProfile property
    medium_risk_profile: Optional[RiskProfile] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionsCreepIndexDistribution:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsCreepIndexDistribution
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionsCreepIndexDistribution()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .entity import Entity
        from .risk_profile import RiskProfile

        from .authorization_system import AuthorizationSystem
        from .entity import Entity
        from .risk_profile import RiskProfile

        fields: dict[str, Callable[[Any], None]] = {
            "authorizationSystem": lambda n : setattr(self, 'authorization_system', n.get_object_value(AuthorizationSystem)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "highRiskProfile": lambda n : setattr(self, 'high_risk_profile', n.get_object_value(RiskProfile)),
            "lowRiskProfile": lambda n : setattr(self, 'low_risk_profile', n.get_object_value(RiskProfile)),
            "mediumRiskProfile": lambda n : setattr(self, 'medium_risk_profile', n.get_object_value(RiskProfile)),
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
        writer.write_object_value("authorizationSystem", self.authorization_system)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("highRiskProfile", self.high_risk_profile)
        writer.write_object_value("lowRiskProfile", self.low_risk_profile)
        writer.write_object_value("mediumRiskProfile", self.medium_risk_profile)
    

