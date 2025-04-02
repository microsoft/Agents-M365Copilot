import { assert, describe, it } from "vitest";
import { GraphAzureIdentityAccessTokenProvider } from "../../src/authentication/AzureIdentityAccessTokenProvider";
import { AgentsM365CopilotTelemetryOption } from "../../src/middleware/AgentsM365CopilotTelemetryOption";
import { AzureIdentityAccessTokenProvider } from "@microsoft/kiota-authentication-azure";
import { TokenCredential } from "@azure/core-auth";

const options: AgentsM365CopilotTelemetryOption = {
  graphServiceTargetVersion: "v1",
  graphProductPrefix: "graph-typescript-test",
  graphServiceLibraryClientVersion: "0.0.0",
};

describe("GraphAzureIdentityAccessTokenProvider tests", () => {
  it("should implement AzureIdentityAccessTokenProvider", () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new GraphAzureIdentityAccessTokenProvider(credential);
    assert.instanceOf(
      provider,
      AzureIdentityAccessTokenProvider,
      "Provider does not implement AzureIdentityAccessTokenProvider",
    );
  });

  it("should add default hosts", async () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new GraphAzureIdentityAccessTokenProvider(credential);
    const allowedHosts = provider.getAllowedHostsValidator().getAllowedHosts();
    assert.equal(allowedHosts.length, 6, "Unexpected number of allowed hosts");
  });
});
