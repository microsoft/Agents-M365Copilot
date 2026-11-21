from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.cost_management_user_usage_detail_user_item_request_builder import CostManagementUserUsageDetailUserItemRequestBuilder

class UserUsageDetailsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /copilot/costManagement/usageReports/userUsageDetails
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UserUsageDetailsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/costManagement/usageReports/userUsageDetails", path_parameters)
    
    def by_cost_management_user_usage_detail_user_id(self,cost_management_user_usage_detail_user_id: str) -> CostManagementUserUsageDetailUserItemRequestBuilder:
        """
        Provides operations to manage the userUsageDetails property of the microsoft.graph.costManagementUsageReportRoot entity.
        param cost_management_user_usage_detail_user_id: The unique identifier of costManagementUserUsageDetail
        Returns: CostManagementUserUsageDetailUserItemRequestBuilder
        """
        if cost_management_user_usage_detail_user_id is None:
            raise TypeError("cost_management_user_usage_detail_user_id cannot be null.")
        from .item.cost_management_user_usage_detail_user_item_request_builder import CostManagementUserUsageDetailUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["costManagementUserUsageDetail%2DuserId"] = cost_management_user_usage_detail_user_id
        return CostManagementUserUsageDetailUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    

