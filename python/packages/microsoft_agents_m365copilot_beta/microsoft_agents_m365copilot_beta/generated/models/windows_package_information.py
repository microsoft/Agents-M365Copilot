from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_architecture import WindowsArchitecture
    from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

@dataclass
class WindowsPackageInformation(AdditionalDataHolder, Parsable):
    """
    Contains properties for the package information for a Windows line-of-business app. Used as property within windowsPhone81AppXBundle object, which is also being deprecated. This complex type will be deprecated in February 2023.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains properties for Windows architecture.
    applicable_architecture: Optional[WindowsArchitecture] = None
    # The Display Name.
    display_name: Optional[str] = None
    # The Identity Name.
    identity_name: Optional[str] = None
    # The Identity Publisher.
    identity_publisher: Optional[str] = None
    # The Identity Resource Identifier.
    identity_resource_identifier: Optional[str] = None
    # The Identity Version.
    identity_version: Optional[str] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[WindowsMinimumOperatingSystem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPackageInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPackageInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPackageInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_architecture import WindowsArchitecture
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

        from .windows_architecture import WindowsArchitecture
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

        fields: dict[str, Callable[[Any], None]] = {
            "applicableArchitecture": lambda n : setattr(self, 'applicable_architecture', n.get_collection_of_enum_values(WindowsArchitecture)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "identityName": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identityPublisher": lambda n : setattr(self, 'identity_publisher', n.get_str_value()),
            "identityResourceIdentifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(WindowsMinimumOperatingSystem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("applicableArchitecture", self.applicable_architecture)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisher", self.identity_publisher)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

