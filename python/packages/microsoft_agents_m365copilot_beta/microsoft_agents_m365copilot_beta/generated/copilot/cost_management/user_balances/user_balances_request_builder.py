from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.cost_management_user_balance_item_request_builder import CostManagementUserBalanceItemRequestBuilder

class UserBalancesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /copilot/costManagement/userBalances
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UserBalancesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/costManagement/userBalances", path_parameters)
    
    def by_cost_management_user_balance_id(self,cost_management_user_balance_id: str) -> CostManagementUserBalanceItemRequestBuilder:
        """
        Provides operations to manage the userBalances property of the microsoft.graph.costManagementRoot entity.
        param cost_management_user_balance_id: The unique identifier of costManagementUserBalance
        Returns: CostManagementUserBalanceItemRequestBuilder
        """
        if cost_management_user_balance_id is None:
            raise TypeError("cost_management_user_balance_id cannot be null.")
        from .item.cost_management_user_balance_item_request_builder import CostManagementUserBalanceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["costManagementUserBalance%2Did"] = cost_management_user_balance_id
        return CostManagementUserBalanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    

