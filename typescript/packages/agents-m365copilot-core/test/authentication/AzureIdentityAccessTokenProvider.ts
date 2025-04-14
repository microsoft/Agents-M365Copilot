import { assert, describe, it } from "vitest";
import { AgentsM365CopilotAzureIdentityAccessTokenProvider } from "../../src/authentication/AzureIdentityAccessTokenProvider";
import { AgentsM365CopilotTelemetryOption } from "../../src/middleware/agentsM365CopilotTelemetryOption";
import { AzureIdentityAccessTokenProvider } from "@microsoft/kiota-authentication-azure";
import { TokenCredential } from "@azure/core-auth";

const options: AgentsM365CopilotTelemetryOption = {
  agentsM365CopilotServiceTargetVersion: "v1",
  agentsM365CopilotProductPrefix: "agentsM365Copilot-typescript-test",
  agentsM365CopilotServiceLibraryClientVersion: "0.0.0",
};

describe("AgentsM365CopilotAzureIdentityAccessTokenProvider tests", () => {
  it("should implement AzureIdentityAccessTokenProvider", () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new AgentsM365CopilotAzureIdentityAccessTokenProvider(credential);
    assert.instanceOf(
      provider,
      AzureIdentityAccessTokenProvider,
      "Provider does not implement AzureIdentityAccessTokenProvider",
    );
  });

  it("should add default hosts", async () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new AgentsM365CopilotAzureIdentityAccessTokenProvider(credential);
    const allowedHosts = provider.getAllowedHostsValidator().getAllowedHosts();
    assert.equal(allowedHosts.length, 6, "Unexpected number of allowed hosts");
  });
});
