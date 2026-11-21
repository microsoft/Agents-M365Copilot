from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .funding_usage_records.funding_usage_records_request_builder import FundingUsageRecordsRequestBuilder
    from .group_usage_records.group_usage_records_request_builder import GroupUsageRecordsRequestBuilder
    from .service_usage_records.service_usage_records_request_builder import ServiceUsageRecordsRequestBuilder
    from .user_usage_details.user_usage_details_request_builder import UserUsageDetailsRequestBuilder
    from .user_usage_records.user_usage_records_request_builder import UserUsageRecordsRequestBuilder

class UsageReportsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /copilot/costManagement/usageReports
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UsageReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/costManagement/usageReports", path_parameters)
    
    @property
    def funding_usage_records(self) -> FundingUsageRecordsRequestBuilder:
        """
        Provides operations to manage the fundingUsageRecords property of the microsoft.graph.costManagementUsageReportRoot entity.
        """
        from .funding_usage_records.funding_usage_records_request_builder import FundingUsageRecordsRequestBuilder

        return FundingUsageRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_usage_records(self) -> GroupUsageRecordsRequestBuilder:
        """
        Provides operations to manage the groupUsageRecords property of the microsoft.graph.costManagementUsageReportRoot entity.
        """
        from .group_usage_records.group_usage_records_request_builder import GroupUsageRecordsRequestBuilder

        return GroupUsageRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_usage_records(self) -> ServiceUsageRecordsRequestBuilder:
        """
        Provides operations to manage the serviceUsageRecords property of the microsoft.graph.costManagementUsageReportRoot entity.
        """
        from .service_usage_records.service_usage_records_request_builder import ServiceUsageRecordsRequestBuilder

        return ServiceUsageRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_usage_details(self) -> UserUsageDetailsRequestBuilder:
        """
        The userUsageDetails property
        """
        from .user_usage_details.user_usage_details_request_builder import UserUsageDetailsRequestBuilder

        return UserUsageDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_usage_records(self) -> UserUsageRecordsRequestBuilder:
        """
        Provides operations to manage the userUsageRecords property of the microsoft.graph.costManagementUsageReportRoot entity.
        """
        from .user_usage_records.user_usage_records_request_builder import UserUsageRecordsRequestBuilder

        return UserUsageRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    

