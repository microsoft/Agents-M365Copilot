from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ServicePrincipalCreationConditionSet(Entity, Parsable):
    # The applicationIds property
    application_ids: Optional[list[str]] = None
    # The applicationPublisherIds property
    application_publisher_ids: Optional[list[str]] = None
    # The applicationTenantIds property
    application_tenant_ids: Optional[list[str]] = None
    # The applicationsFromVerifiedPublisherOnly property
    applications_from_verified_publisher_only: Optional[bool] = None
    # The certifiedApplicationsOnly property
    certified_applications_only: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalCreationConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalCreationConditionSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalCreationConditionSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "applicationIds": lambda n : setattr(self, 'application_ids', n.get_collection_of_primitive_values(str)),
            "applicationPublisherIds": lambda n : setattr(self, 'application_publisher_ids', n.get_collection_of_primitive_values(str)),
            "applicationTenantIds": lambda n : setattr(self, 'application_tenant_ids', n.get_collection_of_primitive_values(str)),
            "applicationsFromVerifiedPublisherOnly": lambda n : setattr(self, 'applications_from_verified_publisher_only', n.get_bool_value()),
            "certifiedApplicationsOnly": lambda n : setattr(self, 'certified_applications_only', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("applicationIds", self.application_ids)
        writer.write_collection_of_primitive_values("applicationPublisherIds", self.application_publisher_ids)
        writer.write_collection_of_primitive_values("applicationTenantIds", self.application_tenant_ids)
        writer.write_bool_value("applicationsFromVerifiedPublisherOnly", self.applications_from_verified_publisher_only)
        writer.write_bool_value("certifiedApplicationsOnly", self.certified_applications_only)
    

