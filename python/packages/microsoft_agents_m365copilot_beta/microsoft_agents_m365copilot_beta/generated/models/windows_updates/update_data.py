from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .applicable_catalog_summary import ApplicableCatalogSummary
    from .device_profile import DeviceProfile
    from .driver_update_report import DriverUpdateReport
    from .policy_assignment import PolicyAssignment

from ..entity import Entity

@dataclass
class UpdateData(Entity, Parsable):
    # Catalog applicability aggregated across Autopatch policies. Read-only.
    applicable_catalog_summaries: Optional[list[ApplicableCatalogSummary]] = None
    # Device profile and Windows servicing information. Read-only.
    device_profiles: Optional[list[DeviceProfile]] = None
    # Driver updates available in the tenant and their per-device rollout status. Read-only.
    drivers: Optional[list[DriverUpdateReport]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Assignments that associate Autopatch policies with devices. Read-only.
    policy_assignments: Optional[list[PolicyAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .applicable_catalog_summary import ApplicableCatalogSummary
        from .device_profile import DeviceProfile
        from .driver_update_report import DriverUpdateReport
        from .policy_assignment import PolicyAssignment

        from ..entity import Entity
        from .applicable_catalog_summary import ApplicableCatalogSummary
        from .device_profile import DeviceProfile
        from .driver_update_report import DriverUpdateReport
        from .policy_assignment import PolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "applicableCatalogSummaries": lambda n : setattr(self, 'applicable_catalog_summaries', n.get_collection_of_object_values(ApplicableCatalogSummary)),
            "deviceProfiles": lambda n : setattr(self, 'device_profiles', n.get_collection_of_object_values(DeviceProfile)),
            "drivers": lambda n : setattr(self, 'drivers', n.get_collection_of_object_values(DriverUpdateReport)),
            "policyAssignments": lambda n : setattr(self, 'policy_assignments', n.get_collection_of_object_values(PolicyAssignment)),
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
        writer.write_collection_of_object_values("applicableCatalogSummaries", self.applicable_catalog_summaries)
        writer.write_collection_of_object_values("deviceProfiles", self.device_profiles)
        writer.write_collection_of_object_values("drivers", self.drivers)
        writer.write_collection_of_object_values("policyAssignments", self.policy_assignments)
    

