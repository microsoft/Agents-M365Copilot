from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .base_site_page import BaseSitePage
    from .column_definition import ColumnDefinition
    from .content_model import ContentModel
    from .content_type import ContentType
    from .deleted import Deleted
    from .document_processing_job import DocumentProcessingJob
    from .drive import Drive
    from .extension import Extension
    from .identity_input import IdentityInput
    from .information_protection import InformationProtection
    from .item_analytics import ItemAnalytics
    from .list_ import List_
    from .onenote import Onenote
    from .page_template import PageTemplate
    from .permission import Permission
    from .recycle_bin import RecycleBin
    from .rich_long_running_operation import RichLongRunningOperation
    from .root import Root
    from .sharepoint_ids import SharepointIds
    from .site_collection import SiteCollection
    from .site_lock_state import SiteLockState
    from .site_settings import SiteSettings
    from .site_template_type import SiteTemplateType
    from .term_store.store import Store

from .base_item import BaseItem

@dataclass
class Site(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.site"
    # Analytics about the view activities that took place on this site.
    analytics: Optional[ItemAnalytics] = None
    # The collection of column definitions reusable across lists under this site.
    columns: Optional[list[ColumnDefinition]] = None
    # The collection of content models applied to this site.
    content_models: Optional[list[ContentModel]] = None
    # The collection of content types defined for this site.
    content_types: Optional[list[ContentType]] = None
    # The deleted property
    deleted: Optional[Deleted] = None
    # The full title for the site. Read-only.
    display_name: Optional[str] = None
    # The document processing jobs running on this site.
    document_processing_jobs: Optional[list[DocumentProcessingJob]] = None
    # The default drive (document library) for this site.
    drive: Optional[Drive] = None
    # The collection of drives (document libraries) under this site.
    drives: Optional[list[Drive]] = None
    # The collection of open extensions defined for this site. Nullable.
    extensions: Optional[list[Extension]] = None
    # The collection of column definitions available in the site that is referenced from the sites in the parent hierarchy of the current site.
    external_columns: Optional[list[ColumnDefinition]] = None
    # The informationProtection property
    information_protection: Optional[InformationProtection] = None
    # The isPersonalSite property
    is_personal_site: Optional[bool] = None
    # Used to address any item contained in this site. This collection can't be enumerated.
    items: Optional[list[BaseItem]] = None
    # The collection of lists under this site.
    lists: Optional[list[List_]] = None
    # The language settings of the site.
    locale: Optional[str] = None
    # The state of the site. The possible values are: unlocked, lockedReadOnly, lockedNoAccess, lockedNoAdditions, unknownFutureValue
    lock_state: Optional[SiteLockState] = None
    # The onenote property
    onenote: Optional[Onenote] = None
    # The collection of long running operations for the site.
    operations: Optional[list[RichLongRunningOperation]] = None
    # The site owner to be provided at the time of site creation only.
    owner_identity_to_resolve: Optional[IdentityInput] = None
    # The collection of page templates on this site.
    page_templates: Optional[list[PageTemplate]] = None
    # The collection of pages in the baseSitePages list on this site.
    pages: Optional[list[BaseSitePage]] = None
    # The permissions associated with the site. Nullable.
    permissions: Optional[list[Permission]] = None
    # A container for a collection of recycleBinItem resources in this site.
    recycle_bin: Optional[RecycleBin] = None
    # If present, provides the root site in the site collection. Read-only.
    root: Optional[Root] = None
    # The settings on this site. Read-only.
    settings: Optional[SiteSettings] = None
    # Determines whether the site and its content can be shared via email.
    share_by_email_enabled: Optional[bool] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[SharepointIds] = None
    # Provides details about the site's site collection. Available only on the root site. Read-only.
    site_collection: Optional[SiteCollection] = None
    # The collection of the sub-sites under this site.
    sites: Optional[list[Site]] = None
    # Specifies the template applied to the site. The possible values are: sitepagepublishing, sts, unknownFutureValue.
    template: Optional[SiteTemplateType] = None
    # The termStore under this site.
    term_store: Optional[Store] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Site:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Site
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Site()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .base_site_page import BaseSitePage
        from .column_definition import ColumnDefinition
        from .content_model import ContentModel
        from .content_type import ContentType
        from .deleted import Deleted
        from .document_processing_job import DocumentProcessingJob
        from .drive import Drive
        from .extension import Extension
        from .identity_input import IdentityInput
        from .information_protection import InformationProtection
        from .item_analytics import ItemAnalytics
        from .list_ import List_
        from .onenote import Onenote
        from .page_template import PageTemplate
        from .permission import Permission
        from .recycle_bin import RecycleBin
        from .rich_long_running_operation import RichLongRunningOperation
        from .root import Root
        from .sharepoint_ids import SharepointIds
        from .site_collection import SiteCollection
        from .site_lock_state import SiteLockState
        from .site_settings import SiteSettings
        from .site_template_type import SiteTemplateType
        from .term_store.store import Store

        from .base_item import BaseItem
        from .base_site_page import BaseSitePage
        from .column_definition import ColumnDefinition
        from .content_model import ContentModel
        from .content_type import ContentType
        from .deleted import Deleted
        from .document_processing_job import DocumentProcessingJob
        from .drive import Drive
        from .extension import Extension
        from .identity_input import IdentityInput
        from .information_protection import InformationProtection
        from .item_analytics import ItemAnalytics
        from .list_ import List_
        from .onenote import Onenote
        from .page_template import PageTemplate
        from .permission import Permission
        from .recycle_bin import RecycleBin
        from .rich_long_running_operation import RichLongRunningOperation
        from .root import Root
        from .sharepoint_ids import SharepointIds
        from .site_collection import SiteCollection
        from .site_lock_state import SiteLockState
        from .site_settings import SiteSettings
        from .site_template_type import SiteTemplateType
        from .term_store.store import Store

        fields: dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(ItemAnalytics)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(ColumnDefinition)),
            "contentModels": lambda n : setattr(self, 'content_models', n.get_collection_of_object_values(ContentModel)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(ContentType)),
            "deleted": lambda n : setattr(self, 'deleted', n.get_object_value(Deleted)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "documentProcessingJobs": lambda n : setattr(self, 'document_processing_jobs', n.get_collection_of_object_values(DocumentProcessingJob)),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(Drive)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "externalColumns": lambda n : setattr(self, 'external_columns', n.get_collection_of_object_values(ColumnDefinition)),
            "informationProtection": lambda n : setattr(self, 'information_protection', n.get_object_value(InformationProtection)),
            "isPersonalSite": lambda n : setattr(self, 'is_personal_site', n.get_bool_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(BaseItem)),
            "lists": lambda n : setattr(self, 'lists', n.get_collection_of_object_values(List_)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "lockState": lambda n : setattr(self, 'lock_state', n.get_enum_value(SiteLockState)),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(Onenote)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(RichLongRunningOperation)),
            "ownerIdentityToResolve": lambda n : setattr(self, 'owner_identity_to_resolve', n.get_object_value(IdentityInput)),
            "pageTemplates": lambda n : setattr(self, 'page_templates', n.get_collection_of_object_values(PageTemplate)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(BaseSitePage)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(Permission)),
            "recycleBin": lambda n : setattr(self, 'recycle_bin', n.get_object_value(RecycleBin)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(Root)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(SiteSettings)),
            "shareByEmailEnabled": lambda n : setattr(self, 'share_by_email_enabled', n.get_bool_value()),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(SharepointIds)),
            "siteCollection": lambda n : setattr(self, 'site_collection', n.get_object_value(SiteCollection)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(Site)),
            "template": lambda n : setattr(self, 'template', n.get_enum_value(SiteTemplateType)),
            "termStore": lambda n : setattr(self, 'term_store', n.get_object_value(Store)),
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
        writer.write_object_value("analytics", self.analytics)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_collection_of_object_values("contentModels", self.content_models)
        writer.write_collection_of_object_values("contentTypes", self.content_types)
        writer.write_object_value("deleted", self.deleted)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("documentProcessingJobs", self.document_processing_jobs)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_object_values("externalColumns", self.external_columns)
        writer.write_object_value("informationProtection", self.information_protection)
        writer.write_bool_value("isPersonalSite", self.is_personal_site)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_collection_of_object_values("lists", self.lists)
        writer.write_str_value("locale", self.locale)
        writer.write_enum_value("lockState", self.lock_state)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("ownerIdentityToResolve", self.owner_identity_to_resolve)
        writer.write_collection_of_object_values("pageTemplates", self.page_templates)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_object_value("recycleBin", self.recycle_bin)
        writer.write_object_value("root", self.root)
        writer.write_object_value("settings", self.settings)
        writer.write_bool_value("shareByEmailEnabled", self.share_by_email_enabled)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_object_value("siteCollection", self.site_collection)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_enum_value("template", self.template)
        writer.write_object_value("termStore", self.term_store)
    

