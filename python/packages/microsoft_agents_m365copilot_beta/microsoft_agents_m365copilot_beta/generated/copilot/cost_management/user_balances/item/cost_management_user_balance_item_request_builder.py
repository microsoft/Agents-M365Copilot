from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.cost_management_user_balance import CostManagementUserBalance
    from .....models.o_data_errors.o_data_error import ODataError
    from .service_balances.service_balances_request_builder import ServiceBalancesRequestBuilder

class CostManagementUserBalanceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the userBalances property of the microsoft.graph.costManagementRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CostManagementUserBalanceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/costManagement/userBalances/{costManagementUserBalance%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CostManagementUserBalanceItemRequestBuilderGetQueryParameters]] = None) -> Optional[CostManagementUserBalance]:
        """
        Per-user consumption balances, addressed by the user's identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CostManagementUserBalance]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cost_management_user_balance import CostManagementUserBalance

        return await self.request_adapter.send_async(request_info, CostManagementUserBalance, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CostManagementUserBalanceItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Per-user consumption balances, addressed by the user's identifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CostManagementUserBalanceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CostManagementUserBalanceItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CostManagementUserBalanceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def service_balances(self) -> ServiceBalancesRequestBuilder:
        """
        Provides operations to manage the serviceBalances property of the microsoft.graph.costManagementUserBalance entity.
        """
        from .service_balances.service_balances_request_builder import ServiceBalancesRequestBuilder

        return ServiceBalancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CostManagementUserBalanceItemRequestBuilderGetQueryParameters():
        """
        Per-user consumption balances, addressed by the user's identifier.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class CostManagementUserBalanceItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CostManagementUserBalanceItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

