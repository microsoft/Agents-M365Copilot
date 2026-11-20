from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_drift_detail import AccessDriftDetail
    from .drift_access_package_info import DriftAccessPackageInfo

from .access_drift_detail import AccessDriftDetail

@dataclass
class EntraAccessDriftDetail(AccessDriftDetail, Parsable):
    # The access package associated with this drift record.
    access_package: Optional[DriftAccessPackageInfo] = None
    # The role currently assigned to the identity on the resource.
    assigned_role: Optional[str] = None
    # The role expected based on the access package assignment.
    expected_role: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntraAccessDriftDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntraAccessDriftDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntraAccessDriftDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_drift_detail import AccessDriftDetail
        from .drift_access_package_info import DriftAccessPackageInfo

        from .access_drift_detail import AccessDriftDetail
        from .drift_access_package_info import DriftAccessPackageInfo

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(DriftAccessPackageInfo)),
            "assignedRole": lambda n : setattr(self, 'assigned_role', n.get_str_value()),
            "expectedRole": lambda n : setattr(self, 'expected_role', n.get_str_value()),
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
    

