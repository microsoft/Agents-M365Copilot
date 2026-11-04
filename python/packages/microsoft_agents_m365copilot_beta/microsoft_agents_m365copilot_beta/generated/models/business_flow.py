from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_flow_settings import BusinessFlowSettings
    from .entity import Entity
    from .governance_policy import GovernancePolicy

from .entity import Entity

@dataclass
class BusinessFlow(Entity, Parsable):
    # The customData property
    custom_data: Optional[str] = None
    # The deDuplicationId property
    de_duplication_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[GovernancePolicy] = None
    # The policyTemplateId property
    policy_template_id: Optional[str] = None
    # The recordVersion property
    record_version: Optional[str] = None
    # The schemaId property
    schema_id: Optional[str] = None
    # The settings property
    settings: Optional[BusinessFlowSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessFlow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_flow_settings import BusinessFlowSettings
        from .entity import Entity
        from .governance_policy import GovernancePolicy

        from .business_flow_settings import BusinessFlowSettings
        from .entity import Entity
        from .governance_policy import GovernancePolicy

        fields: dict[str, Callable[[Any], None]] = {
            "customData": lambda n : setattr(self, 'custom_data', n.get_str_value()),
            "deDuplicationId": lambda n : setattr(self, 'de_duplication_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(GovernancePolicy)),
            "policyTemplateId": lambda n : setattr(self, 'policy_template_id', n.get_str_value()),
            "recordVersion": lambda n : setattr(self, 'record_version', n.get_str_value()),
            "schemaId": lambda n : setattr(self, 'schema_id', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(BusinessFlowSettings)),
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
        writer.write_str_value("customData", self.custom_data)
        writer.write_str_value("deDuplicationId", self.de_duplication_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyTemplateId", self.policy_template_id)
        writer.write_str_value("recordVersion", self.record_version)
        writer.write_str_value("schemaId", self.schema_id)
        writer.write_object_value("settings", self.settings)
    

