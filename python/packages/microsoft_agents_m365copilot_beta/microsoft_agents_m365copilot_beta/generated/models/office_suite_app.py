from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .excluded_apps import ExcludedApps
    from .mobile_app import MobileApp
    from .office_product_id import OfficeProductId
    from .office_suite_default_file_format_type import OfficeSuiteDefaultFileFormatType
    from .office_suite_install_progress_display_level import OfficeSuiteInstallProgressDisplayLevel
    from .office_update_channel import OfficeUpdateChannel
    from .windows_architecture import WindowsArchitecture

from .mobile_app import MobileApp

@dataclass
class OfficeSuiteApp(MobileApp, Parsable):
    """
    Contains properties and inherited properties for the Office365 Suite App.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.officeSuiteApp"
    # The value to accept the EULA automatically on the enduser's device.
    auto_accept_eula: Optional[bool] = None
    # The property to represent the apps which are excluded from the selected Office365 Product Id.
    excluded_apps: Optional[ExcludedApps] = None
    # The Enum to specify the level of display for the Installation Progress Setup UI on the Device.
    install_progress_display_level: Optional[OfficeSuiteInstallProgressDisplayLevel] = None
    # The property to represent the locales which are installed when the apps from Office365 is installed. It uses standard RFC 6033. Ref: https://technet.microsoft.com/library/cc179219(v=office.16).aspx
    locales_to_install: Optional[list[str]] = None
    # The property to represent the XML configuration file that can be specified for Office ProPlus Apps. Takes precedence over all other properties. When present, the XML configuration file will be used to create the app.
    office_configuration_xml: Optional[bytes] = None
    # Contains properties for Windows architecture.
    office_platform_architecture: Optional[WindowsArchitecture] = None
    # Describes the OfficeSuiteApp file format types that can be selected.
    office_suite_app_default_file_format: Optional[OfficeSuiteDefaultFileFormatType] = None
    # The Product Ids that represent the Office365 Suite SKU.
    product_ids: Optional[list[OfficeProductId]] = None
    # The property to determine whether to uninstall existing Office MSI if an Office365 app suite is deployed to the device or not.
    should_uninstall_older_versions_of_office: Optional[bool] = None
    # The property to represent the specific target version for the Office365 app suite that should be remained deployed on the devices.
    target_version: Optional[str] = None
    # The Enum to specify the Office365 Updates Channel.
    update_channel: Optional[OfficeUpdateChannel] = None
    # The property to represent the update version in which the specific target version is available for the Office365 app suite.
    update_version: Optional[str] = None
    # The property to represent that whether the shared computer activation is used not for Office365 app suite.
    use_shared_computer_activation: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OfficeSuiteApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OfficeSuiteApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OfficeSuiteApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .excluded_apps import ExcludedApps
        from .mobile_app import MobileApp
        from .office_product_id import OfficeProductId
        from .office_suite_default_file_format_type import OfficeSuiteDefaultFileFormatType
        from .office_suite_install_progress_display_level import OfficeSuiteInstallProgressDisplayLevel
        from .office_update_channel import OfficeUpdateChannel
        from .windows_architecture import WindowsArchitecture

        from .excluded_apps import ExcludedApps
        from .mobile_app import MobileApp
        from .office_product_id import OfficeProductId
        from .office_suite_default_file_format_type import OfficeSuiteDefaultFileFormatType
        from .office_suite_install_progress_display_level import OfficeSuiteInstallProgressDisplayLevel
        from .office_update_channel import OfficeUpdateChannel
        from .windows_architecture import WindowsArchitecture

        fields: dict[str, Callable[[Any], None]] = {
            "autoAcceptEula": lambda n : setattr(self, 'auto_accept_eula', n.get_bool_value()),
            "excludedApps": lambda n : setattr(self, 'excluded_apps', n.get_object_value(ExcludedApps)),
            "installProgressDisplayLevel": lambda n : setattr(self, 'install_progress_display_level', n.get_enum_value(OfficeSuiteInstallProgressDisplayLevel)),
            "localesToInstall": lambda n : setattr(self, 'locales_to_install', n.get_collection_of_primitive_values(str)),
            "officeConfigurationXml": lambda n : setattr(self, 'office_configuration_xml', n.get_bytes_value()),
            "officePlatformArchitecture": lambda n : setattr(self, 'office_platform_architecture', n.get_collection_of_enum_values(WindowsArchitecture)),
            "officeSuiteAppDefaultFileFormat": lambda n : setattr(self, 'office_suite_app_default_file_format', n.get_enum_value(OfficeSuiteDefaultFileFormatType)),
            "productIds": lambda n : setattr(self, 'product_ids', n.get_collection_of_enum_values(OfficeProductId)),
            "shouldUninstallOlderVersionsOfOffice": lambda n : setattr(self, 'should_uninstall_older_versions_of_office', n.get_bool_value()),
            "targetVersion": lambda n : setattr(self, 'target_version', n.get_str_value()),
            "updateChannel": lambda n : setattr(self, 'update_channel', n.get_enum_value(OfficeUpdateChannel)),
            "updateVersion": lambda n : setattr(self, 'update_version', n.get_str_value()),
            "useSharedComputerActivation": lambda n : setattr(self, 'use_shared_computer_activation', n.get_bool_value()),
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
        writer.write_bool_value("autoAcceptEula", self.auto_accept_eula)
        writer.write_object_value("excludedApps", self.excluded_apps)
        writer.write_enum_value("installProgressDisplayLevel", self.install_progress_display_level)
        writer.write_collection_of_primitive_values("localesToInstall", self.locales_to_install)
        writer.write_bytes_value("officeConfigurationXml", self.office_configuration_xml)
        writer.write_enum_value("officePlatformArchitecture", self.office_platform_architecture)
        writer.write_enum_value("officeSuiteAppDefaultFileFormat", self.office_suite_app_default_file_format)
        writer.write_collection_of_enum_values("productIds", self.product_ids)
        writer.write_bool_value("shouldUninstallOlderVersionsOfOffice", self.should_uninstall_older_versions_of_office)
        writer.write_str_value("targetVersion", self.target_version)
        writer.write_enum_value("updateChannel", self.update_channel)
        writer.write_str_value("updateVersion", self.update_version)
        writer.write_bool_value("useSharedComputerActivation", self.use_shared_computer_activation)
    

