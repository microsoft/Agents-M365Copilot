from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .credit_requests.credit_requests_request_builder import CreditRequestsRequestBuilder
    from .spending_policies.spending_policies_request_builder import SpendingPoliciesRequestBuilder
    from .usage_reports.usage_reports_request_builder import UsageReportsRequestBuilder
    from .user_balances.user_balances_request_builder import UserBalancesRequestBuilder

class CostManagementRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /copilot/costManagement
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CostManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/costManagement", path_parameters)
    
    @property
    def credit_requests(self) -> CreditRequestsRequestBuilder:
        """
        Provides operations to manage the creditRequests property of the microsoft.graph.costManagementRoot entity.
        """
        from .credit_requests.credit_requests_request_builder import CreditRequestsRequestBuilder

        return CreditRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def spending_policies(self) -> SpendingPoliciesRequestBuilder:
        """
        Provides operations to manage the spendingPolicies property of the microsoft.graph.costManagementRoot entity.
        """
        from .spending_policies.spending_policies_request_builder import SpendingPoliciesRequestBuilder

        return SpendingPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usage_reports(self) -> UsageReportsRequestBuilder:
        """
        The usageReports property
        """
        from .usage_reports.usage_reports_request_builder import UsageReportsRequestBuilder

        return UsageReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_balances(self) -> UserBalancesRequestBuilder:
        """
        The userBalances property
        """
        from .user_balances.user_balances_request_builder import UserBalancesRequestBuilder

        return UserBalancesRequestBuilder(self.request_adapter, self.path_parameters)
    

