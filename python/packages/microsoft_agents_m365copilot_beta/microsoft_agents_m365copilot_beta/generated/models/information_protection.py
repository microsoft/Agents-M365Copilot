from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bitlocker import Bitlocker
    from .data_loss_prevention_policy import DataLossPreventionPolicy
    from .entity import Entity
    from .information_protection_policy import InformationProtectionPolicy
    from .sensitivity_label import SensitivityLabel
    from .sensitivity_policy_settings import SensitivityPolicySettings
    from .threat_assessment_request import ThreatAssessmentRequest

from .entity import Entity

@dataclass
class InformationProtection(Entity, Parsable):
    # The bitlocker property
    bitlocker: Optional[Bitlocker] = None
    # The dataLossPreventionPolicies property
    data_loss_prevention_policies: Optional[list[DataLossPreventionPolicy]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[InformationProtectionPolicy] = None
    # The sensitivityLabels property
    sensitivity_labels: Optional[list[SensitivityLabel]] = None
    # The sensitivityPolicySettings property
    sensitivity_policy_settings: Optional[SensitivityPolicySettings] = None
    # The threatAssessmentRequests property
    threat_assessment_requests: Optional[list[ThreatAssessmentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InformationProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bitlocker import Bitlocker
        from .data_loss_prevention_policy import DataLossPreventionPolicy
        from .entity import Entity
        from .information_protection_policy import InformationProtectionPolicy
        from .sensitivity_label import SensitivityLabel
        from .sensitivity_policy_settings import SensitivityPolicySettings
        from .threat_assessment_request import ThreatAssessmentRequest

        from .bitlocker import Bitlocker
        from .data_loss_prevention_policy import DataLossPreventionPolicy
        from .entity import Entity
        from .information_protection_policy import InformationProtectionPolicy
        from .sensitivity_label import SensitivityLabel
        from .sensitivity_policy_settings import SensitivityPolicySettings
        from .threat_assessment_request import ThreatAssessmentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "bitlocker": lambda n : setattr(self, 'bitlocker', n.get_object_value(Bitlocker)),
            "dataLossPreventionPolicies": lambda n : setattr(self, 'data_loss_prevention_policies', n.get_collection_of_object_values(DataLossPreventionPolicy)),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(InformationProtectionPolicy)),
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(SensitivityLabel)),
            "sensitivityPolicySettings": lambda n : setattr(self, 'sensitivity_policy_settings', n.get_object_value(SensitivityPolicySettings)),
            "threatAssessmentRequests": lambda n : setattr(self, 'threat_assessment_requests', n.get_collection_of_object_values(ThreatAssessmentRequest)),
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
        writer.write_object_value("bitlocker", self.bitlocker)
        writer.write_collection_of_object_values("dataLossPreventionPolicies", self.data_loss_prevention_policies)
        writer.write_object_value("policy", self.policy)
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
        writer.write_object_value("sensitivityPolicySettings", self.sensitivity_policy_settings)
        writer.write_collection_of_object_values("threatAssessmentRequests", self.threat_assessment_requests)
    

