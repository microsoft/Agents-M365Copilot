from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .add_to_review_set_operation import AddToReviewSetOperation
    from .data_source import DataSource
    from .data_source_scopes import DataSourceScopes
    from .estimate_statistics_operation import EstimateStatisticsOperation
    from .noncustodial_data_source import NoncustodialDataSource

from ..entity import Entity

@dataclass
class SourceCollection(Entity, Parsable):
    # Adds the results of the sourceCollection to the specified reviewSet.
    add_to_review_set_operation: Optional[AddToReviewSetOperation] = None
    # Adds an additional source to the sourceCollection.
    additional_sources: Optional[list[DataSource]] = None
    # The query string in KQL (Keyword Query Language) query. For details, see Keyword queries and search conditions for Content Search and eDiscovery. You can refine searches by using fields paired with values; for example, subject:'Quarterly Financials' AND Date>=06/01/2016 AND Date<=07/01/2016.
    content_query: Optional[str] = None
    # The user who created the sourceCollection.
    created_by: Optional[IdentitySet] = None
    # The date and time the sourceCollection was created.
    created_date_time: Optional[datetime.datetime] = None
    # Custodian sources that are included in the sourceCollection.
    custodian_sources: Optional[list[DataSource]] = None
    # When specified, the collection spans across a service for an entire workload. The possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
    data_source_scopes: Optional[DataSourceScopes] = None
    # The description of the sourceCollection.
    description: Optional[str] = None
    # The display name of the sourceCollection.
    display_name: Optional[str] = None
    # The last estimate operation associated with the sourceCollection.
    last_estimate_statistics_operation: Optional[EstimateStatisticsOperation] = None
    # The last user who modified the sourceCollection.
    last_modified_by: Optional[IdentitySet] = None
    # The last date and time the sourceCollection was modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # noncustodialDataSource sources that are included in the sourceCollection
    noncustodial_sources: Optional[list[NoncustodialDataSource]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SourceCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SourceCollection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SourceCollection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .add_to_review_set_operation import AddToReviewSetOperation
        from .data_source import DataSource
        from .data_source_scopes import DataSourceScopes
        from .estimate_statistics_operation import EstimateStatisticsOperation
        from .noncustodial_data_source import NoncustodialDataSource

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .add_to_review_set_operation import AddToReviewSetOperation
        from .data_source import DataSource
        from .data_source_scopes import DataSourceScopes
        from .estimate_statistics_operation import EstimateStatisticsOperation
        from .noncustodial_data_source import NoncustodialDataSource

        fields: dict[str, Callable[[Any], None]] = {
            "addToReviewSetOperation": lambda n : setattr(self, 'add_to_review_set_operation', n.get_object_value(AddToReviewSetOperation)),
            "additionalSources": lambda n : setattr(self, 'additional_sources', n.get_collection_of_object_values(DataSource)),
            "contentQuery": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custodianSources": lambda n : setattr(self, 'custodian_sources', n.get_collection_of_object_values(DataSource)),
            "dataSourceScopes": lambda n : setattr(self, 'data_source_scopes', n.get_collection_of_enum_values(DataSourceScopes)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastEstimateStatisticsOperation": lambda n : setattr(self, 'last_estimate_statistics_operation', n.get_object_value(EstimateStatisticsOperation)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "noncustodialSources": lambda n : setattr(self, 'noncustodial_sources', n.get_collection_of_object_values(NoncustodialDataSource)),
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
        writer.write_object_value("addToReviewSetOperation", self.add_to_review_set_operation)
        writer.write_collection_of_object_values("additionalSources", self.additional_sources)
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("custodianSources", self.custodian_sources)
        writer.write_enum_value("dataSourceScopes", self.data_source_scopes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastEstimateStatisticsOperation", self.last_estimate_statistics_operation)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("noncustodialSources", self.noncustodial_sources)
    

