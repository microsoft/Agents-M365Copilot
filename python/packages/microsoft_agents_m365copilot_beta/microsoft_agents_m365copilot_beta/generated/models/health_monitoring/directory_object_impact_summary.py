from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..directory_object import DirectoryObject
    from .application_impact_summary import ApplicationImpactSummary
    from .device_impact_summary import DeviceImpactSummary
    from .group_impact_summary import GroupImpactSummary
    from .resource_impact_summary import ResourceImpactSummary
    from .service_principal_impact_summary import ServicePrincipalImpactSummary
    from .user_impact_summary import UserImpactSummary

from .resource_impact_summary import ResourceImpactSummary

@dataclass
class DirectoryObjectImpactSummary(ResourceImpactSummary, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.healthMonitoring.directoryObjectImpactSummary"
    # The resourceSampling property
    resource_sampling: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectoryObjectImpactSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObjectImpactSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.applicationImpactSummary".casefold():
            from .application_impact_summary import ApplicationImpactSummary

            return ApplicationImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.deviceImpactSummary".casefold():
            from .device_impact_summary import DeviceImpactSummary

            return DeviceImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.groupImpactSummary".casefold():
            from .group_impact_summary import GroupImpactSummary

            return GroupImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.servicePrincipalImpactSummary".casefold():
            from .service_principal_impact_summary import ServicePrincipalImpactSummary

            return ServicePrincipalImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.userImpactSummary".casefold():
            from .user_impact_summary import UserImpactSummary

            return UserImpactSummary()
        return DirectoryObjectImpactSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..directory_object import DirectoryObject
        from .application_impact_summary import ApplicationImpactSummary
        from .device_impact_summary import DeviceImpactSummary
        from .group_impact_summary import GroupImpactSummary
        from .resource_impact_summary import ResourceImpactSummary
        from .service_principal_impact_summary import ServicePrincipalImpactSummary
        from .user_impact_summary import UserImpactSummary

        from ..directory_object import DirectoryObject
        from .application_impact_summary import ApplicationImpactSummary
        from .device_impact_summary import DeviceImpactSummary
        from .group_impact_summary import GroupImpactSummary
        from .resource_impact_summary import ResourceImpactSummary
        from .service_principal_impact_summary import ServicePrincipalImpactSummary
        from .user_impact_summary import UserImpactSummary

        fields: dict[str, Callable[[Any], None]] = {
            "resourceSampling": lambda n : setattr(self, 'resource_sampling', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_collection_of_object_values("resourceSampling", self.resource_sampling)
    

