from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .share_point_group_migration_task_parameters import SharePointGroupMigrationTaskParameters
    from .share_point_site_migration_task_parameters import SharePointSiteMigrationTaskParameters
    from .share_point_user_migration_task_parameters import SharePointUserMigrationTaskParameters

@dataclass
class SharePointMigrationTaskParameters(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The preferred latest start date and time. The system cancels the sharePointMigrationTask if it doesn't start by this time. The value must be greater than the preferredStartDateTime, if present. Optional. Only on OneDrive and SharePoint.
    preferred_latest_start_date_time: Optional[datetime.datetime] = None
    # The preferred start date and time that allows the sharePointMigrationTask to start at a future time instead of as soon as possible (default). Optional. Only on OneDrive and SharePoint.
    preferred_start_date_time: Optional[datetime.datetime] = None
    # The SharePoint URL of the source site. Optional. Exactly one of sourceSiteId or sourceUrl must be specified. If both or neither are specified, it's an error. Only on OneDrive and SharePoint.
    source_site_url: Optional[str] = None
    # In Microsoft Entra, this value represents the geographic location (for example, JPN, NAM) of the target organization where the resource must be migrated to ensure data residency and compliance. This property isn't required for single-geo target organizations or when the migration is to the default GEO of a multi-geo target organization. Optional. Only on OneDrive and SharePoint.
    target_data_location_code: Optional[str] = None
    # The root, admin, or my site host of the specific multi-geo instance of the target organization where the resource must be migrated to ensure data residency and compliance. This property isn't required for single-geo target organizations or when the migration is to the default GEO of a multi-geo target organization. Optional. Only on OneDrive and SharePoint.
    target_organization_host: Optional[str] = None
    # The unique Microsoft Entra company ID of the target organization to which the source resource must be migrated. Only on OneDrive and SharePoint.
    target_organization_id: Optional[UUID] = None
    # The SharePoint URL of the target site. Only on OneDrive and SharePoint.
    target_site_url: Optional[str] = None
    # Indicates whether this task is an actual migration or only a validation. If the parameter is missing, the system treats it as false. The default behavior is a real migration. Optional. Only on OneDrive and SharePoint.
    validate_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationTaskParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationTaskParameters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointGroupMigrationTaskParameters".casefold():
            from .share_point_group_migration_task_parameters import SharePointGroupMigrationTaskParameters

            return SharePointGroupMigrationTaskParameters()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointSiteMigrationTaskParameters".casefold():
            from .share_point_site_migration_task_parameters import SharePointSiteMigrationTaskParameters

            return SharePointSiteMigrationTaskParameters()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointUserMigrationTaskParameters".casefold():
            from .share_point_user_migration_task_parameters import SharePointUserMigrationTaskParameters

            return SharePointUserMigrationTaskParameters()
        return SharePointMigrationTaskParameters()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .share_point_group_migration_task_parameters import SharePointGroupMigrationTaskParameters
        from .share_point_site_migration_task_parameters import SharePointSiteMigrationTaskParameters
        from .share_point_user_migration_task_parameters import SharePointUserMigrationTaskParameters

        from .share_point_group_migration_task_parameters import SharePointGroupMigrationTaskParameters
        from .share_point_site_migration_task_parameters import SharePointSiteMigrationTaskParameters
        from .share_point_user_migration_task_parameters import SharePointUserMigrationTaskParameters

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preferredLatestStartDateTime": lambda n : setattr(self, 'preferred_latest_start_date_time', n.get_datetime_value()),
            "preferredStartDateTime": lambda n : setattr(self, 'preferred_start_date_time', n.get_datetime_value()),
            "sourceSiteUrl": lambda n : setattr(self, 'source_site_url', n.get_str_value()),
            "targetDataLocationCode": lambda n : setattr(self, 'target_data_location_code', n.get_str_value()),
            "targetOrganizationHost": lambda n : setattr(self, 'target_organization_host', n.get_str_value()),
            "targetOrganizationId": lambda n : setattr(self, 'target_organization_id', n.get_uuid_value()),
            "targetSiteUrl": lambda n : setattr(self, 'target_site_url', n.get_str_value()),
            "validateOnly": lambda n : setattr(self, 'validate_only', n.get_bool_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("preferredLatestStartDateTime", self.preferred_latest_start_date_time)
        writer.write_datetime_value("preferredStartDateTime", self.preferred_start_date_time)
        writer.write_str_value("sourceSiteUrl", self.source_site_url)
        writer.write_str_value("targetDataLocationCode", self.target_data_location_code)
        writer.write_str_value("targetOrganizationHost", self.target_organization_host)
        writer.write_uuid_value("targetOrganizationId", self.target_organization_id)
        writer.write_str_value("targetSiteUrl", self.target_site_url)
        writer.write_bool_value("validateOnly", self.validate_only)
        writer.write_additional_data_value(self.additional_data)
    

