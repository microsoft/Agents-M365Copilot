from typing import Optional

from kiota_abstractions.request_option import RequestOption

from ..._constants import SDK_VERSION
from ..._enums import APIVersion


class MicrosoftAgentsM365CopilotTelemetryHandlerOption(RequestOption):
    """Config options for the MicrosoftAgentsM365CopilotTelemetryHandlerOption"""

    AGENTS_COPILOT_TELEMETRY_HANDLER_OPTION_KEY = "MicrosoftAgentsM365CopilotTelemetryHandlerOption"

    def __init__(
        self, api_version: Optional[APIVersion] = None, sdk_version: str = SDK_VERSION
    ) -> None:
        """To create an instance of MicrosoftAgentsM365CopilotTelemetryHandlerOption

        Args:
            api_version (Optional[APIVersion], optional): The M365 copilot API version in use.
            Defaults to None.
            sdk_version (str): The sdk version in use.
            Defaults to SDK_VERSION of microsoft_agents_m365copilot_core.
        """
        self._api_version = api_version
        self._sdk_version = sdk_version

    @property
    def api_version(self):
        """The M365 copilot API version in use"""
        return self._api_version

    @api_version.setter
    def api_version(self, value: APIVersion):
        self._api_version = value

    @property
    def sdk_version(self):
        """The sdk version in use"""
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, value: str):
        self._sdk_version = value

    @staticmethod
    def get_key() -> str:
        return MicrosoftAgentsM365CopilotTelemetryHandlerOption.AGENTS_COPILOT_TELEMETRY_HANDLER_OPTION_KEY
