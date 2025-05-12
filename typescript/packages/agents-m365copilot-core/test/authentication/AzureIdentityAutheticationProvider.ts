import { assert, describe, it } from "vitest";
import { AgentsM365CopilotAzureIdentityAuthenticationProvider } from "../../src/authentication/AzureIdentityAuthenticationProvider";
import { AgentsM365CopilotTelemetryOption } from "../../src/middleware/agentsM365CopilotTelemetryOption";
import { AzureIdentityAuthenticationProvider } from "@microsoft/kiota-authentication-azure";
import { TokenCredential } from "@azure/core-auth";

const options: AgentsM365CopilotTelemetryOption = {
  agentsM365CopilotServiceTargetVersion: "v1",
  agentsM365CopilotProductPrefix: "agentsM365Copilot-typescript-test",
  agentsM365CopilotServiceLibraryClientVersion: "0.0.0",
};

describe("AgentsM365CopilotAzureIdentityAuthenticationProvider tests", () => {
  it("should implement AzureIdentityAccessTokenProvider", () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new AgentsM365CopilotAzureIdentityAuthenticationProvider(credential);
    assert.instanceOf(
      provider,
      AzureIdentityAuthenticationProvider,
      "Provider does not implement AzureIdentityAccessTokenProvider",
    );
  });

  it("should add default hosts", async () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new AgentsM365CopilotAzureIdentityAuthenticationProvider(credential);
    const allowedHosts = provider.accessTokenProvider.getAllowedHostsValidator().getAllowedHosts();
    assert.equal(allowedHosts.length, 6, "Unexpected number of allowed hosts");
  });
});
