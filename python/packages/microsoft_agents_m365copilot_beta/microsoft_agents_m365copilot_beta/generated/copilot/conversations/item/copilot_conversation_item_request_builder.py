from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .microsoft_graph_copilot_chat.microsoft_graph_copilot_chat_request_builder import MicrosoftGraphCopilotChatRequestBuilder
    from .microsoft_graph_copilot_chat_over_stream.microsoft_graph_copilot_chat_over_stream_request_builder import MicrosoftGraphCopilotChatOverStreamRequestBuilder

class CopilotConversationItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /copilot/conversations/{copilotConversation-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CopilotConversationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot/conversations/{copilotConversation%2Did}", path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        The messages property
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_copilot_chat(self) -> MicrosoftGraphCopilotChatRequestBuilder:
        """
        Provides operations to call the chat method.
        """
        from .microsoft_graph_copilot_chat.microsoft_graph_copilot_chat_request_builder import MicrosoftGraphCopilotChatRequestBuilder

        return MicrosoftGraphCopilotChatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_copilot_chat_over_stream(self) -> MicrosoftGraphCopilotChatOverStreamRequestBuilder:
        """
        Provides operations to call the chatOverStream method.
        """
        from .microsoft_graph_copilot_chat_over_stream.microsoft_graph_copilot_chat_over_stream_request_builder import MicrosoftGraphCopilotChatOverStreamRequestBuilder

        return MicrosoftGraphCopilotChatOverStreamRequestBuilder(self.request_adapter, self.path_parameters)
    

