from azure.identity import EnvironmentCredential
from kiota_abstractions.authentication import AuthenticationProvider

from microsoft_agents_m365copilot_core.authentication import AzureIdentityAuthenticationProvider


def test_subclassing():
    assert issubclass(AzureIdentityAuthenticationProvider, AuthenticationProvider)
