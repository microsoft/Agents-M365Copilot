from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_aosp_referenced_app import AndroidAospReferencedApp
    from .android_for_work_app import AndroidForWorkApp
    from .android_lob_app import AndroidLobApp
    from .android_managed_store_app import AndroidManagedStoreApp
    from .android_managed_store_web_app import AndroidManagedStoreWebApp
    from .android_store_app import AndroidStoreApp
    from .entity import Entity
    from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
    from .ios_lob_app import IosLobApp
    from .ios_store_app import IosStoreApp
    from .ios_vpp_app import IosVppApp
    from .mac_os_vpp_app import MacOsVppApp
    from .mac_o_s_dmg_app import MacOSDmgApp
    from .mac_o_s_lob_app import MacOSLobApp
    from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
    from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
    from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
    from .mac_o_s_pkg_app import MacOSPkgApp
    from .mac_o_s_web_clip import MacOSWebClip
    from .managed_android_lob_app import ManagedAndroidLobApp
    from .managed_android_store_app import ManagedAndroidStoreApp
    from .managed_app import ManagedApp
    from .managed_i_o_s_lob_app import ManagedIOSLobApp
    from .managed_i_o_s_store_app import ManagedIOSStoreApp
    from .managed_mobile_lob_app import ManagedMobileLobApp
    from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
    from .mime_content import MimeContent
    from .mobile_app_assignment import MobileAppAssignment
    from .mobile_app_category import MobileAppCategory
    from .mobile_app_publishing_state import MobileAppPublishingState
    from .mobile_app_relationship import MobileAppRelationship
    from .mobile_lob_app import MobileLobApp
    from .office_suite_app import OfficeSuiteApp
    from .web_app import WebApp
    from .win32_catalog_app import Win32CatalogApp
    from .win32_lob_app import Win32LobApp
    from .windows_app_x import WindowsAppX
    from .windows_auto_update_catalog_app import WindowsAutoUpdateCatalogApp
    from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
    from .windows_mobile_m_s_i import WindowsMobileMSI
    from .windows_phone81_app_x import WindowsPhone81AppX
    from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
    from .windows_phone81_store_app import WindowsPhone81StoreApp
    from .windows_phone_x_a_p import WindowsPhoneXAP
    from .windows_store_app import WindowsStoreApp
    from .windows_universal_app_x import WindowsUniversalAppX
    from .windows_web_app import WindowsWebApp
    from .win_get_app import WinGetApp

from .entity import Entity

