from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_customization import ContentCustomization
    from .login_page_branding_visual_element import LoginPageBrandingVisualElement
    from .login_page_layout_configuration import LoginPageLayoutConfiguration

@dataclass
class OrganizationalBrandingThemeLocalization(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents 'Can't access your account?' and 'Reset it now' hyperlinks of self-service password reset (SSPR) that can be customized on the sign-in page for a theme. A destination URL can be updated. Optional.
    account_reset_credentials: Optional[LoginPageBrandingVisualElement] = None
    # Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster. Optional.
    background_image: Optional[bytes] = None
    # A relative url for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    background_image_relative_url: Optional[str] = None
    # A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 245 x 36 pixels. We recommend using a transparent image with no padding around the logo. Optional.
    banner_logo: Optional[bytes] = None
    # A relative url for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    banner_logo_relative_url: Optional[str] = None
    # Represents 'Can't access your account?' hyperlink of self-service password reset (SSPR) that can be customized on the sign-in page for a theme. A display text can be updated. Optional.
    cannot_access_your_account: Optional[LoginPageBrandingVisualElement] = None
    # A list of available CDN base urls that are serving the assets of the current resource. There are several CDNs used to provide redundancy hence eliminating Single Point of Failure for blob properties of this resource. Read-only. Optional.
    cdn_hosts: Optional[list[str]] = None
    # Represents the various content options to be customized throughout the authentication flow for a tenant. NOTE: Supported by Microsoft Entra ID for customer tenants only. Optional.
    content_customization: Optional[ContentCustomization] = None
    # CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25KB. Optional.
    custom_c_s_s: Optional[bytes] = None
    # A relative url for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    custom_c_s_s_relative_url: Optional[str] = None
    # A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant. Optional.
    favicon: Optional[bytes] = None
    # A relative url for the favicon property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    favicon_relative_url: Optional[str] = None
    # Represents 'Forgot my password' hyperlink of self-service password reset (SSPR) that can be customized on the sign-in page for a theme. A display text can be updated. Optional.
    forgot_my_password: Optional[LoginPageBrandingVisualElement] = None
    # The RGB color to apply to customize the color of the header. Optional.
    header_background_color: Optional[str] = None
    # A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 245 x 36 pixels. We recommend using a transparent image with no padding around the logo. Optional.
    header_logo: Optional[bytes] = None
    # A relative url for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    header_logo_relative_url: Optional[str] = None
    # An identifier that represents the locale specified using culture names. Culture names follow the RFC 1766 standard in the format 'languagecode2-country/regioncode2'. The portion 'languagecode2' is a lowercase two-letter code derived from ISO 639-1 and 'country/regioncode2' is an uppercase two-letter code derived from ISO 3166. For example, U.S. English is en-US. You can't create the default branding by setting the value of locale to the String types 0 or default.  NOTE: Multiple branding for a single locale are currently not supported.
    locale: Optional[str] = None
    # Represents the layout configuration to be displayed on the login page for a tenant. Optional.
    login_page_layout_configuration: Optional[LoginPageLayoutConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF. Optional.
    page_background_color: Optional[str] = None
    # Represents 'Privacy & cookies' hyperlink in the footer of sign-in page that can be customized for a theme. A destination URL and a display text can be updated. Optional.
    privacy_and_cookies: Optional[LoginPageBrandingVisualElement] = None
    # Represents 'Reset it now' hyperlink of self-service password reset (SSPR) that can be customized on the sign-in page for a theme. A display text can be updated. Optional.
    reset_it_now: Optional[LoginPageBrandingVisualElement] = None
    # Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters. Optional.
    sign_in_page_text: Optional[str] = None
    # A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo. Optional.
    square_logo: Optional[bytes] = None
    # A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo. Optional.
    square_logo_dark: Optional[bytes] = None
    # A relative url for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    square_logo_dark_relative_url: Optional[str] = None
    # A relative url for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only. Optional.
    square_logo_relative_url: Optional[str] = None
    # Represents the Terms of Use hyperlink that can be customized in the footer of the login page for a theme. A destination URL and a display text can be updated. Optional.
    terms_of_use: Optional[LoginPageBrandingVisualElement] = None
    # A string that appears as the hint in the username text box on the sign-in screen. This text must be Unicode, contain no links or code, and can't exceed 64 characters. Optional.
    username_hint_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationalBrandingThemeLocalization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBrandingThemeLocalization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationalBrandingThemeLocalization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_customization import ContentCustomization
        from .login_page_branding_visual_element import LoginPageBrandingVisualElement
        from .login_page_layout_configuration import LoginPageLayoutConfiguration

        from .content_customization import ContentCustomization
        from .login_page_branding_visual_element import LoginPageBrandingVisualElement
        from .login_page_layout_configuration import LoginPageLayoutConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "accountResetCredentials": lambda n : setattr(self, 'account_reset_credentials', n.get_object_value(LoginPageBrandingVisualElement)),
            "backgroundImage": lambda n : setattr(self, 'background_image', n.get_bytes_value()),
            "backgroundImageRelativeUrl": lambda n : setattr(self, 'background_image_relative_url', n.get_str_value()),
            "bannerLogo": lambda n : setattr(self, 'banner_logo', n.get_bytes_value()),
            "bannerLogoRelativeUrl": lambda n : setattr(self, 'banner_logo_relative_url', n.get_str_value()),
            "cannotAccessYourAccount": lambda n : setattr(self, 'cannot_access_your_account', n.get_object_value(LoginPageBrandingVisualElement)),
            "cdnHosts": lambda n : setattr(self, 'cdn_hosts', n.get_collection_of_primitive_values(str)),
            "contentCustomization": lambda n : setattr(self, 'content_customization', n.get_object_value(ContentCustomization)),
            "customCSS": lambda n : setattr(self, 'custom_c_s_s', n.get_bytes_value()),
            "customCSSRelativeUrl": lambda n : setattr(self, 'custom_c_s_s_relative_url', n.get_str_value()),
            "favicon": lambda n : setattr(self, 'favicon', n.get_bytes_value()),
            "faviconRelativeUrl": lambda n : setattr(self, 'favicon_relative_url', n.get_str_value()),
            "forgotMyPassword": lambda n : setattr(self, 'forgot_my_password', n.get_object_value(LoginPageBrandingVisualElement)),
            "headerBackgroundColor": lambda n : setattr(self, 'header_background_color', n.get_str_value()),
            "headerLogo": lambda n : setattr(self, 'header_logo', n.get_bytes_value()),
            "headerLogoRelativeUrl": lambda n : setattr(self, 'header_logo_relative_url', n.get_str_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "loginPageLayoutConfiguration": lambda n : setattr(self, 'login_page_layout_configuration', n.get_object_value(LoginPageLayoutConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pageBackgroundColor": lambda n : setattr(self, 'page_background_color', n.get_str_value()),
            "privacyAndCookies": lambda n : setattr(self, 'privacy_and_cookies', n.get_object_value(LoginPageBrandingVisualElement)),
            "resetItNow": lambda n : setattr(self, 'reset_it_now', n.get_object_value(LoginPageBrandingVisualElement)),
            "signInPageText": lambda n : setattr(self, 'sign_in_page_text', n.get_str_value()),
            "squareLogo": lambda n : setattr(self, 'square_logo', n.get_bytes_value()),
            "squareLogoDark": lambda n : setattr(self, 'square_logo_dark', n.get_bytes_value()),
            "squareLogoDarkRelativeUrl": lambda n : setattr(self, 'square_logo_dark_relative_url', n.get_str_value()),
            "squareLogoRelativeUrl": lambda n : setattr(self, 'square_logo_relative_url', n.get_str_value()),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_object_value(LoginPageBrandingVisualElement)),
            "usernameHintText": lambda n : setattr(self, 'username_hint_text', n.get_str_value()),
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
        writer.write_object_value("accountResetCredentials", self.account_reset_credentials)
        writer.write_bytes_value("backgroundImage", self.background_image)
        writer.write_str_value("backgroundImageRelativeUrl", self.background_image_relative_url)
        writer.write_bytes_value("bannerLogo", self.banner_logo)
        writer.write_str_value("bannerLogoRelativeUrl", self.banner_logo_relative_url)
        writer.write_object_value("cannotAccessYourAccount", self.cannot_access_your_account)
        writer.write_collection_of_primitive_values("cdnHosts", self.cdn_hosts)
        writer.write_object_value("contentCustomization", self.content_customization)
        writer.write_bytes_value("customCSS", self.custom_c_s_s)
        writer.write_str_value("customCSSRelativeUrl", self.custom_c_s_s_relative_url)
        writer.write_bytes_value("favicon", self.favicon)
        writer.write_str_value("faviconRelativeUrl", self.favicon_relative_url)
        writer.write_object_value("forgotMyPassword", self.forgot_my_password)
        writer.write_str_value("headerBackgroundColor", self.header_background_color)
        writer.write_bytes_value("headerLogo", self.header_logo)
        writer.write_str_value("headerLogoRelativeUrl", self.header_logo_relative_url)
        writer.write_str_value("locale", self.locale)
        writer.write_object_value("loginPageLayoutConfiguration", self.login_page_layout_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("pageBackgroundColor", self.page_background_color)
        writer.write_object_value("privacyAndCookies", self.privacy_and_cookies)
        writer.write_object_value("resetItNow", self.reset_it_now)
        writer.write_str_value("signInPageText", self.sign_in_page_text)
        writer.write_bytes_value("squareLogo", self.square_logo)
        writer.write_bytes_value("squareLogoDark", self.square_logo_dark)
        writer.write_str_value("squareLogoDarkRelativeUrl", self.square_logo_dark_relative_url)
        writer.write_str_value("squareLogoRelativeUrl", self.square_logo_relative_url)
        writer.write_object_value("termsOfUse", self.terms_of_use)
        writer.write_str_value("usernameHintText", self.username_hint_text)
        writer.write_additional_data_value(self.additional_data)
    

