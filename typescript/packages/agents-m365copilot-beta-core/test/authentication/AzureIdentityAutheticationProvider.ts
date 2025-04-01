import { assert, describe, it } from "vitest";
import { GraphAzureIdentityAuthenticationProvider } from "../../src/authentication/AzureIdentityAuthenticationProvider";
import { GraphTelemetryOption } from "../../src/middleware/GraphTelemetryOption";
import { AzureIdentityAuthenticationProvider } from "@microsoft/kiota-authentication-azure";
import { TokenCredential } from "@azure/core-auth";

const options: GraphTelemetryOption = {
  graphServiceTargetVersion: "v1",
  graphProductPrefix: "graph-typescript-test",
  graphServiceLibraryClientVersion: "0.0.0",
};

describe("GraphAzureIdentityAuthenticationProvider tests", () => {
  it("should implement AzureIdentityAccessTokenProvider", () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new GraphAzureIdentityAuthenticationProvider(credential);
    assert.instanceOf(
      provider,
      AzureIdentityAuthenticationProvider,
      "Provider does not implement AzureIdentityAccessTokenProvider",
    );
  });

  it("should add default hosts", async () => {
    const credential = {} as TokenCredential; // Replace with actual TokenCredential implementation
    const provider = new GraphAzureIdentityAuthenticationProvider(credential);
    const allowedHosts = provider.accessTokenProvider.getAllowedHostsValidator().getAllowedHosts();
    assert.equal(allowedHosts.length, 6, "Unexpected number of allowed hosts");
  });
});
