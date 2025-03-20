from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin.admin_request_builder import AdminRequestBuilder
    from .interaction_history.interaction_history_request_builder import InteractionHistoryRequestBuilder
    from .retrieval.retrieval_request_builder import RetrievalRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder

class CopilotRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /copilot
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CopilotRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/copilot", path_parameters)
    
    @property
    def admin(self) -> AdminRequestBuilder:
        """
        Provides operations to manage the admin property of the microsoft.graph.copilotRoot entity.
        """
        from .admin.admin_request_builder import AdminRequestBuilder

        return AdminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def interaction_history(self) -> InteractionHistoryRequestBuilder:
        """
        Provides operations to manage the interactionHistory property of the microsoft.graph.copilotRoot entity.
        """
        from .interaction_history.interaction_history_request_builder import InteractionHistoryRequestBuilder

        return InteractionHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieval(self) -> RetrievalRequestBuilder:
        """
        Provides operations to call the retrieval method.
        """
        from .retrieval.retrieval_request_builder import RetrievalRequestBuilder

        return RetrievalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.copilotRoot entity.
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    

