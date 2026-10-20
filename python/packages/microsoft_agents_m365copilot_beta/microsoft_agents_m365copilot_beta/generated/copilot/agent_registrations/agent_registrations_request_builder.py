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
    from ...models.agent_registration import AgentRegistration
    from ...models.o_data_errors.o_data_error import ODataError
    from .item.agent_registration_item_request_builder import AgentRegistrationItemRequestBuilder

class AgentRegistrationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the agentRegistrations property of the microsoft.graph.copilotRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AgentRegistrationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/agentRegistrations", path_parameters)
    
    def by_agent_registration_id(self,agent_registration_id: str) -> AgentRegistrationItemRequestBuilder:
        """
        Provides operations to manage the agentRegistrations property of the microsoft.graph.copilotRoot entity.
        param agent_registration_id: The unique identifier of agentRegistration
        Returns: AgentRegistrationItemRequestBuilder
        """
        if agent_registration_id is None:
            raise TypeError("agent_registration_id cannot be null.")
        from .item.agent_registration_item_request_builder import AgentRegistrationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agentRegistration%2Did"] = agent_registration_id
        return AgentRegistrationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: AgentRegistration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AgentRegistration]:
        """
        Create new navigation property to agentRegistrations for copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AgentRegistration]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.agent_registration import AgentRegistration

        return await self.request_adapter.send_async(request_info, AgentRegistration, error_mapping)
    
    def to_post_request_information(self,body: AgentRegistration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to agentRegistrations for copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AgentRegistrationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AgentRegistrationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AgentRegistrationsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AgentRegistrationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

