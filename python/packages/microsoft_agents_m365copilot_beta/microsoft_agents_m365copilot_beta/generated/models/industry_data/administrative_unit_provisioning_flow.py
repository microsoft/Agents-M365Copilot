from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin_unit_creation_options import AdminUnitCreationOptions
    from .provisioning_flow import ProvisioningFlow

from .provisioning_flow import ProvisioningFlow

@dataclass
class AdministrativeUnitProvisioningFlow(ProvisioningFlow, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.administrativeUnitProvisioningFlow"
    # The creationOptions property
    creation_options: Optional[AdminUnitCreationOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdministrativeUnitProvisioningFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdministrativeUnitProvisioningFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdministrativeUnitProvisioningFlow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .admin_unit_creation_options import AdminUnitCreationOptions
        from .provisioning_flow import ProvisioningFlow

        from .admin_unit_creation_options import AdminUnitCreationOptions
        from .provisioning_flow import ProvisioningFlow

        fields: dict[str, Callable[[Any], None]] = {
            "creationOptions": lambda n : setattr(self, 'creation_options', n.get_object_value(AdminUnitCreationOptions)),
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
        writer.write_object_value("creationOptions", self.creation_options)
    

