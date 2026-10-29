from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_drift_source import AccessDriftSource
    from .access_drift_type import AccessDriftType
    from .drift_identity_info import DriftIdentityInfo
    from .drift_resource_info import DriftResourceInfo
    from .entity import Entity
    from .entra_access_drift_detail import EntraAccessDriftDetail

from .entity import Entity

@dataclass
class AccessDriftDetail(Entity, Parsable):
    # The date and time when the drift record was created.
    created_date_time: Optional[datetime.datetime] = None
    # The driftSource property
    drift_source: Optional[AccessDriftSource] = None
    # The driftType property
    drift_type: Optional[AccessDriftType] = None
    # The identities affected by this drift record.
    identities: Optional[list[DriftIdentityInfo]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resource property
    resource: Optional[DriftResourceInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessDriftDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessDriftDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entraAccessDriftDetail".casefold():
            from .entra_access_drift_detail import EntraAccessDriftDetail

            return EntraAccessDriftDetail()
        return AccessDriftDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_drift_source import AccessDriftSource
        from .access_drift_type import AccessDriftType
        from .drift_identity_info import DriftIdentityInfo
        from .drift_resource_info import DriftResourceInfo
        from .entity import Entity
        from .entra_access_drift_detail import EntraAccessDriftDetail

        from .access_drift_source import AccessDriftSource
        from .access_drift_type import AccessDriftType
        from .drift_identity_info import DriftIdentityInfo
        from .drift_resource_info import DriftResourceInfo
        from .entity import Entity
        from .entra_access_drift_detail import EntraAccessDriftDetail

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "driftSource": lambda n : setattr(self, 'drift_source', n.get_enum_value(AccessDriftSource)),
            "driftType": lambda n : setattr(self, 'drift_type', n.get_enum_value(AccessDriftType)),
            "identities": lambda n : setattr(self, 'identities', n.get_collection_of_object_values(DriftIdentityInfo)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(DriftResourceInfo)),
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
        writer.write_enum_value("driftSource", self.drift_source)
        writer.write_enum_value("driftType", self.drift_type)
        writer.write_collection_of_object_values("identities", self.identities)
        writer.write_object_value("resource", self.resource)
    

