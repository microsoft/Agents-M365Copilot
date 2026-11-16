from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .license_type import LicenseType

from .entity import Entity

@dataclass
class EndpointPrivilegeManagementProvisioningStatus(Entity, Parsable):
    """
    Endpoint privilege management (EPM) tenant provisioning status contains tenant level license and onboarding state information.
    """
    # Indicates whether tenant has a valid Intune Endpoint Privilege Management license. Possible value are : 0 - notPaid, 1 - paid, 2 - trial. See LicenseType enum for more details. Default notPaid .
    license_type: Optional[LicenseType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether tenant is onboarded to Microsoft Managed Platform - Cloud (MMPC). When set to true, implies tenant is onboarded and when set to false, implies tenant is not onboarded. Default set to false.
    onboarded_to_microsoft_managed_platform: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndpointPrivilegeManagementProvisioningStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndpointPrivilegeManagementProvisioningStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndpointPrivilegeManagementProvisioningStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .license_type import LicenseType

        from .entity import Entity
        from .license_type import LicenseType

        fields: dict[str, Callable[[Any], None]] = {
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(LicenseType)),
            "onboardedToMicrosoftManagedPlatform": lambda n : setattr(self, 'onboarded_to_microsoft_managed_platform', n.get_bool_value()),
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
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_bool_value("onboardedToMicrosoftManagedPlatform", self.onboarded_to_microsoft_managed_platform)
    

