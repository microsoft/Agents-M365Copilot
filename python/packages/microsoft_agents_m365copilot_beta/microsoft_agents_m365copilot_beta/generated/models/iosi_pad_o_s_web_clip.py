from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class IosiPadOSWebClip(MobileApp, Parsable):
    """
    Contains properties and inherited properties for iOS web apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosiPadOSWebClip"
    # Indicates iOS/iPadOS web clip app URL. Example: 'https://www.contoso.com'
    app_url: Optional[str] = None
    # Whether or not to open the web clip as a full-screen web app. Defaults to false. If TRUE, opens the web clip as a full-screen web app. If FALSE, the web clip opens inside of another app, such as Safari or the app specified with targetApplicationBundleIdentifier.
    full_screen_enabled: Optional[bool] = None
    # Whether or not a full screen web clip can navigate to an external web site without showing the Safari UI. Defaults to false. If FALSE, the Safari UI appears when navigating away. If TRUE, the Safari UI will not be shown.
    ignore_manifest_scope: Optional[bool] = None
    # Whether or not the icon for the app is precomosed. Defaults to false. If TRUE, prevents SpringBoard from adding 'shine' to the icon. If FALSE, SpringBoard can add 'shine'.
    pre_composed_icon_enabled: Optional[bool] = None
    # Specifies the application bundle identifier which opens the URL. Available in iOS 14 and later.
    target_application_bundle_identifier: Optional[str] = None
    # Whether or not to use managed browser. When TRUE, the app will be required to be opened in Microsoft Edge. When FALSE, the app will not be required to be opened in Microsoft Edge. By default, this property is set to FALSE.
    use_managed_browser: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosiPadOSWebClip:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosiPadOSWebClip
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosiPadOSWebClip()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app import MobileApp

        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "appUrl": lambda n : setattr(self, 'app_url', n.get_str_value()),
            "fullScreenEnabled": lambda n : setattr(self, 'full_screen_enabled', n.get_bool_value()),
            "ignoreManifestScope": lambda n : setattr(self, 'ignore_manifest_scope', n.get_bool_value()),
            "preComposedIconEnabled": lambda n : setattr(self, 'pre_composed_icon_enabled', n.get_bool_value()),
            "targetApplicationBundleIdentifier": lambda n : setattr(self, 'target_application_bundle_identifier', n.get_str_value()),
            "useManagedBrowser": lambda n : setattr(self, 'use_managed_browser', n.get_bool_value()),
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
        writer.write_str_value("appUrl", self.app_url)
        writer.write_bool_value("fullScreenEnabled", self.full_screen_enabled)
        writer.write_bool_value("ignoreManifestScope", self.ignore_manifest_scope)
        writer.write_bool_value("preComposedIconEnabled", self.pre_composed_icon_enabled)
        writer.write_str_value("targetApplicationBundleIdentifier", self.target_application_bundle_identifier)
        writer.write_bool_value("useManagedBrowser", self.use_managed_browser)
    

