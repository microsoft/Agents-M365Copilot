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
    from .....models.credit_request import CreditRequest
    from .....models.o_data_errors.o_data_error import ODataError

class CreditRequestItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the creditRequests property of the microsoft.graph.costManagementRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CreditRequestItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/costManagement/creditRequests/{creditRequest%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CreditRequestItemRequestBuilderGetQueryParameters]] = None) -> Optional[CreditRequest]:
        """
        The collection of credit requests for this tenant. Excludes audit-only requests by default.A list or requested-count dependency failure returns a Graph serviceNotAvailable error.Supports $filter on state and serviceId (eq), $select, $count=true, and $top (default 50, maximum 200).Results are ordered newest-first; $orderby is not supported.Server-driven paging returns an OData nextLink when additional pages are available.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreditRequest]
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
        from .....models.credit_request import CreditRequest

        return await self.request_adapter.send_async(request_info, CreditRequest, error_mapping)
    
    async def patch(self,body: CreditRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreditRequest]:
        """
        Update the navigation property creditRequests in copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreditRequest]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.credit_request import CreditRequest

        return await self.request_adapter.send_async(request_info, CreditRequest, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CreditRequestItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The collection of credit requests for this tenant. Excludes audit-only requests by default.A list or requested-count dependency failure returns a Graph serviceNotAvailable error.Supports $filter on state and serviceId (eq), $select, $count=true, and $top (default 50, maximum 200).Results are ordered newest-first; $orderby is not supported.Server-driven paging returns an OData nextLink when additional pages are available.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CreditRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property creditRequests in copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CreditRequestItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CreditRequestItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CreditRequestItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CreditRequestItemRequestBuilderGetQueryParameters():
        """
        The collection of credit requests for this tenant. Excludes audit-only requests by default.A list or requested-count dependency failure returns a Graph serviceNotAvailable error.Supports $filter on state and serviceId (eq), $select, $count=true, and $top (default 50, maximum 200).Results are ordered newest-first; $orderby is not supported.Server-driven paging returns an OData nextLink when additional pages are available.
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
    class CreditRequestItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CreditRequestItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CreditRequestItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

