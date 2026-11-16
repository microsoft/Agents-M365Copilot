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
    from ...models.copilot_conversation import CopilotConversation
    from ...models.o_data_errors.o_data_error import ODataError
    from .item.copilot_conversation_item_request_builder import CopilotConversationItemRequestBuilder
    from .microsoft_graph_copilot_delete_by_thread_id.microsoft_graph_copilot_delete_by_thread_id_request_builder import MicrosoftGraphCopilotDeleteByThreadIdRequestBuilder

class ConversationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the conversations property of the microsoft.graph.copilotRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConversationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/conversations", path_parameters)
    
    def by_copilot_conversation_id(self,copilot_conversation_id: str) -> CopilotConversationItemRequestBuilder:
        """
        Gets an item from the microsoft_agents_m365copilot_beta.generated.copilot.conversations.item collection
        param copilot_conversation_id: The unique identifier of copilotConversation
        Returns: CopilotConversationItemRequestBuilder
        """
        if copilot_conversation_id is None:
            raise TypeError("copilot_conversation_id cannot be null.")
        from .item.copilot_conversation_item_request_builder import CopilotConversationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["copilotConversation%2Did"] = copilot_conversation_id
        return CopilotConversationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: CopilotConversation, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CopilotConversation]:
        """
        Create new navigation property to conversations for copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CopilotConversation]
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
        from ...models.copilot_conversation import CopilotConversation

        return await self.request_adapter.send_async(request_info, CopilotConversation, error_mapping)
    
    def to_post_request_information(self,body: CopilotConversation, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to conversations for copilot
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
    
    def with_url(self,raw_url: str) -> ConversationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConversationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConversationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def microsoft_graph_copilot_delete_by_thread_id(self) -> MicrosoftGraphCopilotDeleteByThreadIdRequestBuilder:
        """
        Provides operations to call the deleteByThreadId method.
        """
        from .microsoft_graph_copilot_delete_by_thread_id.microsoft_graph_copilot_delete_by_thread_id_request_builder import MicrosoftGraphCopilotDeleteByThreadIdRequestBuilder

        return MicrosoftGraphCopilotDeleteByThreadIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConversationsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

