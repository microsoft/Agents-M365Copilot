from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, Union
from warnings import warn

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory

if TYPE_CHECKING:
    from ....models.copilot_conversation import CopilotConversation
    from ....models.o_data_errors.o_data_error import ODataError
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .microsoft_graph_copilot_chat.microsoft_graph_copilot_chat_request_builder import (
        MicrosoftGraphCopilotChatRequestBuilder,
    )
    from .microsoft_graph_copilot_chat_over_stream.microsoft_graph_copilot_chat_over_stream_request_builder import (
        MicrosoftGraphCopilotChatOverStreamRequestBuilder,
    )

class CopilotConversationItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the conversations property of the microsoft.graph.copilotRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CopilotConversationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/conversations/{copilotConversation%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property conversations for copilot
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CopilotConversationItemRequestBuilderGetQueryParameters]] = None) -> Optional[CopilotConversation]:
        """
        The users conversations with Copilot Chat.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CopilotConversation]
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.copilot_conversation import CopilotConversation

        return await self.request_adapter.send_async(request_info, CopilotConversation, error_mapping)
    
    async def patch(self,body: CopilotConversation, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CopilotConversation]:
        """
        Update the navigation property conversations in copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CopilotConversation]
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.copilot_conversation import CopilotConversation

        return await self.request_adapter.send_async(request_info, CopilotConversation, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property conversations for copilot
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CopilotConversationItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The users conversations with Copilot Chat.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CopilotConversation, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property conversations in copilot
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CopilotConversationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CopilotConversationItemRequestBuilder
        """
        warn(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CopilotConversationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.copilotConversation entity.
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_copilot_chat(self) -> MicrosoftGraphCopilotChatRequestBuilder:
        """
        Provides operations to call the chat method.
        """
        from .microsoft_graph_copilot_chat.microsoft_graph_copilot_chat_request_builder import (
            MicrosoftGraphCopilotChatRequestBuilder,
        )

        return MicrosoftGraphCopilotChatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_copilot_chat_over_stream(self) -> MicrosoftGraphCopilotChatOverStreamRequestBuilder:
        """
        Provides operations to call the chatOverStream method.
        """
        from .microsoft_graph_copilot_chat_over_stream.microsoft_graph_copilot_chat_over_stream_request_builder import (
            MicrosoftGraphCopilotChatOverStreamRequestBuilder,
        )

        return MicrosoftGraphCopilotChatOverStreamRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CopilotConversationItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CopilotConversationItemRequestBuilderGetQueryParameters():
        """
        The users conversations with Copilot Chat.
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
    class CopilotConversationItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CopilotConversationItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CopilotConversationItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