@dataclass
class MobileApp(Entity, Parsable):
    """
    An abstract class containing the base properties for Intune mobile apps. Note: Listing mobile apps with `$expand=assignments` has been deprecated. Instead get the list of apps without the `$expand` query on `assignments`. Then, perform the expansion on individual applications.
    """
    # The list of group assignments for this mobile app.
    assignments: Optional[list[MobileAppAssignment]] = None
    # The list of categories for this app.
    categories: Optional[list[MobileAppCategory]] = None
    # The date and time the app was created. This property is read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The total number of dependencies the child app has. This property is read-only.
    dependent_app_count: Optional[int] = None
    # The description of the app.
    description: Optional[str] = None
    # The developer of the app.
    developer: Optional[str] = None
    # The admin provided or imported title of the app.
    display_name: Optional[str] = None
    # The more information Url.
    information_url: Optional[str] = None
    # The value indicating whether the app is assigned to at least one group. This property is read-only.
    is_assigned: Optional[bool] = None
    # The value indicating whether the app is marked as featured by the admin.
    is_featured: Optional[bool] = None
    # The large icon, to be displayed in the app details and used for upload of the icon.
    large_icon: Optional[MimeContent] = None
    # The date and time the app was last modified. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Notes for the app.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The owner of the app.
    owner: Optional[str] = None
    # The privacy statement Url.
    privacy_information_url: Optional[str] = None
    # The publisher of the app.
    publisher: Optional[str] = None
    # Indicates the publishing state of an app.
    publishing_state: Optional[MobileAppPublishingState] = None
    # The set of direct relationships for this app.
    relationships: Optional[list[MobileAppRelationship]] = None
    # List of scope tag ids for this mobile app.
    role_scope_tag_ids: Optional[list[str]] = None
    # The total number of apps this app is directly or indirectly superseded by. This property is read-only.
    superseded_app_count: Optional[int] = None
    # The total number of apps this app directly or indirectly supersedes. This property is read-only.
    superseding_app_count: Optional[int] = None
    # The upload state. Possible values are: 0 - Not Ready, 1 - Ready, 2 - Processing. This property is read-only.
    upload_state: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidAospReferencedApp".casefold():
            from .android_aosp_referenced_app import AndroidAospReferencedApp

            return AndroidAospReferencedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkApp".casefold():
            from .android_for_work_app import AndroidForWorkApp

            return AndroidForWorkApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidLobApp".casefold():
            from .android_lob_app import AndroidLobApp

            return AndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreApp".casefold():
            from .android_managed_store_app import AndroidManagedStoreApp

            return AndroidManagedStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreWebApp".casefold():
            from .android_managed_store_web_app import AndroidManagedStoreWebApp

            return AndroidManagedStoreWebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidStoreApp".casefold():
            from .android_store_app import AndroidStoreApp

            return AndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosiPadOSWebClip".casefold():
            from .iosi_pad_o_s_web_clip import IosiPadOSWebClip

            return IosiPadOSWebClip()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobApp".casefold():
            from .ios_lob_app import IosLobApp

            return IosLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosStoreApp".casefold():
            from .ios_store_app import IosStoreApp

            return IosStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppApp".casefold():
            from .ios_vpp_app import IosVppApp

            return IosVppApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDmgApp".casefold():
            from .mac_o_s_dmg_app import MacOSDmgApp

            return MacOSDmgApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSLobApp".casefold():
            from .mac_o_s_lob_app import MacOSLobApp

            return MacOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftDefenderApp".casefold():
            from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp

            return MacOSMicrosoftDefenderApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftEdgeApp".casefold():
            from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp

            return MacOSMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSOfficeSuiteApp".casefold():
            from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp

            return MacOSOfficeSuiteApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkgApp".casefold():
            from .mac_o_s_pkg_app import MacOSPkgApp

            return MacOSPkgApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOsVppApp".casefold():
            from .mac_os_vpp_app import MacOsVppApp

            return MacOsVppApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSWebClip".casefold():
            from .mac_o_s_web_clip import MacOSWebClip

            return MacOSWebClip()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from .managed_android_lob_app import ManagedAndroidLobApp

            return ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidStoreApp".casefold():
            from .managed_android_store_app import ManagedAndroidStoreApp

            return ManagedAndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedApp".casefold():
            from .managed_app import ManagedApp

            return ManagedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from .managed_i_o_s_lob_app import ManagedIOSLobApp

            return ManagedIOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSStoreApp".casefold():
            from .managed_i_o_s_store_app import ManagedIOSStoreApp

            return ManagedIOSStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileLobApp".casefold():
            from .managed_mobile_lob_app import ManagedMobileLobApp

            return ManagedMobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftStoreForBusinessApp".casefold():
            from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp

            return MicrosoftStoreForBusinessApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileLobApp".casefold():
            from .mobile_lob_app import MobileLobApp

            return MobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.officeSuiteApp".casefold():
            from .office_suite_app import OfficeSuiteApp

            return OfficeSuiteApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApp".casefold():
            from .web_app import WebApp

            return WebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32CatalogApp".casefold():
            from .win32_catalog_app import Win32CatalogApp

            return Win32CatalogApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobApp".casefold():
            from .win32_lob_app import Win32LobApp

            return Win32LobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppX".casefold():
            from .windows_app_x import WindowsAppX

            return WindowsAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutoUpdateCatalogApp".casefold():
            from .windows_auto_update_catalog_app import WindowsAutoUpdateCatalogApp

            return WindowsAutoUpdateCatalogApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMicrosoftEdgeApp".casefold():
            from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp

            return WindowsMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMobileMSI".casefold():
            from .windows_mobile_m_s_i import WindowsMobileMSI

            return WindowsMobileMSI()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81AppX".casefold():
            from .windows_phone81_app_x import WindowsPhone81AppX

            return WindowsPhone81AppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81AppXBundle".casefold():
            from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

            return WindowsPhone81AppXBundle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81StoreApp".casefold():
            from .windows_phone81_store_app import WindowsPhone81StoreApp

            return WindowsPhone81StoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhoneXAP".casefold():
            from .windows_phone_x_a_p import WindowsPhoneXAP

            return WindowsPhoneXAP()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsStoreApp".casefold():
            from .windows_store_app import WindowsStoreApp

            return WindowsStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppX".casefold():
            from .windows_universal_app_x import WindowsUniversalAppX

            return WindowsUniversalAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWebApp".casefold():
            from .windows_web_app import WindowsWebApp

            return WindowsWebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.winGetApp".casefold():
            from .win_get_app import WinGetApp

            return WinGetApp()
        return MobileApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_aosp_referenced_app import AndroidAospReferencedApp
        from .android_for_work_app import AndroidForWorkApp
        from .android_lob_app import AndroidLobApp
        from .android_managed_store_app import AndroidManagedStoreApp
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .android_store_app import AndroidStoreApp
        from .entity import Entity
        from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
        from .ios_lob_app import IosLobApp
        from .ios_store_app import IosStoreApp
        from .ios_vpp_app import IosVppApp
        from .mac_os_vpp_app import MacOsVppApp
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_lob_app import MacOSLobApp
        from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
        from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
        from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
        from .mac_o_s_pkg_app import MacOSPkgApp
        from .mac_o_s_web_clip import MacOSWebClip
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app import ManagedApp
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
        from .mime_content import MimeContent
        from .mobile_app_assignment import MobileAppAssignment
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_publishing_state import MobileAppPublishingState
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_lob_app import MobileLobApp
        from .office_suite_app import OfficeSuiteApp
        from .web_app import WebApp
        from .win32_catalog_app import Win32CatalogApp
        from .win32_lob_app import Win32LobApp
        from .windows_app_x import WindowsAppX
        from .windows_auto_update_catalog_app import WindowsAutoUpdateCatalogApp
        from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_phone81_app_x import WindowsPhone81AppX
        from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
        from .windows_phone81_store_app import WindowsPhone81StoreApp
        from .windows_phone_x_a_p import WindowsPhoneXAP
        from .windows_store_app import WindowsStoreApp
        from .windows_universal_app_x import WindowsUniversalAppX
        from .windows_web_app import WindowsWebApp
        from .win_get_app import WinGetApp

        from .android_aosp_referenced_app import AndroidAospReferencedApp
        from .android_for_work_app import AndroidForWorkApp
        from .android_lob_app import AndroidLobApp
        from .android_managed_store_app import AndroidManagedStoreApp
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .android_store_app import AndroidStoreApp
        from .entity import Entity
        from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
        from .ios_lob_app import IosLobApp
        from .ios_store_app import IosStoreApp
        from .ios_vpp_app import IosVppApp
        from .mac_os_vpp_app import MacOsVppApp
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_lob_app import MacOSLobApp
        from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
        from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
        from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
        from .mac_o_s_pkg_app import MacOSPkgApp
        from .mac_o_s_web_clip import MacOSWebClip
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app import ManagedApp
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
        from .mime_content import MimeContent
        from .mobile_app_assignment import MobileAppAssignment
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_publishing_state import MobileAppPublishingState
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_lob_app import MobileLobApp
        from .office_suite_app import OfficeSuiteApp
        from .web_app import WebApp
        from .win32_catalog_app import Win32CatalogApp
        from .win32_lob_app import Win32LobApp
        from .windows_app_x import WindowsAppX
        from .windows_auto_update_catalog_app import WindowsAutoUpdateCatalogApp
        from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_phone81_app_x import WindowsPhone81AppX
        from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
        from .windows_phone81_store_app import WindowsPhone81StoreApp
        from .windows_phone_x_a_p import WindowsPhoneXAP
        from .windows_store_app import WindowsStoreApp
        from .windows_universal_app_x import WindowsUniversalAppX
        from .windows_web_app import WindowsWebApp
        from .win_get_app import WinGetApp

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(MobileAppAssignment)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(MobileAppCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dependentAppCount": lambda n : setattr(self, 'dependent_app_count', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "developer": lambda n : setattr(self, 'developer', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationUrl": lambda n : setattr(self, 'information_url', n.get_str_value()),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "largeIcon": lambda n : setattr(self, 'large_icon', n.get_object_value(MimeContent)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "privacyInformationUrl": lambda n : setattr(self, 'privacy_information_url', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "publishingState": lambda n : setattr(self, 'publishing_state', n.get_enum_value(MobileAppPublishingState)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_collection_of_object_values(MobileAppRelationship)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "supersededAppCount": lambda n : setattr(self, 'superseded_app_count', n.get_int_value()),
            "supersedingAppCount": lambda n : setattr(self, 'superseding_app_count', n.get_int_value()),
            "uploadState": lambda n : setattr(self, 'upload_state', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("developer", self.developer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("informationUrl", self.information_url)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_object_value("largeIcon", self.large_icon)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("privacyInformationUrl", self.privacy_information_url)
        writer.write_str_value("publisher", self.publisher)
        writer.write_enum_value("publishingState", self.publishing_state)
        writer.write_collection_of_object_values("relationships", self.relationships)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

