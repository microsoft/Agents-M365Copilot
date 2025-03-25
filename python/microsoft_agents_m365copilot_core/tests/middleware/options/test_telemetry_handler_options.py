import pytest

from microsoft_agents_m365copilot_beta import SDK_VERSION, APIVersion, MicrosoftAgentsM365CopilotTelemetryHandlerOption

def test_telemetry_handler_options_default():
    telemetry_options = MicrosoftAgentsM365CopilotTelemetryHandlerOption()

    assert telemetry_options.get_key() == "MicrosoftAgentsM365CopilotTelemetryHandlerOption"
    assert telemetry_options.api_version is None
    assert telemetry_options.sdk_version == SDK_VERSION


def test_telemetry_handler_options_custom():
    telemetry_options = MicrosoftAgentsM365CopilotTelemetryHandlerOption(
        api_version=APIVersion.beta, sdk_version='1.0.0'
    )

    assert telemetry_options.get_key() == "MicrosoftAgentsM365CopilotTelemetryHandlerOption"
    assert telemetry_options.api_version == APIVersion.beta
    assert telemetry_options.sdk_version == '1.0.0'
